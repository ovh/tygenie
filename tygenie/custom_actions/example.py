from tygenie.custom_actions.custom_action import CustomAction
from tygenie.screens.alerts import AlertsScreen

class ExampleAction(CustomAction):
    """An Example action that notifies the user that the action was executed.

    To use it, add `tygenie.custom_actions.example: { "key": "e" }` in your
    configuration.
    """

    screen_name="alerts"
    description="Example"

    @staticmethod
    def function(screen: AlertsScreen):
        screen.escaped_notify(f"Example command triggered!")

action = ExampleAction
