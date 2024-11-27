from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_incoming_feature_feature_type import BaseIncomingFeatureFeatureType
from ..models.integration_type import IntegrationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_incoming_feature_extra_properties import BaseIncomingFeatureExtraProperties
    from ..models.recipient import Recipient
    from ..models.team_meta import TeamMeta


T = TypeVar("T", bound="OEMEmailIntegration")


@_attrs_define
class OEMEmailIntegration:
    """
    Attributes:
        type (IntegrationType): Type of the integration. (For instance, "API" for API Integration)
        name (str): Name of the integration. Name must be unique for each integration
        id (Union[Unset, str]):
        enabled (Union[Unset, bool]): This parameter is for specifying whether the integration will be enabled or not
        owner_team (Union[Unset, TeamMeta]):
        is_global (Union[Unset, bool]):
        field_read_only (Union[Unset, List[str]]):
        suppress_notifications (Union[Unset, bool]): If enabled, notifications that come from alerts will be suppressed.
            Defaults to false
        ignore_teams_from_payload (Union[Unset, bool]): If enabled, the integration will ignore teams sent in request
            payloads. Defaults to false
        ignore_recipients_from_payload (Union[Unset, bool]): If enabled, the integration will ignore recipients sent in
            request payloads. Defaults to false
        recipients (Union[Unset, List['Recipient']]): Optional user, schedule, teams or escalation names to calculate
            which users will receive the notifications of the alert. Recipients which are exceeding the limit are ignored
        is_advanced (Union[Unset, bool]):
        ignore_responders_from_payload (Union[Unset, bool]):
        ignore_tags_from_payload (Union[Unset, bool]):
        ignore_extra_properties_from_payload (Union[Unset, bool]):
        responders (Union[Unset, List['Recipient']]):
        priority (Union[Unset, str]):
        custom_priority (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        extra_properties (Union[Unset, BaseIncomingFeatureExtraProperties]):
        assigned_team (Union[Unset, TeamMeta]):
        feature_type (Union[Unset, BaseIncomingFeatureFeatureType]):
        email_address (Union[Unset, str]):
        email_username (Union[Unset, str]): The username part of the email address. It must be unique for each
            integration
    """

    type: IntegrationType
    name: str
    id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    owner_team: Union[Unset, "TeamMeta"] = UNSET
    is_global: Union[Unset, bool] = UNSET
    field_read_only: Union[Unset, List[str]] = UNSET
    suppress_notifications: Union[Unset, bool] = UNSET
    ignore_teams_from_payload: Union[Unset, bool] = UNSET
    ignore_recipients_from_payload: Union[Unset, bool] = UNSET
    recipients: Union[Unset, List["Recipient"]] = UNSET
    is_advanced: Union[Unset, bool] = UNSET
    ignore_responders_from_payload: Union[Unset, bool] = UNSET
    ignore_tags_from_payload: Union[Unset, bool] = UNSET
    ignore_extra_properties_from_payload: Union[Unset, bool] = UNSET
    responders: Union[Unset, List["Recipient"]] = UNSET
    priority: Union[Unset, str] = UNSET
    custom_priority: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    extra_properties: Union[Unset, "BaseIncomingFeatureExtraProperties"] = UNSET
    assigned_team: Union[Unset, "TeamMeta"] = UNSET
    feature_type: Union[Unset, BaseIncomingFeatureFeatureType] = UNSET
    email_address: Union[Unset, str] = UNSET
    email_username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name

        id = self.id

        enabled = self.enabled

        owner_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner_team, Unset):
            owner_team = self.owner_team.to_dict()

        is_global = self.is_global

        field_read_only: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_read_only, Unset):
            field_read_only = self.field_read_only

        suppress_notifications = self.suppress_notifications

        ignore_teams_from_payload = self.ignore_teams_from_payload

        ignore_recipients_from_payload = self.ignore_recipients_from_payload

        recipients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        is_advanced = self.is_advanced

        ignore_responders_from_payload = self.ignore_responders_from_payload

        ignore_tags_from_payload = self.ignore_tags_from_payload

        ignore_extra_properties_from_payload = self.ignore_extra_properties_from_payload

        responders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responders, Unset):
            responders = []
            for responders_item_data in self.responders:
                responders_item = responders_item_data.to_dict()
                responders.append(responders_item)

        priority = self.priority

        custom_priority = self.custom_priority

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        extra_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_properties, Unset):
            extra_properties = self.extra_properties.to_dict()

        assigned_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_team, Unset):
            assigned_team = self.assigned_team.to_dict()

        feature_type: Union[Unset, str] = UNSET
        if not isinstance(self.feature_type, Unset):
            feature_type = self.feature_type.value

        email_address = self.email_address

        email_username = self.email_username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if owner_team is not UNSET:
            field_dict["ownerTeam"] = owner_team
        if is_global is not UNSET:
            field_dict["isGlobal"] = is_global
        if field_read_only is not UNSET:
            field_dict["_readOnly"] = field_read_only
        if suppress_notifications is not UNSET:
            field_dict["suppressNotifications"] = suppress_notifications
        if ignore_teams_from_payload is not UNSET:
            field_dict["ignoreTeamsFromPayload"] = ignore_teams_from_payload
        if ignore_recipients_from_payload is not UNSET:
            field_dict["ignoreRecipientsFromPayload"] = ignore_recipients_from_payload
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if is_advanced is not UNSET:
            field_dict["isAdvanced"] = is_advanced
        if ignore_responders_from_payload is not UNSET:
            field_dict["ignoreRespondersFromPayload"] = ignore_responders_from_payload
        if ignore_tags_from_payload is not UNSET:
            field_dict["ignoreTagsFromPayload"] = ignore_tags_from_payload
        if ignore_extra_properties_from_payload is not UNSET:
            field_dict["ignoreExtraPropertiesFromPayload"] = ignore_extra_properties_from_payload
        if responders is not UNSET:
            field_dict["responders"] = responders
        if priority is not UNSET:
            field_dict["priority"] = priority
        if custom_priority is not UNSET:
            field_dict["customPriority"] = custom_priority
        if tags is not UNSET:
            field_dict["tags"] = tags
        if extra_properties is not UNSET:
            field_dict["extraProperties"] = extra_properties
        if assigned_team is not UNSET:
            field_dict["assignedTeam"] = assigned_team
        if feature_type is not UNSET:
            field_dict["feature-type"] = feature_type
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if email_username is not UNSET:
            field_dict["emailUsername"] = email_username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_incoming_feature_extra_properties import BaseIncomingFeatureExtraProperties
        from ..models.recipient import Recipient
        from ..models.team_meta import TeamMeta

        d = src_dict.copy()
        type = IntegrationType(d.pop("type"))

        name = d.pop("name")

        id = d.pop("id", UNSET)

        enabled = d.pop("enabled", UNSET)

        _owner_team = d.pop("ownerTeam", UNSET)
        owner_team: Union[Unset, TeamMeta]
        if isinstance(_owner_team, Unset):
            owner_team = UNSET
        else:
            owner_team = TeamMeta.from_dict(_owner_team)

        is_global = d.pop("isGlobal", UNSET)

        field_read_only = cast(List[str], d.pop("_readOnly", UNSET))

        suppress_notifications = d.pop("suppressNotifications", UNSET)

        ignore_teams_from_payload = d.pop("ignoreTeamsFromPayload", UNSET)

        ignore_recipients_from_payload = d.pop("ignoreRecipientsFromPayload", UNSET)

        recipients = []
        _recipients = d.pop("recipients", UNSET)
        for recipients_item_data in _recipients or []:
            recipients_item = Recipient.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        is_advanced = d.pop("isAdvanced", UNSET)

        ignore_responders_from_payload = d.pop("ignoreRespondersFromPayload", UNSET)

        ignore_tags_from_payload = d.pop("ignoreTagsFromPayload", UNSET)

        ignore_extra_properties_from_payload = d.pop("ignoreExtraPropertiesFromPayload", UNSET)

        responders = []
        _responders = d.pop("responders", UNSET)
        for responders_item_data in _responders or []:
            responders_item = Recipient.from_dict(responders_item_data)

            responders.append(responders_item)

        priority = d.pop("priority", UNSET)

        custom_priority = d.pop("customPriority", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        _extra_properties = d.pop("extraProperties", UNSET)
        extra_properties: Union[Unset, BaseIncomingFeatureExtraProperties]
        if isinstance(_extra_properties, Unset):
            extra_properties = UNSET
        else:
            extra_properties = BaseIncomingFeatureExtraProperties.from_dict(_extra_properties)

        _assigned_team = d.pop("assignedTeam", UNSET)
        assigned_team: Union[Unset, TeamMeta]
        if isinstance(_assigned_team, Unset):
            assigned_team = UNSET
        else:
            assigned_team = TeamMeta.from_dict(_assigned_team)

        _feature_type = d.pop("feature-type", UNSET)
        feature_type: Union[Unset, BaseIncomingFeatureFeatureType]
        if isinstance(_feature_type, Unset):
            feature_type = UNSET
        else:
            feature_type = BaseIncomingFeatureFeatureType(_feature_type)

        email_address = d.pop("emailAddress", UNSET)

        email_username = d.pop("emailUsername", UNSET)

        oem_email_integration = cls(
            type=type,
            name=name,
            id=id,
            enabled=enabled,
            owner_team=owner_team,
            is_global=is_global,
            field_read_only=field_read_only,
            suppress_notifications=suppress_notifications,
            ignore_teams_from_payload=ignore_teams_from_payload,
            ignore_recipients_from_payload=ignore_recipients_from_payload,
            recipients=recipients,
            is_advanced=is_advanced,
            ignore_responders_from_payload=ignore_responders_from_payload,
            ignore_tags_from_payload=ignore_tags_from_payload,
            ignore_extra_properties_from_payload=ignore_extra_properties_from_payload,
            responders=responders,
            priority=priority,
            custom_priority=custom_priority,
            tags=tags,
            extra_properties=extra_properties,
            assigned_team=assigned_team,
            feature_type=feature_type,
            email_address=email_address,
            email_username=email_username,
        )

        oem_email_integration.additional_properties = d
        return oem_email_integration

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
