from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Input, Static

import tygenie.config as config


class TagValueInput(Widget):

    def compose(self) -> ComposeResult:
        default_tag = config.ty_config.tygenie.get("default_tag", "")
        tag_label: Static = Static(
            name="tag_label", id="tag_label", content="Tag value: "
        )
        tag_input: Input = Input(name="tag_input", id="tag_input", value=default_tag)
        yield HorizontalGroup(tag_label, tag_input, id="tag_value_horizontal_group")

    class TagValueChange(Message):
        """A message to indicate that we tag value changed"""

        def __init__(self, label: str | None = None):
            self.label = label
            super().__init__()

    def on_input_submitted(self, submit: Input.Submitted):
        if submit.input.id == "tag_input":
            self.notify(
                severity="information", message=f"tag is now set to '{submit.value}'"
            )
            tag = self.query_one("#tag_input", Input)
            self.post_message(self.TagValueChange(label=tag.value))
            self.app.query_one("#alerts_data_table").focus(True)
