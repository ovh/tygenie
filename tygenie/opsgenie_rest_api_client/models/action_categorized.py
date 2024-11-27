from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_integration_action import BaseIntegrationAction
    from ..models.common_integration_action import CommonIntegrationAction
    from ..models.create_integration_action import CreateIntegrationAction
    from ..models.integration_meta import IntegrationMeta


T = TypeVar("T", bound="ActionCategorized")


@_attrs_define
class ActionCategorized:
    """
    Attributes:
        field_parent (Union[Unset, IntegrationMeta]):
        ignore (Union[Unset, List['BaseIntegrationAction']]):
        create (Union[Unset, List['CreateIntegrationAction']]):
        close (Union[Unset, List['CommonIntegrationAction']]):
        acknowledge (Union[Unset, List['CommonIntegrationAction']]):
        add_note (Union[Unset, List['CommonIntegrationAction']]):
    """

    field_parent: Union[Unset, "IntegrationMeta"] = UNSET
    ignore: Union[Unset, List["BaseIntegrationAction"]] = UNSET
    create: Union[Unset, List["CreateIntegrationAction"]] = UNSET
    close: Union[Unset, List["CommonIntegrationAction"]] = UNSET
    acknowledge: Union[Unset, List["CommonIntegrationAction"]] = UNSET
    add_note: Union[Unset, List["CommonIntegrationAction"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_parent, Unset):
            field_parent = self.field_parent.to_dict()

        ignore: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ignore, Unset):
            ignore = []
            for ignore_item_data in self.ignore:
                ignore_item = ignore_item_data.to_dict()
                ignore.append(ignore_item)

        create: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.create, Unset):
            create = []
            for create_item_data in self.create:
                create_item = create_item_data.to_dict()
                create.append(create_item)

        close: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.close, Unset):
            close = []
            for close_item_data in self.close:
                close_item = close_item_data.to_dict()
                close.append(close_item)

        acknowledge: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acknowledge, Unset):
            acknowledge = []
            for acknowledge_item_data in self.acknowledge:
                acknowledge_item = acknowledge_item_data.to_dict()
                acknowledge.append(acknowledge_item)

        add_note: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.add_note, Unset):
            add_note = []
            for add_note_item_data in self.add_note:
                add_note_item = add_note_item_data.to_dict()
                add_note.append(add_note_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_parent is not UNSET:
            field_dict["_parent"] = field_parent
        if ignore is not UNSET:
            field_dict["ignore"] = ignore
        if create is not UNSET:
            field_dict["create"] = create
        if close is not UNSET:
            field_dict["close"] = close
        if acknowledge is not UNSET:
            field_dict["acknowledge"] = acknowledge
        if add_note is not UNSET:
            field_dict["addNote"] = add_note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_integration_action import BaseIntegrationAction
        from ..models.common_integration_action import CommonIntegrationAction
        from ..models.create_integration_action import CreateIntegrationAction
        from ..models.integration_meta import IntegrationMeta

        d = src_dict.copy()
        _field_parent = d.pop("_parent", UNSET)
        field_parent: Union[Unset, IntegrationMeta]
        if isinstance(_field_parent, Unset):
            field_parent = UNSET
        else:
            field_parent = IntegrationMeta.from_dict(_field_parent)

        ignore = []
        _ignore = d.pop("ignore", UNSET)
        for ignore_item_data in _ignore or []:
            ignore_item = BaseIntegrationAction.from_dict(ignore_item_data)

            ignore.append(ignore_item)

        create = []
        _create = d.pop("create", UNSET)
        for create_item_data in _create or []:
            create_item = CreateIntegrationAction.from_dict(create_item_data)

            create.append(create_item)

        close = []
        _close = d.pop("close", UNSET)
        for close_item_data in _close or []:
            close_item = CommonIntegrationAction.from_dict(close_item_data)

            close.append(close_item)

        acknowledge = []
        _acknowledge = d.pop("acknowledge", UNSET)
        for acknowledge_item_data in _acknowledge or []:
            acknowledge_item = CommonIntegrationAction.from_dict(acknowledge_item_data)

            acknowledge.append(acknowledge_item)

        add_note = []
        _add_note = d.pop("addNote", UNSET)
        for add_note_item_data in _add_note or []:
            add_note_item = CommonIntegrationAction.from_dict(add_note_item_data)

            add_note.append(add_note_item)

        action_categorized = cls(
            field_parent=field_parent,
            ignore=ignore,
            create=create,
            close=close,
            acknowledge=acknowledge,
            add_note=add_note,
        )

        action_categorized.additional_properties = d
        return action_categorized

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
