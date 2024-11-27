import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_address import UserAddress
    from ..models.user_contact import UserContact
    from ..models.user_details import UserDetails
    from ..models.user_role import UserRole


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (Union[Unset, str]):
        username (Union[Unset, str]):
        full_name (Union[Unset, str]):
        role (Union[Unset, UserRole]):
        skype_username (Union[Unset, str]): Skype username of the user
        time_zone (Union[Unset, str]): Timezone of the user. If not set, timezone of the customer will be used instead.
        locale (Union[Unset, str]): Location information of the user. If not set, locale of the customer will be used
            instead.
        user_address (Union[Unset, UserAddress]):
        tags (Union[Unset, List[str]]): List of labels attached to the user. You can label users to differentiate them
            from the rest. For example, you can add ITManager tag to differentiate people with this role from others.
        details (Union[Unset, UserDetails]): Set of user defined properties.
        blocked (Union[Unset, bool]):
        verified (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        muted_until (Union[Unset, datetime.datetime]):
        user_contacts (Union[Unset, List['UserContact']]):
    """

    id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    role: Union[Unset, "UserRole"] = UNSET
    skype_username: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    user_address: Union[Unset, "UserAddress"] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    details: Union[Unset, "UserDetails"] = UNSET
    blocked: Union[Unset, bool] = UNSET
    verified: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    muted_until: Union[Unset, datetime.datetime] = UNSET
    user_contacts: Union[Unset, List["UserContact"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        username = self.username

        full_name = self.full_name

        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
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

        blocked = self.blocked

        verified = self.verified

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        muted_until: Union[Unset, str] = UNSET
        if not isinstance(self.muted_until, Unset):
            muted_until = self.muted_until.isoformat()

        user_contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_contacts, Unset):
            user_contacts = []
            for user_contacts_item_data in self.user_contacts:
                user_contacts_item = user_contacts_item_data.to_dict()
                user_contacts.append(user_contacts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if role is not UNSET:
            field_dict["role"] = role
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
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if verified is not UNSET:
            field_dict["verified"] = verified
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if muted_until is not UNSET:
            field_dict["mutedUntil"] = muted_until
        if user_contacts is not UNSET:
            field_dict["userContacts"] = user_contacts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_address import UserAddress
        from ..models.user_contact import UserContact
        from ..models.user_details import UserDetails
        from ..models.user_role import UserRole

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        full_name = d.pop("fullName", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, UserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UserRole.from_dict(_role)

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
        details: Union[Unset, UserDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = UserDetails.from_dict(_details)

        blocked = d.pop("blocked", UNSET)

        verified = d.pop("verified", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _muted_until = d.pop("mutedUntil", UNSET)
        muted_until: Union[Unset, datetime.datetime]
        if isinstance(_muted_until, Unset):
            muted_until = UNSET
        else:
            muted_until = isoparse(_muted_until)

        user_contacts = []
        _user_contacts = d.pop("userContacts", UNSET)
        for user_contacts_item_data in _user_contacts or []:
            user_contacts_item = UserContact.from_dict(user_contacts_item_data)

            user_contacts.append(user_contacts_item)

        user = cls(
            id=id,
            username=username,
            full_name=full_name,
            role=role,
            skype_username=skype_username,
            time_zone=time_zone,
            locale=locale,
            user_address=user_address,
            tags=tags,
            details=details,
            blocked=blocked,
            verified=verified,
            created_at=created_at,
            muted_until=muted_until,
            user_contacts=user_contacts,
        )

        user.additional_properties = d
        return user

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
