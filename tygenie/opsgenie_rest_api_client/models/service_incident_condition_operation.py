from enum import Enum


class ServiceIncidentConditionOperation(str, Enum):
    CONTAINS = "contains"
    CONTAINS_KEY = "contains-key"
    CONTAINS_VALUE = "contains-value"
    ENDS_WITH = "ends-with"
    EQUALS = "equals"
    EQUALS_IGNORE_WHITESPACE = "equals-ignore-whitespace"
    GREATER_THAN = "greater-than"
    IS_EMPTY = "is-empty"
    LESS_THAN = "less-than"
    MATCHES = "matches"
    STARTS_WITH = "starts-with"

    def __str__(self) -> str:
        return str(self.value)
