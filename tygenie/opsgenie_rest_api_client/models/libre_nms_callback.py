from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bidirectional_callback_new_bidirectional_callback_type import (
    BidirectionalCallbackNewBidirectionalCallbackType,
)
from ..models.outgoing_callback_new_callback_type import OutgoingCallbackNewCallbackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_mapping import ActionMapping
    from ..models.alert_filter import AlertFilter


T = TypeVar("T", bound="LibreNMSCallback")


@_attrs_define
class LibreNMSCallback:
    """
    Attributes:
        alert_filter (Union[Unset, AlertFilter]):
        forwarding_enabled (Union[Unset, bool]):
        forwarding_action_mappings (Union[Unset, List['ActionMapping']]):
        callback_type (Union[Unset, OutgoingCallbackNewCallbackType]):
        updates_action_mappings (Union[Unset, List['ActionMapping']]):
        updates_enabled (Union[Unset, bool]):
        bidirectional_callback_type (Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType]):
        url (Union[Unset, str]):
        api_token (Union[Unset, str]):
    """

    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    forwarding_enabled: Union[Unset, bool] = UNSET
    forwarding_action_mappings: Union[Unset, List["ActionMapping"]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackNewCallbackType] = UNSET
    updates_action_mappings: Union[Unset, List["ActionMapping"]] = UNSET
    updates_enabled: Union[Unset, bool] = UNSET
    bidirectional_callback_type: Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType] = UNSET
    url: Union[Unset, str] = UNSET
    api_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert_filter, Unset):
            alert_filter = self.alert_filter.to_dict()

        forwarding_enabled = self.forwarding_enabled

        forwarding_action_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.forwarding_action_mappings, Unset):
            forwarding_action_mappings = []
            for forwarding_action_mappings_item_data in self.forwarding_action_mappings:
                forwarding_action_mappings_item = forwarding_action_mappings_item_data.to_dict()
                forwarding_action_mappings.append(forwarding_action_mappings_item)

        callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.callback_type, Unset):
            callback_type = self.callback_type.value

        updates_action_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.updates_action_mappings, Unset):
            updates_action_mappings = []
            for updates_action_mappings_item_data in self.updates_action_mappings:
                updates_action_mappings_item = updates_action_mappings_item_data.to_dict()
                updates_action_mappings.append(updates_action_mappings_item)

        updates_enabled = self.updates_enabled

        bidirectional_callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.bidirectional_callback_type, Unset):
            bidirectional_callback_type = self.bidirectional_callback_type.value

        url = self.url

        api_token = self.api_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_filter is not UNSET:
            field_dict["alertFilter"] = alert_filter
        if forwarding_enabled is not UNSET:
            field_dict["forwardingEnabled"] = forwarding_enabled
        if forwarding_action_mappings is not UNSET:
            field_dict["forwardingActionMappings"] = forwarding_action_mappings
        if callback_type is not UNSET:
            field_dict["callback-type"] = callback_type
        if updates_action_mappings is not UNSET:
            field_dict["updatesActionMappings"] = updates_action_mappings
        if updates_enabled is not UNSET:
            field_dict["updatesEnabled"] = updates_enabled
        if bidirectional_callback_type is not UNSET:
            field_dict["bidirectional-callback-type"] = bidirectional_callback_type
        if url is not UNSET:
            field_dict["url"] = url
        if api_token is not UNSET:
            field_dict["apiToken"] = api_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_mapping import ActionMapping
        from ..models.alert_filter import AlertFilter

        d = src_dict.copy()
        _alert_filter = d.pop("alertFilter", UNSET)
        alert_filter: Union[Unset, AlertFilter]
        if isinstance(_alert_filter, Unset):
            alert_filter = UNSET
        else:
            alert_filter = AlertFilter.from_dict(_alert_filter)

        forwarding_enabled = d.pop("forwardingEnabled", UNSET)

        forwarding_action_mappings = []
        _forwarding_action_mappings = d.pop("forwardingActionMappings", UNSET)
        for forwarding_action_mappings_item_data in _forwarding_action_mappings or []:
            forwarding_action_mappings_item = ActionMapping.from_dict(forwarding_action_mappings_item_data)

            forwarding_action_mappings.append(forwarding_action_mappings_item)

        _callback_type = d.pop("callback-type", UNSET)
        callback_type: Union[Unset, OutgoingCallbackNewCallbackType]
        if isinstance(_callback_type, Unset):
            callback_type = UNSET
        else:
            callback_type = OutgoingCallbackNewCallbackType(_callback_type)

        updates_action_mappings = []
        _updates_action_mappings = d.pop("updatesActionMappings", UNSET)
        for updates_action_mappings_item_data in _updates_action_mappings or []:
            updates_action_mappings_item = ActionMapping.from_dict(updates_action_mappings_item_data)

            updates_action_mappings.append(updates_action_mappings_item)

        updates_enabled = d.pop("updatesEnabled", UNSET)

        _bidirectional_callback_type = d.pop("bidirectional-callback-type", UNSET)
        bidirectional_callback_type: Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType]
        if isinstance(_bidirectional_callback_type, Unset):
            bidirectional_callback_type = UNSET
        else:
            bidirectional_callback_type = BidirectionalCallbackNewBidirectionalCallbackType(
                _bidirectional_callback_type
            )

        url = d.pop("url", UNSET)

        api_token = d.pop("apiToken", UNSET)

        libre_nms_callback = cls(
            alert_filter=alert_filter,
            forwarding_enabled=forwarding_enabled,
            forwarding_action_mappings=forwarding_action_mappings,
            callback_type=callback_type,
            updates_action_mappings=updates_action_mappings,
            updates_enabled=updates_enabled,
            bidirectional_callback_type=bidirectional_callback_type,
            url=url,
            api_token=api_token,
        )

        libre_nms_callback.additional_properties = d
        return libre_nms_callback

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
