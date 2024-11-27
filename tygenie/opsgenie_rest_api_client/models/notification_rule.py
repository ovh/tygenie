from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_action_type import NotificationActionType
from ..models.notify_time import NotifyTime
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter
    from ..models.notification_repeat import NotificationRepeat
    from ..models.notification_rule_step import NotificationRuleStep
    from ..models.schedule_recipient import ScheduleRecipient
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="NotificationRule")


@_attrs_define
class NotificationRule:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        action_type (Union[Unset, NotificationActionType]): Type of the action that notification rule will have
        criteria (Union[Unset, Filter]): Defines the conditions that will be checked before applying rules and type of
            the operations that will be applied on conditions
        notification_time (Union[Unset, List[NotifyTime]]):
        order (Union[Unset, int]):
        time_restriction (Union[Unset, TimeRestrictionInterval]):
        steps (Union[Unset, List['NotificationRuleStep']]):
        schedules (Union[Unset, List['ScheduleRecipient']]):
        repeat (Union[Unset, NotificationRepeat]): The amount of time in minutes that notification steps will be
            repeatedly apply
        enabled (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    action_type: Union[Unset, NotificationActionType] = UNSET
    criteria: Union[Unset, "Filter"] = UNSET
    notification_time: Union[Unset, List[NotifyTime]] = UNSET
    order: Union[Unset, int] = UNSET
    time_restriction: Union[Unset, "TimeRestrictionInterval"] = UNSET
    steps: Union[Unset, List["NotificationRuleStep"]] = UNSET
    schedules: Union[Unset, List["ScheduleRecipient"]] = UNSET
    repeat: Union[Unset, "NotificationRepeat"] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        action_type: Union[Unset, str] = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = self.action_type.value

        criteria: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        notification_time: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notification_time, Unset):
            notification_time = []
            for notification_time_item_data in self.notification_time:
                notification_time_item = notification_time_item_data.value
                notification_time.append(notification_time_item)

        order = self.order

        time_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restriction, Unset):
            time_restriction = self.time_restriction.to_dict()

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()
                schedules.append(schedules_item)

        repeat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeat, Unset):
            repeat = self.repeat.to_dict()

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if notification_time is not UNSET:
            field_dict["notificationTime"] = notification_time
        if order is not UNSET:
            field_dict["order"] = order
        if time_restriction is not UNSET:
            field_dict["timeRestriction"] = time_restriction
        if steps is not UNSET:
            field_dict["steps"] = steps
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if repeat is not UNSET:
            field_dict["repeat"] = repeat
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter
        from ..models.notification_repeat import NotificationRepeat
        from ..models.notification_rule_step import NotificationRuleStep
        from ..models.schedule_recipient import ScheduleRecipient
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _action_type = d.pop("actionType", UNSET)
        action_type: Union[Unset, NotificationActionType]
        if isinstance(_action_type, Unset):
            action_type = UNSET
        else:
            action_type = NotificationActionType(_action_type)

        _criteria = d.pop("criteria", UNSET)
        criteria: Union[Unset, Filter]
        if isinstance(_criteria, Unset):
            criteria = UNSET
        else:
            criteria = Filter.from_dict(_criteria)

        notification_time = []
        _notification_time = d.pop("notificationTime", UNSET)
        for notification_time_item_data in _notification_time or []:
            notification_time_item = NotifyTime(notification_time_item_data)

            notification_time.append(notification_time_item)

        order = d.pop("order", UNSET)

        _time_restriction = d.pop("timeRestriction", UNSET)
        time_restriction: Union[Unset, TimeRestrictionInterval]
        if isinstance(_time_restriction, Unset):
            time_restriction = UNSET
        else:
            time_restriction = TimeRestrictionInterval.from_dict(_time_restriction)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = NotificationRuleStep.from_dict(steps_item_data)

            steps.append(steps_item)

        schedules = []
        _schedules = d.pop("schedules", UNSET)
        for schedules_item_data in _schedules or []:
            schedules_item = ScheduleRecipient.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        _repeat = d.pop("repeat", UNSET)
        repeat: Union[Unset, NotificationRepeat]
        if isinstance(_repeat, Unset):
            repeat = UNSET
        else:
            repeat = NotificationRepeat.from_dict(_repeat)

        enabled = d.pop("enabled", UNSET)

        notification_rule = cls(
            id=id,
            name=name,
            action_type=action_type,
            criteria=criteria,
            notification_time=notification_time,
            order=order,
            time_restriction=time_restriction,
            steps=steps,
            schedules=schedules,
            repeat=repeat,
            enabled=enabled,
        )

        notification_rule.additional_properties = d
        return notification_rule

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
