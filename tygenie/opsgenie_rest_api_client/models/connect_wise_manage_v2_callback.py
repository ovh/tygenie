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


T = TypeVar("T", bound="ConnectWiseManageV2Callback")


@_attrs_define
class ConnectWiseManageV2Callback:
    """
    Attributes:
        alert_filter (Union[Unset, AlertFilter]):
        forwarding_enabled (Union[Unset, bool]):
        forwarding_action_mappings (Union[Unset, List['ActionMapping']]):
        callback_type (Union[Unset, OutgoingCallbackNewCallbackType]):
        updates_action_mappings (Union[Unset, List['ActionMapping']]):
        updates_enabled (Union[Unset, bool]):
        bidirectional_callback_type (Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType]):
        public_key (Union[Unset, str]):
        private_key (Union[Unset, str]):
        login_company (Union[Unset, str]):
        company_name (Union[Unset, str]):
        cwm_url (Union[Unset, str]):
        company_id (Union[Unset, str]):
        board_name (Union[Unset, str]):
        board_id (Union[Unset, int]):
    """

    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    forwarding_enabled: Union[Unset, bool] = UNSET
    forwarding_action_mappings: Union[Unset, List["ActionMapping"]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackNewCallbackType] = UNSET
    updates_action_mappings: Union[Unset, List["ActionMapping"]] = UNSET
    updates_enabled: Union[Unset, bool] = UNSET
    bidirectional_callback_type: Union[Unset, BidirectionalCallbackNewBidirectionalCallbackType] = UNSET
    public_key: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    login_company: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    cwm_url: Union[Unset, str] = UNSET
    company_id: Union[Unset, str] = UNSET
    board_name: Union[Unset, str] = UNSET
    board_id: Union[Unset, int] = UNSET
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

        public_key = self.public_key

        private_key = self.private_key

        login_company = self.login_company

        company_name = self.company_name

        cwm_url = self.cwm_url

        company_id = self.company_id

        board_name = self.board_name

        board_id = self.board_id

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
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if login_company is not UNSET:
            field_dict["loginCompany"] = login_company
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if cwm_url is not UNSET:
            field_dict["cwmUrl"] = cwm_url
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if board_name is not UNSET:
            field_dict["boardName"] = board_name
        if board_id is not UNSET:
            field_dict["boardId"] = board_id

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

        public_key = d.pop("publicKey", UNSET)

        private_key = d.pop("privateKey", UNSET)

        login_company = d.pop("loginCompany", UNSET)

        company_name = d.pop("companyName", UNSET)

        cwm_url = d.pop("cwmUrl", UNSET)

        company_id = d.pop("companyId", UNSET)

        board_name = d.pop("boardName", UNSET)

        board_id = d.pop("boardId", UNSET)

        connect_wise_manage_v2_callback = cls(
            alert_filter=alert_filter,
            forwarding_enabled=forwarding_enabled,
            forwarding_action_mappings=forwarding_action_mappings,
            callback_type=callback_type,
            updates_action_mappings=updates_action_mappings,
            updates_enabled=updates_enabled,
            bidirectional_callback_type=bidirectional_callback_type,
            public_key=public_key,
            private_key=private_key,
            login_company=login_company,
            company_name=company_name,
            cwm_url=cwm_url,
            company_id=company_id,
            board_name=board_name,
            board_id=board_id,
        )

        connect_wise_manage_v2_callback.additional_properties = d
        return connect_wise_manage_v2_callback

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
