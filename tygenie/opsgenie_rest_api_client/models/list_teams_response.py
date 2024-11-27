from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team import Team


T = TypeVar("T", bound="ListTeamsResponse")


@_attrs_define
class ListTeamsResponse:
    """
    Attributes:
        request_id (str):
        took (float):  Default: 0.0.
        expandable (Union[Unset, List[str]]):
        data (Union[Unset, List['Team']]):
    """

    request_id: str
    took: float = 0.0
    expandable: Union[Unset, List[str]] = UNSET
    data: Union[Unset, List["Team"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        took = self.took

        expandable: Union[Unset, List[str]] = UNSET
        if not isinstance(self.expandable, Unset):
            expandable = self.expandable

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

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
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team import Team

        d = src_dict.copy()
        request_id = d.pop("requestId")

        took = d.pop("took")

        expandable = cast(List[str], d.pop("expandable", UNSET))

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = Team.from_dict(data_item_data)

            data.append(data_item)

        list_teams_response = cls(
            request_id=request_id,
            took=took,
            expandable=expandable,
            data=data,
        )

        list_teams_response.additional_properties = d
        return list_teams_response

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
