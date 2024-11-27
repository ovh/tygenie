from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_type import IntegrationType
from ..models.outgoing_callback_callback_type import OutgoingCallbackCallbackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_filter import AlertFilter
    from ..models.team_meta import TeamMeta


T = TypeVar("T", bound="PlanioIntegration")


@_attrs_define
class PlanioIntegration:
    """
    Attributes:
        type (IntegrationType): Type of the integration. (For instance, "API" for API Integration)
        name (str): Name of the integration. Name must be unique for each integration
        id (Union[Unset, str]):
        enabled (Union[Unset, bool]): This parameter is for specifying whether the integration will be enabled or not
        owner_team (Union[Unset, TeamMeta]):
        is_global (Union[Unset, bool]):
        field_read_only (Union[Unset, List[str]]):
        alert_filter (Union[Unset, AlertFilter]):
        alert_actions (Union[Unset, List[str]]):
        callback_type (Union[Unset, OutgoingCallbackCallbackType]):
        planio_api_key (Union[Unset, str]):
        project_id (Union[Unset, int]):
        subdomain (Union[Unset, str]):
    """

    type: IntegrationType
    name: str
    id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    owner_team: Union[Unset, "TeamMeta"] = UNSET
    is_global: Union[Unset, bool] = UNSET
    field_read_only: Union[Unset, List[str]] = UNSET
    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    alert_actions: Union[Unset, List[str]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackCallbackType] = UNSET
    planio_api_key: Union[Unset, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    subdomain: Union[Unset, str] = UNSET
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

        alert_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert_filter, Unset):
            alert_filter = self.alert_filter.to_dict()

        alert_actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alert_actions, Unset):
            alert_actions = self.alert_actions

        callback_type: Union[Unset, str] = UNSET
        if not isinstance(self.callback_type, Unset):
            callback_type = self.callback_type.value

        planio_api_key = self.planio_api_key

        project_id = self.project_id

        subdomain = self.subdomain

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
        if alert_filter is not UNSET:
            field_dict["alertFilter"] = alert_filter
        if alert_actions is not UNSET:
            field_dict["alertActions"] = alert_actions
        if callback_type is not UNSET:
            field_dict["callback-type"] = callback_type
        if planio_api_key is not UNSET:
            field_dict["planioApiKey"] = planio_api_key
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_filter import AlertFilter
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

        _alert_filter = d.pop("alertFilter", UNSET)
        alert_filter: Union[Unset, AlertFilter]
        if isinstance(_alert_filter, Unset):
            alert_filter = UNSET
        else:
            alert_filter = AlertFilter.from_dict(_alert_filter)

        alert_actions = cast(List[str], d.pop("alertActions", UNSET))

        _callback_type = d.pop("callback-type", UNSET)
        callback_type: Union[Unset, OutgoingCallbackCallbackType]
        if isinstance(_callback_type, Unset):
            callback_type = UNSET
        else:
            callback_type = OutgoingCallbackCallbackType(_callback_type)

        planio_api_key = d.pop("planioApiKey", UNSET)

        project_id = d.pop("projectId", UNSET)

        subdomain = d.pop("subdomain", UNSET)

        planio_integration = cls(
            type=type,
            name=name,
            id=id,
            enabled=enabled,
            owner_team=owner_team,
            is_global=is_global,
            field_read_only=field_read_only,
            alert_filter=alert_filter,
            alert_actions=alert_actions,
            callback_type=callback_type,
            planio_api_key=planio_api_key,
            project_id=project_id,
            subdomain=subdomain,
        )

        planio_integration.additional_properties = d
        return planio_integration

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
