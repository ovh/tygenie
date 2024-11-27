from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bidirectional_callback_bidirectional_callback_type import BidirectionalCallbackBidirectionalCallbackType
from ..models.outgoing_callback_callback_type import OutgoingCallbackCallbackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_filter import AlertFilter


T = TypeVar("T", bound="HipChatCallbackV2")


@_attrs_define
class HipChatCallbackV2:
    """
    Attributes:
        alert_filter (Union[Unset, AlertFilter]):
        alert_actions (Union[Unset, List[str]]):
        callback_type (Union[Unset, OutgoingCallbackCallbackType]):
        send_alert_actions (Union[Unset, bool]):
        bidirectional_callback_type (Union[Unset, BidirectionalCallbackBidirectionalCallbackType]):
        rooms (Union[Unset, List[str]]):
        token (Union[Unset, str]):
        notify (Union[Unset, bool]):
        host_url (Union[Unset, str]):
    """

    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    alert_actions: Union[Unset, List[str]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackCallbackType] = UNSET
    send_alert_actions: Union[Unset, bool] = UNSET
    bidirectional_callback_type: Union[Unset, BidirectionalCallbackBidirectionalCallbackType] = UNSET
    rooms: Union[Unset, List[str]] = UNSET
    token: Union[Unset, str] = UNSET
    notify: Union[Unset, bool] = UNSET
    host_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert_filter, Unset):
            alert_filter = self.alert_filter.to_dict()

        alert_actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alert_actions, Unset):
            alert_actions = self.alert_actions

        callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.callback_type, Unset):
            callback_type = self.callback_type.value

        send_alert_actions = self.send_alert_actions

        bidirectional_callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.bidirectional_callback_type, Unset):
            bidirectional_callback_type = self.bidirectional_callback_type.value

        rooms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rooms, Unset):
            rooms = self.rooms

        token = self.token

        notify = self.notify

        host_url = self.host_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_filter is not UNSET:
            field_dict["alertFilter"] = alert_filter
        if alert_actions is not UNSET:
            field_dict["alertActions"] = alert_actions
        if callback_type is not UNSET:
            field_dict["callback-type"] = callback_type
        if send_alert_actions is not UNSET:
            field_dict["sendAlertActions"] = send_alert_actions
        if bidirectional_callback_type is not UNSET:
            field_dict["bidirectional-callback-type"] = bidirectional_callback_type
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if token is not UNSET:
            field_dict["token"] = token
        if notify is not UNSET:
            field_dict["notify"] = notify
        if host_url is not UNSET:
            field_dict["hostUrl"] = host_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_filter import AlertFilter

        d = src_dict.copy()
        _alert_filter = d.pop("alertFilter", UNSET)
        alert_filter: Union[Unset, AlertFilter]
        if isinstance(_alert_filter, Unset):
            alert_filter = UNSET
        else:
            alert_filter = AlertFilter.from_dict(_alert_filter)

        alert_actions = cast(List[str], d.pop("alertActions", UNSET))

        _callback_type = d.pop("callback-type", UNSET)
        callback_type: Union[Unset, OutgoingCallbackCallbackType]
        if isinstance(_callback_type, Unset):
            callback_type = UNSET
        else:
            callback_type = OutgoingCallbackCallbackType(_callback_type)

        send_alert_actions = d.pop("sendAlertActions", UNSET)

        _bidirectional_callback_type = d.pop("bidirectional-callback-type", UNSET)
        bidirectional_callback_type: Union[Unset, BidirectionalCallbackBidirectionalCallbackType]
        if isinstance(_bidirectional_callback_type, Unset):
            bidirectional_callback_type = UNSET
        else:
            bidirectional_callback_type = BidirectionalCallbackBidirectionalCallbackType(_bidirectional_callback_type)

        rooms = cast(List[str], d.pop("rooms", UNSET))

        token = d.pop("token", UNSET)

        notify = d.pop("notify", UNSET)

        host_url = d.pop("hostUrl", UNSET)

        hip_chat_callback_v2 = cls(
            alert_filter=alert_filter,
            alert_actions=alert_actions,
            callback_type=callback_type,
            send_alert_actions=send_alert_actions,
            bidirectional_callback_type=bidirectional_callback_type,
            rooms=rooms,
            token=token,
            notify=notify,
            host_url=host_url,
        )

        hip_chat_callback_v2.additional_properties = d
        return hip_chat_callback_v2

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
