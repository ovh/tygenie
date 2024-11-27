from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertReport")


@_attrs_define
class AlertReport:
    """
    Attributes:
        ack_time (Union[Unset, int]):
        close_time (Union[Unset, int]):
        acknowledged_by (Union[Unset, str]):
        closed_by (Union[Unset, str]):
    """

    ack_time: Union[Unset, int] = UNSET
    close_time: Union[Unset, int] = UNSET
    acknowledged_by: Union[Unset, str] = UNSET
    closed_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ack_time = self.ack_time

        close_time = self.close_time

        acknowledged_by = self.acknowledged_by

        closed_by = self.closed_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ack_time is not UNSET:
            field_dict["ackTime"] = ack_time
        if close_time is not UNSET:
            field_dict["closeTime"] = close_time
        if acknowledged_by is not UNSET:
            field_dict["acknowledgedBy"] = acknowledged_by
        if closed_by is not UNSET:
            field_dict["closedBy"] = closed_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ack_time = d.pop("ackTime", UNSET)

        close_time = d.pop("closeTime", UNSET)

        acknowledged_by = d.pop("acknowledgedBy", UNSET)

        closed_by = d.pop("closedBy", UNSET)

        alert_report = cls(
            ack_time=ack_time,
            close_time=close_time,
            acknowledged_by=acknowledged_by,
            closed_by=closed_by,
        )

        alert_report.additional_properties = d
        return alert_report

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
