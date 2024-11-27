from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountPlan")


@_attrs_define
class AccountPlan:
    """
    Attributes:
        max_user_count (Union[Unset, int]):
        name (Union[Unset, str]):
        is_yearly (Union[Unset, bool]):
    """

    max_user_count: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    is_yearly: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_user_count = self.max_user_count

        name = self.name

        is_yearly = self.is_yearly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_user_count is not UNSET:
            field_dict["maxUserCount"] = max_user_count
        if name is not UNSET:
            field_dict["name"] = name
        if is_yearly is not UNSET:
            field_dict["isYearly"] = is_yearly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_user_count = d.pop("maxUserCount", UNSET)

        name = d.pop("name", UNSET)

        is_yearly = d.pop("isYearly", UNSET)

        account_plan = cls(
            max_user_count=max_user_count,
            name=name,
            is_yearly=is_yearly,
        )

        account_plan.additional_properties = d
        return account_plan

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
