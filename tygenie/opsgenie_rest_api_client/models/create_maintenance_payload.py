from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_rule import MaintenanceRule
    from ..models.maintenance_time import MaintenanceTime


T = TypeVar("T", bound="CreateMaintenancePayload")


@_attrs_define
class CreateMaintenancePayload:
    """
    Attributes:
        time (MaintenanceTime):
        rules (List['MaintenanceRule']): Rules of maintenance, which takes a list of rule objects and defines the
            maintenance rules over integrations and policies.
        description (Union[Unset, str]): Description for the maintenance
    """

    time: "MaintenanceTime"
    rules: List["MaintenanceRule"]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time.to_dict()

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "rules": rules,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.maintenance_rule import MaintenanceRule
        from ..models.maintenance_time import MaintenanceTime

        d = src_dict.copy()
        time = MaintenanceTime.from_dict(d.pop("time"))

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = MaintenanceRule.from_dict(rules_item_data)

            rules.append(rules_item)

        description = d.pop("description", UNSET)

        create_maintenance_payload = cls(
            time=time,
            rules=rules,
            description=description,
        )

        create_maintenance_payload.additional_properties = d
        return create_maintenance_payload

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
