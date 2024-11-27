from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delay_action_delay_option import DelayActionDelayOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="DelayAction")


@_attrs_define
class DelayAction:
    """
    Attributes:
        delay_option (DelayActionDelayOption):
        until_hour (Union[Unset, int]):
        until_minute (Union[Unset, int]):
        duration (Union[Unset, Duration]):
    """

    delay_option: DelayActionDelayOption
    until_hour: Union[Unset, int] = UNSET
    until_minute: Union[Unset, int] = UNSET
    duration: Union[Unset, "Duration"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delay_option = self.delay_option.value

        until_hour = self.until_hour

        until_minute = self.until_minute

        duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delayOption": delay_option,
            }
        )
        if until_hour is not UNSET:
            field_dict["untilHour"] = until_hour
        if until_minute is not UNSET:
            field_dict["untilMinute"] = until_minute
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        delay_option = DelayActionDelayOption(d.pop("delayOption"))

        until_hour = d.pop("untilHour", UNSET)

        until_minute = d.pop("untilMinute", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, Duration]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = Duration.from_dict(_duration)

        delay_action = cls(
            delay_option=delay_option,
            until_hour=until_hour,
            until_minute=until_minute,
            duration=duration,
        )

        delay_action.additional_properties = d
        return delay_action

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
