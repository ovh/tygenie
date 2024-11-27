from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="AddAttachmentBody")


@_attrs_define
class AddAttachmentBody:
    """
    Attributes:
        file (File): Attachment file to be uploaded
        user (Union[Unset, str]): Display name of the request owner
        index_file (Union[Unset, str]): Name of html file which will be shown when attachment clicked on UI
    """

    file: File
    user: Union[Unset, str] = UNSET
    index_file: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        user = self.user

        index_file = self.index_file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if index_file is not UNSET:
            field_dict["indexFile"] = index_file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")

        index_file = (
            self.index_file
            if isinstance(self.index_file, Unset)
            else (None, str(self.index_file).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "file": file,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if index_file is not UNSET:
            field_dict["indexFile"] = index_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        user = d.pop("user", UNSET)

        index_file = d.pop("indexFile", UNSET)

        add_attachment_body = cls(
            file=file,
            user=user,
            index_file=index_file,
        )

        add_attachment_body.additional_properties = d
        return add_attachment_body

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
