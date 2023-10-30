from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_entry_v2_response_body import CatalogEntryV2ResponseBody
    from ..models.catalog_type_v2_response_body import CatalogTypeV2ResponseBody


T = TypeVar("T", bound="CatalogV2UpdateEntryResponseBody")


@_attrs_define
class CatalogV2UpdateEntryResponseBody:
    """
    Example:
        {'catalog_entry': {'aliases': ['lawrence@incident.io', 'lawrence'], 'archived_at':
            '2021-08-17T14:28:57.801578Z', 'attribute_values': {'abc123': {'array_value': [{'catalog_entry': {'archived_at':
            '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary
            escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations
            like auto-closing incidents.', 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': '000020', 'unavailable':
            False, 'value': 'abc123'}], 'value': {'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z',
            'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations like auto-closing incidents.',
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': '000020', 'unavailable': False, 'value': 'abc123'}}}, 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank':
            3, 'updated_at': '2021-08-17T13:28:57.801578Z'}, 'catalog_type': {'annotations': {'incident.io/catalog-
            importer/id': 'id-of-config'}, 'color': 'yellow', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Represents Kubernetes clusters that we run inside of GKE.', 'estimated_count': 7, 'external_type':
            'PagerDutyService', 'icon': 'bolt', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'name':
            'Kubernetes Cluster', 'ranked': True, 'required_integrations': ['pager_duty'], 'schema': {'attributes':
            [{'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'type':
            'Custom["Service"]'}], 'version': 1}, 'semantic_type': 'custom', 'type_name': 'Custom["BackstageGroup"]',
            'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        catalog_entry (CatalogEntryV2ResponseBody):  Example: {'aliases': ['lawrence@incident.io', 'lawrence'],
            'archived_at': '2021-08-17T14:28:57.801578Z', 'attribute_values': {'abc123': {'array_value': [{'catalog_entry':
            {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'catalog_entry_name': 'Primary escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext':
            'Collection of standalone automations like auto-closing incidents.', 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': '000020', 'unavailable':
            False, 'value': 'abc123'}], 'value': {'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z',
            'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations like auto-closing incidents.',
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': '000020', 'unavailable': False, 'value': 'abc123'}}}, 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'created_at': '2021-08-17T13:28:57.801578Z', 'external_id':
            '761722cd-d1d7-477b-ac7e-90f9e079dc33', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Primary On-call', 'rank':
            3, 'updated_at': '2021-08-17T13:28:57.801578Z'}.
        catalog_type (CatalogTypeV2ResponseBody):  Example: {'annotations': {'incident.io/catalog-importer/id': 'id-of-
            config'}, 'color': 'yellow', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes
            clusters that we run inside of GKE.', 'estimated_count': 7, 'external_type': 'PagerDutyService', 'icon': 'bolt',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'name': 'Kubernetes Cluster', 'ranked': True,
            'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'type': 'Custom["Service"]'}], 'version': 1},
            'semantic_type': 'custom', 'type_name': 'Custom["BackstageGroup"]', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    catalog_entry: "CatalogEntryV2ResponseBody"
    catalog_type: "CatalogTypeV2ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        catalog_v2_update_entry_response_body = cls(
            catalog_entry=catalog_entry,
            catalog_type=catalog_type,
        )

        catalog_v2_update_entry_response_body.additional_properties = d
        return catalog_v2_update_entry_response_body

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
