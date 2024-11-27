import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schedule_rotation_type import ScheduleRotationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipient import Recipient
    from ..models.schedule_meta import ScheduleMeta
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="ScheduleRotationWithParent")


@_attrs_define
class ScheduleRotationWithParent:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        type (Union[Unset, ScheduleRotationType]):
        length (Union[Unset, int]):
        participants (Union[Unset, List['Recipient']]):
        time_restriction (Union[Unset, TimeRestrictionInterval]):
        field_parent (Union[Unset, ScheduleMeta]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, ScheduleRotationType] = UNSET
    length: Union[Unset, int] = UNSET
    participants: Union[Unset, List["Recipient"]] = UNSET
    time_restriction: Union[Unset, "TimeRestrictionInterval"] = UNSET
    field_parent: Union[Unset, "ScheduleMeta"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

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

        field_parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_parent, Unset):
            field_parent = self.field_parent.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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
        if field_parent is not UNSET:
            field_dict["_parent"] = field_parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recipient import Recipient
        from ..models.schedule_meta import ScheduleMeta
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        id = d.pop("id", UNSET)

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
        type: Union[Unset, ScheduleRotationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ScheduleRotationType(_type)

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

        _field_parent = d.pop("_parent", UNSET)
        field_parent: Union[Unset, ScheduleMeta]
        if isinstance(_field_parent, Unset):
            field_parent = UNSET
        else:
            field_parent = ScheduleMeta.from_dict(_field_parent)

        schedule_rotation_with_parent = cls(
            id=id,
            name=name,
            start_date=start_date,
            end_date=end_date,
            type=type,
            length=length,
            participants=participants,
            time_restriction=time_restriction,
            field_parent=field_parent,
        )

        schedule_rotation_with_parent.additional_properties = d
        return schedule_rotation_with_parent

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
