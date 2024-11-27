import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_details import AlertDetails
    from ..models.alert_integration import AlertIntegration
    from ..models.alert_report import AlertReport
    from ..models.responder import Responder


T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """
    Attributes:
        id (str):
        tiny_id (Union[Unset, str]):
        alias (Union[Unset, str]):
        message (Union[Unset, str]):
        status (Union[Unset, str]):
        acknowledged (Union[Unset, bool]):
        is_seen (Union[Unset, bool]):
        tags (Union[Unset, List[str]]):
        snoozed (Union[Unset, bool]):
        snoozed_until (Union[Unset, datetime.datetime]):
        count (Union[Unset, int]):
        last_occurred_at (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        source (Union[Unset, str]):
        owner (Union[Unset, str]):
        priority (Union[Unset, str]):
        responders (Union[Unset, List['Responder']]):
        integration (Union[Unset, AlertIntegration]):
        report (Union[Unset, AlertReport]):
        actions (Union[Unset, List[str]]):
        entity (Union[Unset, str]):
        description (Union[Unset, str]):
        details (Union[Unset, AlertDetails]):
    """

    id: str
    tiny_id: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    acknowledged: Union[Unset, bool] = UNSET
    is_seen: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    snoozed: Union[Unset, bool] = UNSET
    snoozed_until: Union[Unset, datetime.datetime] = UNSET
    count: Union[Unset, int] = UNSET
    last_occurred_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    source: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    responders: Union[Unset, List["Responder"]] = UNSET
    integration: Union[Unset, "AlertIntegration"] = UNSET
    report: Union[Unset, "AlertReport"] = UNSET
    actions: Union[Unset, List[str]] = UNSET
    entity: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    details: Union[Unset, "AlertDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        tiny_id = self.tiny_id

        alias = self.alias

        message = self.message

        status = self.status

        acknowledged = self.acknowledged

        is_seen = self.is_seen

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        snoozed = self.snoozed

        snoozed_until: Union[Unset, str] = UNSET
        if not isinstance(self.snoozed_until, Unset):
            snoozed_until = self.snoozed_until.isoformat()

        count = self.count

        last_occurred_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_occurred_at, Unset):
            last_occurred_at = self.last_occurred_at.isoformat()

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

        integration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        report: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions

        entity = self.entity

        description = self.description

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if tiny_id is not UNSET:
            field_dict["tinyId"] = tiny_id
        if alias is not UNSET:
            field_dict["alias"] = alias
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if acknowledged is not UNSET:
            field_dict["acknowledged"] = acknowledged
        if is_seen is not UNSET:
            field_dict["isSeen"] = is_seen
        if tags is not UNSET:
            field_dict["tags"] = tags
        if snoozed is not UNSET:
            field_dict["snoozed"] = snoozed
        if snoozed_until is not UNSET:
            field_dict["snoozedUntil"] = snoozed_until
        if count is not UNSET:
            field_dict["count"] = count
        if last_occurred_at is not UNSET:
            field_dict["lastOccurredAt"] = last_occurred_at
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
        if integration is not UNSET:
            field_dict["integration"] = integration
        if report is not UNSET:
            field_dict["report"] = report
        if actions is not UNSET:
            field_dict["actions"] = actions
        if entity is not UNSET:
            field_dict["entity"] = entity
        if description is not UNSET:
            field_dict["description"] = description
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_details import AlertDetails
        from ..models.alert_integration import AlertIntegration
        from ..models.alert_report import AlertReport
        from ..models.responder import Responder

        d = src_dict.copy()
        id = d.pop("id")

        tiny_id = d.pop("tinyId", UNSET)

        alias = d.pop("alias", UNSET)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        acknowledged = d.pop("acknowledged", UNSET)

        is_seen = d.pop("isSeen", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        snoozed = d.pop("snoozed", UNSET)

        _snoozed_until = d.pop("snoozedUntil", UNSET)
        snoozed_until: Union[Unset, datetime.datetime]
        if isinstance(_snoozed_until, Unset):
            snoozed_until = UNSET
        else:
            snoozed_until = isoparse(_snoozed_until)

        count = d.pop("count", UNSET)

        _last_occurred_at = d.pop("lastOccurredAt", UNSET)
        last_occurred_at: Union[Unset, datetime.datetime]
        if isinstance(_last_occurred_at, Unset):
            last_occurred_at = UNSET
        else:
            last_occurred_at = isoparse(_last_occurred_at)

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

        _integration = d.pop("integration", UNSET)
        integration: Union[Unset, AlertIntegration]
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = AlertIntegration.from_dict(_integration)

        _report = d.pop("report", UNSET)
        report: Union[Unset, AlertReport]
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = AlertReport.from_dict(_report)

        actions = cast(List[str], d.pop("actions", UNSET))

        entity = d.pop("entity", UNSET)

        description = d.pop("description", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, AlertDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = AlertDetails.from_dict(_details)

        alert = cls(
            id=id,
            tiny_id=tiny_id,
            alias=alias,
            message=message,
            status=status,
            acknowledged=acknowledged,
            is_seen=is_seen,
            tags=tags,
            snoozed=snoozed,
            snoozed_until=snoozed_until,
            count=count,
            last_occurred_at=last_occurred_at,
            created_at=created_at,
            updated_at=updated_at,
            source=source,
            owner=owner,
            priority=priority,
            responders=responders,
            integration=integration,
            report=report,
            actions=actions,
            entity=entity,
            description=description,
            details=details,
        )

        alert.additional_properties = d
        return alert

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
