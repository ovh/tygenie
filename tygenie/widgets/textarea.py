from textual.binding import Binding
from textual.widgets import TextArea


class TygenieTextArea(TextArea, inherit_bindings=False):
    BINDINGS = [
        Binding("up", "cursor_up", "Cursor up", show=False),
        Binding("down", "cursor_down", "Cursor down", show=False),
        Binding("left", "cursor_left", "Cursor left", show=False),
        Binding("right", "cursor_right", "Cursor right", show=False),
        Binding("ctrl+left", "cursor_word_left", "Cursor word left", show=False),
        Binding("ctrl+right", "cursor_word_right", "Cursor word right", show=False),
        Binding("home", "cursor_line_start", "Cursor line start", show=False),
        Binding("end,ctrl+e", "cursor_line_end", "Cursor line end", show=False),
        Binding("pageup", "cursor_page_up", "Cursor page up", show=False),
        Binding("pagedown", "cursor_page_down", "Cursor page down", show=False),
        # Making selections (generally holding the shift key and moving cursor)
        Binding(
            "ctrl+shift+left",
            "cursor_word_left(True)",
            "Cursor left word select",
            show=False,
        ),
        Binding(
            "ctrl+shift+right",
            "cursor_word_right(True)",
            "Cursor right word select",
            show=False,
        ),
        Binding(
            "shift+home",
            "cursor_line_start(True)",
            "Cursor line start select",
            show=False,
        ),
        Binding(
            "shift+end", "cursor_line_end(True)", "Cursor line end select", show=False
        ),
        Binding("shift+up", "cursor_up(True)", "Cursor up select", show=False),
        Binding("shift+down", "cursor_down(True)", "Cursor down select", show=False),
        Binding("shift+left", "cursor_left(True)", "Cursor left select", show=False),
        Binding("shift+right", "cursor_right(True)", "Cursor right select", show=False),
        # Shortcut ways of making selections
        # Binding("f5", "select_word", "select word", show=False),
        Binding("f6", "select_line", "Select line", show=False),
        Binding("f7", "select_all", "Select all", show=False),
        # Deletion
        Binding("backspace", "delete_left", "Delete character left", show=False),
        Binding(
            "ctrl+w", "delete_word_left", "Delete left to start of word", show=False
        ),
        Binding("delete,ctrl+d", "delete_right", "Delete character right", show=False),
        Binding(
            "ctrl+f", "delete_word_right", "Delete right to start of word", show=False
        ),
        Binding("ctrl+x", "delete_line", "Delete line", show=False),
        Binding(
            "ctrl+u", "delete_to_start_of_line", "Delete to line start", show=False
        ),
        Binding(
            "ctrl+k",
            "delete_to_end_of_line_or_delete_line",
            "Delete to line end",
            show=False,
        ),
        Binding("ctrl+z", "undo", "Undo", show=False),
        Binding("ctrl+y", "redo", "Redo", show=False),
    ]
