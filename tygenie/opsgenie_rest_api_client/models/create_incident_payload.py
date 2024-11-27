from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_incident_payload_priority import CreateIncidentPayloadPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_incident_payload_details import CreateIncidentPayloadDetails
    from ..models.create_incident_payload_status_page_entry import CreateIncidentPayloadStatusPageEntry
    from ..models.recipient import Recipient


T = TypeVar("T", bound="CreateIncidentPayload")


@_attrs_define
class CreateIncidentPayload:
    """
    Attributes:
        message (str): Message of the incident
        service_id (str): Service on which incident will be created.
        description (Union[Unset, str]): Description field of the incident that is generally used to provide a detailed
            information about the incident.
        responders (Union[Unset, List['Recipient']]): Responders that the incident will be routed to send notifications
        tags (Union[Unset, List[str]]): Tags of the incident.
        details (Union[Unset, CreateIncidentPayloadDetails]): Map of key-value pairs to use as custom properties of the
            incident
        priority (Union[Unset, CreateIncidentPayloadPriority]): Priority level of the incident
        note (Union[Unset, str]): Additional note that will be added while creating the incident
        status_page_entry (Union[Unset, CreateIncidentPayloadStatusPageEntry]): Status page entry fields. If this field
            is leaved blank, message and description of incident will be used for title and detail respectively.
        notify_stakeholders (Union[Unset, bool]): Indicate whether stakeholders are notified or not. Default value is
            false.
    """

    message: str
    service_id: str
    description: Union[Unset, str] = UNSET
    responders: Union[Unset, List["Recipient"]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    details: Union[Unset, "CreateIncidentPayloadDetails"] = UNSET
    priority: Union[Unset, CreateIncidentPayloadPriority] = UNSET
    note: Union[Unset, str] = UNSET
    status_page_entry: Union[Unset, "CreateIncidentPayloadStatusPageEntry"] = UNSET
    notify_stakeholders: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        service_id = self.service_id

        description = self.description

        responders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responders, Unset):
            responders = []
            for responders_item_data in self.responders:
                responders_item = responders_item_data.to_dict()
                responders.append(responders_item)

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        note = self.note

        status_page_entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status_page_entry, Unset):
            status_page_entry = self.status_page_entry.to_dict()

        notify_stakeholders = self.notify_stakeholders

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "serviceId": service_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if responders is not UNSET:
            field_dict["responders"] = responders
        if tags is not UNSET:
            field_dict["tags"] = tags
        if details is not UNSET:
            field_dict["details"] = details
        if priority is not UNSET:
            field_dict["priority"] = priority
        if note is not UNSET:
            field_dict["note"] = note
        if status_page_entry is not UNSET:
            field_dict["statusPageEntry"] = status_page_entry
        if notify_stakeholders is not UNSET:
            field_dict["notifyStakeholders"] = notify_stakeholders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_incident_payload_details import CreateIncidentPayloadDetails
        from ..models.create_incident_payload_status_page_entry import CreateIncidentPayloadStatusPageEntry
        from ..models.recipient import Recipient

        d = src_dict.copy()
        message = d.pop("message")

        service_id = d.pop("serviceId")

        description = d.pop("description", UNSET)

        responders = []
        _responders = d.pop("responders", UNSET)
        for responders_item_data in _responders or []:
            responders_item = Recipient.from_dict(responders_item_data)

            responders.append(responders_item)

        tags = cast(List[str], d.pop("tags", UNSET))

        _details = d.pop("details", UNSET)
        details: Union[Unset, CreateIncidentPayloadDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = CreateIncidentPayloadDetails.from_dict(_details)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, CreateIncidentPayloadPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateIncidentPayloadPriority(_priority)

        note = d.pop("note", UNSET)

        _status_page_entry = d.pop("statusPageEntry", UNSET)
        status_page_entry: Union[Unset, CreateIncidentPayloadStatusPageEntry]
        if isinstance(_status_page_entry, Unset):
            status_page_entry = UNSET
        else:
            status_page_entry = CreateIncidentPayloadStatusPageEntry.from_dict(_status_page_entry)

        notify_stakeholders = d.pop("notifyStakeholders", UNSET)

        create_incident_payload = cls(
            message=message,
            service_id=service_id,
            description=description,
            responders=responders,
            tags=tags,
            details=details,
            priority=priority,
            note=note,
            status_page_entry=status_page_entry,
            notify_stakeholders=notify_stakeholders,
        )

        create_incident_payload.additional_properties = d
        return create_incident_payload

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
