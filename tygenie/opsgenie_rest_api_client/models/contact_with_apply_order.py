from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_status import ContactStatus


T = TypeVar("T", bound="ContactWithApplyOrder")


@_attrs_define
class ContactWithApplyOrder:
    """
    Attributes:
        id (Union[Unset, str]):
        method (Union[Unset, str]):
        to (Union[Unset, str]):
        status (Union[Unset, ContactStatus]):
        apply_order (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    status: Union[Unset, "ContactStatus"] = UNSET
    apply_order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        method = self.method

        to = self.to

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        apply_order = self.apply_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if method is not UNSET:
            field_dict["method"] = method
        if to is not UNSET:
            field_dict["to"] = to
        if status is not UNSET:
            field_dict["status"] = status
        if apply_order is not UNSET:
            field_dict["applyOrder"] = apply_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_status import ContactStatus

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        method = d.pop("method", UNSET)

        to = d.pop("to", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ContactStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ContactStatus.from_dict(_status)

        apply_order = d.pop("applyOrder", UNSET)

        contact_with_apply_order = cls(
            id=id,
            method=method,
            to=to,
            status=status,
            apply_order=apply_order,
        )

        contact_with_apply_order.additional_properties = d
        return contact_with_apply_order

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
