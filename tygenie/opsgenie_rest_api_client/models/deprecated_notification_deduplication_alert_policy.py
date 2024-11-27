from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deprecated_alert_policy_type import DeprecatedAlertPolicyType
from ..models.deprecated_notification_deduplication_alert_policy_deduplication_action_type import (
    DeprecatedNotificationDeduplicationAlertPolicyDeduplicationActionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration
    from ..models.filter_ import Filter
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="DeprecatedNotificationDeduplicationAlertPolicy")


@_attrs_define
class DeprecatedNotificationDeduplicationAlertPolicy:
    """
    Attributes:
        type (DeprecatedAlertPolicyType): Type of the policy
        id (Union[Unset, str]):
        name (Union[Unset, str]): Name of the policy
        policy_description (Union[Unset, str]): Description of the policy
        filter_ (Union[Unset, Filter]): Defines the conditions that will be checked before applying rules and type of
            the operations that will be applied on conditions
        time_restrictions (Union[Unset, TimeRestrictionInterval]):
        enabled (Union[Unset, bool]): Activity status of the alert policy
        deduplication_action_type (Union[Unset, DeprecatedNotificationDeduplicationAlertPolicyDeduplicationActionType]):
            Deduplication type
        count (Union[Unset, int]): Number of alerts before deduplication
        duration (Union[Unset, Duration]):
    """

    type: DeprecatedAlertPolicyType
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    policy_description: Union[Unset, str] = UNSET
    filter_: Union[Unset, "Filter"] = UNSET
    time_restrictions: Union[Unset, "TimeRestrictionInterval"] = UNSET
    enabled: Union[Unset, bool] = UNSET
    deduplication_action_type: Union[Unset, DeprecatedNotificationDeduplicationAlertPolicyDeduplicationActionType] = (
        UNSET
    )
    count: Union[Unset, int] = UNSET
    duration: Union[Unset, "Duration"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        name = self.name

        policy_description = self.policy_description

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        time_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restrictions, Unset):
            time_restrictions = self.time_restrictions.to_dict()

        enabled = self.enabled

        deduplication_action_type: Union[Unset, str] = UNSET
        if not isinstance(self.deduplication_action_type, Unset):
            deduplication_action_type = self.deduplication_action_type.value

        count = self.count

        duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

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
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if time_restrictions is not UNSET:
            field_dict["timeRestrictions"] = time_restrictions
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if deduplication_action_type is not UNSET:
            field_dict["deduplicationActionType"] = deduplication_action_type
        if count is not UNSET:
            field_dict["count"] = count
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration
        from ..models.filter_ import Filter
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        type = DeprecatedAlertPolicyType(d.pop("type"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        policy_description = d.pop("policyDescription", UNSET)

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

        _deduplication_action_type = d.pop("deduplicationActionType", UNSET)
        deduplication_action_type: Union[Unset, DeprecatedNotificationDeduplicationAlertPolicyDeduplicationActionType]
        if isinstance(_deduplication_action_type, Unset):
            deduplication_action_type = UNSET
        else:
            deduplication_action_type = DeprecatedNotificationDeduplicationAlertPolicyDeduplicationActionType(
                _deduplication_action_type
            )

        count = d.pop("count", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, Duration]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = Duration.from_dict(_duration)

        deprecated_notification_deduplication_alert_policy = cls(
            type=type,
            id=id,
            name=name,
            policy_description=policy_description,
            filter_=filter_,
            time_restrictions=time_restrictions,
            enabled=enabled,
            deduplication_action_type=deduplication_action_type,
            count=count,
            duration=duration,
        )

        deprecated_notification_deduplication_alert_policy.additional_properties = d
        return deprecated_notification_deduplication_alert_policy

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