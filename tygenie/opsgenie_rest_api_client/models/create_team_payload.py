from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_member import TeamMember


T = TypeVar("T", bound="CreateTeamPayload")


@_attrs_define
class CreateTeamPayload:
    """
    Attributes:
        name (str): Name of the team
        description (Union[Unset, str]): The description of team
        members (Union[Unset, List['TeamMember']]): The users which will be added to team, and optionally their roles.
    """

    name: str
    description: Union[Unset, str] = UNSET
    members: Union[Unset, List["TeamMember"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_member import TeamMember

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = TeamMember.from_dict(members_item_data)

            members.append(members_item)

        create_team_payload = cls(
            name=name,
            description=description,
            members=members,
        )

        create_team_payload.additional_properties = d
        return create_team_payload

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
