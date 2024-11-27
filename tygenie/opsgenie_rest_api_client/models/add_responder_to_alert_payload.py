from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipient import Recipient


T = TypeVar("T", bound="AddResponderToAlertPayload")


@_attrs_define
class AddResponderToAlertPayload:
    """
    Attributes:
        responder (Recipient):
        user (Union[Unset, str]): Display name of the request owner
        note (Union[Unset, str]): Additional note that will be added while creating the alert
        source (Union[Unset, str]): Source field of the alert. Default value is IP address of the incoming request
    """

    responder: "Recipient"
    user: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        responder = self.responder.to_dict()

        user = self.user

        note = self.note

        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "responder": responder,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if note is not UNSET:
            field_dict["note"] = note
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recipient import Recipient

        d = src_dict.copy()
        responder = Recipient.from_dict(d.pop("responder"))

        user = d.pop("user", UNSET)

        note = d.pop("note", UNSET)

        source = d.pop("source", UNSET)

        add_responder_to_alert_payload = cls(
            responder=responder,
            user=user,
            note=note,
            source=source,
        )

        add_responder_to_alert_payload.additional_properties = d
        return add_responder_to_alert_payload

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