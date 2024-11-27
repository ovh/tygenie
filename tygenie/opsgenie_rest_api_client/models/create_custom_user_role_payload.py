from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCustomUserRolePayload")


@_attrs_define
class CreateCustomUserRolePayload:
    """
    Attributes:
        name (str): Name of custom user role
        extended_role (Union[Unset, str]): Custom role. Must not be one of the defined values (i.e. "user", "observer",
            "stakeholder")
        granted_rights (Union[Unset, List[str]]): Rights granted to the custom user role.
        disallowed_rights (Union[Unset, List[str]]): Rights disallowed for the custom user role.
    """

    name: str
    extended_role: Union[Unset, str] = UNSET
    granted_rights: Union[Unset, List[str]] = UNSET
    disallowed_rights: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        extended_role = self.extended_role

        granted_rights: Union[Unset, List[str]] = UNSET
        if not isinstance(self.granted_rights, Unset):
            granted_rights = self.granted_rights

        disallowed_rights: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disallowed_rights, Unset):
            disallowed_rights = self.disallowed_rights

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if extended_role is not UNSET:
            field_dict["extendedRole"] = extended_role
        if granted_rights is not UNSET:
            field_dict["grantedRights"] = granted_rights
        if disallowed_rights is not UNSET:
            field_dict["disallowedRights"] = disallowed_rights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        extended_role = d.pop("extendedRole", UNSET)

        granted_rights = cast(List[str], d.pop("grantedRights", UNSET))

        disallowed_rights = cast(List[str], d.pop("disallowedRights", UNSET))

        create_custom_user_role_payload = cls(
            name=name,
            extended_role=extended_role,
            granted_rights=granted_rights,
            disallowed_rights=disallowed_rights,
        )

        create_custom_user_role_payload.additional_properties = d
        return create_custom_user_role_payload

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
