from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant import Participant
    from ..models.schedule_meta import ScheduleMeta


T = TypeVar("T", bound="NextOnCall")


@_attrs_define
class NextOnCall:
    """
    Attributes:
        field_parent (Union[Unset, ScheduleMeta]):
        next_on_call_recipients (Union[Unset, List['Participant']]):
        exact_next_on_call_recipients (Union[Unset, List['Participant']]):
        next_on_call_participants (Union[Unset, List[str]]):
        exact_next_on_call_participants (Union[Unset, List[str]]):
    """

    field_parent: Union[Unset, "ScheduleMeta"] = UNSET
    next_on_call_recipients: Union[Unset, List["Participant"]] = UNSET
    exact_next_on_call_recipients: Union[Unset, List["Participant"]] = UNSET
    next_on_call_participants: Union[Unset, List[str]] = UNSET
    exact_next_on_call_participants: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_parent, Unset):
            field_parent = self.field_parent.to_dict()

        next_on_call_recipients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.next_on_call_recipients, Unset):
            next_on_call_recipients = []
            for next_on_call_recipients_item_data in self.next_on_call_recipients:
                next_on_call_recipients_item = next_on_call_recipients_item_data.to_dict()
                next_on_call_recipients.append(next_on_call_recipients_item)

        exact_next_on_call_recipients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exact_next_on_call_recipients, Unset):
            exact_next_on_call_recipients = []
            for exact_next_on_call_recipients_item_data in self.exact_next_on_call_recipients:
                exact_next_on_call_recipients_item = exact_next_on_call_recipients_item_data.to_dict()
                exact_next_on_call_recipients.append(exact_next_on_call_recipients_item)

        next_on_call_participants: Union[Unset, List[str]] = UNSET
        if not isinstance(self.next_on_call_participants, Unset):
            next_on_call_participants = self.next_on_call_participants

        exact_next_on_call_participants: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exact_next_on_call_participants, Unset):
            exact_next_on_call_participants = self.exact_next_on_call_participants

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_parent is not UNSET:
            field_dict["_parent"] = field_parent
        if next_on_call_recipients is not UNSET:
            field_dict["nextOnCallRecipients"] = next_on_call_recipients
        if exact_next_on_call_recipients is not UNSET:
            field_dict["exactNextOnCallRecipients"] = exact_next_on_call_recipients
        if next_on_call_participants is not UNSET:
            field_dict["nextOnCallParticipants"] = next_on_call_participants
        if exact_next_on_call_participants is not UNSET:
            field_dict["exactNextOnCallParticipants"] = exact_next_on_call_participants

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

        next_on_call_recipients = []
        _next_on_call_recipients = d.pop("nextOnCallRecipients", UNSET)
        for next_on_call_recipients_item_data in _next_on_call_recipients or []:
            next_on_call_recipients_item = Participant.from_dict(next_on_call_recipients_item_data)

            next_on_call_recipients.append(next_on_call_recipients_item)

        exact_next_on_call_recipients = []
        _exact_next_on_call_recipients = d.pop("exactNextOnCallRecipients", UNSET)
        for exact_next_on_call_recipients_item_data in _exact_next_on_call_recipients or []:
            exact_next_on_call_recipients_item = Participant.from_dict(exact_next_on_call_recipients_item_data)

            exact_next_on_call_recipients.append(exact_next_on_call_recipients_item)

        next_on_call_participants = cast(List[str], d.pop("nextOnCallParticipants", UNSET))

        exact_next_on_call_participants = cast(List[str], d.pop("exactNextOnCallParticipants", UNSET))

        next_on_call = cls(
            field_parent=field_parent,
            next_on_call_recipients=next_on_call_recipients,
            exact_next_on_call_recipients=exact_next_on_call_recipients,
            next_on_call_participants=next_on_call_participants,
            exact_next_on_call_participants=exact_next_on_call_participants,
        )

        next_on_call.additional_properties = d
        return next_on_call

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
