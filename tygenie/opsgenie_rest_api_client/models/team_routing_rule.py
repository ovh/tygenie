from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter
    from ..models.recipient import Recipient
    from ..models.time_restriction_interval import TimeRestrictionInterval


T = TypeVar("T", bound="TeamRoutingRule")


@_attrs_define
class TeamRoutingRule:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        is_default (Union[Unset, bool]):
        order (Union[Unset, int]):
        criteria (Union[Unset, Filter]): Defines the conditions that will be checked before applying rules and type of
            the operations that will be applied on conditions
        timezone (Union[Unset, str]):
        time_restriction (Union[Unset, TimeRestrictionInterval]):
        notify (Union[Unset, Recipient]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    order: Union[Unset, int] = UNSET
    criteria: Union[Unset, "Filter"] = UNSET
    timezone: Union[Unset, str] = UNSET
    time_restriction: Union[Unset, "TimeRestrictionInterval"] = UNSET
    notify: Union[Unset, "Recipient"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        is_default = self.is_default

        order = self.order

        criteria: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        timezone = self.timezone

        time_restriction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restriction, Unset):
            time_restriction = self.time_restriction.to_dict()

        notify: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notify, Unset):
            notify = self.notify.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if order is not UNSET:
            field_dict["order"] = order
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if time_restriction is not UNSET:
            field_dict["timeRestriction"] = time_restriction
        if notify is not UNSET:
            field_dict["notify"] = notify

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter
        from ..models.recipient import Recipient
        from ..models.time_restriction_interval import TimeRestrictionInterval

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_default = d.pop("isDefault", UNSET)

        order = d.pop("order", UNSET)

        _criteria = d.pop("criteria", UNSET)
        criteria: Union[Unset, Filter]
        if isinstance(_criteria, Unset):
            criteria = UNSET
        else:
            criteria = Filter.from_dict(_criteria)

        timezone = d.pop("timezone", UNSET)

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

        team_routing_rule = cls(
            id=id,
            name=name,
            is_default=is_default,
            order=order,
            criteria=criteria,
            timezone=timezone,
            time_restriction=time_restriction,
            notify=notify,
        )

        team_routing_rule.additional_properties = d
        return team_routing_rule

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
