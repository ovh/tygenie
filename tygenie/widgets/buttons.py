from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widget import Widget

from tygenie.widgets.button import TyButtonOpenInWebBrowser


class Buttons(Widget):

    names = reactive("names", recompose=True)

    def __init__(self, names: list[tuple] = [], **kwargs):
        super().__init__(**kwargs)
        self.names_urls = names

    def compose(self) -> ComposeResult:
        with Horizontal():
            for name, _ in self.names_urls:
                yield TyButtonOpenInWebBrowser(label=name, name=name)

    def update(self, names_urls: list[tuple]):
        self.names_urls = names_urls
