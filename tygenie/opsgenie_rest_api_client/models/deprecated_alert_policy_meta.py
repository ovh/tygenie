from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deprecated_alert_policy_meta_type import DeprecatedAlertPolicyMetaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeprecatedAlertPolicyMeta")


@_attrs_define
class DeprecatedAlertPolicyMeta:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[Unset, DeprecatedAlertPolicyMetaType]):
        order (Union[Unset, int]):
        enabled (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, DeprecatedAlertPolicyMetaType] = UNSET
    order: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        order = self.order

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
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

        _type = d.pop("type", UNSET)
        type: Union[Unset, DeprecatedAlertPolicyMetaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DeprecatedAlertPolicyMetaType(_type)

        order = d.pop("order", UNSET)

        enabled = d.pop("enabled", UNSET)

        deprecated_alert_policy_meta = cls(
            id=id,
            name=name,
            type=type,
            order=order,
            enabled=enabled,
        )

        deprecated_alert_policy_meta.additional_properties = d
        return deprecated_alert_policy_meta

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
