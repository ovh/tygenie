import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_meta import ScheduleMeta
    from ..models.timeline import Timeline


T = TypeVar("T", bound="ScheduleTimeline")


@_attrs_define
class ScheduleTimeline:
    """
    Attributes:
        field_parent (Union[Unset, ScheduleMeta]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        final_timeline (Union[Unset, Timeline]):
        base_timeline (Union[Unset, Timeline]):
        override_timeline (Union[Unset, Timeline]):
        forwarding_timeline (Union[Unset, Timeline]):
    """

    field_parent: Union[Unset, "ScheduleMeta"] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    final_timeline: Union[Unset, "Timeline"] = UNSET
    base_timeline: Union[Unset, "Timeline"] = UNSET
    override_timeline: Union[Unset, "Timeline"] = UNSET
    forwarding_timeline: Union[Unset, "Timeline"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_parent, Unset):
            field_parent = self.field_parent.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        final_timeline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.final_timeline, Unset):
            final_timeline = self.final_timeline.to_dict()

        base_timeline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_timeline, Unset):
            base_timeline = self.base_timeline.to_dict()

        override_timeline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.override_timeline, Unset):
            override_timeline = self.override_timeline.to_dict()

        forwarding_timeline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forwarding_timeline, Unset):
            forwarding_timeline = self.forwarding_timeline.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_parent is not UNSET:
            field_dict["_parent"] = field_parent
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if final_timeline is not UNSET:
            field_dict["finalTimeline"] = final_timeline
        if base_timeline is not UNSET:
            field_dict["baseTimeline"] = base_timeline
        if override_timeline is not UNSET:
            field_dict["overrideTimeline"] = override_timeline
        if forwarding_timeline is not UNSET:
            field_dict["forwardingTimeline"] = forwarding_timeline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule_meta import ScheduleMeta
        from ..models.timeline import Timeline

        d = src_dict.copy()
        _field_parent = d.pop("_parent", UNSET)
        field_parent: Union[Unset, ScheduleMeta]
        if isinstance(_field_parent, Unset):
            field_parent = UNSET
        else:
            field_parent = ScheduleMeta.from_dict(_field_parent)

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

        _final_timeline = d.pop("finalTimeline", UNSET)
        final_timeline: Union[Unset, Timeline]
        if isinstance(_final_timeline, Unset):
            final_timeline = UNSET
        else:
            final_timeline = Timeline.from_dict(_final_timeline)

        _base_timeline = d.pop("baseTimeline", UNSET)
        base_timeline: Union[Unset, Timeline]
        if isinstance(_base_timeline, Unset):
            base_timeline = UNSET
        else:
            base_timeline = Timeline.from_dict(_base_timeline)

        _override_timeline = d.pop("overrideTimeline", UNSET)
        override_timeline: Union[Unset, Timeline]
        if isinstance(_override_timeline, Unset):
            override_timeline = UNSET
        else:
            override_timeline = Timeline.from_dict(_override_timeline)

        _forwarding_timeline = d.pop("forwardingTimeline", UNSET)
        forwarding_timeline: Union[Unset, Timeline]
        if isinstance(_forwarding_timeline, Unset):
            forwarding_timeline = UNSET
        else:
            forwarding_timeline = Timeline.from_dict(_forwarding_timeline)

        schedule_timeline = cls(
            field_parent=field_parent,
            start_date=start_date,
            end_date=end_date,
            final_timeline=final_timeline,
            base_timeline=base_timeline,
            override_timeline=override_timeline,
            forwarding_timeline=forwarding_timeline,
        )

        schedule_timeline.additional_properties = d
        return schedule_timeline

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
