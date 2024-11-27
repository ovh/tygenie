import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertRequestStatus")


@_attrs_define
class AlertRequestStatus:
    """
    Attributes:
        action (Union[Unset, str]):
        processed_at (Union[Unset, datetime.datetime]):
        integration_id (Union[Unset, str]):
        is_success (Union[Unset, bool]):
        status (Union[Unset, str]):
        alert_id (Union[Unset, str]):
        alias (Union[Unset, str]):
    """

    action: Union[Unset, str] = UNSET
    processed_at: Union[Unset, datetime.datetime] = UNSET
    integration_id: Union[Unset, str] = UNSET
    is_success: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    alert_id: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action

        processed_at: Union[Unset, str] = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        integration_id = self.integration_id

        is_success = self.is_success

        status = self.status

        alert_id = self.alert_id

        alias = self.alias

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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

        alert_id = d.pop("alertId", UNSET)

        alias = d.pop("alias", UNSET)

        alert_request_status = cls(
            action=action,
            processed_at=processed_at,
            integration_id=integration_id,
            is_success=is_success,
            status=status,
            alert_id=alert_id,
            alias=alias,
        )

        alert_request_status.additional_properties = d
        return alert_request_status

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
