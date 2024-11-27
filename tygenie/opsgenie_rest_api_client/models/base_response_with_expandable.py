from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseResponseWithExpandable")


@_attrs_define
class BaseResponseWithExpandable:
    """
    Attributes:
        request_id (str):
        took (float):  Default: 0.0.
        expandable (Union[Unset, List[str]]):
    """

    request_id: str
    took: float = 0.0
    expandable: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        took = self.took

        expandable: Union[Unset, List[str]] = UNSET
        if not isinstance(self.expandable, Unset):
            expandable = self.expandable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
                "took": took,
            }
        )
        if expandable is not UNSET:
            field_dict["expandable"] = expandable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("requestId")

        took = d.pop("took")

        expandable = cast(List[str], d.pop("expandable", UNSET))

        base_response_with_expandable = cls(
            request_id=request_id,
            took=took,
            expandable=expandable,
        )

        base_response_with_expandable.additional_properties = d
        return base_response_with_expandable

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
