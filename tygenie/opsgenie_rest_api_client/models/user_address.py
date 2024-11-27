from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAddress")


@_attrs_define
class UserAddress:
    """
    Attributes:
        country (Union[Unset, str]):
        state (Union[Unset, str]):
        city (Union[Unset, str]):
        line (Union[Unset, str]):
        zip_code (Union[Unset, str]):
    """

    country: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    line: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country = self.country

        state = self.state

        city = self.city

        line = self.line

        zip_code = self.zip_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if line is not UNSET:
            field_dict["line"] = line
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        line = d.pop("line", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        user_address = cls(
            country=country,
            state=state,
            city=city,
            line=line,
            zip_code=zip_code,
        )

        user_address.additional_properties = d
        return user_address

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
