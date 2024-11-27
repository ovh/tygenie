import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRequestStatus")


@_attrs_define
class IncidentRequestStatus:
    """
    Attributes:
        success (Union[Unset, bool]):
        action (Union[Unset, str]):
        processed_at (Union[Unset, datetime.datetime]):
        integration_id (Union[Unset, str]):
        is_success (Union[Unset, bool]):
        status (Union[Unset, str]):
        incident_id (Union[Unset, str]):
    """

    success: Union[Unset, bool] = UNSET
    action: Union[Unset, str] = UNSET
    processed_at: Union[Unset, datetime.datetime] = UNSET
    integration_id: Union[Unset, str] = UNSET
    is_success: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    incident_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        action = self.action

        processed_at: Union[Unset, str] = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        integration_id = self.integration_id

        is_success = self.is_success

        status = self.status

        incident_id = self.incident_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if action is not UNSET:
            field_dict["action"] = action
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at
        if integration_id is not UNSET:
            field_dict["integrationId"] = integration_id
        if is_success is not UNSET:
            field_dict["isSuccess"] = is_success
        if status is not UNSET:
            field_dict["status"] = status
        if incident_id is not UNSET:
            field_dict["incidentId"] = incident_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("success", UNSET)

        action = d.pop("action", UNSET)

        _processed_at = d.pop("processedAt", UNSET)
        processed_at: Union[Unset, datetime.datetime]
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = isoparse(_processed_at)

        integration_id = d.pop("integrationId", UNSET)

        is_success = d.pop("isSuccess", UNSET)

        status = d.pop("status", UNSET)

        incident_id = d.pop("incidentId", UNSET)

        incident_request_status = cls(
            success=success,
            action=action,
            processed_at=processed_at,
            integration_id=integration_id,
            is_success=is_success,
            status=status,
            incident_id=incident_id,
        )

        incident_request_status.additional_properties = d
        return incident_request_status

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
