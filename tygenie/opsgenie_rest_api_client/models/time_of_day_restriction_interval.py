from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_restriction_interval_type import TimeRestrictionIntervalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_of_day_restriction import TimeOfDayRestriction


T = TypeVar("T", bound="TimeOfDayRestrictionInterval")


@_attrs_define
class TimeOfDayRestrictionInterval:
    """Time of day restriction interval

    Attributes:
        type (TimeRestrictionIntervalType):
        restriction (Union[Unset, TimeOfDayRestriction]):
    """

    type: TimeRestrictionIntervalType
    restriction: Union[Unset, "TimeOfDayRestriction"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restriction, Unset):
            restriction = self.restriction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if restriction is not UNSET:
            field_dict["restriction"] = restriction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_of_day_restriction import TimeOfDayRestriction

        d = src_dict.copy()
        type = TimeRestrictionIntervalType(d.pop("type"))

        _restriction = d.pop("restriction", UNSET)
        restriction: Union[Unset, TimeOfDayRestriction]
        if isinstance(_restriction, Unset):
            restriction = UNSET
        else:
            restriction = TimeOfDayRestriction.from_dict(_restriction)

        time_of_day_restriction_interval = cls(
            type=type,
            restriction=restriction,
        )

        time_of_day_restriction_interval.additional_properties = d
        return time_of_day_restriction_interval

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
