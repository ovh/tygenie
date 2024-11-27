from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipient_type import RecipientType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleRecipient")


@_attrs_define
class ScheduleRecipient:
    """Schedule recipient

    Attributes:
        type (RecipientType):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    type: RecipientType
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RecipientType(d.pop("type"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        schedule_recipient = cls(
            type=type,
            id=id,
            name=name,
        )

        schedule_recipient.additional_properties = d
        return schedule_recipient

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
