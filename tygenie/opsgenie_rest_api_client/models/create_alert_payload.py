from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_alert_payload_priority import CreateAlertPayloadPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_alert_payload_details import CreateAlertPayloadDetails
    from ..models.recipient import Recipient


T = TypeVar("T", bound="CreateAlertPayload")


@_attrs_define
class CreateAlertPayload:
    """
    Attributes:
        message (str): Message of the alert
        user (Union[Unset, str]): Display name of the request owner
        note (Union[Unset, str]): Additional note that will be added while creating the alert
        source (Union[Unset, str]): Source field of the alert. Default value is IP address of the incoming request
        alias (Union[Unset, str]): Client-defined identifier of the alert, that is also the key element of alert
            deduplication.
        description (Union[Unset, str]): Description field of the alert that is generally used to provide a detailed
            information about the alert.
        responders (Union[Unset, List['Recipient']]): Responders that the alert will be routed to send notifications
        visible_to (Union[Unset, List['Recipient']]): Teams and users that the alert will become visible to without
            sending any notification
        actions (Union[Unset, List[str]]): Custom actions that will be available for the alert
        tags (Union[Unset, List[str]]): Tags of the alert
        details (Union[Unset, CreateAlertPayloadDetails]): Map of key-value pairs to use as custom properties of the
            alert
        entity (Union[Unset, str]): Entity field of the alert that is generally used to specify which domain alert is
            related to
        priority (Union[Unset, CreateAlertPayloadPriority]): Priority level of the alert
    """

    message: str
    user: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    responders: Union[Unset, List["Recipient"]] = UNSET
    visible_to: Union[Unset, List["Recipient"]] = UNSET
    actions: Union[Unset, List[str]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    details: Union[Unset, "CreateAlertPayloadDetails"] = UNSET
    entity: Union[Unset, str] = UNSET
    priority: Union[Unset, CreateAlertPayloadPriority] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        user = self.user

        note = self.note

        source = self.source

        alias = self.alias

        description = self.description

        responders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responders, Unset):
            responders = []
            for responders_item_data in self.responders:
                responders_item = responders_item_data.to_dict()
                responders.append(responders_item)

        visible_to: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.visible_to, Unset):
            visible_to = []
            for visible_to_item_data in self.visible_to:
                visible_to_item = visible_to_item_data.to_dict()
                visible_to.append(visible_to_item)

        actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        entity = self.entity

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if note is not UNSET:
            field_dict["note"] = note
        if source is not UNSET:
            field_dict["source"] = source
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if responders is not UNSET:
            field_dict["responders"] = responders
        if visible_to is not UNSET:
            field_dict["visibleTo"] = visible_to
        if actions is not UNSET:
            field_dict["actions"] = actions
        if tags is not UNSET:
            field_dict["tags"] = tags
        if details is not UNSET:
            field_dict["details"] = details
        if entity is not UNSET:
            field_dict["entity"] = entity
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_alert_payload_details import CreateAlertPayloadDetails
        from ..models.recipient import Recipient

        d = src_dict.copy()
        message = d.pop("message")

        user = d.pop("user", UNSET)

        note = d.pop("note", UNSET)

        source = d.pop("source", UNSET)

        alias = d.pop("alias", UNSET)

        description = d.pop("description", UNSET)

        responders = []
        _responders = d.pop("responders", UNSET)
        for responders_item_data in _responders or []:
            responders_item = Recipient.from_dict(responders_item_data)

            responders.append(responders_item)

        visible_to = []
        _visible_to = d.pop("visibleTo", UNSET)
        for visible_to_item_data in _visible_to or []:
            visible_to_item = Recipient.from_dict(visible_to_item_data)

            visible_to.append(visible_to_item)

        actions = cast(List[str], d.pop("actions", UNSET))

        tags = cast(List[str], d.pop("tags", UNSET))

        _details = d.pop("details", UNSET)
        details: Union[Unset, CreateAlertPayloadDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = CreateAlertPayloadDetails.from_dict(_details)

        entity = d.pop("entity", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, CreateAlertPayloadPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateAlertPayloadPriority(_priority)

        create_alert_payload = cls(
            message=message,
            user=user,
            note=note,
            source=source,
            alias=alias,
            description=description,
            responders=responders,
            visible_to=visible_to,
            actions=actions,
            tags=tags,
            details=details,
            entity=entity,
            priority=priority,
        )

        create_alert_payload.additional_properties = d
        return create_alert_payload

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
