from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_right import TeamRight


T = TypeVar("T", bound="CreateTeamRolePayload")


@_attrs_define
class CreateTeamRolePayload:
    """
    Attributes:
        name (str): Name of the team role
        rights (List['TeamRight']): List of team role rights.
    """

    name: str
    rights: List["TeamRight"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        rights = []
        for rights_item_data in self.rights:
            rights_item = rights_item_data.to_dict()
            rights.append(rights_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rights": rights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_right import TeamRight

        d = src_dict.copy()
        name = d.pop("name")

        rights = []
        _rights = d.pop("rights")
        for rights_item_data in _rights:
            rights_item = TeamRight.from_dict(rights_item_data)

            rights.append(rights_item)

        create_team_role_payload = cls(
            name=name,
            rights=rights,
        )

        create_team_role_payload.additional_properties = d
        return create_team_role_payload

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
