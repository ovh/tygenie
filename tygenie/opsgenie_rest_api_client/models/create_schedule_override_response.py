from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_override_meta import ScheduleOverrideMeta


T = TypeVar("T", bound="CreateScheduleOverrideResponse")


@_attrs_define
class CreateScheduleOverrideResponse:
    """
    Attributes:
        request_id (str):
        took (float):  Default: 0.0.
        data (Union[Unset, ScheduleOverrideMeta]):
    """

    request_id: str
    took: float = 0.0
    data: Union[Unset, "ScheduleOverrideMeta"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        took = self.took

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
                "took": took,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_override_meta import ScheduleOverrideMeta

        d = src_dict.copy()
        request_id = d.pop("requestId")

        took = d.pop("took")

        _data = d.pop("data", UNSET)
        data: Union[Unset, ScheduleOverrideMeta]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ScheduleOverrideMeta.from_dict(_data)

        create_schedule_override_response = cls(
            request_id=request_id,
            took=took,
            data=data,
        )

        create_schedule_override_response.additional_properties = d
        return create_schedule_override_response

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
