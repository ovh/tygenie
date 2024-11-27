from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_integration_action_type import BaseIntegrationActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_action_filter import IntegrationActionFilter


T = TypeVar("T", bound="BaseIntegrationAction")


@_attrs_define
class BaseIntegrationAction:
    """
    Attributes:
        name (str):
        filter_ (IntegrationActionFilter):
        type (BaseIntegrationActionType):
        order (Union[Unset, int]):
    """

    name: str
    filter_: "IntegrationActionFilter"
    type: BaseIntegrationActionType
    order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        filter_ = self.filter_.to_dict()

        type = self.type.value

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filter": filter_,
                "type": type,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.integration_action_filter import IntegrationActionFilter

        d = src_dict.copy()
        name = d.pop("name")

        filter_ = IntegrationActionFilter.from_dict(d.pop("filter"))

        type = BaseIntegrationActionType(d.pop("type"))

        order = d.pop("order", UNSET)

        base_integration_action = cls(
            name=name,
            filter_=filter_,
            type=type,
            order=order,
        )

        base_integration_action.additional_properties = d
        return base_integration_action

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
