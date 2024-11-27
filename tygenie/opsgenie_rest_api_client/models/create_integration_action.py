from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_integration_action_type import BaseIntegrationActionType
from ..models.create_integration_action_priority import CreateIntegrationActionPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_integration_action_extra_properties import CreateIntegrationActionExtraProperties
    from ..models.integration_action_filter import IntegrationActionFilter
    from ..models.recipient import Recipient


T = TypeVar("T", bound="CreateIntegrationAction")


@_attrs_define
class CreateIntegrationAction:
    """
    Attributes:
        name (str):
        filter_ (IntegrationActionFilter):
        type (BaseIntegrationActionType):
        order (Union[Unset, int]):
        user (Union[Unset, str]):
        note (Union[Unset, str]):
        alias (Union[Unset, str]):
        source (Union[Unset, str]):
        message (Union[Unset, str]):
        description (Union[Unset, str]):
        entity (Union[Unset, str]):
        priority (Union[Unset, CreateIntegrationActionPriority]):
        custom_priority (Union[Unset, str]):
        append_attachments (Union[Unset, bool]):
        alert_actions (Union[Unset, List[str]]):
        ignore_alert_actions_from_payload (Union[Unset, bool]):
        recipients (Union[Unset, List['Recipient']]):
        responders (Union[Unset, List['Recipient']]):
        ignore_recipients_from_payload (Union[Unset, bool]):
        ignore_teams_from_payload (Union[Unset, bool]):
        tags (Union[Unset, List[str]]):
        ignore_tags_from_payload (Union[Unset, bool]):
        extra_properties (Union[Unset, CreateIntegrationActionExtraProperties]):
        ignore_extra_properties_from_payload (Union[Unset, bool]):
        ignore_responders_from_payload (Union[Unset, bool]):
    """

    name: str
    filter_: "IntegrationActionFilter"
    type: BaseIntegrationActionType
    order: Union[Unset, int] = UNSET
    user: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    entity: Union[Unset, str] = UNSET
    priority: Union[Unset, CreateIntegrationActionPriority] = UNSET
    custom_priority: Union[Unset, str] = UNSET
    append_attachments: Union[Unset, bool] = UNSET
    alert_actions: Union[Unset, List[str]] = UNSET
    ignore_alert_actions_from_payload: Union[Unset, bool] = UNSET
    recipients: Union[Unset, List["Recipient"]] = UNSET
    responders: Union[Unset, List["Recipient"]] = UNSET
    ignore_recipients_from_payload: Union[Unset, bool] = UNSET
    ignore_teams_from_payload: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    ignore_tags_from_payload: Union[Unset, bool] = UNSET
    extra_properties: Union[Unset, "CreateIntegrationActionExtraProperties"] = UNSET
    ignore_extra_properties_from_payload: Union[Unset, bool] = UNSET
    ignore_responders_from_payload: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        filter_ = self.filter_.to_dict()

        type = self.type.value

        order = self.order

        user = self.user

        note = self.note

        alias = self.alias

        source = self.source

        message = self.message

        description = self.description

        entity = self.entity

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        custom_priority = self.custom_priority

        append_attachments = self.append_attachments

        alert_actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alert_actions, Unset):
            alert_actions = self.alert_actions

        ignore_alert_actions_from_payload = self.ignore_alert_actions_from_payload

        recipients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        responders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responders, Unset):
            responders = []
            for responders_item_data in self.responders:
                responders_item = responders_item_data.to_dict()
                responders.append(responders_item)

        ignore_recipients_from_payload = self.ignore_recipients_from_payload

        ignore_teams_from_payload = self.ignore_teams_from_payload

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        ignore_tags_from_payload = self.ignore_tags_from_payload

        extra_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_properties, Unset):
            extra_properties = self.extra_properties.to_dict()

        ignore_extra_properties_from_payload = self.ignore_extra_properties_from_payload

        ignore_responders_from_payload = self.ignore_responders_from_payload

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filter": filter_,
                "type": type,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if user is not UNSET:
            field_dict["user"] = user
        if note is not UNSET:
            field_dict["note"] = note
        if alias is not UNSET:
            field_dict["alias"] = alias
        if source is not UNSET:
            field_dict["source"] = source
        if message is not UNSET:
            field_dict["message"] = message
        if description is not UNSET:
            field_dict["description"] = description
        if entity is not UNSET:
            field_dict["entity"] = entity
        if priority is not UNSET:
            field_dict["priority"] = priority
        if custom_priority is not UNSET:
            field_dict["customPriority"] = custom_priority
        if append_attachments is not UNSET:
            field_dict["appendAttachments"] = append_attachments
        if alert_actions is not UNSET:
            field_dict["alertActions"] = alert_actions
        if ignore_alert_actions_from_payload is not UNSET:
            field_dict["ignoreAlertActionsFromPayload"] = ignore_alert_actions_from_payload
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if responders is not UNSET:
            field_dict["responders"] = responders
        if ignore_recipients_from_payload is not UNSET:
            field_dict["ignoreRecipientsFromPayload"] = ignore_recipients_from_payload
        if ignore_teams_from_payload is not UNSET:
            field_dict["ignoreTeamsFromPayload"] = ignore_teams_from_payload
        if tags is not UNSET:
            field_dict["tags"] = tags
        if ignore_tags_from_payload is not UNSET:
            field_dict["ignoreTagsFromPayload"] = ignore_tags_from_payload
        if extra_properties is not UNSET:
            field_dict["extraProperties"] = extra_properties
        if ignore_extra_properties_from_payload is not UNSET:
            field_dict["ignoreExtraPropertiesFromPayload"] = ignore_extra_properties_from_payload
        if ignore_responders_from_payload is not UNSET:
            field_dict["ignoreRespondersFromPayload"] = ignore_responders_from_payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_integration_action_extra_properties import CreateIntegrationActionExtraProperties
        from ..models.integration_action_filter import IntegrationActionFilter
        from ..models.recipient import Recipient

        d = src_dict.copy()
        name = d.pop("name")

        filter_ = IntegrationActionFilter.from_dict(d.pop("filter"))

        type = BaseIntegrationActionType(d.pop("type"))

        order = d.pop("order", UNSET)

        user = d.pop("user", UNSET)

        note = d.pop("note", UNSET)

        alias = d.pop("alias", UNSET)

        source = d.pop("source", UNSET)

        message = d.pop("message", UNSET)

        description = d.pop("description", UNSET)

        entity = d.pop("entity", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, CreateIntegrationActionPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateIntegrationActionPriority(_priority)

        custom_priority = d.pop("customPriority", UNSET)

        append_attachments = d.pop("appendAttachments", UNSET)

        alert_actions = cast(List[str], d.pop("alertActions", UNSET))

        ignore_alert_actions_from_payload = d.pop("ignoreAlertActionsFromPayload", UNSET)

        recipients = []
        _recipients = d.pop("recipients", UNSET)
        for recipients_item_data in _recipients or []:
            recipients_item = Recipient.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        responders = []
        _responders = d.pop("responders", UNSET)
        for responders_item_data in _responders or []:
            responders_item = Recipient.from_dict(responders_item_data)

            responders.append(responders_item)

        ignore_recipients_from_payload = d.pop("ignoreRecipientsFromPayload", UNSET)

        ignore_teams_from_payload = d.pop("ignoreTeamsFromPayload", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        ignore_tags_from_payload = d.pop("ignoreTagsFromPayload", UNSET)

        _extra_properties = d.pop("extraProperties", UNSET)
        extra_properties: Union[Unset, CreateIntegrationActionExtraProperties]
        if isinstance(_extra_properties, Unset):
            extra_properties = UNSET
        else:
            extra_properties = CreateIntegrationActionExtraProperties.from_dict(_extra_properties)

        ignore_extra_properties_from_payload = d.pop("ignoreExtraPropertiesFromPayload", UNSET)

        ignore_responders_from_payload = d.pop("ignoreRespondersFromPayload", UNSET)

        create_integration_action = cls(
            name=name,
            filter_=filter_,
            type=type,
            order=order,
            user=user,
            note=note,
            alias=alias,
            source=source,
            message=message,
            description=description,
            entity=entity,
            priority=priority,
            custom_priority=custom_priority,
            append_attachments=append_attachments,
            alert_actions=alert_actions,
            ignore_alert_actions_from_payload=ignore_alert_actions_from_payload,
            recipients=recipients,
            responders=responders,
            ignore_recipients_from_payload=ignore_recipients_from_payload,
            ignore_teams_from_payload=ignore_teams_from_payload,
            tags=tags,
            ignore_tags_from_payload=ignore_tags_from_payload,
            extra_properties=extra_properties,
            ignore_extra_properties_from_payload=ignore_extra_properties_from_payload,
            ignore_responders_from_payload=ignore_responders_from_payload,
        )

        create_integration_action.additional_properties = d
        return create_integration_action

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
