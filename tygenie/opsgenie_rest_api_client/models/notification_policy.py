from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_type import PolicyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_close_action import AutoCloseAction
    from ..models.auto_restart_action import AutoRestartAction
    from ..models.deduplication_action import DeduplicationAction
    from ..models.delay_action import DelayAction
    from ..models.filter_ import Filter
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="NotificationPolicy")


@_attrs_define
class NotificationPolicy:
    """
    Attributes:
        type (PolicyType): Type of the policy
        id (Union[Unset, str]):
        name (Union[Unset, str]): Name of the policy
        policy_description (Union[Unset, str]): Description of the policy
        team_id (Union[Unset, str]): TeamId of the policy
        filter_ (Union[Unset, Filter]): Defines the conditions that will be checked before applying rules and type of
            the operations that will be applied on conditions
        time_restrictions (Union[Unset, TimeRestrictionInterval]):
        enabled (Union[Unset, bool]): Activity status of the alert policy
        auto_restart_action (Union[Unset, AutoRestartAction]):
        auto_close_action (Union[Unset, AutoCloseAction]):
        deduplication_action (Union[Unset, DeduplicationAction]):
        delay_action (Union[Unset, DelayAction]):
        suppress (Union[Unset, bool]): If set to true, notifications related to the matching alert will be suppressed.
            Default value is false.
    """

    type: PolicyType
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    policy_description: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    filter_: Union[Unset, "Filter"] = UNSET
    time_restrictions: Union[Unset, "TimeRestrictionInterval"] = UNSET
    enabled: Union[Unset, bool] = UNSET
    auto_restart_action: Union[Unset, "AutoRestartAction"] = UNSET
    auto_close_action: Union[Unset, "AutoCloseAction"] = UNSET
    deduplication_action: Union[Unset, "DeduplicationAction"] = UNSET
    delay_action: Union[Unset, "DelayAction"] = UNSET
    suppress: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        name = self.name

        policy_description = self.policy_description

        team_id = self.team_id

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        time_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restrictions, Unset):
            time_restrictions = self.time_restrictions.to_dict()

        enabled = self.enabled

        auto_restart_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_restart_action, Unset):
            auto_restart_action = self.auto_restart_action.to_dict()

        auto_close_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_close_action, Unset):
            auto_close_action = self.auto_close_action.to_dict()

        deduplication_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deduplication_action, Unset):
            deduplication_action = self.deduplication_action.to_dict()

        delay_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delay_action, Unset):
            delay_action = self.delay_action.to_dict()

        suppress = self.suppress

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if policy_description is not UNSET:
            field_dict["policyDescription"] = policy_description
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if time_restrictions is not UNSET:
            field_dict["timeRestrictions"] = time_restrictions
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if auto_restart_action is not UNSET:
            field_dict["autoRestartAction"] = auto_restart_action
        if auto_close_action is not UNSET:
            field_dict["autoCloseAction"] = auto_close_action
        if deduplication_action is not UNSET:
            field_dict["deduplicationAction"] = deduplication_action
        if delay_action is not UNSET:
            field_dict["delayAction"] = delay_action
        if suppress is not UNSET:
            field_dict["suppress"] = suppress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auto_close_action import AutoCloseAction
        from ..models.auto_restart_action import AutoRestartAction
        from ..models.deduplication_action import DeduplicationAction
        from ..models.delay_action import DelayAction
        from ..models.filter_ import Filter
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        type = PolicyType(d.pop("type"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        policy_description = d.pop("policyDescription", UNSET)

        team_id = d.pop("teamId", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, Filter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        _time_restrictions = d.pop("timeRestrictions", UNSET)
        time_restrictions: Union[Unset, TimeRestrictionInterval]
        if isinstance(_time_restrictions, Unset):
            time_restrictions = UNSET
        else:
            time_restrictions = TimeRestrictionInterval.from_dict(_time_restrictions)

        enabled = d.pop("enabled", UNSET)

        _auto_restart_action = d.pop("autoRestartAction", UNSET)
        auto_restart_action: Union[Unset, AutoRestartAction]
        if isinstance(_auto_restart_action, Unset):
            auto_restart_action = UNSET
        else:
            auto_restart_action = AutoRestartAction.from_dict(_auto_restart_action)

        _auto_close_action = d.pop("autoCloseAction", UNSET)
        auto_close_action: Union[Unset, AutoCloseAction]
        if isinstance(_auto_close_action, Unset):
            auto_close_action = UNSET
        else:
            auto_close_action = AutoCloseAction.from_dict(_auto_close_action)

        _deduplication_action = d.pop("deduplicationAction", UNSET)
        deduplication_action: Union[Unset, DeduplicationAction]
        if isinstance(_deduplication_action, Unset):
            deduplication_action = UNSET
        else:
            deduplication_action = DeduplicationAction.from_dict(_deduplication_action)

        _delay_action = d.pop("delayAction", UNSET)
        delay_action: Union[Unset, DelayAction]
        if isinstance(_delay_action, Unset):
            delay_action = UNSET
        else:
            delay_action = DelayAction.from_dict(_delay_action)

        suppress = d.pop("suppress", UNSET)

        notification_policy = cls(
            type=type,
            id=id,
            name=name,
            policy_description=policy_description,
            team_id=team_id,
            filter_=filter_,
            time_restrictions=time_restrictions,
            enabled=enabled,
            auto_restart_action=auto_restart_action,
            auto_close_action=auto_close_action,
            deduplication_action=deduplication_action,
            delay_action=delay_action,
            suppress=suppress,
        )

        notification_policy.additional_properties = d
        return notification_policy

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
