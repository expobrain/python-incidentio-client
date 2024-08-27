from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_type_attribute_v2_mode import CatalogTypeAttributeV2Mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_type_attribute_path_item_v2 import (
        CatalogTypeAttributePathItemV2,
    )


T = TypeVar("T", bound="CatalogTypeAttributeV2")


@_attrs_define
class CatalogTypeAttributeV2:
    """
    Example:
        {'array': False, 'backlink_attribute': 'abc123', 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name':
            'tier', 'path': [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}], 'type': 'Custom["Service"]'}

    Attributes:
        array (bool): Whether this attribute is an array
        id (str): The ID of this attribute Example: 01GW2G3V0S59R238FAHPDS1R66.
        mode (CatalogTypeAttributeV2Mode): Controls how this attribute is modified Example: manual.
        name (str): Unique name of this attribute Example: tier.
        type (str): Catalog type name for this attribute Example: Custom["Service"].
        backlink_attribute (Union[Unset, str]): The attribute to use (if this is a backlink) Example: abc123.
        path (Union[Unset, List['CatalogTypeAttributePathItemV2']]): The path to use (if this is a path attribute)
            Example: [{'attribute_id': 'abc123', 'attribute_name': 'abc123'}].
    """

    array: bool
    id: str
    mode: CatalogTypeAttributeV2Mode
    name: str
    type: str
    backlink_attribute: Union[Unset, str] = UNSET
    path: Union[Unset, List["CatalogTypeAttributePathItemV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array

        id = self.id

        mode = self.mode.value

        name = self.name

        type = self.type

        backlink_attribute = self.backlink_attribute

        path: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.path, Unset):
            path = []
            for path_item_data in self.path:
                path_item = path_item_data.to_dict()
                path.append(path_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "id": id,
                "mode": mode,
                "name": name,
                "type": type,
            }
        )
        if backlink_attribute is not UNSET:
            field_dict["backlink_attribute"] = backlink_attribute
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_type_attribute_path_item_v2 import (
            CatalogTypeAttributePathItemV2,
        )

        d = src_dict.copy()
        array = d.pop("array")

        id = d.pop("id")

        mode = CatalogTypeAttributeV2Mode(d.pop("mode"))

        name = d.pop("name")

        type = d.pop("type")

        backlink_attribute = d.pop("backlink_attribute", UNSET)

        path = []
        _path = d.pop("path", UNSET)
        for path_item_data in _path or []:
            path_item = CatalogTypeAttributePathItemV2.from_dict(path_item_data)

            path.append(path_item)

        catalog_type_attribute_v2 = cls(
            array=array,
            id=id,
            mode=mode,
            name=name,
            type=type,
            backlink_attribute=backlink_attribute,
            path=path,
        )

        catalog_type_attribute_v2.additional_properties = d
        return catalog_type_attribute_v2

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
