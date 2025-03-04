import asyncio
import re
import time
import webbrowser
from math import ceil
from typing import TYPE_CHECKING

from desktop_notifier import Urgency
from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Vertical
from textual.content import Content
from textual.css.query import NoMatches
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import (
    ContentSwitcher,
    DataTable,
    Footer,
    Input,
    Label,
    Markdown,
    Pretty,
)
from textual.widgets._data_table import CellDoesNotExist
from udatetime import from_string as dtfstr

import tygenie.config as config
import tygenie.opsgenie as opsgenie
from tygenie import consts
from tygenie.screen import TyScreen
from tygenie.widgets.alert_actions import AlertActionContainer
from tygenie.widgets.alert_details import (
    AlertDetails,
    AlertDetailsTabbedContent,
    AlertDetailTitle,
)
from tygenie.widgets.alert_notes import AlertNotes
from tygenie.widgets.center_middle import CenterMiddle
from tygenie.widgets.datatable import TygenieDataTable
from tygenie.widgets.tags import Tags

if TYPE_CHECKING:
    from tygenie.app import TygenieApp


class AlertsScreen(TyScreen):

    DEFAULT_CSS = """\
    AlertsScreen{
        & #no_alerts_list_label_container {
            height: 1fr;
            hatch: right $surface-lighten-1 70%;
        }
    }
"""

    kb = {
        "ack": "a",
        "unack": "u",
        "close": "c",
        "tag": "t",
        "untag": "T",
        "refresh": "r",
        "next_page": "right",
        "previous_page": "left",
        "add_note": "n",
        "open_in_webbrowser": "ctrl+w",
        "focus_on_alerts_list": "f5",
        "focus_on_alert_details": "f6",
        "focus_on_alert_notes": "f7",
    }

    BINDINGS = [
        Binding(key=kb["ack"], id="ack", action="post_ack_alert()", description="Ack"),
        Binding(
            key=kb["unack"],
            id="unack",
            action="post_unack_alert()",
            description="Unack",
        ),
        Binding(
            key=kb["close"],
            id="close",
            action="post_close_alert()",
            description="Close",
        ),
        Binding(key=kb["tag"], id="tag", action="post_tag_alert()", description="Tag"),
        Binding(
            key=kb["untag"],
            id="untag",
            action="post_remove_tag_alert()",
            description="Untag",
        ),
        Binding(
            key=kb["refresh"],
            id="refresh",
            action="manual_refresh()",
            description="Refresh",
        ),
        Binding(
            key=kb["add_note"],
            id="add_note",
            action="open_add_note()",
            description="Add note",
        ),
        Binding(
            key=kb["previous_page"],
            id="previous_page",
            action="previous_page()",
            description="Prev page",
            show=True,
        ),
        Binding(
            key=kb["next_page"],
            id="next_page",
            action="next_page()",
            description="Next page",
            show=True,
        ),
        Binding(
            key=kb["open_in_webbrowser"],
            id="open_in_webbrowser",
            action="open_in_webbrowser()",
            description="In Web Browser",
        ),
        Binding(
            key=kb["focus_on_alerts_list"],
            id="focus_on_alerts_list",
            action="alerts_list_focus()",
            show=False,
        ),
        Binding(
            key=kb["focus_on_alert_details"],
            id="focus_on_alert_details",
            action="alert_details_focus()",
            show=False,
        ),
        Binding(
            key=kb["focus_on_alert_notes"],
            id="focus_on_alert_notes",
            action="alert_notes_focus()",
            show=False,
        ),
        Binding(
            key="ctrl+down",
            id="increase_height",
            action="increase_height()",
            show=False,
        ),
        Binding(
            key="ctrl+up",
            id="decrease_height",
            action="decrease_height()",
            show=False,
        ),
    ]

    def action_increase_height(self):
        content = self.query_one("#alerts_list_switcher", ContentSwitcher)
        match = re.match(r"^(\d+)(\%|vw|vh|w|h)$", str(content.styles.height))
        if match is not None:
            numeric_height = int(match.group(1))
            unit_height = match.group(2)
            content.styles.height = f"{int(numeric_height)+2}{unit_height}"
        else:
            self.notify(
                severity="error",
                message=f'Wrong height style format: "{content.styles.height}"',
            )

    def action_decrease_height(self):
        content = self.query_one("#alerts_list_switcher", ContentSwitcher)
        match = re.match(r"^(\d+)(\%|vw|vh|w|h)$", str(content.styles.height))
        if match is not None:
            numeric_height = int(match.group(1))
            unit_height = match.group(2)
            content.styles.height = f"{int(numeric_height)-2}{unit_height}"
        else:
            self.notify(
                severity="error",
                message=f'Wrong height style format: "{content.styles.height}"',
            )

    class AckAlert(Message):
        """A message to ack the selected alert"""

    class UnackAlert(Message):
        """A message to un-ack the selected alert"""

    class CloseAlert(Message):
        """A message to close the selected alert"""

    class GetAlertsList(Message):
        """A message to fetch alerts list"""

        def __init__(
            self,
            next: bool = False,
            previous: bool = False,
            filter_name: str | None = None,
        ):
            self.previous = previous
            self.next = next
            self.filter_name = filter_name
            super().__init__()

    class GetWhoisOnCall(Message):
        """A message to get the team member who is on call"""

    class GetAlertsCount(Message):
        """A message to get total count of alerts matching the current filter"""

        def __init__(self, parameters: dict = {}):
            self.parameters = parameters
            super().__init__()

    class TagAlert(Message):
        """A message to tag the selected alert"""

    class RemoveTagAlert(Message):
        """A message to remove tag of the selected alert"""

    class AddNote(Message):
        """A message to add note on selected alert"""

        def __init__(self, opsgenie_id: str = "", note: str = ""):
            self.opsgenie_id = opsgenie_id
            self.note = note
            super().__init__()

    class DesktopNotify(Message):
        """A message to send destop notification"""

        def __init__(self, result={}):
            self.result = result
            super().__init__()

    class LookupDataWithDelay(Message):
        """A message to proceed to getting alert list after a delay"""

        def __init__(self, delay: float = 1.75) -> None:
            self.delay = delay
            super().__init__()

    class NotifyMessage(Message):
        """A message to send in-app notification"""

        def __init__(self, message="", severity="information"):
            self.severity = severity
            self.message = message
            super().__init__()

    data = {}
    opsgenie_query = opsgenie.Query()
    page = reactive(1)
    first_alert_count = reactive(0)
    last_alert_count = reactive(0)
    current_filter = reactive("")
    total_alerts = reactive(0)
    lookup_count_rows = reactive(0)
    current_on_call_member = reactive("")

    def __init__(self):
        super().__init__()
        self.app: "TygenieApp"

    async def reload(self):
        await self.recompose()

    @work(exclusive=True, exit_on_error=True, thread=True)
    async def on_screen_resume(self):
        await self.lookup_data()

    def _update_paging_label(self):
        label = (
            f"[$accent]Page:[/] [b]{self.page}/{ceil(self.total_alerts / self.opsgenie_query.limit)}[/b]"
            f" | [$accent]Displayed:[/] [b]{self.first_alert_count}-{self.last_alert_count}/{self.total_alerts}[/b]"
            f' | [$accent]Filter:[/] [b]{config.ty_config.tygenie.get("filters", "")[self.opsgenie_query.current_filter]["description"]}[/b]'
        )

        if config.ty_config.opsgenie.get("on_call_schedule_ids"):
            label += f" | [$accent]OnCall:[/] [b]{self.current_on_call_member}[/b]"

        self.query_one("#alerts_list_switcher", ContentSwitcher).border_subtitle = (
            Content.from_markup(label)
        )

    def update_paging_label(self):
        try:
            self.query_one("#alerts_list_switcher")
        except NoMatches:
            pass
        else:
            self._update_paging_label()

    def _update_no_alert_label(self):
        filter = config.ty_config.tygenie.get("filters", "")[
            self.opsgenie_query.current_filter
        ]
        content = f"There is no alert for filter '[b]{filter['description']}[/b]' ([i]{filter['filter']}[/i])"
        self.query_one("#no_alerts_list_label", Label).update(
            content=Content.from_markup(content)
        )

    def update_no_alert_label(self):
        try:
            self.query_one("#no_alerts_list_label", Label)
        except NoMatches:
            pass
        else:
            self._update_no_alert_label()

    def watch_page(self):
        self.update_paging_label()

    def watch_current_filter(self):
        self.update_paging_label()

    def watch_total_alerts(self):
        self.update_paging_label()
        self.update_no_alert_label()

    def watch_lookup_count_rows(self):
        self.update_paging_label()

    def watch_opsgenie_query_offset(self):
        self.update_paging_label()

    def watch_first_alert_count(self):
        self.update_paging_label()

    def watch_last_alert_count(self):
        self.update_paging_label()

    def watch_current_on_call_member(self):
        self.update_paging_label()

    def _set_custom_bindings(self):
        self.app.set_keymap(
            {
                k: v
                for k, v in config.ty_config.tygenie.get("keybindings", {}).items()
                if k != "palette"
            }
        )

    def _add_filters_to_bindings(self):
        filters = config.ty_config.tygenie.get("filters", {})
        for filter_name, value in filters.items():
            self.bind(
                value["key"],
                action=f"lookup_data('{filter_name}')",
                description=f"Filter: {value['description']}",
                key_display=value["key"],
            )
        self.refresh_bindings()

    def compose(self) -> ComposeResult:
        content_switcher = ContentSwitcher(initial=None, id="alerts_list_switcher")
        content_switcher.border_title = "Alerts list"
        content_switcher.focus()

        with content_switcher:
            yield CenterMiddle(
                Label(
                    "",
                    id="no_alerts_list_label",
                ),
                id="no_alerts_list_label_container",
            )
            with Vertical(id="alerts_container"):
                yield TygenieDataTable(id="alerts_data_table")

        yield Container(
            AlertDetails(id="raw_alert_details"),
            AlertNotes(id="alert_notes"),
            AlertActionContainer(id="alert_action_container"),
            id="alert_detail_container",
        )
        self._set_custom_bindings()
        self._add_filters_to_bindings()

        footer = Footer(id="footer")
        footer.compact = True
        yield footer

    def on_data_table_row_highlighted(self, event):
        event.stop(stop=True)
        if not re.match(r"data_table_", event.row_key.value):
            return
        # Check if in config we enabled open_detail_alert_on_enter
        open_detail_alert_on_enter = config.ty_config.tygenie.get(
            "open_detail_alert_on_enter", False
        )
        if not open_detail_alert_on_enter:
            self.open_detail_and_note_alert()

    def on_data_table_row_selected(self, event):
        event.stop(stop=True)
        # Check if in config we enabled open_detail_alert_on_enter
        open_detail_alert_on_enter = config.ty_config.tygenie.get(
            "open_detail_alert_on_enter", False
        )
        if not open_detail_alert_on_enter:
            self.open_detail_and_note_alert()

    @work(exclusive=True, exit_on_error=True, thread=False)
    async def open_detail_and_note_alert(self):
        alert_note = self.query_one("#alert_notes", AlertNotes)
        raw_alert_details = self.query_one("#raw_alert_details", AlertDetails)
        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return
        asyncio.create_task(alert_note.get_alert_notes(opsgenie_id))
        asyncio.create_task(raw_alert_details.get_alert_detail(opsgenie_id))

    @on(GetWhoisOnCall)
    async def get_whois_on_call(self, message: GetWhoisOnCall):
        on_call_schedule_ids = config.ty_config.opsgenie.get("on_call_schedule_ids", [])
        self.current_on_call_member = ""
        for on_call_schedule_id in on_call_schedule_ids:
            result = await opsgenie.client.api.whois_on_call(
                parameters={"identifier": on_call_schedule_id}
            )
            if result is not None and len(result.data.on_call_recipients):
                self.current_on_call_member = re.sub(
                    "@.*$", "", result.data.on_call_recipients[0]
                )
                break
            else:
                if on_call_schedule_id == on_call_schedule_ids[-1]:
                    self.post_message(
                        self.NotifyMessage(
                            severity="error",
                            message=f"Unable to find oncall user: {result}",
                        )
                    )

    @on(GetAlertsList)
    async def _get_alerts_list_from_message(self, message: GetAlertsList):
        await self._get_alerts_list(
            previous=message.previous,
            next=message.next,
            filter_name=message.filter_name,
        )

    async def _get_alerts_list(
        self,
        previous: bool = False,
        next: bool = False,
        filter_name: str | None = None,
    ):
        parameters = self.opsgenie_query.current
        new_filter = False

        if filter_name is None:
            filter_name = self.opsgenie_query.current_filter
        elif filter_name != self.opsgenie_query.current_filter:
            new_filter = True
            # reset offset in case we are changing filter
            self.opsgenie_query.offset = 0

        if filter_name is not None:
            parameters = self.opsgenie_query.get(filter_name=filter_name)

        if previous is True:
            parameters = self.opsgenie_query.get_previous()
        elif next is True:
            parameters = self.opsgenie_query.get_next()

        self.opsgenie_query.current = parameters

        def _update_data_table(alerts=None):
            alerts_list_switcher = self.query_one(
                "#alerts_list_switcher", ContentSwitcher
            )

            if alerts is None:
                alerts_list_switcher.current = "no_alerts_list_label_container"
                return

            if not alerts.data and (previous or next):
                # keep displayed data because previous or next returned no more data
                return

            if not alerts.data and not (previous or next):
                # there is no alert, switch content
                alerts_list_switcher.current = "no_alerts_list_label_container"
                return

            table = self.query_one("#alerts_data_table", TygenieDataTable)
            table.cursor_type = "row"
            table.zebra_stripes = True
            table.show_header = True
            table.show_cursor = True
            table.cell_padding = 1

            # it means we change filter
            if filter_name is not None:
                table.focus(True)

            if not table.columns:
                table.add_columns(
                    *self.app.alerts_list_formatter.displayed_fields.values()
                )
                cursor_opsgenie_id = 0
            else:  # table exist, let's keep current selected alert
                cursor_opsgenie_id = self._get_cursor_opsgenie_id() or 0

            # Store current rows indexes to build a notifiication
            previous_rows = [r.key.value for r in table.rows.values()]
            rows_messages = []
            current_row = table.cursor_row
            row_coordinate = 0

            table.clear()

            self.page = self.opsgenie_query.current_page()
            self.current_filter = self.opsgenie_query.current_filter

            # display alerts with highest priority first
            # only sort the current page
            if config.ty_config.tygenie.get("alerts", {}).get(
                "display_page_by_priority", False
            ):
                alerts = sorted(alerts.data, key=lambda alert: alert.priority)
            else:
                alerts = alerts.data

            for index, alert in enumerate(alerts):
                key = f"data_table_{alert.id}"
                self.app.alerts_list_formatter.alert = alert
                formatted_values = self.app.alerts_list_formatter.format()
                table.add_row(
                    *tuple(
                        [
                            formatted_values[f]
                            for f in self.app.alerts_list_formatter.displayed_fields.keys()
                        ]
                    ),
                    key=key,
                )
                # If this is the alert selected before the update, keep coordinates
                # to be the one selected
                if alert.id == cursor_opsgenie_id:
                    row_coordinate = index

                # Check if this is a new alert, in such case keep the message only
                # It works if we are on first page of data
                if self.page == 1 and key not in previous_rows:
                    rows_messages.append(alert.message)

            # Compute the highlighted row depending the mode we are
            # If previous or next or new_filter => 0
            if previous:
                row_coordinate = len(alerts) - 1
            if next or new_filter:
                row_coordinate = 0
            # We did not find the alert previously highlighted
            elif row_coordinate == 0:
                if current_row <= len(alerts):
                    row_coordinate = current_row
                else:
                    row_coordinate = len(alerts) - 1

            # Move cursor to the correct alert
            table.move_cursor(row=row_coordinate)

            alerts_list_switcher.current = "alerts_container"

            result = {"rows_messages": rows_messages}
            if self.app.started and not new_filter and not next and not previous:
                self.post_message(self.DesktopNotify(result=result))

            if not self.app.started:
                # First time data are lookup, now we can flag the app as started
                self.app.started = True

        alerts = await opsgenie.client.api.list_alerts(parameters=parameters)

        if alerts is not None:
            _update_data_table(alerts)
            self._update_paging_label()
            self.lookup_count_rows = len(alerts.data)
            if not len(alerts.data) and (next or previous):
                pass
            else:
                self.first_alert_count = self.opsgenie_query.offset + 1
                self.last_alert_count = (
                    self.opsgenie_query.offset + self.lookup_count_rows
                )
        else:
            self.post_message(
                self.NotifyMessage(message="Unable to get alert list", severity="error")
            )

    @on(GetAlertsCount)
    async def get_alerts_count(self, message):
        parameters = self.opsgenie_query.current
        result = await opsgenie.client.api.count_alerts(parameters=parameters)
        if result is not None:
            self.total_alerts = result.data.count
        else:
            self.post_message(
                self.NotifyMessage(
                    severity="error", message="Unable to get alerts count"
                )
            )

    async def on_mount(self) -> None:
        self.send_lookup_data()
        refresh_period = max(60, config.ty_config.tygenie.get("refresh_period", 300))
        self.set_interval(refresh_period, self.send_lookup_data)

    def send_lookup_data(self):
        self.post_message(self.LookupDataWithDelay(delay=0))

    async def _lookup_data(self, filter_name=None, previous=False, next=False):
        # Do not lookup in case we have the modal AddNote screen pop up to
        # prevent adding a note to the wrong alert
        # (in case the alert disappear)
        if self.app.screen.name == consts.ADD_NOTE_SCREEN_NAME:
            return

        self.post_message(
            self.GetAlertsList(
                next=next,
                previous=previous,
                filter_name=filter_name,
            )
        )
        self.post_message(self.GetAlertsCount())
        self.post_message(self.GetWhoisOnCall())

    @on(DesktopNotify)
    async def desktop_notify(self, event):
        result = event.result
        dn_config = config.ty_config.tygenie.get("desktop_notification", {})
        if dn_config.get("enable", True) is True and len(result["rows_messages"]):
            if (
                dn_config.get("when_on_call_only", False) is True
                and re.sub("@.+$", "", config.ty_config.opsgenie.get("username", ""))
                != self.current_on_call_member
            ):
                # Nothing to do unless we are on call
                return

            # Urgency can be: Critical, Normal, Low
            urgency = str(dn_config.get("urgency", "Critical")).capitalize()
            messages = [f"- {r}" for r in result["rows_messages"]]
            notifier = self.app.notifier
            await notifier.send(
                title=f'Tygenie: {len(result["rows_messages"])} new alerts',
                message="\n".join(messages),
                urgency=getattr(Urgency, urgency),
            )

    async def lookup_data(self, filter_name=None):
        await self._lookup_data(filter_name=filter_name)

    @on(LookupDataWithDelay)
    @work(exclusive=True, exit_on_error=True, thread=True)
    async def lookup_data_with_delay(self, event: LookupDataWithDelay | None = None):
        if event is not None:
            time.sleep(event.delay)
        await self._lookup_data()

    # Method useed for manual refresh
    async def action_manual_refresh(self):
        self.notify("Refreshing data...")
        await self.lookup_data()

    async def action_lookup_data(self, filter_name=None):
        # Refreshing because want to filter on an other filter
        if filter_name is not None:
            self.notify(
                f"Refreshing data with filter '{filter_name}'",
                title="Filtering alerts",
                severity="information",
            )
        await self.lookup_data(filter_name=filter_name)

    @on(NotifyMessage)
    def notify_message(self, message):
        self.notify(severity=message.severity, message=message.message)

    @on(TygenieDataTable.NextPage)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def action_next_page(self, event: TygenieDataTable.NextPage | None = None):
        await self._get_alerts_list(next=True)
        if not self.lookup_count_rows:
            # reset get_next by using get_previous
            self.opsgenie_query.get_previous()
            self.post_message(self.NotifyMessage(message="No more data to fetch"))
        else:
            self.page = self.opsgenie_query.current_page()
            self.post_message(self.NotifyMessage(message=f"Page {self.page} loaded"))

    @on(TygenieDataTable.PreviousPage)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def action_previous_page(
        self, event: TygenieDataTable.PreviousPage | None = None
    ):
        if self.opsgenie_query.current_page() == 1:
            self.post_message(
                self.NotifyMessage(message="You are already on first page")
            )
        else:
            await self._get_alerts_list(previous=True)
            if not self.lookup_count_rows:
                # reset get_previous by using get_next
                self.opsgenie_query.get_next()
            else:
                self.page = self.opsgenie_query.current_page()
                self.post_message(
                    self.NotifyMessage(message=f"Page {self.page} loaded")
                )

    def _get_note_on_action(self, action):
        note_on_action = config.ty_config.tygenie.get(f"note_on_{action}", {})
        if note_on_action["enable"] is False:
            return ""
        return note_on_action["message"]

    def action_post_ack_alert(self):
        self.post_message(self.AckAlert())

    @on(AckAlert)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def ack_alert(self):
        # Check if we can ack
        current_status = self._get_cursor_status()
        if str(current_status) != "open":
            self.notify(
                severity="warning",
                message=f'Alert can not be acked because in status "{current_status}"',
            )
            return

        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        message = self._get_cursor_message()
        self.notify(f"Acking alert\n{message}")
        await opsgenie.client.api.ack_alert(
            parameters={"identifier": opsgenie_id},
            note=self._get_note_on_action("ack"),
        )
        self.post_message(self.LookupDataWithDelay(delay=1.75))

    def action_post_unack_alert(self):
        self.post_message(self.UnackAlert())

    @on(UnackAlert)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def unack_alert(self):
        current_status = self._get_cursor_status()
        if str(current_status) != "acked":
            self.notify(
                severity="warning",
                message=f'Alert can not be unacked because in status "{current_status}"',
            )
            return

        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        message = self._get_cursor_message()
        self.notify(f"Unacking alert\n{message} ...")
        await opsgenie.client.api.unack_alert(
            parameters={"identifier": opsgenie_id},
            note=self._get_note_on_action("unack"),
        )
        self.post_message(self.LookupDataWithDelay(delay=1.75))

    def action_post_close_alert(self):
        self.post_message(self.CloseAlert())

    @on(CloseAlert)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def close_alert(self):
        current_status = self._get_cursor_status()
        if str(current_status) == "closed":
            self.notify(
                severity="warning",
                message=f'Alert can not be closed because in status "{current_status}"',
            )
            return

        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        message = self._get_cursor_message()
        self.notify(f"Closing alert\n{message}...")
        await opsgenie.client.api.close_alert(
            parameters={"identifier": opsgenie_id},
            note=self._get_note_on_action("close"),
        )
        self.post_message(self.LookupDataWithDelay(delay=1.75))

    def action_post_remove_tag_alert(self):
        self.post_message(self.RemoveTagAlert())

    def _get_cursor_rowkey(self):
        dt = self.query_one("#alerts_data_table", TygenieDataTable)
        row_key, _ = dt.coordinate_to_cell_key(dt.cursor_coordinate)
        return row_key

    def _get_cursor_values(self) -> list:
        row_key = self._get_cursor_rowkey()
        dt = self.query_one("#alerts_data_table", TygenieDataTable)
        return dt.get_row(row_key)

    def _get_cursor_message(self) -> str:
        displayed_fields = [k for k in self.app.alerts_list_formatter.displayed_fields]
        return self._get_cursor_values()[displayed_fields.index("message")]

    def _get_cursor_status(self) -> str:
        displayed_fields = [k for k in self.app.alerts_list_formatter.displayed_fields]
        return self._get_cursor_values()[displayed_fields.index("status")]

    def _get_cursor_opsgenie_id(self, row_key=None) -> str | None:
        try:
            if row_key is None:
                row_key = self._get_cursor_rowkey()

            return re.sub("data_table_", "", str(row_key.value))
        except CellDoesNotExist:
            return None

    @on(AlertDetails.UpdateAlertDetails)
    def _update_alert_details(self, event):
        alert_detail_title = self.query_one("#alert_details_title", AlertDetailTitle)
        alert_detail_title.title = Content.from_markup(
            "$message", message=event.alert.message
        )

        def set_class_handler(css_class):
            classes = ["open", "closed", "acked"]
            for class_to_remove in [c for c in classes if c != css_class]:
                alert_detail_title.remove_class(class_to_remove)
            alert_detail_title.add_class(css_class)

        if event.alert.status == "open":
            if event.alert.acknowledged:
                set_class_handler("acked")
            else:
                set_class_handler("open")

        if event.alert.status == "closed":
            set_class_handler("closed")

        alert_details_details_swicher = self.query_one(
            "#alert_details_details_switcher", ContentSwitcher
        )

        if event.alert.details:
            alert_details = self.query_one("#datatable_alert_details", DataTable)
            alert_details.cursor_type = "row"
            alert_details.zebra_stripes = True
            alert_details.show_header = False
            alert_details.show_cursor = False
            alert_details.cell_padding = 1

            alert_details.clear(columns=True)
            if not alert_details.columns:
                alert_details.add_columns(*["key", "value"])
            for key, value in sorted(event.alert.details.additional_properties.items()):
                alert_details.add_row(*tuple([key, value]))

            # alert_details.update(event.alert.details)
            alert_details_details_swicher.current = "alert_detail_pretty_container"
        else:
            alert_details_details_swicher.current = "no_alert_details_label"

        alert_details_tags_swicher = self.query_one(
            "#alert_details_tags_switcher", ContentSwitcher
        )

        if event.alert.tags:
            alert_tags = self.query_one("#alert_tags_checkboxes", Tags)
            alert_tags.update(names=event.alert.tags)
            alert_details_tags_swicher.current = "alert_tags_container"
        else:
            alert_details_tags_swicher.current = "no_alert_tags_label"

        alert_details_description_swicher = self.query_one(
            "#alert_details_description_switcher", ContentSwitcher
        )

        if event.alert.description:
            alert_description = self.query_one("#pretty_alert_description", Markdown)
            self.app.alert_description_formatter.content = event.alert.description
            self.app.alert_description_formatter.format()

            alert_description.update(self.app.alert_description_formatter.content)
            alert_details_description_swicher.current = "alert_description_md_container"
        else:
            alert_details_description_swicher.current = "no_alert_description_label"

        pretty = self.query_one("#pretty_raw_alert_detail", Pretty)
        pretty.update(event.alert)

    @on(AlertNotes.UpdateAlertNotes)
    def _update_alert_notes(self, event):
        content_switcher = self.query_one("#alert_notes_switcher", ContentSwitcher)
        if len(event.alert_notes):
            md_content = ""
            date_format = config.ty_config.tygenie.get("alerts", {}).get(
                "date_format", "%d/%m %H:%M"
            )
            md = self.query_one("#md_alert_note", Markdown)
            for note in event.alert_notes:
                created_at = dtfstr(note.created_at.isoformat()).strftime(date_format)
                md_content += f"""
- *{created_at}* by **{re.sub('@.*$', '', note.owner)}**

> {note.note}
"""
            md.update(md_content)
            content_switcher.current = "alert_notes_markdown_container"
        else:
            content_switcher.current = "no_note_label"

    def _set_alerts_list_focus(self):
        self.query_one("#alerts_data_table", TygenieDataTable).focus()

    def action_alerts_list_focus(self):
        self._set_alerts_list_focus()

    def _set_alert_details_focus(self):
        self.app.query_one(
            "#alert_detail_tabbed_content", AlertDetailsTabbedContent
        ).focus()

    def action_alert_details_focus(self):
        self._set_alert_details_focus()

    def _set_alert_notes_focus(self):
        self.app.query_one("#alert_notes", AlertNotes).focus()

    def action_alert_notes_focus(self):
        self._set_alert_notes_focus()

    def _notify_invalid_opsgenie_id(self):
        self.notify(message="No valid opsgenie id found", severity="error")

    @on(AlertActionContainer.OpenInBrowser)
    def open_in_webbrowser(self):
        # keep focus on alert list
        self._set_alerts_list_focus()
        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        webapp_url = config.ty_config.opsgenie.get("webapp_url")
        webbrowser.open_new_tab(f"{webapp_url}/alert/detail/{opsgenie_id}/details")

    def action_open_in_webbrowser(self):
        self.open_in_webbrowser()

    @on(TagAlert)
    @on(AlertActionContainer.AddTag)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def tag_alert(self):
        tag_value = self.query_one(
            "#alert_action_container", AlertActionContainer
        ).tag_value

        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        message = self._get_cursor_message()
        self.notify(f'Adding tag "{tag_value}" on alert: \n{message}')
        note = f"{self._get_note_on_action('tag')}".format(tag=tag_value)
        await opsgenie.client.api.tag_alert(
            parameters={"identifier": opsgenie_id}, tags=[tag_value], note=note
        )
        self.post_message(self.LookupDataWithDelay(delay=1.75))

    def action_post_tag_alert(self):
        self.post_message(self.TagAlert())

    @on(RemoveTagAlert)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def remove_default_tag_from_selected_alert(self):
        tag: Input = self.query_one(
            "#alert_action_container", AlertActionContainer
        ).query_one("#tag_input", Input)

        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        message = self._get_cursor_message()
        self.notify(f'Removing tag "{tag.value}" on alert: \n{message}')
        note = f"{self._get_note_on_action('untag')}".format(tag=tag.value)
        await opsgenie.client.api.remove_tag_alert(
            parameters={"identifier": opsgenie_id}, tags=[tag.value], note=note
        )
        self.post_message(self.LookupDataWithDelay(delay=1.75))

    @on(Tags.RemoveTag)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def remove_tag(self, tag):
        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        message = self._get_cursor_message()
        self.notify(f'Removing tag "{tag.value}" on alert: \n{message}')

        await opsgenie.client.api.remove_tag_alert(
            parameters={"identifier": opsgenie_id}, tags=[tag.value]
        )
        self.post_message(self.LookupDataWithDelay(delay=1.75))

    @on(AddNote)
    async def _add_note_from_message(self, message: AddNote):
        opsgenie_id: str = message.opsgenie_id
        note: str = message.note
        if not note or not opsgenie_id:
            return
        await opsgenie.client.api.add_note(
            parameters={"identifier": opsgenie_id}, note=note
        )

    @on(AlertActionContainer.AddNote)
    @work(exclusive=True, exit_on_error=False, thread=False)
    async def action_open_add_note(self):
        opsgenie_id = self._get_cursor_opsgenie_id()
        if opsgenie_id is None:
            self._notify_invalid_opsgenie_id()
            return

        async def _add_note(result):
            await opsgenie.client.api.add_note(
                parameters={"identifier": opsgenie_id}, note=result
            )
            if result and not re.match("^\n+$", result):
                self.notify(f"Note added to alert #f{opsgenie_id}")
                self.post_message(self.LookupDataWithDelay(delay=1))

        self.app.push_screen("add_note", _add_note)
