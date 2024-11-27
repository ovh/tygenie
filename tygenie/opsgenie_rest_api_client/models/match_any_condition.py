from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_type import FilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition import Condition


T = TypeVar("T", bound="MatchAnyCondition")


@_attrs_define
class MatchAnyCondition:
    """Match any condition filter

    Attributes:
        type (FilterType):
        conditions (Union[Unset, List['Condition']]):
    """

    type: FilterType
    conditions: Union[Unset, List["Condition"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition import Condition

        d = src_dict.copy()
        type = FilterType(d.pop("type"))

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = Condition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        match_any_condition = cls(
            type=type,
            conditions=conditions,
        )

        match_any_condition.additional_properties = d
        return match_any_condition

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
