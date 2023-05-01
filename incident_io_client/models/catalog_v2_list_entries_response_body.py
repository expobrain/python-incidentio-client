from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.catalog_entry_v2_response_body import CatalogEntryV2ResponseBody
    from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody
    from ..models.pagination_meta_result_response_body import (
        PaginationMetaResultResponseBody,
    )


T = TypeVar("T", bound="CatalogV2ListEntriesResponseBody")


@attr.s(auto_attribs=True)
class CatalogV2ListEntriesResponseBody:
    """
    Example:
        {'catalog_entries': [{'aliases': ['lawrence@incident.io', 'lawrence'], 'attribute_values': {'abc123':
            {'array_value': [{'catalog_entry': {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name':
            'Primary escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}], 'value': {'catalog_entry': {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'created_at': '2021-08-17T13:28:57.801578Z', 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank': 3, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}], 'catalog_type': {'annotations': {'incident.io/catalog-importer/id': 'id-of-
            config'}, 'color': 'slate', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes
            clusters that we run inside of GKE.', 'estimated_count': 7, 'external_type': 'PagerDutyService', 'icon': 'bolt',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'name': 'Kubernetes Cluster', 'ranked': True,
            'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]'}], 'version':
            1}, 'semantic_type': 'custom', 'type_name': 'CatalogEntry["01FCNDV6P870EA6S7TK1DSYDG2"]', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, 'pagination_meta': {'after': '01FCNDV6P870EA6S7TK1DSYDG0', 'page_size': 25}}

    Attributes:
        catalog_entries (List['CatalogEntryV2ResponseBody']):  Example: [{'aliases': ['lawrence@incident.io',
            'lawrence'], 'attribute_values': {'abc123': {'array_value': [{'catalog_entry': {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}], 'value': {'catalog_entry': {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}}}, 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'created_at': '2021-08-17T13:28:57.801578Z', 'external_id': '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank': 3, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
        catalog_type (CatalogTypeV2ResponseBody):  Example: {'annotations': {'incident.io/catalog-importer/id': 'id-of-
            config'}, 'color': 'slate', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes
            clusters that we run inside of GKE.', 'estimated_count': 7, 'external_type': 'PagerDutyService', 'icon': 'bolt',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'name': 'Kubernetes Cluster', 'ranked': True,
            'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]'}], 'version':
            1}, 'semantic_type': 'custom', 'type_name': 'CatalogEntry["01FCNDV6P870EA6S7TK1DSYDG2"]', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        pagination_meta (PaginationMetaResultResponseBody):  Example: {'after': '01FCNDV6P870EA6S7TK1DSYDG0',
            'page_size': 25}.
    """

    catalog_entries: List["CatalogEntryV2ResponseBody"]
    catalog_type: "CatalogTypeV2ResponseBody"
    pagination_meta: "PaginationMetaResultResponseBody"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_entries = []
        for catalog_entries_item_data in self.catalog_entries:
            catalog_entries_item = catalog_entries_item_data.to_dict()

            catalog_entries.append(catalog_entries_item)

        catalog_type = self.catalog_type.to_dict()

        pagination_meta = self.pagination_meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entries": catalog_entries,
                "catalog_type": catalog_type,
                "pagination_meta": pagination_meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_entry_v2_response_body import CatalogEntryV2ResponseBody
        from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody
        from ..models.pagination_meta_result_response_body import (
            PaginationMetaResultResponseBody,
        )

        d = src_dict.copy()
        catalog_entries = []
        _catalog_entries = d.pop("catalog_entries")
        for catalog_entries_item_data in _catalog_entries:
            catalog_entries_item = CatalogEntryV2ResponseBody.from_dict(catalog_entries_item_data)

            catalog_entries.append(catalog_entries_item)

        catalog_type = CatalogTypeV2ResponseBody.from_dict(d.pop("catalog_type"))

        pagination_meta = PaginationMetaResultResponseBody.from_dict(d.pop("pagination_meta"))

        catalog_v2_list_entries_response_body = cls(
            catalog_entries=catalog_entries,
            catalog_type=catalog_type,
            pagination_meta=pagination_meta,
        )

        catalog_v2_list_entries_response_body.additional_properties = d
        return catalog_v2_list_entries_response_body

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