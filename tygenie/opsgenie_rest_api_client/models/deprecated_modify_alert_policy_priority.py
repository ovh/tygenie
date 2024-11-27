from enum import Enum


class DeprecatedModifyAlertPolicyPriority(str, Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"
    P5 = "P5"

    def __str__(self) -> str:
        return str(self.value)
