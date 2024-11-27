from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_entry import StatusPageEntry


T = TypeVar("T", bound="CreateIncidentPayloadStatusPageEntry")


@_attrs_define
class CreateIncidentPayloadStatusPageEntry:
    """Status page entry fields. If this field is leaved blank, message and description of incident will be used for title
    and detail respectively.

    """

    additional_properties: Dict[str, "StatusPageEntry"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.status_page_entry import StatusPageEntry

        d = src_dict.copy()
        create_incident_payload_status_page_entry = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StatusPageEntry.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        create_incident_payload_status_page_entry.additional_properties = additional_properties
        return create_incident_payload_status_page_entry

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "StatusPageEntry":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "StatusPageEntry") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
