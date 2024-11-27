from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.success_data import SuccessData


T = TypeVar("T", bound="SuccessResponse")


@_attrs_define
class SuccessResponse:
    """
    Attributes:
        request_id (str):
        took (float):  Default: 0.0.
        result (Union[Unset, str]):
        data (Union[Unset, SuccessData]):
    """

    request_id: str
    took: float = 0.0
    result: Union[Unset, str] = UNSET
    data: Union[Unset, "SuccessData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        took = self.took

        result = self.result

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
                "took": took,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.success_data import SuccessData

        d = src_dict.copy()
        request_id = d.pop("requestId")

        took = d.pop("took")

        result = d.pop("result", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, SuccessData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SuccessData.from_dict(_data)

        success_response = cls(
            request_id=request_id,
            took=took,
            result=result,
            data=data,
        )

        success_response.additional_properties = d
        return success_response

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
