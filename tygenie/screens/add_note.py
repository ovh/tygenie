from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Label, TextArea


class AddNoteScreen(ModalScreen):
    """Screen with a textbox to add a note to an alert"""

    BINDINGS = [
        Binding(
            key="escape",
            action="close_modal()",
            description="Close",
            key_display="<esc>",
        ),
    ]

    def compose(self) -> ComposeResult:
        yield Label("[b]Add a note to alert[/b]")
        message = ""
        textarea = TextArea(message, language=None, id="add_note_textarea")
        textarea.language = "markdown"
        textarea.show_line_numbers = True
        yield Grid(
            textarea,
            Button("Cancel", variant="error", id="cancel"),
            Button("Add", variant="success", id="add"),
            id="add_note_grid",
        )
        yield Footer()

    def action_close_modal(self, note: None | str = None):
        textarea = self.query_one("#add_note_textarea", TextArea)
        textarea.focus(True)
        textarea.clear()
        self.dismiss(result=note)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        note = ""
        if event.button.id == "add":
            textarea = self.query_one("#add_note_textarea", TextArea)
            note = textarea.text

        self.action_close_modal(note=note)
