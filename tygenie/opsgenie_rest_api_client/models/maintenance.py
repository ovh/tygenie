from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.maintenance_status import MaintenanceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_rule import MaintenanceRule
    from ..models.maintenance_time import MaintenanceTime


T = TypeVar("T", bound="Maintenance")


@_attrs_define
class Maintenance:
    """
    Attributes:
        id (Union[Unset, str]): Identifier of the maintenance meta data
        status (Union[Unset, MaintenanceStatus]): Status of the maintenance data
        rules (Union[Unset, List['MaintenanceRule']]): Rules of maintenance, which takes a list of rule objects and
            defines the maintenance rules over integrations and policies.
        time (Union[Unset, MaintenanceTime]):
        description (Union[Unset, str]): Description for maintenance data
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, MaintenanceStatus] = UNSET
    rules: Union[Unset, List["MaintenanceRule"]] = UNSET
    time: Union[Unset, "MaintenanceTime"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if rules is not UNSET:
            field_dict["rules"] = rules
        if time is not UNSET:
            field_dict["time"] = time
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.maintenance_rule import MaintenanceRule
        from ..models.maintenance_time import MaintenanceTime

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MaintenanceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MaintenanceStatus(_status)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = MaintenanceRule.from_dict(rules_item_data)

            rules.append(rules_item)

        _time = d.pop("time", UNSET)
        time: Union[Unset, MaintenanceTime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = MaintenanceTime.from_dict(_time)

        description = d.pop("description", UNSET)

        maintenance = cls(
            id=id,
            status=status,
            rules=rules,
            time=time,
            description=description,
        )

        maintenance.additional_properties = d
        return maintenance

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
