import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipient import Recipient
    from ..models.schedule_meta import ScheduleMeta
    from ..models.schedule_override_rotation import ScheduleOverrideRotation


T = TypeVar("T", bound="ScheduleOverride")


@_attrs_define
class ScheduleOverride:
    """
    Attributes:
        field_parent (Union[Unset, ScheduleMeta]):
        alias (Union[Unset, str]):
        user (Union[Unset, Recipient]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        rotations (Union[Unset, List['ScheduleOverrideRotation']]):
    """

    field_parent: Union[Unset, "ScheduleMeta"] = UNSET
    alias: Union[Unset, str] = UNSET
    user: Union[Unset, "Recipient"] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    rotations: Union[Unset, List["ScheduleOverrideRotation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_parent, Unset):
            field_parent = self.field_parent.to_dict()

        alias = self.alias

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        rotations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rotations, Unset):
            rotations = []
            for rotations_item_data in self.rotations:
                rotations_item = rotations_item_data.to_dict()
                rotations.append(rotations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_parent is not UNSET:
            field_dict["_parent"] = field_parent
        if alias is not UNSET:
            field_dict["alias"] = alias
        if user is not UNSET:
            field_dict["user"] = user
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if rotations is not UNSET:
            field_dict["rotations"] = rotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recipient import Recipient
        from ..models.schedule_meta import ScheduleMeta
        from ..models.schedule_override_rotation import ScheduleOverrideRotation

        d = src_dict.copy()
        _field_parent = d.pop("_parent", UNSET)
        field_parent: Union[Unset, ScheduleMeta]
        if isinstance(_field_parent, Unset):
            field_parent = UNSET
        else:
            field_parent = ScheduleMeta.from_dict(_field_parent)

        alias = d.pop("alias", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, Recipient]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Recipient.from_dict(_user)

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

        rotations = []
        _rotations = d.pop("rotations", UNSET)
        for rotations_item_data in _rotations or []:
            rotations_item = ScheduleOverrideRotation.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        schedule_override = cls(
            field_parent=field_parent,
            alias=alias,
            user=user,
            start_date=start_date,
            end_date=end_date,
            rotations=rotations,
        )

        schedule_override.additional_properties = d
        return schedule_override

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
