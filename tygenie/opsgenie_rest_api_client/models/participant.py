from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Participant")


@_attrs_define
class Participant:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        on_call_participants (Union[Unset, List['Participant']]):
        forwarded_from (Union[Unset, Participant]):
        escalation_time (Union[Unset, int]): Only used by 'escalation' participants
        notify_type (Union[Unset, str]): Only used by 'escalation' participants
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    on_call_participants: Union[Unset, List["Participant"]] = UNSET
    forwarded_from: Union[Unset, "Participant"] = UNSET
    escalation_time: Union[Unset, int] = UNSET
    notify_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type = self.type

        on_call_participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.on_call_participants, Unset):
            on_call_participants = []
            for on_call_participants_item_data in self.on_call_participants:
                on_call_participants_item = on_call_participants_item_data.to_dict()
                on_call_participants.append(on_call_participants_item)

        forwarded_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forwarded_from, Unset):
            forwarded_from = self.forwarded_from.to_dict()

        escalation_time = self.escalation_time

        notify_type = self.notify_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if on_call_participants is not UNSET:
            field_dict["onCallParticipants"] = on_call_participants
        if forwarded_from is not UNSET:
            field_dict["forwardedFrom"] = forwarded_from
        if escalation_time is not UNSET:
            field_dict["escalationTime"] = escalation_time
        if notify_type is not UNSET:
            field_dict["notifyType"] = notify_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        on_call_participants = []
        _on_call_participants = d.pop("onCallParticipants", UNSET)
        for on_call_participants_item_data in _on_call_participants or []:
            on_call_participants_item = Participant.from_dict(on_call_participants_item_data)

            on_call_participants.append(on_call_participants_item)

        _forwarded_from = d.pop("forwardedFrom", UNSET)
        forwarded_from: Union[Unset, Participant]
        if isinstance(_forwarded_from, Unset):
            forwarded_from = UNSET
        else:
            forwarded_from = Participant.from_dict(_forwarded_from)

        escalation_time = d.pop("escalationTime", UNSET)

        notify_type = d.pop("notifyType", UNSET)

        participant = cls(
            id=id,
            name=name,
            type=type,
            on_call_participants=on_call_participants,
            forwarded_from=forwarded_from,
            escalation_time=escalation_time,
            notify_type=notify_type,
        )

        participant.additional_properties = d
        return participant

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
