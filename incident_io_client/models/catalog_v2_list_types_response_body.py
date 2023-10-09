from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody


T = TypeVar("T", bound="CatalogV2ListTypesResponseBody")


@_attrs_define
class CatalogV2ListTypesResponseBody:
    """
    Example:
        {'catalog_types': [{'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'color': 'yellow',
            'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes clusters that we run inside
            of GKE.', 'estimated_count': 7, 'external_type': 'PagerDutyService', 'icon': 'bolt', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'name': 'Kubernetes Cluster', 'ranked': True,
            'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'type': 'Custom["Service"]'}], 'version': 1},
            'semantic_type': 'custom', 'type_name': 'Custom["BackstageGroup"]', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        catalog_types (List['CatalogTypeV2ResponseBody']):  Example: [{'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'color': 'yellow', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'estimated_count': 7, 'external_type':
            'PagerDutyService', 'icon': 'bolt', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'name':
            'Kubernetes Cluster', 'ranked': True, 'required_integrations': ['pager_duty'], 'schema': {'attributes':
            [{'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'type':
            'Custom["Service"]'}], 'version': 1}, 'semantic_type': 'custom', 'type_name': 'Custom["BackstageGroup"]',
            'updated_at': '2021-08-17T13:28:57.801578Z'}].
    """

    catalog_types: List["CatalogTypeV2ResponseBody"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_types = []
        for catalog_types_item_data in self.catalog_types:
            catalog_types_item = catalog_types_item_data.to_dict()

            catalog_types.append(catalog_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_types": catalog_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody

        d = src_dict.copy()
        catalog_types = []
        _catalog_types = d.pop("catalog_types")
        for catalog_types_item_data in _catalog_types:
            catalog_types_item = CatalogTypeV2ResponseBody.from_dict(catalog_types_item_data)

            catalog_types.append(catalog_types_item)

        catalog_v2_list_types_response_body = cls(
            catalog_types=catalog_types,
        )

        catalog_v2_list_types_response_body.additional_properties = d
        return catalog_v2_list_types_response_body

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
