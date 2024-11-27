from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_meta import UserMeta


T = TypeVar("T", bound="AddTeamMemberPayload")


@_attrs_define
class AddTeamMemberPayload:
    """
    Attributes:
        user (UserMeta):
        role (Union[Unset, str]): Member role of the user, consisting 'user', 'admin' or a custom team role. Default
            value is 'user' Default: 'user'.
    """

    user: "UserMeta"
    role: Union[Unset, str] = "user"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user.to_dict()

        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_meta import UserMeta

        d = src_dict.copy()
        user = UserMeta.from_dict(d.pop("user"))

        role = d.pop("role", UNSET)

        add_team_member_payload = cls(
            user=user,
            role=role,
        )

        add_team_member_payload.additional_properties = d
        return add_team_member_payload

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
