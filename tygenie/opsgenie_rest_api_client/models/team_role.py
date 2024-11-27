from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_right import TeamRight


T = TypeVar("T", bound="TeamRole")


@_attrs_define
class TeamRole:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        rights (Union[Unset, List['TeamRight']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rights: Union[Unset, List["TeamRight"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        rights: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rights, Unset):
            rights = []
            for rights_item_data in self.rights:
                rights_item = rights_item_data.to_dict()
                rights.append(rights_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rights is not UNSET:
            field_dict["rights"] = rights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_right import TeamRight

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rights = []
        _rights = d.pop("rights", UNSET)
        for rights_item_data in _rights or []:
            rights_item = TeamRight.from_dict(rights_item_data)

            rights.append(rights_item)

        team_role = cls(
            id=id,
            name=name,
            rights=rights,
        )

        team_role.additional_properties = d
        return team_role

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
