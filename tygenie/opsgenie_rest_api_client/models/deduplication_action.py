from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deduplication_action_deduplication_action_type import DeduplicationActionDeduplicationActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="DeduplicationAction")


@_attrs_define
class DeduplicationAction:
    """
    Attributes:
        deduplication_action_type (DeduplicationActionDeduplicationActionType):
        count (int):
        duration (Union[Unset, Duration]):
    """

    deduplication_action_type: DeduplicationActionDeduplicationActionType
    count: int
    duration: Union[Unset, "Duration"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deduplication_action_type = self.deduplication_action_type.value

        count = self.count

        duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deduplicationActionType": deduplication_action_type,
                "count": count,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        deduplication_action_type = DeduplicationActionDeduplicationActionType(d.pop("deduplicationActionType"))

        count = d.pop("count")

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, Duration]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = Duration.from_dict(_duration)

        deduplication_action = cls(
            deduplication_action_type=deduplication_action_type,
            count=count,
            duration=duration,
        )

        deduplication_action.additional_properties = d
        return deduplication_action

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
