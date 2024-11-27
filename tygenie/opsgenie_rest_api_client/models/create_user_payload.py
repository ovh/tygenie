from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_user_payload_details import CreateUserPayloadDetails
    from ..models.user_address import UserAddress
    from ..models.user_role import UserRole


T = TypeVar("T", bound="CreateUserPayload")


@_attrs_define
class CreateUserPayload:
    """
    Attributes:
        username (str): E-mail address of the user
        full_name (str): Name of the user
        role (UserRole):
        skype_username (Union[Unset, str]): Skype username of the user
        time_zone (Union[Unset, str]): Timezone of the user. If not set, timezone of the customer will be used instead.
        locale (Union[Unset, str]): Location information of the user. If not set, locale of the customer will be used
            instead.
        user_address (Union[Unset, UserAddress]):
        tags (Union[Unset, List[str]]): List of labels attached to the user. You can label users to differentiate them
            from the rest. For example, you can add ITManager tag to differentiate people with this role from others.
        details (Union[Unset, CreateUserPayloadDetails]): Set of user defined properties.
        invitation_disabled (Union[Unset, bool]): Invitation email will not be sent if set to true. Default value is
            false
    """

    username: str
    full_name: str
    role: "UserRole"
    skype_username: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    user_address: Union[Unset, "UserAddress"] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    details: Union[Unset, "CreateUserPayloadDetails"] = UNSET
    invitation_disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        full_name = self.full_name

        role = self.role.to_dict()

        skype_username = self.skype_username

        time_zone = self.time_zone

        locale = self.locale

        user_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_address, Unset):
            user_address = self.user_address.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        invitation_disabled = self.invitation_disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "fullName": full_name,
                "role": role,
            }
        )
        if skype_username is not UNSET:
            field_dict["skypeUsername"] = skype_username
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if locale is not UNSET:
            field_dict["locale"] = locale
        if user_address is not UNSET:
            field_dict["userAddress"] = user_address
        if tags is not UNSET:
            field_dict["tags"] = tags
        if details is not UNSET:
            field_dict["details"] = details
        if invitation_disabled is not UNSET:
            field_dict["invitationDisabled"] = invitation_disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_user_payload_details import CreateUserPayloadDetails
        from ..models.user_address import UserAddress
        from ..models.user_role import UserRole

        d = src_dict.copy()
        username = d.pop("username")

        full_name = d.pop("fullName")

        role = UserRole.from_dict(d.pop("role"))

        skype_username = d.pop("skypeUsername", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        locale = d.pop("locale", UNSET)

        _user_address = d.pop("userAddress", UNSET)
        user_address: Union[Unset, UserAddress]
        if isinstance(_user_address, Unset):
            user_address = UNSET
        else:
            user_address = UserAddress.from_dict(_user_address)

        tags = cast(List[str], d.pop("tags", UNSET))

        _details = d.pop("details", UNSET)
        details: Union[Unset, CreateUserPayloadDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = CreateUserPayloadDetails.from_dict(_details)

        invitation_disabled = d.pop("invitationDisabled", UNSET)

        create_user_payload = cls(
            username=username,
            full_name=full_name,
            role=role,
            skype_username=skype_username,
            time_zone=time_zone,
            locale=locale,
            user_address=user_address,
            tags=tags,
            details=details,
            invitation_disabled=invitation_disabled,
        )

        create_user_payload.additional_properties = d
        return create_user_payload

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
