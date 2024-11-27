import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_incident_extra_properties import BaseIncidentExtraProperties
    from ..models.responder import Responder


T = TypeVar("T", bound="BaseIncident")


@_attrs_define
class BaseIncident:
    """
    Attributes:
        id (str):
        tiny_id (Union[Unset, str]):
        message (Union[Unset, str]):
        status (Union[Unset, str]):
        is_seen (Union[Unset, bool]):
        tags (Union[Unset, List[str]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        source (Union[Unset, str]):
        owner (Union[Unset, str]):
        priority (Union[Unset, str]):
        responders (Union[Unset, List['Responder']]):
        owner_team (Union[Unset, str]):
        extra_properties (Union[Unset, BaseIncidentExtraProperties]): Map of key-value pairs to use as custom properties
            of the incident
    """

    id: str
    tiny_id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    is_seen: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    source: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    responders: Union[Unset, List["Responder"]] = UNSET
    owner_team: Union[Unset, str] = UNSET
    extra_properties: Union[Unset, "BaseIncidentExtraProperties"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        tiny_id = self.tiny_id

        message = self.message

        status = self.status

        is_seen = self.is_seen

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        source = self.source

        owner = self.owner

        priority = self.priority

        responders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responders, Unset):
            responders = []
            for responders_item_data in self.responders:
                responders_item = responders_item_data.to_dict()
                responders.append(responders_item)

        owner_team = self.owner_team

        extra_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_properties, Unset):
            extra_properties = self.extra_properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if tiny_id is not UNSET:
            field_dict["tinyId"] = tiny_id
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if is_seen is not UNSET:
            field_dict["isSeen"] = is_seen
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if source is not UNSET:
            field_dict["source"] = source
        if owner is not UNSET:
            field_dict["owner"] = owner
        if priority is not UNSET:
            field_dict["priority"] = priority
        if responders is not UNSET:
            field_dict["responders"] = responders
        if owner_team is not UNSET:
            field_dict["ownerTeam"] = owner_team
        if extra_properties is not UNSET:
            field_dict["extraProperties"] = extra_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_incident_extra_properties import BaseIncidentExtraProperties
        from ..models.responder import Responder

        d = src_dict.copy()
        id = d.pop("id")

        tiny_id = d.pop("tinyId", UNSET)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        is_seen = d.pop("isSeen", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        source = d.pop("source", UNSET)

        owner = d.pop("owner", UNSET)

        priority = d.pop("priority", UNSET)

        responders = []
        _responders = d.pop("responders", UNSET)
        for responders_item_data in _responders or []:
            responders_item = Responder.from_dict(responders_item_data)

            responders.append(responders_item)

        owner_team = d.pop("ownerTeam", UNSET)

        _extra_properties = d.pop("extraProperties", UNSET)
        extra_properties: Union[Unset, BaseIncidentExtraProperties]
        if isinstance(_extra_properties, Unset):
            extra_properties = UNSET
        else:
            extra_properties = BaseIncidentExtraProperties.from_dict(_extra_properties)

        base_incident = cls(
            id=id,
            tiny_id=tiny_id,
            message=message,
            status=status,
            is_seen=is_seen,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
            source=source,
            owner=owner,
            priority=priority,
            responders=responders,
            owner_team=owner_team,
            extra_properties=extra_properties,
        )

        base_incident.additional_properties = d
        return base_incident

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
