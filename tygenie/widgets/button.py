import webbrowser

from textual.widgets import Button


class TyButtonOpenInWebBrowser(Button):

    def __init__(self, href: str = "", **kwargs):
        super().__init__(**kwargs)
        self.href = href

    def on_button_pressed(self, event: Button.Pressed) -> None:
        webbrowser.open_new_tab(self.href)
