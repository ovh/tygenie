from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_contact_payload_method import CreateContactPayloadMethod

T = TypeVar("T", bound="CreateContactPayload")


@_attrs_define
class CreateContactPayload:
    """
    Attributes:
        method (CreateContactPayloadMethod): Contact method of user
        to (str): Address of contact method
    """

    method: CreateContactPayloadMethod
    to: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method.value

        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = CreateContactPayloadMethod(d.pop("method"))

        to = d.pop("to")

        create_contact_payload = cls(
            method=method,
            to=to,
        )

        create_contact_payload.additional_properties = d
        return create_contact_payload

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
