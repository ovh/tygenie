import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_schedule_rotation_payload_type import UpdateScheduleRotationPayloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipient import Recipient
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="UpdateScheduleRotationPayload")


@_attrs_define
class UpdateScheduleRotationPayload:
    """
    Attributes:
        name (Union[Unset, str]): Name of rotation
        start_date (Union[Unset, datetime.datetime]): Defines a date time as an override start. Minutes may take 0 or 30
            as value. Otherwise they will be converted to nearest 0 or 30 automatically
        end_date (Union[Unset, datetime.datetime]): Defines a date time as an override end. Minutes may take 0 or 30 as
            value. Otherwise they will be converted to nearest 0 or 30 automatically
        type (Union[Unset, UpdateScheduleRotationPayloadType]): Type of rotation. May be one of 'daily', 'weekly' and
            'hourly'
        length (Union[Unset, int]): Length of the rotation with default value 1
        participants (Union[Unset, List['Recipient']]): List of escalations, teams, users or the reserved word none
            which will be used in schedule. Each of them can be used multiple times and will be rotated in the order they
            given.
        time_restriction (Union[Unset, TimeRestrictionInterval]):
    """

    name: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, UpdateScheduleRotationPayloadType] = UNSET
    length: Union[Unset, int] = UNSET
    participants: Union[Unset, List["Recipient"]] = UNSET
    time_restriction: Union[Unset, "TimeRestrictionInterval"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        length = self.length

        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        time_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restriction, Unset):
            time_restriction = self.time_restriction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if type is not UNSET:
            field_dict["type"] = type
        if length is not UNSET:
            field_dict["length"] = length
        if participants is not UNSET:
            field_dict["participants"] = participants
        if time_restriction is not UNSET:
            field_dict["timeRestriction"] = time_restriction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recipient import Recipient
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        name = d.pop("name", UNSET)

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

        _type = d.pop("type", UNSET)
        type: Union[Unset, UpdateScheduleRotationPayloadType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = UpdateScheduleRotationPayloadType(_type)

        length = d.pop("length", UNSET)

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = Recipient.from_dict(participants_item_data)

            participants.append(participants_item)

        _time_restriction = d.pop("timeRestriction", UNSET)
        time_restriction: Union[Unset, TimeRestrictionInterval]
        if isinstance(_time_restriction, Unset):
            time_restriction = UNSET
        else:
            time_restriction = TimeRestrictionInterval.from_dict(_time_restriction)

        update_schedule_rotation_payload = cls(
            name=name,
            start_date=start_date,
            end_date=end_date,
            type=type,
            length=length,
            participants=participants,
            time_restriction=time_restriction,
        )

        update_schedule_rotation_payload.additional_properties = d
        return update_schedule_rotation_payload

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
