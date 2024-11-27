from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_incident_properties_priority import ServiceIncidentPropertiesPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_incident_properties_details import ServiceIncidentPropertiesDetails
    from ..models.service_incident_stakeholder_properties import ServiceIncidentStakeholderProperties


T = TypeVar("T", bound="ServiceIncidentProperties")


@_attrs_define
class ServiceIncidentProperties:
    """
    Attributes:
        message (str): Message of the related incident rule.
        priority (ServiceIncidentPropertiesPriority): Priority level of the alert. Possible values are P1, P2, P3, P4
            and P5
        stakeholder_properties (ServiceIncidentStakeholderProperties):
        tags (Union[Unset, List[str]]): Tags of the alert.
        details (Union[Unset, ServiceIncidentPropertiesDetails]): Map of key-value pairs to use as custom properties of
            the alert.
        description (Union[Unset, str]): Description field of the incident rule.
    """

    message: str
    priority: ServiceIncidentPropertiesPriority
    stakeholder_properties: "ServiceIncidentStakeholderProperties"
    tags: Union[Unset, List[str]] = UNSET
    details: Union[Unset, "ServiceIncidentPropertiesDetails"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        priority = self.priority.value

        stakeholder_properties = self.stakeholder_properties.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "priority": priority,
                "stakeholderProperties": stakeholder_properties,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if details is not UNSET:
            field_dict["details"] = details
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_incident_properties_details import ServiceIncidentPropertiesDetails
        from ..models.service_incident_stakeholder_properties import ServiceIncidentStakeholderProperties

        d = src_dict.copy()
        message = d.pop("message")

        priority = ServiceIncidentPropertiesPriority(d.pop("priority"))

        stakeholder_properties = ServiceIncidentStakeholderProperties.from_dict(d.pop("stakeholderProperties"))

        tags = cast(List[str], d.pop("tags", UNSET))

        _details = d.pop("details", UNSET)
        details: Union[Unset, ServiceIncidentPropertiesDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ServiceIncidentPropertiesDetails.from_dict(_details)

        description = d.pop("description", UNSET)

        service_incident_properties = cls(
            message=message,
            priority=priority,
            stakeholder_properties=stakeholder_properties,
            tags=tags,
            details=details,
            description=description,
        )

        service_incident_properties.additional_properties = d
        return service_incident_properties

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
