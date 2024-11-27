from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_visibility import ServiceVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="Service")


@_attrs_define
class Service:
    """
    Attributes:
        name (str): Name of the service
        id (Union[Unset, str]): Id of the service
        team_id (Union[Unset, str]): Team id of the service.
        description (Union[Unset, str]): Description field of the service that is generally used to provide a detailed
            information about the service.
        visibility (Union[Unset, ServiceVisibility]):
        tags (Union[Unset, List[str]]):
    """

    name: str
    id: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    visibility: Union[Unset, ServiceVisibility] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        id = self.id

        team_id = self.team_id

        description = self.description

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        team_id = d.pop("teamId", UNSET)

        description = d.pop("description", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, ServiceVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ServiceVisibility(_visibility)

        tags = cast(List[str], d.pop("tags", UNSET))

        service = cls(
            name=name,
            id=id,
            team_id=team_id,
            description=description,
            visibility=visibility,
            tags=tags,
        )

        service.additional_properties = d
        return service

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
