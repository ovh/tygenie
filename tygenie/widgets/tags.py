from textual.message import Message

from tygenie.widgets.checkboxes import Checkboxes


class Tags(Checkboxes):

    class RemoveTag(Message):
        """Posted when a tag has to be removed"""

        def __init__(self, value: str = ""):
            self.value = value
            super().__init__()

    async def on_checkbox_changed(self, event):
        if event.value is False:  # unchecked
            event.checkbox.disabled = True
            if self.post_message(self.RemoveTag(value=event.checkbox.name)):
                if event.checkbox.name in self.names:
                    self.names.remove(event.checkbox.name)
                    await self.recompose()
