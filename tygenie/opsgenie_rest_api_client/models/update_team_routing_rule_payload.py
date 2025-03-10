from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter
    from ..models.recipient import Recipient
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="UpdateTeamRoutingRulePayload")


@_attrs_define
class UpdateTeamRoutingRulePayload:
    """
    Attributes:
        name (Union[Unset, str]): Name of the team routing rule
        criteria (Union[Unset, Filter]): Defines the conditions that will be checked before applying rules and type of
            the operations that will be applied on conditions
        time_restriction (Union[Unset, TimeRestrictionInterval]):
        notify (Union[Unset, Recipient]):
        timezone (Union[Unset, str]): Timezone of team routing rule. If timezone field is not given, account timezone is
            used as default.
    """

    name: Union[Unset, str] = UNSET
    criteria: Union[Unset, "Filter"] = UNSET
    time_restriction: Union[Unset, "TimeRestrictionInterval"] = UNSET
    notify: Union[Unset, "Recipient"] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        criteria: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        time_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restriction, Unset):
            time_restriction = self.time_restriction.to_dict()

        notify: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notify, Unset):
            notify = self.notify.to_dict()

        timezone = self.timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if time_restriction is not UNSET:
            field_dict["timeRestriction"] = time_restriction
        if notify is not UNSET:
            field_dict["notify"] = notify
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter
        from ..models.recipient import Recipient
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _criteria = d.pop("criteria", UNSET)
        criteria: Union[Unset, Filter]
        if isinstance(_criteria, Unset):
            criteria = UNSET
        else:
            criteria = Filter.from_dict(_criteria)

        _time_restriction = d.pop("timeRestriction", UNSET)
        time_restriction: Union[Unset, TimeRestrictionInterval]
        if isinstance(_time_restriction, Unset):
            time_restriction = UNSET
        else:
            time_restriction = TimeRestrictionInterval.from_dict(_time_restriction)

        _notify = d.pop("notify", UNSET)
        notify: Union[Unset, Recipient]
        if isinstance(_notify, Unset):
            notify = UNSET
        else:
            notify = Recipient.from_dict(_notify)

        timezone = d.pop("timezone", UNSET)

        update_team_routing_rule_payload = cls(
            name=name,
            criteria=criteria,
            time_restriction=time_restriction,
            notify=notify,
            timezone=timezone,
        )

        update_team_routing_rule_payload.additional_properties = d
        return update_team_routing_rule_payload

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
