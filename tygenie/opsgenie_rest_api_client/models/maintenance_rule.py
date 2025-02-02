from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.maintenance_rule_state import MaintenanceRuleState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_entity import MaintenanceEntity


T = TypeVar("T", bound="MaintenanceRule")


@_attrs_define
class MaintenanceRule:
    """
    Attributes:
        entity (MaintenanceEntity):
        state (Union[Unset, MaintenanceRuleState]): Defines the state of the rule
    """

    entity: "MaintenanceEntity"
    state: Union[Unset, MaintenanceRuleState] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity = self.entity.to_dict()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity": entity,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.maintenance_entity import MaintenanceEntity

        d = src_dict.copy()
        entity = MaintenanceEntity.from_dict(d.pop("entity"))

        _state = d.pop("state", UNSET)
        state: Union[Unset, MaintenanceRuleState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = MaintenanceRuleState(_state)

        maintenance_rule = cls(
            entity=entity,
            state=state,
        )

        maintenance_rule.additional_properties = d
        return maintenance_rule

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
