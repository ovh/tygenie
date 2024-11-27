from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationRepeat")


@_attrs_define
class EscalationRepeat:
    """
    Attributes:
        wait_interval (Union[Unset, int]):
        count (Union[Unset, int]):
        reset_recipient_states (Union[Unset, bool]):
        close_alert_after_all (Union[Unset, bool]):
    """

    wait_interval: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    reset_recipient_states: Union[Unset, bool] = UNSET
    close_alert_after_all: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wait_interval = self.wait_interval

        count = self.count

        reset_recipient_states = self.reset_recipient_states

        close_alert_after_all = self.close_alert_after_all

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wait_interval is not UNSET:
            field_dict["waitInterval"] = wait_interval
        if count is not UNSET:
            field_dict["count"] = count
        if reset_recipient_states is not UNSET:
            field_dict["resetRecipientStates"] = reset_recipient_states
        if close_alert_after_all is not UNSET:
            field_dict["closeAlertAfterAll"] = close_alert_after_all

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wait_interval = d.pop("waitInterval", UNSET)

        count = d.pop("count", UNSET)

        reset_recipient_states = d.pop("resetRecipientStates", UNSET)

        close_alert_after_all = d.pop("closeAlertAfterAll", UNSET)

        escalation_repeat = cls(
            wait_interval=wait_interval,
            count=count,
            reset_recipient_states=reset_recipient_states,
            close_alert_after_all=close_alert_after_all,
        )

        escalation_repeat.additional_properties = d
        return escalation_repeat

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
