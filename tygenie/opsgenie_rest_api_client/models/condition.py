from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.condition_field import ConditionField
from ..models.condition_operation import ConditionOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="Condition")


@_attrs_define
class Condition:
    """
    Attributes:
        field (ConditionField): Specifies which alert field will be used in condition. Possible values are message,
            alias, description, source, entity, tags, actions, extra-properties, recipients or teams
        operation (ConditionOperation): It is the operation that will be executed for the given field and key.
        key (Union[Unset, str]): If field is set as extra-properties, key could be used for key-value pair
        not_ (Union[Unset, bool]): Indicates behaviour of the given operation. Default value is false
        expected_value (Union[Unset, str]): User defined value that will be compared with alert field according to the
            operation. Default value is empty string
        order (Union[Unset, int]): Order of the condition in conditions list
    """

    field: ConditionField
    operation: ConditionOperation
    key: Union[Unset, str] = UNSET
    not_: Union[Unset, bool] = UNSET
    expected_value: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field.value

        operation = self.operation.value

        key = self.key

        not_ = self.not_

        expected_value = self.expected_value

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "operation": operation,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if not_ is not UNSET:
            field_dict["not"] = not_
        if expected_value is not UNSET:
            field_dict["expectedValue"] = expected_value
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = ConditionField(d.pop("field"))

        operation = ConditionOperation(d.pop("operation"))

        key = d.pop("key", UNSET)

        not_ = d.pop("not", UNSET)

        expected_value = d.pop("expectedValue", UNSET)

        order = d.pop("order", UNSET)

        condition = cls(
            field=field,
            operation=operation,
            key=key,
            not_=not_,
            expected_value=expected_value,
            order=order,
        )

        condition.additional_properties = d
        return condition

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
