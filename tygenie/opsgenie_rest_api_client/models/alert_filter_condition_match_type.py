from enum import Enum


class AlertFilterConditionMatchType(str, Enum):
    MATCH_ALL = "match-all"
    MATCH_ALL_CONDITIONS = "match-all-conditions"
    MATCH_ANY_CONDITION = "match-any-condition"

    def __str__(self) -> str:
        return str(self.value)
