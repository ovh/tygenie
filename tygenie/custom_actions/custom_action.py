from collections.abc import Callable

class CustomAction:
    """Action executed on `screen_name` when a keybinding is triggered.

    `function` is a method that has a single argument `screen` which will be the
    screen object referenced by `screen_name`.
    """
    description: str
    function: Callable
    screen_name: str
