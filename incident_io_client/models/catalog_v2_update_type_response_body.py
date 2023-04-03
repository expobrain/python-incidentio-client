from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody


T = TypeVar("T", bound="CatalogV2UpdateTypeResponseBody")


@attr.s(auto_attribs=True)
class CatalogV2UpdateTypeResponseBody:
    """
    Example:
        {'catalog_type': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes clusters
            that we run inside of GKE.', 'estimated_count': 7, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Kubernetes
            Cluster', 'ranked': True, 'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False,
            'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]'}],
            'version': 1}, 'semantic_type': 'custom', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        catalog_type (CatalogTypeV2ResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'estimated_count': 7, 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Kubernetes Cluster', 'ranked': True, 'required_integrations':
            ['pager_duty'], 'schema': {'attributes': [{'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier',
            'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]'}], 'version': 1}, 'semantic_type': 'custom', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    catalog_type: "CatalogTypeV2ResponseBody"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_type = self.catalog_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_type": catalog_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody

        d = src_dict.copy()
        catalog_type = CatalogTypeV2ResponseBody.from_dict(d.pop("catalog_type"))

        catalog_v2_update_type_response_body = cls(
            catalog_type=catalog_type,
        )

        catalog_v2_update_type_response_body.additional_properties = d
        return catalog_v2_update_type_response_body

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
