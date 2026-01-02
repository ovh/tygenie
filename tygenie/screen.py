from textual.screen import Screen
from tygenie.custom_actions.custom_action import CustomAction


class TyScreen(Screen):

    def bind(
        self,
        keys: str,
        action: str,
        *,
        description: str = "",
        show: bool = True,
        key_display: str | None = None,
    ) -> None:
        """Bind a key to an action.

        Args:
            keys: A comma separated list of keys, i.e.
            action: Action to bind to.
            description: Short description of action.
            show: Show key in UI.
            key_display: Replacement text for key, or None to use default.
        """
        self._bindings.bind(
            keys, action, description, show=show, key_display=key_display
        )

    def register_action(self, name: str, key: str, action: CustomAction) -> None:
        """Register a method to run when pressing a key.

        Args:
            name: Unique name of the action.
            key: The key that will trigger the action.
            action: CustomAction to bind to.
        """
        self.bind(
            key,
            action=f"{name}()",
            description=action.description,
            key_display=key
        )
        self.refresh_bindings()
        setattr(self.__class__, f"action_{name}", action.function)
