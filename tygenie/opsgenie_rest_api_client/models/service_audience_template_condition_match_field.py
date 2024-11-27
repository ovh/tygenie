from enum import Enum


class ServiceAudienceTemplateConditionMatchField(str, Enum):
    CITY = "city"
    COUNTRY = "country"
    CUSTOMPROPERTY = "customProperty"
    LINE = "line"
    STATE = "state"
    TAG = "tag"
    ZIPCODE = "zipCode"

    def __str__(self) -> str:
        return str(self.value)
