from enum import Enum


class EscalationRuleCondition(str, Enum):
    IF_NOT_ACKED = "if-not-acked"
    IF_NOT_CLOSED = "if-not-closed"

    def __str__(self) -> str:
        return str(self.value)
