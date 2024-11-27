from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant import Participant
    from ..models.schedule_meta import ScheduleMeta


T = TypeVar("T", bound="OnCall")


@_attrs_define
class OnCall:
    """
    Attributes:
        field_parent (Union[Unset, ScheduleMeta]):
        on_call_participants (Union[Unset, List['Participant']]):
        on_call_recipients (Union[Unset, List[str]]):
    """

    field_parent: Union[Unset, "ScheduleMeta"] = UNSET
    on_call_participants: Union[Unset, List["Participant"]] = UNSET
    on_call_recipients: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_parent, Unset):
            field_parent = self.field_parent.to_dict()

        on_call_participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.on_call_participants, Unset):
            on_call_participants = []
            for on_call_participants_item_data in self.on_call_participants:
                on_call_participants_item = on_call_participants_item_data.to_dict()
                on_call_participants.append(on_call_participants_item)

        on_call_recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.on_call_recipients, Unset):
            on_call_recipients = self.on_call_recipients

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_parent is not UNSET:
            field_dict["_parent"] = field_parent
        if on_call_participants is not UNSET:
            field_dict["onCallParticipants"] = on_call_participants
        if on_call_recipients is not UNSET:
            field_dict["onCallRecipients"] = on_call_recipients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.participant import Participant
        from ..models.schedule_meta import ScheduleMeta

        d = src_dict.copy()
        _field_parent = d.pop("_parent", UNSET)
        field_parent: Union[Unset, ScheduleMeta]
        if isinstance(_field_parent, Unset):
            field_parent = UNSET
        else:
            field_parent = ScheduleMeta.from_dict(_field_parent)

        on_call_participants = []
        _on_call_participants = d.pop("onCallParticipants", UNSET)
        for on_call_participants_item_data in _on_call_participants or []:
            on_call_participants_item = Participant.from_dict(on_call_participants_item_data)

            on_call_participants.append(on_call_participants_item)

        on_call_recipients = cast(List[str], d.pop("onCallRecipients", UNSET))

        on_call = cls(
            field_parent=field_parent,
            on_call_participants=on_call_participants,
            on_call_recipients=on_call_recipients,
        )

        on_call.additional_properties = d
        return on_call

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
