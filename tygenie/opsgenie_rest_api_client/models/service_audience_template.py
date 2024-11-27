from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_audience_template_responder import ServiceAudienceTemplateResponder
    from ..models.service_audience_template_stakeholder import ServiceAudienceTemplateStakeholder


T = TypeVar("T", bound="ServiceAudienceTemplate")


@_attrs_define
class ServiceAudienceTemplate:
    """
    Attributes:
        responder (Union[Unset, ServiceAudienceTemplateResponder]):
        stakeholder (Union[Unset, ServiceAudienceTemplateStakeholder]):
    """

    responder: Union[Unset, "ServiceAudienceTemplateResponder"] = UNSET
    stakeholder: Union[Unset, "ServiceAudienceTemplateStakeholder"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        responder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.responder, Unset):
            responder = self.responder.to_dict()

        stakeholder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stakeholder, Unset):
            stakeholder = self.stakeholder.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responder is not UNSET:
            field_dict["responder"] = responder
        if stakeholder is not UNSET:
            field_dict["stakeholder"] = stakeholder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_audience_template_responder import ServiceAudienceTemplateResponder
        from ..models.service_audience_template_stakeholder import ServiceAudienceTemplateStakeholder

        d = src_dict.copy()
        _responder = d.pop("responder", UNSET)
        responder: Union[Unset, ServiceAudienceTemplateResponder]
        if isinstance(_responder, Unset):
            responder = UNSET
        else:
            responder = ServiceAudienceTemplateResponder.from_dict(_responder)

        _stakeholder = d.pop("stakeholder", UNSET)
        stakeholder: Union[Unset, ServiceAudienceTemplateStakeholder]
        if isinstance(_stakeholder, Unset):
            stakeholder = UNSET
        else:
            stakeholder = ServiceAudienceTemplateStakeholder.from_dict(_stakeholder)

        service_audience_template = cls(
            responder=responder,
            stakeholder=stakeholder,
        )

        service_audience_template.additional_properties = d
        return service_audience_template

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
