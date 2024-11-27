from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notify_time import NotifyTime
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_notification_rule_step_payload import CreateNotificationRuleStepPayload
    from ..models.filter_ import Filter
    from ..models.notification_repeat import NotificationRepeat
    from ..models.schedule_recipient import ScheduleRecipient
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="UpdateNotificationRulePayload")


@_attrs_define
class UpdateNotificationRulePayload:
    """
    Attributes:
        name (Union[Unset, str]): Name of the notification rule
        criteria (Union[Unset, Filter]): Defines the conditions that will be checked before applying rules and type of
            the operations that will be applied on conditions
        notification_time (Union[Unset, List[NotifyTime]]): List of Time Periods that notification for schedule
            start/end will be sent
        time_restriction (Union[Unset, TimeRestrictionInterval]):
        schedules (Union[Unset, List['ScheduleRecipient']]): List of schedules that notification rule will be applied
            when on call of that schedule starts/ends. This field is valid for Schedule Start/End rules
        steps (Union[Unset, List['CreateNotificationRuleStepPayload']]): List of steps that will be added to
            notification rule
        repeat (Union[Unset, NotificationRepeat]): The amount of time in minutes that notification steps will be
            repeatedly apply
        order (Union[Unset, int]): The order of the notification rule within the notification rules with the same action
            type
        enabled (Union[Unset, bool]): Defines if notification rule will be enabled or not when it is created
    """

    name: Union[Unset, str] = UNSET
    criteria: Union[Unset, "Filter"] = UNSET
    notification_time: Union[Unset, List[NotifyTime]] = UNSET
    time_restriction: Union[Unset, "TimeRestrictionInterval"] = UNSET
    schedules: Union[Unset, List["ScheduleRecipient"]] = UNSET
    steps: Union[Unset, List["CreateNotificationRuleStepPayload"]] = UNSET
    repeat: Union[Unset, "NotificationRepeat"] = UNSET
    order: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        criteria: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        notification_time: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notification_time, Unset):
            notification_time = []
            for notification_time_item_data in self.notification_time:
                notification_time_item = notification_time_item_data.value
                notification_time.append(notification_time_item)

        time_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restriction, Unset):
            time_restriction = self.time_restriction.to_dict()

        schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()
                schedules.append(schedules_item)

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        repeat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeat, Unset):
            repeat = self.repeat.to_dict()

        order = self.order

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if notification_time is not UNSET:
            field_dict["notificationTime"] = notification_time
        if time_restriction is not UNSET:
            field_dict["timeRestriction"] = time_restriction
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if steps is not UNSET:
            field_dict["steps"] = steps
        if repeat is not UNSET:
            field_dict["repeat"] = repeat
        if order is not UNSET:
            field_dict["order"] = order
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_notification_rule_step_payload import CreateNotificationRuleStepPayload
        from ..models.filter_ import Filter
        from ..models.notification_repeat import NotificationRepeat
        from ..models.schedule_recipient import ScheduleRecipient
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        name = d.pop("name", UNSET)

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

        _time_restriction = d.pop("timeRestriction", UNSET)
        time_restriction: Union[Unset, TimeRestrictionInterval]
        if isinstance(_time_restriction, Unset):
            time_restriction = UNSET
        else:
            time_restriction = TimeRestrictionInterval.from_dict(_time_restriction)

        schedules = []
        _schedules = d.pop("schedules", UNSET)
        for schedules_item_data in _schedules or []:
            schedules_item = ScheduleRecipient.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = CreateNotificationRuleStepPayload.from_dict(steps_item_data)

            steps.append(steps_item)

        _repeat = d.pop("repeat", UNSET)
        repeat: Union[Unset, NotificationRepeat]
        if isinstance(_repeat, Unset):
            repeat = UNSET
        else:
            repeat = NotificationRepeat.from_dict(_repeat)

        order = d.pop("order", UNSET)

        enabled = d.pop("enabled", UNSET)

        update_notification_rule_payload = cls(
            name=name,
            criteria=criteria,
            notification_time=notification_time,
            time_restriction=time_restriction,
            schedules=schedules,
            steps=steps,
            repeat=repeat,
            order=order,
            enabled=enabled,
        )

        update_notification_rule_payload.additional_properties = d
        return update_notification_rule_payload

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
