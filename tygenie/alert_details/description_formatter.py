import re
from importlib import import_module

from markdownify import markdownify as md
from textual import log


class BaseContentFormatter:

    def __init__(self, content: str = "") -> None:
        self.execution_order = {"pre": [], "post": []}
        self.content = content
        self.methods = []

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.methods = sorted(dir(cls))

    def _format(self, step: str = ""):
        if not step:
            return

        for method in self.execution_order[step]:
            if method.startswith(f"{step}_substitute_"):
                result = getattr(self, method)()
                log(
                    f"Substituing method {method}: {result['regexp']} by {result['sub']}"
                )
                self.content = re.sub(result["regexp"], result["sub"], self.content)
                continue

            if method.startswith(f"{step}_custom_"):
                log(f"Running custom method {method}")
                getattr(self, method)()
                continue

    def _pre_format(self):
        self._format(step="pre")

    def _post_format(self):
        self._format(step="post")

    def format(self):
        self._pre_format()
        self.content = md(
            self.content,
            default_title=True,
            escape_misc=False,
            escape_asterisks=False,
            escape_underscores=False,
        )
        self._post_format()
        return self.content


class ContentFormatter:

    def __init__(self, content: str = "", formatter: str | None = None) -> None:
        self.content: str = content
        self.formatter: str | None = formatter
        if formatter is None:
            self.module = import_module("tygenie.alert_details.description_formatter")
            self.formatter = "DefaultContentFormatter"
        else:
            self.module = import_module(
                f"tygenie.plugins.{self.formatter}.alert_description_formatter"
            )

    def format(self):
        self.content = getattr(self.module, self.formatter)(
            content=self.content
        ).format()
        return self.content


class DefaultContentFormatter(BaseContentFormatter):
    """Default content formatter"""
