from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_schedule_rotation_payload import CreateScheduleRotationPayload
    from ..models.team_meta import TeamMeta


T = TypeVar("T", bound="CreateSchedulePayload")


@_attrs_define
class CreateSchedulePayload:
    """
    Attributes:
        name (str): Name of the schedule
        description (Union[Unset, str]): The description of schedule
        timezone (Union[Unset, str]): Timezone of schedule
        enabled (Union[Unset, bool]): Enable/disable state of schedule
        owner_team (Union[Unset, TeamMeta]):
        rotations (Union[Unset, List['CreateScheduleRotationPayload']]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    owner_team: Union[Unset, "TeamMeta"] = UNSET
    rotations: Union[Unset, List["CreateScheduleRotationPayload"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        timezone = self.timezone

        enabled = self.enabled

        owner_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner_team, Unset):
            owner_team = self.owner_team.to_dict()

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
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if owner_team is not UNSET:
            field_dict["ownerTeam"] = owner_team
        if rotations is not UNSET:
            field_dict["rotations"] = rotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_schedule_rotation_payload import CreateScheduleRotationPayload
        from ..models.team_meta import TeamMeta

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        timezone = d.pop("timezone", UNSET)

        enabled = d.pop("enabled", UNSET)

        _owner_team = d.pop("ownerTeam", UNSET)
        owner_team: Union[Unset, TeamMeta]
        if isinstance(_owner_team, Unset):
            owner_team = UNSET
        else:
            owner_team = TeamMeta.from_dict(_owner_team)

        rotations = []
        _rotations = d.pop("rotations", UNSET)
        for rotations_item_data in _rotations or []:
            rotations_item = CreateScheduleRotationPayload.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        create_schedule_payload = cls(
            name=name,
            description=description,
            timezone=timezone,
            enabled=enabled,
            owner_team=owner_team,
            rotations=rotations,
        )

        create_schedule_payload.additional_properties = d
        return create_schedule_payload

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
