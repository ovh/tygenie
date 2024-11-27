from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_incident_rule_condition_match_type import ServiceIncidentRuleConditionMatchType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_incident_condition import ServiceIncidentCondition
    from ..models.service_incident_properties import ServiceIncidentProperties


T = TypeVar("T", bound="ServiceIncidentRule")


@_attrs_define
class ServiceIncidentRule:
    """
    Attributes:
        id (str): Id of the incident rule.
        condition_match_type (Union[Unset, ServiceIncidentRuleConditionMatchType]):  Default:
            ServiceIncidentRuleConditionMatchType.MATCH_ALL.
        conditions (Union[Unset, List['ServiceIncidentCondition']]):
        incident_properties (Union[Unset, ServiceIncidentProperties]):
        order (Union[Unset, int]): Order for the rule.
    """

    id: str
    condition_match_type: Union[Unset, ServiceIncidentRuleConditionMatchType] = (
        ServiceIncidentRuleConditionMatchType.MATCH_ALL
    )
    conditions: Union[Unset, List["ServiceIncidentCondition"]] = UNSET
    incident_properties: Union[Unset, "ServiceIncidentProperties"] = UNSET
    order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        condition_match_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_match_type, Unset):
            condition_match_type = self.condition_match_type.value

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        incident_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incident_properties, Unset):
            incident_properties = self.incident_properties.to_dict()

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if condition_match_type is not UNSET:
            field_dict["conditionMatchType"] = condition_match_type
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if incident_properties is not UNSET:
            field_dict["incidentProperties"] = incident_properties
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_incident_condition import ServiceIncidentCondition
        from ..models.service_incident_properties import ServiceIncidentProperties

        d = src_dict.copy()
        id = d.pop("id")

        _condition_match_type = d.pop("conditionMatchType", UNSET)
        condition_match_type: Union[Unset, ServiceIncidentRuleConditionMatchType]
        if isinstance(_condition_match_type, Unset):
            condition_match_type = UNSET
        else:
            condition_match_type = ServiceIncidentRuleConditionMatchType(_condition_match_type)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ServiceIncidentCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        _incident_properties = d.pop("incidentProperties", UNSET)
        incident_properties: Union[Unset, ServiceIncidentProperties]
        if isinstance(_incident_properties, Unset):
            incident_properties = UNSET
        else:
            incident_properties = ServiceIncidentProperties.from_dict(_incident_properties)

        order = d.pop("order", UNSET)

        service_incident_rule = cls(
            id=id,
            condition_match_type=condition_match_type,
            conditions=conditions,
            incident_properties=incident_properties,
            order=order,
        )

        service_incident_rule.additional_properties = d
        return service_incident_rule

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
