from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_type import IntegrationType
from ..models.outgoing_callback_new_callback_type import OutgoingCallbackNewCallbackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_mapping import ActionMapping
    from ..models.alert_filter import AlertFilter
    from ..models.team_meta import TeamMeta


T = TypeVar("T", bound="AmazonSnsOutgoingIntegration")


@_attrs_define
class AmazonSnsOutgoingIntegration:
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
        forwarding_enabled (Union[Unset, bool]):
        forwarding_action_mappings (Union[Unset, List['ActionMapping']]):
        callback_type (Union[Unset, OutgoingCallbackNewCallbackType]):
        topic_arn (Union[Unset, str]):
        region (Union[Unset, str]):
        new_conf_type (Union[Unset, bool]):
    """

    type: IntegrationType
    name: str
    id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    owner_team: Union[Unset, "TeamMeta"] = UNSET
    is_global: Union[Unset, bool] = UNSET
    field_read_only: Union[Unset, List[str]] = UNSET
    alert_filter: Union[Unset, "AlertFilter"] = UNSET
    forwarding_enabled: Union[Unset, bool] = UNSET
    forwarding_action_mappings: Union[Unset, List["ActionMapping"]] = UNSET
    callback_type: Union[Unset, OutgoingCallbackNewCallbackType] = UNSET
    topic_arn: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    new_conf_type: Union[Unset, bool] = UNSET
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

        topic_arn = self.topic_arn

        region = self.region

        new_conf_type = self.new_conf_type

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
        if forwarding_enabled is not UNSET:
            field_dict["forwardingEnabled"] = forwarding_enabled
        if forwarding_action_mappings is not UNSET:
            field_dict["forwardingActionMappings"] = forwarding_action_mappings
        if callback_type is not UNSET:
            field_dict["callback-type"] = callback_type
        if topic_arn is not UNSET:
            field_dict["topicArn"] = topic_arn
        if region is not UNSET:
            field_dict["region"] = region
        if new_conf_type is not UNSET:
            field_dict["newConfType"] = new_conf_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_mapping import ActionMapping
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

        topic_arn = d.pop("topicArn", UNSET)

        region = d.pop("region", UNSET)

        new_conf_type = d.pop("newConfType", UNSET)

        amazon_sns_outgoing_integration = cls(
            type=type,
            name=name,
            id=id,
            enabled=enabled,
            owner_team=owner_team,
            is_global=is_global,
            field_read_only=field_read_only,
            alert_filter=alert_filter,
            forwarding_enabled=forwarding_enabled,
            forwarding_action_mappings=forwarding_action_mappings,
            callback_type=callback_type,
            topic_arn=topic_arn,
            region=region,
            new_conf_type=new_conf_type,
        )

        amazon_sns_outgoing_integration.additional_properties = d
        return amazon_sns_outgoing_integration

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
