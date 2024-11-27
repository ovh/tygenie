from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.callback_condition_field import CallbackConditionField
from ..models.callback_condition_operation import CallbackConditionOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallbackCondition")


@_attrs_define
class CallbackCondition:
    """
    Attributes:
        field (CallbackConditionField):
        operation (CallbackConditionOperation):
        expected_value (str):
        not_ (Union[Unset, bool]):
        order (Union[Unset, int]):
    """

    field: CallbackConditionField
    operation: CallbackConditionOperation
    expected_value: str
    not_: Union[Unset, bool] = UNSET
    order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field.value

        operation = self.operation.value

        expected_value = self.expected_value

        not_ = self.not_

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "operation": operation,
                "expectedValue": expected_value,
            }
        )
        if not_ is not UNSET:
            field_dict["not"] = not_
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = CallbackConditionField(d.pop("field"))

        operation = CallbackConditionOperation(d.pop("operation"))

        expected_value = d.pop("expectedValue")

        not_ = d.pop("not", UNSET)

        order = d.pop("order", UNSET)

        callback_condition = cls(
            field=field,
            operation=operation,
            expected_value=expected_value,
            not_=not_,
            order=order,
        )

        callback_condition.additional_properties = d
        return callback_condition

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
