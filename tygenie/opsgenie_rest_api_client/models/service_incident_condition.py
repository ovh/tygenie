from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_incident_condition_field import ServiceIncidentConditionField
from ..models.service_incident_condition_operation import ServiceIncidentConditionOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceIncidentCondition")


@_attrs_define
class ServiceIncidentCondition:
    """
    Attributes:
        field (ServiceIncidentConditionField): Specifies which alert field will be used in condition. Possible values
            are message, description, tags, extra-properties, recipients, teams or priority
        operation (ServiceIncidentConditionOperation): It is the operation that will be executed for the given field and
            key.
        key (Union[Unset, str]): If field is set as extra-properties, key could be used for key-value pair
        not_ (Union[Unset, bool]): Indicates behaviour of the given operation. Default value is false
        expected_value (Union[Unset, str]): User defined value that will be compared with alert field according to the
            operation. Default value is empty string
    """

    field: ServiceIncidentConditionField
    operation: ServiceIncidentConditionOperation
    key: Union[Unset, str] = UNSET
    not_: Union[Unset, bool] = UNSET
    expected_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field.value

        operation = self.operation.value

        key = self.key

        not_ = self.not_

        expected_value = self.expected_value

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = ServiceIncidentConditionField(d.pop("field"))

        operation = ServiceIncidentConditionOperation(d.pop("operation"))

        key = d.pop("key", UNSET)

        not_ = d.pop("not", UNSET)

        expected_value = d.pop("expectedValue", UNSET)

        service_incident_condition = cls(
            field=field,
            operation=operation,
            key=key,
            not_=not_,
            expected_value=expected_value,
        )

        service_incident_condition.additional_properties = d
        return service_incident_condition

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
