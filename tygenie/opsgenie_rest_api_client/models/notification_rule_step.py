from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_meta import ContactMeta
    from ..models.duration import Duration
    from ..models.notification_rule_step_parent import NotificationRuleStepParent


T = TypeVar("T", bound="NotificationRuleStep")


@_attrs_define
class NotificationRuleStep:
    """
    Attributes:
        field_parent (Union[Unset, NotificationRuleStepParent]):
        id (Union[Unset, str]):
        send_after (Union[Unset, Duration]):
        contact (Union[Unset, ContactMeta]):
        enabled (Union[Unset, bool]):
    """

    field_parent: Union[Unset, "NotificationRuleStepParent"] = UNSET
    id: Union[Unset, str] = UNSET
    send_after: Union[Unset, "Duration"] = UNSET
    contact: Union[Unset, "ContactMeta"] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_parent, Unset):
            field_parent = self.field_parent.to_dict()

        id = self.id

        send_after: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.send_after, Unset):
            send_after = self.send_after.to_dict()

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_parent is not UNSET:
            field_dict["_parent"] = field_parent
        if id is not UNSET:
            field_dict["id"] = id
        if send_after is not UNSET:
            field_dict["sendAfter"] = send_after
        if contact is not UNSET:
            field_dict["contact"] = contact
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_meta import ContactMeta
        from ..models.duration import Duration
        from ..models.notification_rule_step_parent import NotificationRuleStepParent

        d = src_dict.copy()
        _field_parent = d.pop("_parent", UNSET)
        field_parent: Union[Unset, NotificationRuleStepParent]
        if isinstance(_field_parent, Unset):
            field_parent = UNSET
        else:
            field_parent = NotificationRuleStepParent.from_dict(_field_parent)

        id = d.pop("id", UNSET)

        _send_after = d.pop("sendAfter", UNSET)
        send_after: Union[Unset, Duration]
        if isinstance(_send_after, Unset):
            send_after = UNSET
        else:
            send_after = Duration.from_dict(_send_after)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ContactMeta]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactMeta.from_dict(_contact)

        enabled = d.pop("enabled", UNSET)

        notification_rule_step = cls(
            field_parent=field_parent,
            id=id,
            send_after=send_after,
            contact=contact,
            enabled=enabled,
        )

        notification_rule_step.additional_properties = d
        return notification_rule_step

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
