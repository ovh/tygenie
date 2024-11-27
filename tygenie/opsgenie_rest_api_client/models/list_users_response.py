from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_details import PageDetails
    from ..models.user import User


T = TypeVar("T", bound="ListUsersResponse")


@_attrs_define
class ListUsersResponse:
    """
    Attributes:
        request_id (str):
        took (float):  Default: 0.0.
        data (Union[Unset, List['User']]):
        total_count (Union[Unset, int]):
        paging (Union[Unset, PageDetails]):
    """

    request_id: str
    took: float = 0.0
    data: Union[Unset, List["User"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    paging: Union[Unset, "PageDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        took = self.took

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        total_count = self.total_count

        paging: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
                "took": took,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if paging is not UNSET:
            field_dict["paging"] = paging

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.page_details import PageDetails
        from ..models.user import User

        d = src_dict.copy()
        request_id = d.pop("requestId")

        took = d.pop("took")

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = User.from_dict(data_item_data)

            data.append(data_item)

        total_count = d.pop("totalCount", UNSET)

        _paging = d.pop("paging", UNSET)
        paging: Union[Unset, PageDetails]
        if isinstance(_paging, Unset):
            paging = UNSET
        else:
            paging = PageDetails.from_dict(_paging)

        list_users_response = cls(
            request_id=request_id,
            took=took,
            data=data,
            total_count=total_count,
            paging=paging,
        )

        list_users_response.additional_properties = d
        return list_users_response

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
