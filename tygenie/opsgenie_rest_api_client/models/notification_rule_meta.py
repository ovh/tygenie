from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_action_type import NotificationActionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationRuleMeta")


@_attrs_define
class NotificationRuleMeta:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        action_type (Union[Unset, NotificationActionType]): Type of the action that notification rule will have
        order (Union[Unset, int]):
        enabled (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    action_type: Union[Unset, NotificationActionType] = UNSET
    order: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        action_type: Union[Unset, str] = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = self.action_type.value

        order = self.order

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if order is not UNSET:
            field_dict["order"] = order
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _action_type = d.pop("actionType", UNSET)
        action_type: Union[Unset, NotificationActionType]
        if isinstance(_action_type, Unset):
            action_type = UNSET
        else:
            action_type = NotificationActionType(_action_type)

        order = d.pop("order", UNSET)

        enabled = d.pop("enabled", UNSET)

        notification_rule_meta = cls(
            id=id,
            name=name,
            action_type=action_type,
            order=order,
            enabled=enabled,
        )

        notification_rule_meta.additional_properties = d
        return notification_rule_meta

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
