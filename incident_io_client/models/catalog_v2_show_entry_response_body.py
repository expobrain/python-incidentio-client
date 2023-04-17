from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.catalog_entry_v2_response_body import CatalogEntryV2ResponseBody
    from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody


T = TypeVar("T", bound="CatalogV2ShowEntryResponseBody")


@attr.s(auto_attribs=True)
class CatalogV2ShowEntryResponseBody:
    """
    Example:
        {'catalog_entry': {'attribute_values': {'abc123': {'array_value': [{'catalog_entry': {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url':
            'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon':
            False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}], 'value': {'catalog_entry':
            {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'},
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}}},
            'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'catalog_type': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes clusters
            that we run inside of GKE.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Kubernetes Cluster', 'schema':
            {'attributes': [{'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}],
            'version': 1}, 'semantic_type': 'service', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        catalog_entry (CatalogEntryV2ResponseBody):  Example: {'attribute_values': {'abc123': {'array_value':
            [{'catalog_entry': {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}], 'value': {'catalog_entry': {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url':
            'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon':
            False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}}}, 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Primary On-call', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
        catalog_type (CatalogTypeV2ResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Kubernetes Cluster', 'schema': {'attributes': [{'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name':
            'tier', 'type': 'tier'}], 'version': 1}, 'semantic_type': 'service', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    catalog_entry: "CatalogEntryV2ResponseBody"
    catalog_type: "CatalogTypeV2ResponseBody"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_entry = self.catalog_entry.to_dict()

        catalog_type = self.catalog_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entry": catalog_entry,
                "catalog_type": catalog_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_entry_v2_response_body import CatalogEntryV2ResponseBody
        from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody

        d = src_dict.copy()
        catalog_entry = CatalogEntryV2ResponseBody.from_dict(d.pop("catalog_entry"))

        catalog_type = CatalogTypeV2ResponseBody.from_dict(d.pop("catalog_type"))

        catalog_v2_show_entry_response_body = cls(
            catalog_entry=catalog_entry,
            catalog_type=catalog_type,
        )

        catalog_v2_show_entry_response_body.additional_properties = d
        return catalog_v2_show_entry_response_body

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
