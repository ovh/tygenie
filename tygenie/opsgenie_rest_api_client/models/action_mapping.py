from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_mapping_action import ActionMappingAction
from ..models.action_mapping_mapped_action import ActionMappingMappedAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionMapping")


@_attrs_define
class ActionMapping:
    """
    Attributes:
        action (ActionMappingAction):
        extra_field (Union[Unset, str]):
        extra_field_for_mapped_action (Union[Unset, str]):
        mapped_action (Union[Unset, ActionMappingMappedAction]):
    """

    action: ActionMappingAction
    extra_field: Union[Unset, str] = UNSET
    extra_field_for_mapped_action: Union[Unset, str] = UNSET
    mapped_action: Union[Unset, ActionMappingMappedAction] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        extra_field = self.extra_field

        extra_field_for_mapped_action = self.extra_field_for_mapped_action

        mapped_action: Union[Unset, str] = UNSET
        if not isinstance(self.mapped_action, Unset):
            mapped_action = self.mapped_action.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if extra_field is not UNSET:
            field_dict["extraField"] = extra_field
        if extra_field_for_mapped_action is not UNSET:
            field_dict["extraFieldForMappedAction"] = extra_field_for_mapped_action
        if mapped_action is not UNSET:
            field_dict["mappedAction"] = mapped_action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = ActionMappingAction(d.pop("action"))

        extra_field = d.pop("extraField", UNSET)

        extra_field_for_mapped_action = d.pop("extraFieldForMappedAction", UNSET)

        _mapped_action = d.pop("mappedAction", UNSET)
        mapped_action: Union[Unset, ActionMappingMappedAction]
        if isinstance(_mapped_action, Unset):
            mapped_action = UNSET
        else:
            mapped_action = ActionMappingMappedAction(_mapped_action)

        action_mapping = cls(
            action=action,
            extra_field=extra_field,
            extra_field_for_mapped_action=extra_field_for_mapped_action,
            mapped_action=mapped_action,
        )

        action_mapping.additional_properties = d
        return action_mapping

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
