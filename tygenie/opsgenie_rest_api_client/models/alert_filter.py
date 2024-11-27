from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_filter_condition_match_type import AlertFilterConditionMatchType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.callback_condition import CallbackCondition


T = TypeVar("T", bound="AlertFilter")


@_attrs_define
class AlertFilter:
    """
    Attributes:
        condition_match_type (Union[Unset, AlertFilterConditionMatchType]):
        conditions (Union[Unset, List['CallbackCondition']]):
    """

    condition_match_type: Union[Unset, AlertFilterConditionMatchType] = UNSET
    conditions: Union[Unset, List["CallbackCondition"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        if condition_match_type is not UNSET:
            field_dict["conditionMatchType"] = condition_match_type
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.callback_condition import CallbackCondition

        d = src_dict.copy()
        _condition_match_type = d.pop("conditionMatchType", UNSET)
        condition_match_type: Union[Unset, AlertFilterConditionMatchType]
        if isinstance(_condition_match_type, Unset):
            condition_match_type = UNSET
        else:
            condition_match_type = AlertFilterConditionMatchType(_condition_match_type)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = CallbackCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        alert_filter = cls(
            condition_match_type=condition_match_type,
            conditions=conditions,
        )

        alert_filter.additional_properties = d
        return alert_filter

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