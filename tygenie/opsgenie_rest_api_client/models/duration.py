from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.duration_time_unit import DurationTimeUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="Duration")


@_attrs_define
class Duration:
    """
    Attributes:
        time_amount (int):
        time_unit (Union[Unset, DurationTimeUnit]):  Default: DurationTimeUnit.MINUTES.
    """

    time_amount: int
    time_unit: Union[Unset, DurationTimeUnit] = DurationTimeUnit.MINUTES
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_amount = self.time_amount

        time_unit: Union[Unset, str] = UNSET
        if not isinstance(self.time_unit, Unset):
            time_unit = self.time_unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeAmount": time_amount,
            }
        )
        if time_unit is not UNSET:
            field_dict["timeUnit"] = time_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_amount = d.pop("timeAmount")

        _time_unit = d.pop("timeUnit", UNSET)
        time_unit: Union[Unset, DurationTimeUnit]
        if isinstance(_time_unit, Unset):
            time_unit = UNSET
        else:
            time_unit = DurationTimeUnit(_time_unit)

        duration = cls(
            time_amount=time_amount,
            time_unit=time_unit,
        )

        duration.additional_properties = d
        return duration

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
