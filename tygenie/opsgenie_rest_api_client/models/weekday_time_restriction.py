from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.weekday_time_restriction_end_day import WeekdayTimeRestrictionEndDay
from ..models.weekday_time_restriction_start_day import WeekdayTimeRestrictionStartDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="WeekdayTimeRestriction")


@_attrs_define
class WeekdayTimeRestriction:
    """
    Attributes:
        start_day (Union[Unset, WeekdayTimeRestrictionStartDay]):
        start_hour (Union[Unset, int]):
        start_min (Union[Unset, int]):
        end_day (Union[Unset, WeekdayTimeRestrictionEndDay]):
        end_hour (Union[Unset, int]):
        end_min (Union[Unset, int]):
    """

    start_day: Union[Unset, WeekdayTimeRestrictionStartDay] = UNSET
    start_hour: Union[Unset, int] = UNSET
    start_min: Union[Unset, int] = UNSET
    end_day: Union[Unset, WeekdayTimeRestrictionEndDay] = UNSET
    end_hour: Union[Unset, int] = UNSET
    end_min: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_day: Union[Unset, str] = UNSET
        if not isinstance(self.start_day, Unset):
            start_day = self.start_day.value

        start_hour = self.start_hour

        start_min = self.start_min

        end_day: Union[Unset, str] = UNSET
        if not isinstance(self.end_day, Unset):
            end_day = self.end_day.value

        end_hour = self.end_hour

        end_min = self.end_min

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_day is not UNSET:
            field_dict["startDay"] = start_day
        if start_hour is not UNSET:
            field_dict["startHour"] = start_hour
        if start_min is not UNSET:
            field_dict["startMin"] = start_min
        if end_day is not UNSET:
            field_dict["endDay"] = end_day
        if end_hour is not UNSET:
            field_dict["endHour"] = end_hour
        if end_min is not UNSET:
            field_dict["endMin"] = end_min

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_day = d.pop("startDay", UNSET)
        start_day: Union[Unset, WeekdayTimeRestrictionStartDay]
        if isinstance(_start_day, Unset):
            start_day = UNSET
        else:
            start_day = WeekdayTimeRestrictionStartDay(_start_day)

        start_hour = d.pop("startHour", UNSET)

        start_min = d.pop("startMin", UNSET)

        _end_day = d.pop("endDay", UNSET)
        end_day: Union[Unset, WeekdayTimeRestrictionEndDay]
        if isinstance(_end_day, Unset):
            end_day = UNSET
        else:
            end_day = WeekdayTimeRestrictionEndDay(_end_day)

        end_hour = d.pop("endHour", UNSET)

        end_min = d.pop("endMin", UNSET)

        weekday_time_restriction = cls(
            start_day=start_day,
            start_hour=start_hour,
            start_min=start_min,
            end_day=end_day,
            end_hour=end_hour,
            end_min=end_min,
        )

        weekday_time_restriction.additional_properties = d
        return weekday_time_restriction

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
