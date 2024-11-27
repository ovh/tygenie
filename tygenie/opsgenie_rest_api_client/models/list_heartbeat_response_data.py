from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heartbeat import Heartbeat


T = TypeVar("T", bound="ListHeartbeatResponseData")


@_attrs_define
class ListHeartbeatResponseData:
    """
    Attributes:
        heartbeats (Union[Unset, List['Heartbeat']]):
    """

    heartbeats: Union[Unset, List["Heartbeat"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        heartbeats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.heartbeats, Unset):
            heartbeats = []
            for heartbeats_item_data in self.heartbeats:
                heartbeats_item = heartbeats_item_data.to_dict()
                heartbeats.append(heartbeats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heartbeats is not UNSET:
            field_dict["heartbeats"] = heartbeats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.heartbeat import Heartbeat

        d = src_dict.copy()
        heartbeats = []
        _heartbeats = d.pop("heartbeats", UNSET)
        for heartbeats_item_data in _heartbeats or []:
            heartbeats_item = Heartbeat.from_dict(heartbeats_item_data)

            heartbeats.append(heartbeats_item)

        list_heartbeat_response_data = cls(
            heartbeats=heartbeats,
        )

        list_heartbeat_response_data.additional_properties = d
        return list_heartbeat_response_data

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
