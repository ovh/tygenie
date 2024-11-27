from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_service_payload_visibility import UpdateServicePayloadVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateServicePayload")


@_attrs_define
class UpdateServicePayload:
    """
    Attributes:
        name (str): Name of the service
        description (Union[Unset, str]): Description field of the service that is generally used to provide a detailed
            information about the service.
        visibility (Union[Unset, UpdateServicePayloadVisibility]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    visibility: Union[Unset, UpdateServicePayloadVisibility] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, UpdateServicePayloadVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = UpdateServicePayloadVisibility(_visibility)

        update_service_payload = cls(
            name=name,
            description=description,
            visibility=visibility,
        )

        update_service_payload.additional_properties = d
        return update_service_payload

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
