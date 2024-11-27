from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_type import IntegrationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_meta import TeamMeta


T = TypeVar("T", bound="Integration")


@_attrs_define
class Integration:
    """
    Attributes:
        type (IntegrationType): Type of the integration. (For instance, "API" for API Integration)
        name (str): Name of the integration. Name must be unique for each integration
        id (Union[Unset, str]):
        enabled (Union[Unset, bool]): This parameter is for specifying whether the integration will be enabled or not
        owner_team (Union[Unset, TeamMeta]):
        is_global (Union[Unset, bool]):
        field_read_only (Union[Unset, List[str]]):
    """

    type: IntegrationType
    name: str
    id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    owner_team: Union[Unset, "TeamMeta"] = UNSET
    is_global: Union[Unset, bool] = UNSET
    field_read_only: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name

        id = self.id

        enabled = self.enabled

        owner_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner_team, Unset):
            owner_team = self.owner_team.to_dict()

        is_global = self.is_global

        field_read_only: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_read_only, Unset):
            field_read_only = self.field_read_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if owner_team is not UNSET:
            field_dict["ownerTeam"] = owner_team
        if is_global is not UNSET:
            field_dict["isGlobal"] = is_global
        if field_read_only is not UNSET:
            field_dict["_readOnly"] = field_read_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_meta import TeamMeta

        d = src_dict.copy()
        type = IntegrationType(d.pop("type"))

        name = d.pop("name")

        id = d.pop("id", UNSET)

        enabled = d.pop("enabled", UNSET)

        _owner_team = d.pop("ownerTeam", UNSET)
        owner_team: Union[Unset, TeamMeta]
        if isinstance(_owner_team, Unset):
            owner_team = UNSET
        else:
            owner_team = TeamMeta.from_dict(_owner_team)

        is_global = d.pop("isGlobal", UNSET)

        field_read_only = cast(List[str], d.pop("_readOnly", UNSET))

        integration = cls(
            type=type,
            name=name,
            id=id,
            enabled=enabled,
            owner_team=owner_team,
            is_global=is_global,
            field_read_only=field_read_only,
        )

        integration.additional_properties = d
        return integration

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
