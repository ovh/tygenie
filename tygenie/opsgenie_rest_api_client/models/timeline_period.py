import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeline_recipient import TimelineRecipient


T = TypeVar("T", bound="TimelinePeriod")


@_attrs_define
class TimelinePeriod:
    """
    Attributes:
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        type (Union[Unset, str]):
        from_user (Union[Unset, str]): Only used by 'forwarding' period types
        recipient (Union[Unset, TimelineRecipient]):
        flattened_recipients (Union[Unset, List['TimelineRecipient']]): Only used by 'historical' period types
    """

    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, str] = UNSET
    from_user: Union[Unset, str] = UNSET
    recipient: Union[Unset, "TimelineRecipient"] = UNSET
    flattened_recipients: Union[Unset, List["TimelineRecipient"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        type = self.type

        from_user = self.from_user

        recipient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        flattened_recipients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.flattened_recipients, Unset):
            flattened_recipients = []
            for flattened_recipients_item_data in self.flattened_recipients:
                flattened_recipients_item = flattened_recipients_item_data.to_dict()
                flattened_recipients.append(flattened_recipients_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if type is not UNSET:
            field_dict["type"] = type
        if from_user is not UNSET:
            field_dict["fromUser"] = from_user
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if flattened_recipients is not UNSET:
            field_dict["flattenedRecipients"] = flattened_recipients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.timeline_recipient import TimelineRecipient

        d = src_dict.copy()
        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        type = d.pop("type", UNSET)

        from_user = d.pop("fromUser", UNSET)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, TimelineRecipient]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = TimelineRecipient.from_dict(_recipient)

        flattened_recipients = []
        _flattened_recipients = d.pop("flattenedRecipients", UNSET)
        for flattened_recipients_item_data in _flattened_recipients or []:
            flattened_recipients_item = TimelineRecipient.from_dict(flattened_recipients_item_data)

            flattened_recipients.append(flattened_recipients_item)

        timeline_period = cls(
            start_date=start_date,
            end_date=end_date,
            type=type,
            from_user=from_user,
            recipient=recipient,
            flattened_recipients=flattened_recipients,
        )

        timeline_period.additional_properties = d
        return timeline_period

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
