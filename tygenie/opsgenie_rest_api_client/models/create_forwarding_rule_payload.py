import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_meta import UserMeta


T = TypeVar("T", bound="CreateForwardingRulePayload")


@_attrs_define
class CreateForwardingRulePayload:
    """
    Attributes:
        from_user (UserMeta):
        to_user (UserMeta):
        start_date (datetime.datetime): The date and time for forwarding will start
        end_date (datetime.datetime): The date and time for forwarding will end
        alias (Union[Unset, str]): A user defined identifier for the forwarding rule.
    """

    from_user: "UserMeta"
    to_user: "UserMeta"
    start_date: datetime.datetime
    end_date: datetime.datetime
    alias: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_user = self.from_user.to_dict()

        to_user = self.to_user.to_dict()

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        alias = self.alias

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromUser": from_user,
                "toUser": to_user,
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_meta import UserMeta

        d = src_dict.copy()
        from_user = UserMeta.from_dict(d.pop("fromUser"))

        to_user = UserMeta.from_dict(d.pop("toUser"))

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        alias = d.pop("alias", UNSET)

        create_forwarding_rule_payload = cls(
            from_user=from_user,
            to_user=to_user,
            start_date=start_date,
            end_date=end_date,
            alias=alias,
        )

        create_forwarding_rule_payload.additional_properties = d
        return create_forwarding_rule_payload

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
