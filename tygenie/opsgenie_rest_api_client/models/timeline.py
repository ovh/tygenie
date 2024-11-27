from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeline_rotation import TimelineRotation


T = TypeVar("T", bound="Timeline")


@_attrs_define
class Timeline:
    """
    Attributes:
        rotations (Union[Unset, List['TimelineRotation']]):
    """

    rotations: Union[Unset, List["TimelineRotation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rotations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rotations, Unset):
            rotations = []
            for rotations_item_data in self.rotations:
                rotations_item = rotations_item_data.to_dict()
                rotations.append(rotations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rotations is not UNSET:
            field_dict["rotations"] = rotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.timeline_rotation import TimelineRotation

        d = src_dict.copy()
        rotations = []
        _rotations = d.pop("rotations", UNSET)
        for rotations_item_data in _rotations or []:
            rotations_item = TimelineRotation.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        timeline = cls(
            rotations=rotations,
        )

        timeline.additional_properties = d
        return timeline

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
