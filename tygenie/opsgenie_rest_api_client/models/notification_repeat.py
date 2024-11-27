from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationRepeat")


@_attrs_define
class NotificationRepeat:
    """The amount of time in minutes that notification steps will be repeatedly apply

    Attributes:
        loop_after (Union[Unset, int]):
        enabled (Union[Unset, bool]):
    """

    loop_after: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        loop_after = self.loop_after

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loop_after is not UNSET:
            field_dict["loopAfter"] = loop_after
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        loop_after = d.pop("loopAfter", UNSET)

        enabled = d.pop("enabled", UNSET)

        notification_repeat = cls(
            loop_after=loop_after,
            enabled=enabled,
        )

        notification_repeat.additional_properties = d
        return notification_repeat

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
