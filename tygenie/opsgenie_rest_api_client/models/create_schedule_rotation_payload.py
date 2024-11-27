import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_schedule_rotation_payload_type import CreateScheduleRotationPayloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipient import Recipient
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="CreateScheduleRotationPayload")


@_attrs_define
class CreateScheduleRotationPayload:
    """
    Attributes:
        start_date (datetime.datetime): Defines a date time as an override start. Minutes may take 0 or 30 as value.
            Otherwise they will be converted to nearest 0 or 30 automatically
        type (CreateScheduleRotationPayloadType): Type of rotation. May be one of 'daily', 'weekly' and 'hourly'
        participants (List['Recipient']): List of escalations, teams, users or the reserved word none which will be used
            in schedule. Each of them can be used multiple times and will be rotated in the order they given.
        name (Union[Unset, str]): Name of rotation
        end_date (Union[Unset, datetime.datetime]): Defines a date time as an override end. Minutes may take 0 or 30 as
            value. Otherwise they will be converted to nearest 0 or 30 automatically
        length (Union[Unset, int]): Length of the rotation with default value 1
        time_restriction (Union[Unset, TimeRestrictionInterval]):
    """

    start_date: datetime.datetime
    type: CreateScheduleRotationPayloadType
    participants: List["Recipient"]
    name: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    length: Union[Unset, int] = UNSET
    time_restriction: Union[Unset, "TimeRestrictionInterval"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()

        type = self.type.value

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        name = self.name

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        length = self.length

        time_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restriction, Unset):
            time_restriction = self.time_restriction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startDate": start_date,
                "type": type,
                "participants": participants,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if length is not UNSET:
            field_dict["length"] = length
        if time_restriction is not UNSET:
            field_dict["timeRestriction"] = time_restriction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recipient import Recipient
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        start_date = isoparse(d.pop("startDate"))

        type = CreateScheduleRotationPayloadType(d.pop("type"))

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = Recipient.from_dict(participants_item_data)

            participants.append(participants_item)

        name = d.pop("name", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        length = d.pop("length", UNSET)

        _time_restriction = d.pop("timeRestriction", UNSET)
        time_restriction: Union[Unset, TimeRestrictionInterval]
        if isinstance(_time_restriction, Unset):
            time_restriction = UNSET
        else:
            time_restriction = TimeRestrictionInterval.from_dict(_time_restriction)

        create_schedule_rotation_payload = cls(
            start_date=start_date,
            type=type,
            participants=participants,
            name=name,
            end_date=end_date,
            length=length,
            time_restriction=time_restriction,
        )

        create_schedule_rotation_payload.additional_properties = d
        return create_schedule_rotation_payload

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
