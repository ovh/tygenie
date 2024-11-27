from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_recipient import EscalationRecipient


T = TypeVar("T", bound="EscalateAlertToNextPayload")


@_attrs_define
class EscalateAlertToNextPayload:
    """
    Attributes:
        escalation (EscalationRecipient): Escalation recipient
        user (Union[Unset, str]): Display name of the request owner
        note (Union[Unset, str]): Additional note that will be added while creating the alert
        source (Union[Unset, str]): Source field of the alert. Default value is IP address of the incoming request
    """

    escalation: "EscalationRecipient"
    user: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        escalation = self.escalation.to_dict()

        user = self.user

        note = self.note

        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation": escalation,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if note is not UNSET:
            field_dict["note"] = note
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_recipient import EscalationRecipient

        d = src_dict.copy()
        escalation = EscalationRecipient.from_dict(d.pop("escalation"))

        user = d.pop("user", UNSET)

        note = d.pop("note", UNSET)

        source = d.pop("source", UNSET)

        escalate_alert_to_next_payload = cls(
            escalation=escalation,
            user=user,
            note=note,
            source=source,
        )

        escalate_alert_to_next_payload.additional_properties = d
        return escalate_alert_to_next_payload

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
