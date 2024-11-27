from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_plan import AccountPlan


T = TypeVar("T", bound="AccountInfo")


@_attrs_define
class AccountInfo:
    """
    Attributes:
        name (Union[Unset, str]):
        user_count (Union[Unset, int]):
        plan (Union[Unset, AccountPlan]):
    """

    name: Union[Unset, str] = UNSET
    user_count: Union[Unset, int] = UNSET
    plan: Union[Unset, "AccountPlan"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        user_count = self.user_count

        plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if user_count is not UNSET:
            field_dict["userCount"] = user_count
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_plan import AccountPlan

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        user_count = d.pop("userCount", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, AccountPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = AccountPlan.from_dict(_plan)

        account_info = cls(
            name=name,
            user_count=user_count,
            plan=plan,
        )

        account_info.additional_properties = d
        return account_info

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
