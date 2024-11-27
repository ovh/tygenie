from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_repeat import EscalationRepeat
    from ..models.escalation_rule import EscalationRule
    from ..models.team_meta import TeamMeta


T = TypeVar("T", bound="CreateEscalationPayload")


@_attrs_define
class CreateEscalationPayload:
    """
    Attributes:
        name (str): Name of the escalation
        rules (List['EscalationRule']): List of escalation rules.
        description (Union[Unset, str]): Description of the escalation
        owner_team (Union[Unset, TeamMeta]):
        repeat (Union[Unset, EscalationRepeat]):
    """

    name: str
    rules: List["EscalationRule"]
    description: Union[Unset, str] = UNSET
    owner_team: Union[Unset, "TeamMeta"] = UNSET
    repeat: Union[Unset, "EscalationRepeat"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        description = self.description

        owner_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner_team, Unset):
            owner_team = self.owner_team.to_dict()

        repeat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeat, Unset):
            repeat = self.repeat.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rules": rules,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if owner_team is not UNSET:
            field_dict["ownerTeam"] = owner_team
        if repeat is not UNSET:
            field_dict["repeat"] = repeat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_repeat import EscalationRepeat
        from ..models.escalation_rule import EscalationRule
        from ..models.team_meta import TeamMeta

        d = src_dict.copy()
        name = d.pop("name")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = EscalationRule.from_dict(rules_item_data)

            rules.append(rules_item)

        description = d.pop("description", UNSET)

        _owner_team = d.pop("ownerTeam", UNSET)
        owner_team: Union[Unset, TeamMeta]
        if isinstance(_owner_team, Unset):
            owner_team = UNSET
        else:
            owner_team = TeamMeta.from_dict(_owner_team)

        _repeat = d.pop("repeat", UNSET)
        repeat: Union[Unset, EscalationRepeat]
        if isinstance(_repeat, Unset):
            repeat = UNSET
        else:
            repeat = EscalationRepeat.from_dict(_repeat)

        create_escalation_payload = cls(
            name=name,
            rules=rules,
            description=description,
            owner_team=owner_team,
            repeat=repeat,
        )

        create_escalation_payload.additional_properties = d
        return create_escalation_payload

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
