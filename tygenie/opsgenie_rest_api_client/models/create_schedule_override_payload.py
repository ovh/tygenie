import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipient import Recipient
    from ..models.schedule_override_rotation import ScheduleOverrideRotation


T = TypeVar("T", bound="CreateScheduleOverridePayload")


@_attrs_define
class CreateScheduleOverridePayload:
    """
    Attributes:
        user (Recipient):
        start_date (datetime.datetime): Time for override starting
        end_date (datetime.datetime): Time for override ending
        alias (Union[Unset, str]): A user defined identifier for the override
        rotations (Union[Unset, List['ScheduleOverrideRotation']]): Identifier (id or name) of rotations that override
            will apply. When it's set, only specified schedule rotations will be overridden
    """

    user: "Recipient"
    start_date: datetime.datetime
    end_date: datetime.datetime
    alias: Union[Unset, str] = UNSET
    rotations: Union[Unset, List["ScheduleOverrideRotation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user.to_dict()

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        alias = self.alias

        rotations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rotations, Unset):
            rotations = []
            for rotations_item_data in self.rotations:
                rotations_item = rotations_item_data.to_dict()
                rotations.append(rotations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if rotations is not UNSET:
            field_dict["rotations"] = rotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recipient import Recipient
        from ..models.schedule_override_rotation import ScheduleOverrideRotation

        d = src_dict.copy()
        user = Recipient.from_dict(d.pop("user"))

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        alias = d.pop("alias", UNSET)

        rotations = []
        _rotations = d.pop("rotations", UNSET)
        for rotations_item_data in _rotations or []:
            rotations_item = ScheduleOverrideRotation.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        create_schedule_override_payload = cls(
            user=user,
            start_date=start_date,
            end_date=end_date,
            alias=alias,
            rotations=rotations,
        )

        create_schedule_override_payload.additional_properties = d
        return create_schedule_override_payload

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
