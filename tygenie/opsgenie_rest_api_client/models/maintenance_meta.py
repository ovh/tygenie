from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.maintenance_meta_status import MaintenanceMetaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_time import MaintenanceTime


T = TypeVar("T", bound="MaintenanceMeta")


@_attrs_define
class MaintenanceMeta:
    """
    Attributes:
        id (Union[Unset, str]): Identifier of the maintenance meta data
        status (Union[Unset, MaintenanceMetaStatus]): Status of the maintenance meta data
        time (Union[Unset, MaintenanceTime]):
        description (Union[Unset, str]): Description for maintenance meta data
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, MaintenanceMetaStatus] = UNSET
    time: Union[Unset, "MaintenanceTime"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if time is not UNSET:
            field_dict["time"] = time
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.maintenance_time import MaintenanceTime

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MaintenanceMetaStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MaintenanceMetaStatus(_status)

        _time = d.pop("time", UNSET)
        time: Union[Unset, MaintenanceTime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = MaintenanceTime.from_dict(_time)

        description = d.pop("description", UNSET)

        maintenance_meta = cls(
            id=id,
            status=status,
            time=time,
            description=description,
        )

        maintenance_meta.additional_properties = d
        return maintenance_meta

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
