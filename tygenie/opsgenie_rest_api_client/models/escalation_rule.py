from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_rule_condition import EscalationRuleCondition
from ..models.escalation_rule_notify_type import EscalationRuleNotifyType

if TYPE_CHECKING:
    from ..models.duration import Duration
    from ..models.recipient import Recipient


T = TypeVar("T", bound="EscalationRule")


@_attrs_define
class EscalationRule:
    """
    Attributes:
        condition (EscalationRuleCondition):  Default: EscalationRuleCondition.IF_NOT_ACKED.
        notify_type (EscalationRuleNotifyType):  Default: EscalationRuleNotifyType.DEFAULT.
        delay (Duration):
        recipient (Recipient):
    """

    delay: "Duration"
    recipient: "Recipient"
    condition: EscalationRuleCondition = EscalationRuleCondition.IF_NOT_ACKED
    notify_type: EscalationRuleNotifyType = EscalationRuleNotifyType.DEFAULT
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition = self.condition.value

        notify_type = self.notify_type.value

        delay = self.delay.to_dict()

        recipient = self.recipient.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition": condition,
                "notifyType": notify_type,
                "delay": delay,
                "recipient": recipient,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration
        from ..models.recipient import Recipient

        d = src_dict.copy()
        condition = EscalationRuleCondition(d.pop("condition"))

        notify_type = EscalationRuleNotifyType(d.pop("notifyType"))

        delay = Duration.from_dict(d.pop("delay"))

        recipient = Recipient.from_dict(d.pop("recipient"))

        escalation_rule = cls(
            condition=condition,
            notify_type=notify_type,
            delay=delay,
            recipient=recipient,
        )

        escalation_rule.additional_properties = d
        return escalation_rule

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
