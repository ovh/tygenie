from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceIncidentStakeholderProperties")


@_attrs_define
class ServiceIncidentStakeholderProperties:
    """
    Attributes:
        message (str): Message that is to be passed to audience that is generally used to provide a content information
            about the alert.
        enable (Union[Unset, bool]): Option to enable stakeholder notifications.Default value is true.
        description (Union[Unset, str]): Description that is generally used to provide a detailed information about the
            alert.
    """

    message: str
    enable: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        enable = self.enable

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if enable is not UNSET:
            field_dict["enable"] = enable
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        enable = d.pop("enable", UNSET)

        description = d.pop("description", UNSET)

        service_incident_stakeholder_properties = cls(
            message=message,
            enable=enable,
            description=description,
        )

        service_incident_stakeholder_properties.additional_properties = d
        return service_incident_stakeholder_properties

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
