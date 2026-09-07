from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageV2")


@_attrs_define
class StatusPageV2:
    """
    Example:
        {'description': 'This status page is our public status page.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Our
            public status page', 'public_url': 'https://statuspage.incident.io/our-public-status-page'}

    Attributes:
        id (str): Unique ID of this status page Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): The title of this status page Example: Our public status page.
        description (Union[Unset, str]): The description of this status page Example: This status page is our public
            status page..
        public_url (Union[Unset, str]): The public URL of this status page Example: https://statuspage.incident.io/our-
            public-status-page.
    """

    id: str
    name: str
    description: Union[Unset, str] = UNSET
    public_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        public_url = self.public_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if public_url is not UNSET:
            field_dict["public_url"] = public_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        public_url = d.pop("public_url", UNSET)

        status_page_v2 = cls(
            id=id,
            name=name,
            description=description,
            public_url=public_url,
        )

        status_page_v2.additional_properties = d
        return status_page_v2

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
