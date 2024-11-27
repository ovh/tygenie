from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.responder_type import ResponderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamResponder")


@_attrs_define
class TeamResponder:
    """Team responder

    Attributes:
        type (ResponderType):
        id (str):
        name (Union[Unset, str]):
    """

    type: ResponderType
    id: str
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
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ResponderType(d.pop("type"))

        id = d.pop("id")

        name = d.pop("name", UNSET)

        team_responder = cls(
            type=type,
            id=id,
            name=name,
        )

        team_responder.additional_properties = d
        return team_responder

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
