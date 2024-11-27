from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="AutoRestartAction")


@_attrs_define
class AutoRestartAction:
    """
    Attributes:
        duration (Duration):
        max_repeat_count (int):
    """

    duration: "Duration"
    max_repeat_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration = self.duration.to_dict()

        max_repeat_count = self.max_repeat_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "maxRepeatCount": max_repeat_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        duration = Duration.from_dict(d.pop("duration"))

        max_repeat_count = d.pop("maxRepeatCount")

        auto_restart_action = cls(
            duration=duration,
            max_repeat_count=max_repeat_count,
        )

        auto_restart_action.additional_properties = d
        return auto_restart_action

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
