from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outgoing_callback_callback_type import OutgoingCallbackCallbackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_filter import AlertFilter


T = TypeVar("T", bound="FlowdockCallback")


@_attrs_define
class FlowdockCallback:
    """
    Attributes:
        alert_filter (Union[Unset, AlertFilter]):
        alert_actions (Union[Unset, List[str]]):
        callback_type (Union[Unset, OutgoingCallbackCallbackType]):
        flowdock_api_token (Union[Unset, str]):
        flowdock_tags (Union[Unset, List[str]]):
        external_username (Union[Unset, str]):
    """

    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    alert_actions: Union[Unset, List[str]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackCallbackType] = UNSET
    flowdock_api_token: Union[Unset, str] = UNSET
    flowdock_tags: Union[Unset, List[str]] = UNSET
    external_username: Union[Unset, str] = UNSET
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

        flowdock_api_token = self.flowdock_api_token

        flowdock_tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flowdock_tags, Unset):
            flowdock_tags = self.flowdock_tags

        external_username = self.external_username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_filter is not UNSET:
            field_dict["alertFilter"] = alert_filter
        if alert_actions is not UNSET:
            field_dict["alertActions"] = alert_actions
        if callback_type is not UNSET:
            field_dict["callback-type"] = callback_type
        if flowdock_api_token is not UNSET:
            field_dict["flowdockApiToken"] = flowdock_api_token
        if flowdock_tags is not UNSET:
            field_dict["flowdockTags"] = flowdock_tags
        if external_username is not UNSET:
            field_dict["externalUsername"] = external_username

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

        flowdock_api_token = d.pop("flowdockApiToken", UNSET)

        flowdock_tags = cast(List[str], d.pop("flowdockTags", UNSET))

        external_username = d.pop("externalUsername", UNSET)

        flowdock_callback = cls(
            alert_filter=alert_filter,
            alert_actions=alert_actions,
            callback_type=callback_type,
            flowdock_api_token=flowdock_api_token,
            flowdock_tags=flowdock_tags,
            external_username=external_username,
        )

        flowdock_callback.additional_properties = d
        return flowdock_callback

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
