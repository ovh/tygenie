from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Checkbox
from typing import List


class Checkboxes(Widget):

    names: reactive[List[str]] = reactive([], recompose=True)

    def __init__(self, names: list[str] = [], **kwargs):
        super().__init__(**kwargs)
        if names:
            self.update(names=names)

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            for name in self.names:
                yield Checkbox(name, value=True, name=name)

    def update(self, names: List[str]):
        self.names = names

    def watch_names(self, names: List[str]):
        self.update(names=names)
