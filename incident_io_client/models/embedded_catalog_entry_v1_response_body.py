from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddedCatalogEntryV1ResponseBody")


@_attrs_define
class EmbeddedCatalogEntryV1ResponseBody:
    """
    Example:
        {'aliases': ['lawrence@incident.io', 'lawrence'], 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call'}

    Attributes:
        id (str): ID of this catalog entry Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this entry Example: Primary On-call.
        aliases (Union[Unset, List[str]]): Optional aliases that can be used to reference this entry Example:
            ['lawrence@incident.io', 'lawrence'].
        external_id (Union[Unset, str]): An optional alternative ID for this entry, which is ensured to be unique for
            the type Example: 761722cd-d1d7-477b-ac7e-90f9e079dc33.
    """

    id: str
    name: str
    aliases: Union[Unset, List[str]] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        aliases: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        external_id = self.external_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        aliases = cast(List[str], d.pop("aliases", UNSET))

        external_id = d.pop("external_id", UNSET)

        embedded_catalog_entry_v1_response_body = cls(
            id=id,
            name=name,
            aliases=aliases,
            external_id=external_id,
        )

        embedded_catalog_entry_v1_response_body.additional_properties = d
        return embedded_catalog_entry_v1_response_body

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
