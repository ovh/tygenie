import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_meta import UserMeta


T = TypeVar("T", bound="ForwardingRule")


@_attrs_define
class ForwardingRule:
    """
    Attributes:
        from_user (Union[Unset, UserMeta]):
        to_user (Union[Unset, UserMeta]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        alias (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    from_user: Union[Unset, "UserMeta"] = UNSET
    to_user: Union[Unset, "UserMeta"] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    alias: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.from_user, Unset):
            from_user = self.from_user.to_dict()

        to_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.to_user, Unset):
            to_user = self.to_user.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        alias = self.alias

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_user is not UNSET:
            field_dict["fromUser"] = from_user
        if to_user is not UNSET:
            field_dict["toUser"] = to_user
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if alias is not UNSET:
            field_dict["alias"] = alias
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_meta import UserMeta

        d = src_dict.copy()
        _from_user = d.pop("fromUser", UNSET)
        from_user: Union[Unset, UserMeta]
        if isinstance(_from_user, Unset):
            from_user = UNSET
        else:
            from_user = UserMeta.from_dict(_from_user)

        _to_user = d.pop("toUser", UNSET)
        to_user: Union[Unset, UserMeta]
        if isinstance(_to_user, Unset):
            to_user = UNSET
        else:
            to_user = UserMeta.from_dict(_to_user)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        alias = d.pop("alias", UNSET)

        id = d.pop("id", UNSET)

        forwarding_rule = cls(
            from_user=from_user,
            to_user=to_user,
            start_date=start_date,
            end_date=end_date,
            alias=alias,
            id=id,
        )

        forwarding_rule.additional_properties = d
        return forwarding_rule

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
