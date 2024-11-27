import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.heartbeat_interval_unit import HeartbeatIntervalUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="Heartbeat")


@_attrs_define
class Heartbeat:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        interval (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        interval_unit (Union[Unset, HeartbeatIntervalUnit]):
        expired (Union[Unset, bool]):
        last_ping_time (Union[Unset, datetime.datetime]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    interval: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    interval_unit: Union[Unset, HeartbeatIntervalUnit] = UNSET
    expired: Union[Unset, bool] = UNSET
    last_ping_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        interval = self.interval

        enabled = self.enabled

        interval_unit: Union[Unset, str] = UNSET
        if not isinstance(self.interval_unit, Unset):
            interval_unit = self.interval_unit.value

        expired = self.expired

        last_ping_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_ping_time, Unset):
            last_ping_time = self.last_ping_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if interval is not UNSET:
            field_dict["interval"] = interval
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if interval_unit is not UNSET:
            field_dict["intervalUnit"] = interval_unit
        if expired is not UNSET:
            field_dict["expired"] = expired
        if last_ping_time is not UNSET:
            field_dict["lastPingTime"] = last_ping_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        interval = d.pop("interval", UNSET)

        enabled = d.pop("enabled", UNSET)

        _interval_unit = d.pop("intervalUnit", UNSET)
        interval_unit: Union[Unset, HeartbeatIntervalUnit]
        if isinstance(_interval_unit, Unset):
            interval_unit = UNSET
        else:
            interval_unit = HeartbeatIntervalUnit(_interval_unit)

        expired = d.pop("expired", UNSET)

        _last_ping_time = d.pop("lastPingTime", UNSET)
        last_ping_time: Union[Unset, datetime.datetime]
        if isinstance(_last_ping_time, Unset):
            last_ping_time = UNSET
        else:
            last_ping_time = isoparse(_last_ping_time)

        heartbeat = cls(
            name=name,
            description=description,
            interval=interval,
            enabled=enabled,
            interval_unit=interval_unit,
            expired=expired,
            last_ping_time=last_ping_time,
        )

        heartbeat.additional_properties = d
        return heartbeat

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
