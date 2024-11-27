from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_incoming_feature_feature_type import BaseIncomingFeatureFeatureType
from ..models.bidirectional_callback_new_bidirectional_callback_type import (
    BidirectionalCallbackNewBidirectionalCallbackType,
)
from ..models.integration_type import IntegrationType
from ..models.outgoing_callback_new_callback_type import OutgoingCallbackNewCallbackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_mapping import ActionMapping
    from ..models.alert_filter import AlertFilter
    from ..models.base_incoming_feature_extra_properties import BaseIncomingFeatureExtraProperties
    from ..models.recipient import Recipient
    from ..models.team_meta import TeamMeta


T = TypeVar("T", bound="ConnectWiseManageV2Integration")


@_attrs_define
class ConnectWiseManageV2Integration:
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
        allow_configuration_access (Union[Unset, bool]): This parameter is for allowing or restricting the configuration
            access. If configuration access is restricted, the integration will be limited to Alert API requests and sending
            heartbeats. Defaults to false
        allow_read_access (Union[Unset, bool]):
        allow_write_access (Union[Unset, bool]): This parameter is for configuring the read-only access of integration.
            If the integration is limited to read-only access, the integration will not be authorized to perform any create,
            update or delete action within any domain. Defaults to true
        allow_delete_access (Union[Unset, bool]):
        alert_filter (Union[Unset, AlertFilter]):
        forwarding_enabled (Union[Unset, bool]):
        forwarding_action_mappings (Union[Unset, List['ActionMapping']]):
        callback_type (Union[Unset, OutgoingCallbackNewCallbackType]):
        updates_action_mappings (Union[Unset, List['ActionMapping']]):
        updates_enabled (Union[Unset, bool]):
        bidirectional_callback_type (Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType]):
        public_key (Union[Unset, str]):
        private_key (Union[Unset, str]):
        login_company (Union[Unset, str]):
        company_name (Union[Unset, str]):
        cwm_url (Union[Unset, str]):
        company_id (Union[Unset, str]):
        board_name (Union[Unset, str]):
        board_id (Union[Unset, int]):
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
    allow_configuration_access: Union[Unset, bool] = UNSET
    allow_read_access: Union[Unset, bool] = UNSET
    allow_write_access: Union[Unset, bool] = UNSET
    allow_delete_access: Union[Unset, bool] = UNSET
    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    forwarding_enabled: Union[Unset, bool] = UNSET
    forwarding_action_mappings: Union[Unset, List["ActionMapping"]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackNewCallbackType] = UNSET
    updates_action_mappings: Union[Unset, List["ActionMapping"]] = UNSET
    updates_enabled: Union[Unset, bool] = UNSET
    bidirectional_callback_type: Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType] = UNSET
    public_key: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    login_company: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    cwm_url: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    board_name: Union[Unset, str] = UNSET
    board_id: Union[Unset, int] = UNSET
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

        allow_configuration_access = self.allow_configuration_access

        allow_read_access = self.allow_read_access

        allow_write_access = self.allow_write_access

        allow_delete_access = self.allow_delete_access

        alert_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert_filter, Unset):
            alert_filter = self.alert_filter.to_dict()

        forwarding_enabled = self.forwarding_enabled

        forwarding_action_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.forwarding_action_mappings, Unset):
            forwarding_action_mappings = []
            for forwarding_action_mappings_item_data in self.forwarding_action_mappings:
                forwarding_action_mappings_item = forwarding_action_mappings_item_data.to_dict()
                forwarding_action_mappings.append(forwarding_action_mappings_item)

        callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.callback_type, Unset):
            callback_type = self.callback_type.value

        updates_action_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.updates_action_mappings, Unset):
            updates_action_mappings = []
            for updates_action_mappings_item_data in self.updates_action_mappings:
                updates_action_mappings_item = updates_action_mappings_item_data.to_dict()
                updates_action_mappings.append(updates_action_mappings_item)

        updates_enabled = self.updates_enabled

        bidirectional_callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.bidirectional_callback_type, Unset):
            bidirectional_callback_type = self.bidirectional_callback_type.value

        public_key = self.public_key

        private_key = self.private_key

        login_company = self.login_company

        company_name = self.company_name

        cwm_url = self.cwm_url

        company_id = self.company_id

        board_name = self.board_name

        board_id = self.board_id

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
        if allow_configuration_access is not UNSET:
            field_dict["allowConfigurationAccess"] = allow_configuration_access
        if allow_read_access is not UNSET:
            field_dict["allowReadAccess"] = allow_read_access
        if allow_write_access is not UNSET:
            field_dict["allowWriteAccess"] = allow_write_access
        if allow_delete_access is not UNSET:
            field_dict["allowDeleteAccess"] = allow_delete_access
        if alert_filter is not UNSET:
            field_dict["alertFilter"] = alert_filter
        if forwarding_enabled is not UNSET:
            field_dict["forwardingEnabled"] = forwarding_enabled
        if forwarding_action_mappings is not UNSET:
            field_dict["forwardingActionMappings"] = forwarding_action_mappings
        if callback_type is not UNSET:
            field_dict["callback-type"] = callback_type
        if updates_action_mappings is not UNSET:
            field_dict["updatesActionMappings"] = updates_action_mappings
        if updates_enabled is not UNSET:
            field_dict["updatesEnabled"] = updates_enabled
        if bidirectional_callback_type is not UNSET:
            field_dict["bidirectional-callback-type"] = bidirectional_callback_type
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if login_company is not UNSET:
            field_dict["loginCompany"] = login_company
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if cwm_url is not UNSET:
            field_dict["cwmUrl"] = cwm_url
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if board_name is not UNSET:
            field_dict["boardName"] = board_name
        if board_id is not UNSET:
            field_dict["boardId"] = board_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_mapping import ActionMapping
        from ..models.alert_filter import AlertFilter
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

        allow_configuration_access = d.pop("allowConfigurationAccess", UNSET)

        allow_read_access = d.pop("allowReadAccess", UNSET)

        allow_write_access = d.pop("allowWriteAccess", UNSET)

        allow_delete_access = d.pop("allowDeleteAccess", UNSET)

        _alert_filter = d.pop("alertFilter", UNSET)
        alert_filter: Union[Unset, AlertFilter]
        if isinstance(_alert_filter, Unset):
            alert_filter = UNSET
        else:
            alert_filter = AlertFilter.from_dict(_alert_filter)

        forwarding_enabled = d.pop("forwardingEnabled", UNSET)

        forwarding_action_mappings = []
        _forwarding_action_mappings = d.pop("forwardingActionMappings", UNSET)
        for forwarding_action_mappings_item_data in _forwarding_action_mappings or []:
            forwarding_action_mappings_item = ActionMapping.from_dict(forwarding_action_mappings_item_data)

            forwarding_action_mappings.append(forwarding_action_mappings_item)

        _callback_type = d.pop("callback-type", UNSET)
        callback_type: Union[Unset, OutgoingCallbackNewCallbackType]
        if isinstance(_callback_type, Unset):
            callback_type = UNSET
        else:
            callback_type = OutgoingCallbackNewCallbackType(_callback_type)

        updates_action_mappings = []
        _updates_action_mappings = d.pop("updatesActionMappings", UNSET)
        for updates_action_mappings_item_data in _updates_action_mappings or []:
            updates_action_mappings_item = ActionMapping.from_dict(updates_action_mappings_item_data)

            updates_action_mappings.append(updates_action_mappings_item)

        updates_enabled = d.pop("updatesEnabled", UNSET)

        _bidirectional_callback_type = d.pop("bidirectional-callback-type", UNSET)
        bidirectional_callback_type: Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType]
        if isinstance(_bidirectional_callback_type, Unset):
            bidirectional_callback_type = UNSET
        else:
            bidirectional_callback_type = BidirectionalCallbackNewBidirectionalCallbackType(
                _bidirectional_callback_type
            )

        public_key = d.pop("publicKey", UNSET)

        private_key = d.pop("privateKey", UNSET)

        login_company = d.pop("loginCompany", UNSET)

        company_name = d.pop("companyName", UNSET)

        cwm_url = d.pop("cwmUrl", UNSET)

        company_id = d.pop("companyId", UNSET)

        board_name = d.pop("boardName", UNSET)

        board_id = d.pop("boardId", UNSET)

        connect_wise_manage_v2_integration = cls(
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
            allow_configuration_access=allow_configuration_access,
            allow_read_access=allow_read_access,
            allow_write_access=allow_write_access,
            allow_delete_access=allow_delete_access,
            alert_filter=alert_filter,
            forwarding_enabled=forwarding_enabled,
            forwarding_action_mappings=forwarding_action_mappings,
            callback_type=callback_type,
            updates_action_mappings=updates_action_mappings,
            updates_enabled=updates_enabled,
            bidirectional_callback_type=bidirectional_callback_type,
            public_key=public_key,
            private_key=private_key,
            login_company=login_company,
            company_name=company_name,
            cwm_url=cwm_url,
            company_id=company_id,
            board_name=board_name,
            board_id=board_id,
        )

        connect_wise_manage_v2_integration.additional_properties = d
        return connect_wise_manage_v2_integration

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
