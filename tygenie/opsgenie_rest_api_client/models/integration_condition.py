from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_condition_operation import IntegrationConditionOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationCondition")


@_attrs_define
class IntegrationCondition:
    """
    Attributes:
        field (Union[Unset, str]):
        not_ (Union[Unset, bool]):
        operation (Union[Unset, IntegrationConditionOperation]):
        expected_value (Union[Unset, str]):
    """

    field: Union[Unset, str] = UNSET
    not_: Union[Unset, bool] = UNSET
    operation: Union[Unset, IntegrationConditionOperation] = UNSET
    expected_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        not_ = self.not_

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        expected_value = self.expected_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if not_ is not UNSET:
            field_dict["not"] = not_
        if operation is not UNSET:
            field_dict["operation"] = operation
        if expected_value is not UNSET:
            field_dict["expectedValue"] = expected_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field", UNSET)

        not_ = d.pop("not", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, IntegrationConditionOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = IntegrationConditionOperation(_operation)

        expected_value = d.pop("expectedValue", UNSET)

        integration_condition = cls(
            field=field,
            not_=not_,
            operation=operation,
            expected_value=expected_value,
        )

        integration_condition.additional_properties = d
        return integration_condition

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
