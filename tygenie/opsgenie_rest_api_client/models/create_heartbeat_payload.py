from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_heartbeat_payload_alert_priority import CreateHeartbeatPayloadAlertPriority
from ..models.create_heartbeat_payload_interval_unit import CreateHeartbeatPayloadIntervalUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_heartbeat_payload_owner_team import CreateHeartbeatPayloadOwnerTeam


T = TypeVar("T", bound="CreateHeartbeatPayload")


@_attrs_define
class CreateHeartbeatPayload:
    """
    Attributes:
        name (str): Name of the heartbeat
        interval (int): Specifies how often a heartbeat message should be expected
        interval_unit (CreateHeartbeatPayloadIntervalUnit): Interval specified as 'minutes', 'hours' or 'days'
        enabled (bool): Enable/disable heartbeat monitoring
        description (Union[Unset, str]): An optional description of the heartbeat
        owner_team (Union[Unset, CreateHeartbeatPayloadOwnerTeam]): Owner team of the heartbeat, consisting id and/or
            name of the owner team
        alert_message (Union[Unset, str]): Specifies the alert message for heartbeat expiration alert. If this is not
            provided, default alert message is 'HeartbeatName is expired'
        alert_tags (Union[Unset, List[str]]): Specifies the alert tags for heartbeat expiration alert
        alert_priority (Union[Unset, CreateHeartbeatPayloadAlertPriority]): Specifies the alert priority for heartbeat
            expiration alert. If this is not provided, default priority is P3
    """

    name: str
    interval: int
    interval_unit: CreateHeartbeatPayloadIntervalUnit
    enabled: bool
    description: Union[Unset, str] = UNSET
    owner_team: Union[Unset, "CreateHeartbeatPayloadOwnerTeam"] = UNSET
    alert_message: Union[Unset, str] = UNSET
    alert_tags: Union[Unset, List[str]] = UNSET
    alert_priority: Union[Unset, CreateHeartbeatPayloadAlertPriority] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        interval = self.interval

        interval_unit = self.interval_unit.value

        enabled = self.enabled

        description = self.description

        owner_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner_team, Unset):
            owner_team = self.owner_team.to_dict()

        alert_message = self.alert_message

        alert_tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alert_tags, Unset):
            alert_tags = self.alert_tags

        alert_priority: Union[Unset, str] = UNSET
        if not isinstance(self.alert_priority, Unset):
            alert_priority = self.alert_priority.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "interval": interval,
                "intervalUnit": interval_unit,
                "enabled": enabled,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if owner_team is not UNSET:
            field_dict["ownerTeam"] = owner_team
        if alert_message is not UNSET:
            field_dict["alertMessage"] = alert_message
        if alert_tags is not UNSET:
            field_dict["alertTags"] = alert_tags
        if alert_priority is not UNSET:
            field_dict["alertPriority"] = alert_priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_heartbeat_payload_owner_team import CreateHeartbeatPayloadOwnerTeam

        d = src_dict.copy()
        name = d.pop("name")

        interval = d.pop("interval")

        interval_unit = CreateHeartbeatPayloadIntervalUnit(d.pop("intervalUnit"))

        enabled = d.pop("enabled")

        description = d.pop("description", UNSET)

        _owner_team = d.pop("ownerTeam", UNSET)
        owner_team: Union[Unset, CreateHeartbeatPayloadOwnerTeam]
        if isinstance(_owner_team, Unset):
            owner_team = UNSET
        else:
            owner_team = CreateHeartbeatPayloadOwnerTeam.from_dict(_owner_team)

        alert_message = d.pop("alertMessage", UNSET)

        alert_tags = cast(List[str], d.pop("alertTags", UNSET))

        _alert_priority = d.pop("alertPriority", UNSET)
        alert_priority: Union[Unset, CreateHeartbeatPayloadAlertPriority]
        if isinstance(_alert_priority, Unset):
            alert_priority = UNSET
        else:
            alert_priority = CreateHeartbeatPayloadAlertPriority(_alert_priority)

        create_heartbeat_payload = cls(
            name=name,
            interval=interval,
            interval_unit=interval_unit,
            enabled=enabled,
            description=description,
            owner_team=owner_team,
            alert_message=alert_message,
            alert_tags=alert_tags,
            alert_priority=alert_priority,
        )

        create_heartbeat_payload.additional_properties = d
        return create_heartbeat_payload

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
