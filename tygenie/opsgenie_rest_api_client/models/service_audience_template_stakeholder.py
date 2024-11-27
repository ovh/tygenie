from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_audience_template_stakeholder_condition_match_type import (
    ServiceAudienceTemplateStakeholderConditionMatchType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_audience_template_condition import ServiceAudienceTemplateCondition


T = TypeVar("T", bound="ServiceAudienceTemplateStakeholder")


@_attrs_define
class ServiceAudienceTemplateStakeholder:
    """
    Attributes:
        individuals (Union[Unset, List[str]]):
        condition_match_type (Union[Unset, ServiceAudienceTemplateStakeholderConditionMatchType]): Match type for given
            conditions. Possible values are [match-all-conditions, match-any-condition]. Default value is [match-any-
            condition].
        conditions (Union[Unset, List['ServiceAudienceTemplateCondition']]):
    """

    individuals: Union[Unset, List[str]] = UNSET
    condition_match_type: Union[Unset, ServiceAudienceTemplateStakeholderConditionMatchType] = UNSET
    conditions: Union[Unset, List["ServiceAudienceTemplateCondition"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        individuals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.individuals, Unset):
            individuals = self.individuals

        condition_match_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_match_type, Unset):
            condition_match_type = self.condition_match_type.value

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individuals is not UNSET:
            field_dict["individuals"] = individuals
        if condition_match_type is not UNSET:
            field_dict["conditionMatchType"] = condition_match_type
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_audience_template_condition import ServiceAudienceTemplateCondition

        d = src_dict.copy()
        individuals = cast(List[str], d.pop("individuals", UNSET))

        _condition_match_type = d.pop("conditionMatchType", UNSET)
        condition_match_type: Union[Unset, ServiceAudienceTemplateStakeholderConditionMatchType]
        if isinstance(_condition_match_type, Unset):
            condition_match_type = UNSET
        else:
            condition_match_type = ServiceAudienceTemplateStakeholderConditionMatchType(_condition_match_type)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ServiceAudienceTemplateCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        service_audience_template_stakeholder = cls(
            individuals=individuals,
            condition_match_type=condition_match_type,
            conditions=conditions,
        )

        service_audience_template_stakeholder.additional_properties = d
        return service_audience_template_stakeholder

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
