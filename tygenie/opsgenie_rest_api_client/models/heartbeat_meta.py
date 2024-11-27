from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeartbeatMeta")


@_attrs_define
class HeartbeatMeta:
    """
    Attributes:
        name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        expired (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    expired: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        enabled = self.enabled

        expired = self.expired

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if expired is not UNSET:
            field_dict["expired"] = expired

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        expired = d.pop("expired", UNSET)

        heartbeat_meta = cls(
            name=name,
            enabled=enabled,
            expired=expired,
        )

        heartbeat_meta.additional_properties = d
        return heartbeat_meta

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
