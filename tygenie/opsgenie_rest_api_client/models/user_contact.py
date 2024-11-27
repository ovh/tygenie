from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_contact_contact_method import UserContactContactMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserContact")


@_attrs_define
class UserContact:
    """
    Attributes:
        to (Union[Unset, str]):
        id (Union[Unset, str]):
        contact_method (Union[Unset, UserContactContactMethod]):
        disabled_reason (Union[Unset, str]):
        enabled (Union[Unset, bool]):
    """

    to: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    contact_method: Union[Unset, UserContactContactMethod] = UNSET
    disabled_reason: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        to = self.to

        id = self.id

        contact_method: Union[Unset, str] = UNSET
        if not isinstance(self.contact_method, Unset):
            contact_method = self.contact_method.value

        disabled_reason = self.disabled_reason

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if to is not UNSET:
            field_dict["to"] = to
        if id is not UNSET:
            field_dict["id"] = id
        if contact_method is not UNSET:
            field_dict["contactMethod"] = contact_method
        if disabled_reason is not UNSET:
            field_dict["disabledReason"] = disabled_reason
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        to = d.pop("to", UNSET)

        id = d.pop("id", UNSET)

        _contact_method = d.pop("contactMethod", UNSET)
        contact_method: Union[Unset, UserContactContactMethod]
        if isinstance(_contact_method, Unset):
            contact_method = UNSET
        else:
            contact_method = UserContactContactMethod(_contact_method)

        disabled_reason = d.pop("disabledReason", UNSET)

        enabled = d.pop("enabled", UNSET)

        user_contact = cls(
            to=to,
            id=id,
            contact_method=contact_method,
            disabled_reason=disabled_reason,
            enabled=enabled,
        )

        user_contact.additional_properties = d
        return user_contact

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
