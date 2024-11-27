from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_integration_action_type import BaseIntegrationActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_action_filter import IntegrationActionFilter


T = TypeVar("T", bound="CommonIntegrationAction")


@_attrs_define
class CommonIntegrationAction:
    """
    Attributes:
        name (str):
        filter_ (IntegrationActionFilter):
        type (BaseIntegrationActionType):
        order (Union[Unset, int]):
        user (Union[Unset, str]):
        note (Union[Unset, str]):
        alias (Union[Unset, str]):
    """

    name: str
    filter_: "IntegrationActionFilter"
    type: BaseIntegrationActionType
    order: Union[Unset, int] = UNSET
    user: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        filter_ = self.filter_.to_dict()

        type = self.type.value

        order = self.order

        user = self.user

        note = self.note

        alias = self.alias

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
        if user is not UNSET:
            field_dict["user"] = user
        if note is not UNSET:
            field_dict["note"] = note
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.integration_action_filter import IntegrationActionFilter

        d = src_dict.copy()
        name = d.pop("name")

        filter_ = IntegrationActionFilter.from_dict(d.pop("filter"))

        type = BaseIntegrationActionType(d.pop("type"))

        order = d.pop("order", UNSET)

        user = d.pop("user", UNSET)

        note = d.pop("note", UNSET)

        alias = d.pop("alias", UNSET)

        common_integration_action = cls(
            name=name,
            filter_=filter_,
            type=type,
            order=order,
            user=user,
            note=note,
            alias=alias,
        )

        common_integration_action.additional_properties = d
        return common_integration_action

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
