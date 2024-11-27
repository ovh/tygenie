from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Checkbox


class Checkboxes(Widget):

    names = reactive("names", recompose=True)

    def __init__(self, names: list[str] = [], **kwargs):
        super().__init__(**kwargs)
        self.names: list[str] = names

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            for name in self.names:
                yield Checkbox(name, value=True, name=name)

    def update(self, names: list[str]):
        self.names = names
