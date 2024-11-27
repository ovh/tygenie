from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_heartbeat_payload_interval_unit import UpdateHeartbeatPayloadIntervalUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateHeartbeatPayload")


@_attrs_define
class UpdateHeartbeatPayload:
    """
    Attributes:
        description (Union[Unset, str]): An optional description of the heartbeat
        interval (Union[Unset, int]): Specifies how often a heartbeat message should be expected
        interval_unit (Union[Unset, UpdateHeartbeatPayloadIntervalUnit]): Interval specified as 'minutes', 'hours' or
            'days'
        enabled (Union[Unset, bool]): Enable/disable heartbeat monitoring
    """

    description: Union[Unset, str] = UNSET
    interval: Union[Unset, int] = UNSET
    interval_unit: Union[Unset, UpdateHeartbeatPayloadIntervalUnit] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        interval = self.interval

        interval_unit: Union[Unset, str] = UNSET
        if not isinstance(self.interval_unit, Unset):
            interval_unit = self.interval_unit.value

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if interval is not UNSET:
            field_dict["interval"] = interval
        if interval_unit is not UNSET:
            field_dict["intervalUnit"] = interval_unit
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        interval = d.pop("interval", UNSET)

        _interval_unit = d.pop("intervalUnit", UNSET)
        interval_unit: Union[Unset, UpdateHeartbeatPayloadIntervalUnit]
        if isinstance(_interval_unit, Unset):
            interval_unit = UNSET
        else:
            interval_unit = UpdateHeartbeatPayloadIntervalUnit(_interval_unit)

        enabled = d.pop("enabled", UNSET)

        update_heartbeat_payload = cls(
            description=description,
            interval=interval,
            interval_unit=interval_unit,
            enabled=enabled,
        )

        update_heartbeat_payload.additional_properties = d
        return update_heartbeat_payload

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
