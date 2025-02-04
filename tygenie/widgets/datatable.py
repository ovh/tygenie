from textual import events
from textual.binding import Binding
from textual.message import Message
from textual.widgets import DataTable


class TygenieDataTable(DataTable, inherit_bindings=False):
    BINDINGS = [
        Binding(
            "G,pageup",
            "cursor_up_or_previous_page",
            "Go on first alert or load previous page",
            show=False,
        ),
        Binding(
            "g,pagedown",
            "cursor_down_or_next_page",
            "Go on last alert or load next page",
            show=False,
        ),
    ]

    class NextPage(Message):
        """Send a message to request next page"""

    class PreviousPage(Message):
        """Send a message to request previous page"""

    async def on_mouse_scroll_up(self, event):
        self.action_cursor_up()

    async def on_mouse_scroll_down(self, event):
        self.action_cursor_down()

    def on_key(self, event: events.Key) -> None:
        if event.key == "up":
            if self.cursor_row == 0:
                self.action_cursor_up_or_previous_page()
            else:
                self.action_cursor_up()
        elif event.key == "down":
            if self.cursor_row == self.row_count - 1:
                self.action_cursor_down_or_next_page()
            else:
                self.action_cursor_down()
        elif event.key == "left":
            self.post_message(self.PreviousPage())
        elif event.key == "right":
            self.post_message(self.NextPage())

    def action_cursor_up_or_previous_page(self):
        if self.cursor_row > 0:
            self.action_scroll_top()
        elif self.cursor_row == 0:
            self.post_message(self.PreviousPage())

    def action_cursor_down_or_next_page(self):
        if self.cursor_row < self.row_count - 1:
            self.action_scroll_bottom()
        elif self.cursor_row == self.row_count - 1:
            self.post_message(self.NextPage())
