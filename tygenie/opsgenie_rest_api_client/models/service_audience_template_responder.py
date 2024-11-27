from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAudienceTemplateResponder")


@_attrs_define
class ServiceAudienceTemplateResponder:
    """
    Attributes:
        teams (Union[Unset, List[str]]):
        individuals (Union[Unset, List[str]]):
    """

    teams: Union[Unset, List[str]] = UNSET
    individuals: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        teams: Union[Unset, List[str]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams

        individuals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.individuals, Unset):
            individuals = self.individuals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if teams is not UNSET:
            field_dict["teams"] = teams
        if individuals is not UNSET:
            field_dict["individuals"] = individuals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        teams = cast(List[str], d.pop("teams", UNSET))

        individuals = cast(List[str], d.pop("individuals", UNSET))

        service_audience_template_responder = cls(
            teams=teams,
            individuals=individuals,
        )

        service_audience_template_responder.additional_properties = d
        return service_audience_template_responder

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
