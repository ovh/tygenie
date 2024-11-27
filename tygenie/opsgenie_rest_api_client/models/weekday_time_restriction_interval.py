from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_restriction_interval_type import TimeRestrictionIntervalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weekday_time_restriction import WeekdayTimeRestriction


T = TypeVar("T", bound="WeekdayTimeRestrictionInterval")


@_attrs_define
class WeekdayTimeRestrictionInterval:
    """Weekday time restriction interval

    Attributes:
        type (TimeRestrictionIntervalType):
        restrictions (Union[Unset, List['WeekdayTimeRestriction']]):
    """

    type: TimeRestrictionIntervalType
    restrictions: Union[Unset, List["WeekdayTimeRestriction"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        restrictions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = []
            for restrictions_item_data in self.restrictions:
                restrictions_item = restrictions_item_data.to_dict()
                restrictions.append(restrictions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.weekday_time_restriction import WeekdayTimeRestriction

        d = src_dict.copy()
        type = TimeRestrictionIntervalType(d.pop("type"))

        restrictions = []
        _restrictions = d.pop("restrictions", UNSET)
        for restrictions_item_data in _restrictions or []:
            restrictions_item = WeekdayTimeRestriction.from_dict(restrictions_item_data)

            restrictions.append(restrictions_item)

        weekday_time_restriction_interval = cls(
            type=type,
            restrictions=restrictions,
        )

        weekday_time_restriction_interval.additional_properties = d
        return weekday_time_restriction_interval

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
