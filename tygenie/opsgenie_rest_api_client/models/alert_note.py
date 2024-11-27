import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertNote")


@_attrs_define
class AlertNote:
    """
    Attributes:
        note (Union[Unset, str]):
        owner (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        offset (Union[Unset, str]):
    """

    note: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    offset: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note = self.note

        owner = self.owner

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if owner is not UNSET:
            field_dict["owner"] = owner
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        note = d.pop("note", UNSET)

        owner = d.pop("owner", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        offset = d.pop("offset", UNSET)

        alert_note = cls(
            note=note,
            owner=owner,
            created_at=created_at,
            offset=offset,
        )

        alert_note.additional_properties = d
        return alert_note

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