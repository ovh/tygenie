from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_meta import ContactMeta
    from ..models.duration import Duration


T = TypeVar("T", bound="CreateNotificationRuleStepPayload")


@_attrs_define
class CreateNotificationRuleStepPayload:
    """
    Attributes:
        contact (ContactMeta):
        enabled (bool): Specifies whether given step will be enabled or not when it is created.
        send_after (Union[Unset, Duration]):
    """

    contact: "ContactMeta"
    enabled: bool
    send_after: Union[Unset, "Duration"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact.to_dict()

        enabled = self.enabled

        send_after: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.send_after, Unset):
            send_after = self.send_after.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "enabled": enabled,
            }
        )
        if send_after is not UNSET:
            field_dict["sendAfter"] = send_after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_meta import ContactMeta
        from ..models.duration import Duration

        d = src_dict.copy()
        contact = ContactMeta.from_dict(d.pop("contact"))

        enabled = d.pop("enabled")

        _send_after = d.pop("sendAfter", UNSET)
        send_after: Union[Unset, Duration]
        if isinstance(_send_after, Unset):
            send_after = UNSET
        else:
            send_after = Duration.from_dict(_send_after)

        create_notification_rule_step_payload = cls(
            contact=contact,
            enabled=enabled,
            send_after=send_after,
        )

        create_notification_rule_step_payload.additional_properties = d
        return create_notification_rule_step_payload

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