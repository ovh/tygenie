from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageDetails")


@_attrs_define
class PageDetails:
    """
    Attributes:
        prev (Union[Unset, str]):
        next_ (Union[Unset, str]):
        first (Union[Unset, str]):
        last (Union[Unset, str]):
    """

    prev: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    first: Union[Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prev = self.prev

        next_ = self.next_

        first = self.first

        last = self.last

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prev is not UNSET:
            field_dict["prev"] = prev
        if next_ is not UNSET:
            field_dict["next"] = next_
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prev = d.pop("prev", UNSET)

        next_ = d.pop("next", UNSET)

        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        page_details = cls(
            prev=prev,
            next_=next_,
            first=first,
            last=last,
        )

        page_details.additional_properties = d
        return page_details

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
