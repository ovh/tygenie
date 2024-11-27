from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bidirectional_callback_bidirectional_callback_type import BidirectionalCallbackBidirectionalCallbackType
from ..models.outgoing_callback_callback_type import OutgoingCallbackCallbackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_filter import AlertFilter


T = TypeVar("T", bound="SlackAppCallback")


@_attrs_define
class SlackAppCallback:
    """
    Attributes:
        alert_filter (Union[Unset, AlertFilter]):
        alert_actions (Union[Unset, List[str]]):
        callback_type (Union[Unset, OutgoingCallbackCallbackType]):
        send_alert_actions (Union[Unset, bool]):
        bidirectional_callback_type (Union[Unset, BidirectionalCallbackBidirectionalCallbackType]):
        channel (Union[Unset, str]):
        team_name (Union[Unset, str]):
        send_description (Union[Unset, bool]):
        send_routed_teams (Union[Unset, bool]):
        send_tags (Union[Unset, bool]):
    """

    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    alert_actions: Union[Unset, List[str]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackCallbackType] = UNSET
    send_alert_actions: Union[Unset, bool] = UNSET
    bidirectional_callback_type: Union[Unset, BidirectionalCallbackBidirectionalCallbackType] = UNSET
    channel: Union[Unset, str] = UNSET
    team_name: Union[Unset, str] = UNSET
    send_description: Union[Unset, bool] = UNSET
    send_routed_teams: Union[Unset, bool] = UNSET
    send_tags: Union[Unset, bool] = UNSET
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

        channel = self.channel

        team_name = self.team_name

        send_description = self.send_description

        send_routed_teams = self.send_routed_teams

        send_tags = self.send_tags

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
        if channel is not UNSET:
            field_dict["channel"] = channel
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if send_description is not UNSET:
            field_dict["sendDescription"] = send_description
        if send_routed_teams is not UNSET:
            field_dict["sendRoutedTeams"] = send_routed_teams
        if send_tags is not UNSET:
            field_dict["sendTags"] = send_tags

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

        channel = d.pop("channel", UNSET)

        team_name = d.pop("teamName", UNSET)

        send_description = d.pop("sendDescription", UNSET)

        send_routed_teams = d.pop("sendRoutedTeams", UNSET)

        send_tags = d.pop("sendTags", UNSET)

        slack_app_callback = cls(
            alert_filter=alert_filter,
            alert_actions=alert_actions,
            callback_type=callback_type,
            send_alert_actions=send_alert_actions,
            bidirectional_callback_type=bidirectional_callback_type,
            channel=channel,
            team_name=team_name,
            send_description=send_description,
            send_routed_teams=send_routed_teams,
            send_tags=send_tags,
        )

        slack_app_callback.additional_properties = d
        return slack_app_callback

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
