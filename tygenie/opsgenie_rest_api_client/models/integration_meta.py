from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationMeta")


@_attrs_define
class IntegrationMeta:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        type (Union[Unset, str]):
        team_id (Union[Unset, str]):
        api_key (Union[Unset, str]):
        email_address (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        enabled = self.enabled

        type = self.type

        team_id = self.team_id

        api_key = self.api_key

        email_address = self.email_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if type is not UNSET:
            field_dict["type"] = type
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        type = d.pop("type", UNSET)

        team_id = d.pop("teamId", UNSET)

        api_key = d.pop("apiKey", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        integration_meta = cls(
            id=id,
            name=name,
            enabled=enabled,
            type=type,
            team_id=team_id,
            api_key=api_key,
            email_address=email_address,
        )

        integration_meta.additional_properties = d
        return integration_meta

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
