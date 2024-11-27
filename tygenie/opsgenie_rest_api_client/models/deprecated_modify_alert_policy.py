from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deprecated_alert_policy_type import DeprecatedAlertPolicyType
from ..models.deprecated_modify_alert_policy_priority import DeprecatedModifyAlertPolicyPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deprecated_modify_alert_policy_details import DeprecatedModifyAlertPolicyDetails
    from ..models.filter_ import Filter
    from ..models.recipient import Recipient
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="DeprecatedModifyAlertPolicy")


@_attrs_define
class DeprecatedModifyAlertPolicy:
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
        ignore_original_alert_actions (Union[Unset, bool]):
        ignore_original_details (Union[Unset, bool]): If set to true, policy will ignore the original details of the
            alert. Default value is false
        ignore_original_recipients (Union[Unset, bool]): If set to true, policy will ignore the original recipients of
            the alert. Default value is false
        ignore_original_tags (Union[Unset, bool]): If set to true, policy will ignore the original tags of the alert.
            Default value is false
        ignore_original_teams (Union[Unset, bool]): If set to true, policy will ignore the original teams of the alert.
            Default value is false
        continue_ (Union[Unset, bool]): Will continue with other modify policies if set to true
        alias (Union[Unset, str]): Alias of the alert. You can use {{alias}} to refer to the original alias. Default
            value is {{alias}}
        description (Union[Unset, str]): Description of the alert. You can use {{description}} to refer to the original
            alert description. Default value is {{description}}
        entity (Union[Unset, str]): Entity field of the alert. You can use {{entity}} to refer to the original entity.
            Default value is {{entity}}
        message (Union[Unset, str]): Message of the alert
        source (Union[Unset, str]): Source field of the alert. You can use {{source}} to refer to the original source.
            Default value is {{source}}
        actions (Union[Unset, List[str]]): Alert actions as a list of strings to add to the alerts original actions
            value. If ignoreOriginalAlertActions field is set to true, this will replace the original actions.
        recipients (Union[Unset, List['Recipient']]): Recipients to add to the alerts original recipients value as a
            list of escalations, schedules, teams, users or the reserved word none or all. If ignoreOriginalRecipients field
            is set to true, this will replace the original recipients.
        tags (Union[Unset, List[str]]): Tags to add to the alerts original tags value as a list of strings. If
            ignoreOriginalRecipients field is set to true, this will replace the original recipients.
        details (Union[Unset, DeprecatedModifyAlertPolicyDetails]): Custom properties to add to the alerts original
            details value as a list of strings. If ignoreOriginalDetails field is set to true, this will replace the
            original details.
        priority (Union[Unset, DeprecatedModifyAlertPolicyPriority]): Priority level of the alert
    """

    type: DeprecatedAlertPolicyType
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    policy_description: Union[Unset, str] = UNSET
    filter_: Union[Unset, "Filter"] = UNSET
    time_restrictions: Union[Unset, "TimeRestrictionInterval"] = UNSET
    enabled: Union[Unset, bool] = UNSET
    ignore_original_alert_actions: Union[Unset, bool] = UNSET
    ignore_original_details: Union[Unset, bool] = UNSET
    ignore_original_recipients: Union[Unset, bool] = UNSET
    ignore_original_tags: Union[Unset, bool] = UNSET
    ignore_original_teams: Union[Unset, bool] = UNSET
    continue_: Union[Unset, bool] = UNSET
    alias: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    entity: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    actions: Union[Unset, List[str]] = UNSET
    recipients: Union[Unset, List["Recipient"]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    details: Union[Unset, "DeprecatedModifyAlertPolicyDetails"] = UNSET
    priority: Union[Unset, DeprecatedModifyAlertPolicyPriority] = UNSET
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

        ignore_original_alert_actions = self.ignore_original_alert_actions

        ignore_original_details = self.ignore_original_details

        ignore_original_recipients = self.ignore_original_recipients

        ignore_original_tags = self.ignore_original_tags

        ignore_original_teams = self.ignore_original_teams

        continue_ = self.continue_

        alias = self.alias

        description = self.description

        entity = self.entity

        message = self.message

        source = self.source

        actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions

        recipients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

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
        if ignore_original_alert_actions is not UNSET:
            field_dict["ignoreOriginalAlertActions"] = ignore_original_alert_actions
        if ignore_original_details is not UNSET:
            field_dict["ignoreOriginalDetails"] = ignore_original_details
        if ignore_original_recipients is not UNSET:
            field_dict["ignoreOriginalRecipients"] = ignore_original_recipients
        if ignore_original_tags is not UNSET:
            field_dict["ignoreOriginalTags"] = ignore_original_tags
        if ignore_original_teams is not UNSET:
            field_dict["ignoreOriginalTeams"] = ignore_original_teams
        if continue_ is not UNSET:
            field_dict["continue"] = continue_
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if entity is not UNSET:
            field_dict["entity"] = entity
        if message is not UNSET:
            field_dict["message"] = message
        if source is not UNSET:
            field_dict["source"] = source
        if actions is not UNSET:
            field_dict["actions"] = actions
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if tags is not UNSET:
            field_dict["tags"] = tags
        if details is not UNSET:
            field_dict["details"] = details
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deprecated_modify_alert_policy_details import DeprecatedModifyAlertPolicyDetails
        from ..models.filter_ import Filter
        from ..models.recipient import Recipient
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

        ignore_original_alert_actions = d.pop("ignoreOriginalAlertActions", UNSET)

        ignore_original_details = d.pop("ignoreOriginalDetails", UNSET)

        ignore_original_recipients = d.pop("ignoreOriginalRecipients", UNSET)

        ignore_original_tags = d.pop("ignoreOriginalTags", UNSET)

        ignore_original_teams = d.pop("ignoreOriginalTeams", UNSET)

        continue_ = d.pop("continue", UNSET)

        alias = d.pop("alias", UNSET)

        description = d.pop("description", UNSET)

        entity = d.pop("entity", UNSET)

        message = d.pop("message", UNSET)

        source = d.pop("source", UNSET)

        actions = cast(List[str], d.pop("actions", UNSET))

        recipients = []
        _recipients = d.pop("recipients", UNSET)
        for recipients_item_data in _recipients or []:
            recipients_item = Recipient.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        tags = cast(List[str], d.pop("tags", UNSET))

        _details = d.pop("details", UNSET)
        details: Union[Unset, DeprecatedModifyAlertPolicyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = DeprecatedModifyAlertPolicyDetails.from_dict(_details)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, DeprecatedModifyAlertPolicyPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = DeprecatedModifyAlertPolicyPriority(_priority)

        deprecated_modify_alert_policy = cls(
            type=type,
            id=id,
            name=name,
            policy_description=policy_description,
            filter_=filter_,
            time_restrictions=time_restrictions,
            enabled=enabled,
            ignore_original_alert_actions=ignore_original_alert_actions,
            ignore_original_details=ignore_original_details,
            ignore_original_recipients=ignore_original_recipients,
            ignore_original_tags=ignore_original_tags,
            ignore_original_teams=ignore_original_teams,
            continue_=continue_,
            alias=alias,
            description=description,
            entity=entity,
            message=message,
            source=source,
            actions=actions,
            recipients=recipients,
            tags=tags,
            details=details,
            priority=priority,
        )

        deprecated_modify_alert_policy.additional_properties = d
        return deprecated_modify_alert_policy

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
