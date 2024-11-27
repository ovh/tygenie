from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_response_headers import ErrorResponseResponseHeaders


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        request_id (str):
        took (float):  Default: 0.0.
        message (Union[Unset, str]):
        code (Union[Unset, int]):
        response_headers (Union[Unset, ErrorResponseResponseHeaders]):
    """

    request_id: str
    took: float = 0.0
    message: Union[Unset, str] = UNSET
    code: Union[Unset, int] = UNSET
    response_headers: Union[Unset, "ErrorResponseResponseHeaders"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        took = self.took

        message = self.message

        code = self.code

        response_headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response_headers, Unset):
            response_headers = self.response_headers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
                "took": took,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if response_headers is not UNSET:
            field_dict["responseHeaders"] = response_headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response_response_headers import ErrorResponseResponseHeaders

        d = src_dict.copy()
        request_id = d.pop("requestId")

        took = d.pop("took")

        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        _response_headers = d.pop("responseHeaders", UNSET)
        response_headers: Union[Unset, ErrorResponseResponseHeaders]
        if isinstance(_response_headers, Unset):
            response_headers = UNSET
        else:
            response_headers = ErrorResponseResponseHeaders.from_dict(_response_headers)

        error_response = cls(
            request_id=request_id,
            took=took,
            message=message,
            code=code,
            response_headers=response_headers,
        )

        error_response.additional_properties = d
        return error_response

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
