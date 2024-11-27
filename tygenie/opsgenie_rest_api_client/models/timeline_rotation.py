from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeline_period import TimelinePeriod


T = TypeVar("T", bound="TimelineRotation")


@_attrs_define
class TimelineRotation:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        order (Union[Unset, float]):
        periods (Union[Unset, List['TimelinePeriod']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, float] = UNSET
    periods: Union[Unset, List["TimelinePeriod"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        order = self.order

        periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.timeline_period import TimelinePeriod

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = TimelinePeriod.from_dict(periods_item_data)

            periods.append(periods_item)

        timeline_rotation = cls(
            id=id,
            name=name,
            order=order,
            periods=periods,
        )

        timeline_rotation.additional_properties = d
        return timeline_rotation

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
