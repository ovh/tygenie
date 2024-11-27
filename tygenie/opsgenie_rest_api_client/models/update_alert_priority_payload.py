from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alert_priority_payload_priority import UpdateAlertPriorityPayloadPriority

T = TypeVar("T", bound="UpdateAlertPriorityPayload")


@_attrs_define
class UpdateAlertPriorityPayload:
    """
    Attributes:
        priority (UpdateAlertPriorityPayloadPriority): Priority level of the alert
    """

    priority: UpdateAlertPriorityPayloadPriority
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        priority = self.priority.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priority": priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        priority = UpdateAlertPriorityPayloadPriority(d.pop("priority"))

        update_alert_priority_payload = cls(
            priority=priority,
        )

        update_alert_priority_payload.additional_properties = d
        return update_alert_priority_payload

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
