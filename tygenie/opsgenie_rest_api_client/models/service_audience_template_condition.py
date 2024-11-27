from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_audience_template_condition_match_field import ServiceAudienceTemplateConditionMatchField
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAudienceTemplateCondition")


@_attrs_define
class ServiceAudienceTemplateCondition:
    """
    Attributes:
        match_field (ServiceAudienceTemplateConditionMatchField): Field to be matched for users. Possible values are
            [country, state, city, zipCode, line, tag, customProperty]. customProperty can be used while actionType is
            keyValue.
        value (str): Value to be check for the match field.
        key (Union[Unset, str]): If matchField is customProperty, key must be given.
    """

    match_field: ServiceAudienceTemplateConditionMatchField
    value: str
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_field = self.match_field.value

        value = self.value

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matchField": match_field,
                "value": value,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_field = ServiceAudienceTemplateConditionMatchField(d.pop("matchField"))

        value = d.pop("value")

        key = d.pop("key", UNSET)

        service_audience_template_condition = cls(
            match_field=match_field,
            value=value,
            key=key,
        )

        service_audience_template_condition.additional_properties = d
        return service_audience_template_condition

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
