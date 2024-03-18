import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.catalog_type_v2_response_body_color import CatalogTypeV2ResponseBodyColor
from ..models.catalog_type_v2_response_body_icon import CatalogTypeV2ResponseBodyIcon
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_type_schema_v2_response_body import (
        CatalogTypeSchemaV2ResponseBody,
    )
    from ..models.catalog_type_v2_response_body_annotations import (
        CatalogTypeV2ResponseBodyAnnotations,
    )


T = TypeVar("T", bound="CatalogTypeV2ResponseBody")


@_attrs_define
class CatalogTypeV2ResponseBody:
    """
    Example:
        {'annotations': {'incident.io/catalog-importer/id': 'id-of-config'}, 'color': 'yellow', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes clusters that we run inside of GKE.',
            'dynamic_resource_parameter': 'abc123', 'estimated_count': 7, 'icon': 'bolt', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'is_editable': False, 'last_synced_at': '2021-08-17T13:28:57.801578Z', 'name':
            'Kubernetes Cluster', 'ranked': True, 'registry_type': 'PagerDutyService', 'required_integrations':
            ['pager_duty'], 'schema': {'attributes': [{'array': False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual',
            'name': 'tier', 'type': 'Custom["Service"]'}], 'version': 1}, 'semantic_type': 'custom', 'source_repo_url':
            'https://github.com/my-company/incident-io-catalog', 'type_name': 'Custom["BackstageGroup"]', 'updated_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        annotations (CatalogTypeV2ResponseBodyAnnotations): Annotations that can track metadata about this type Example:
            {'incident.io/catalog-importer/id': 'id-of-config'}.
        color (CatalogTypeV2ResponseBodyColor): Sets the display color of this type in the dashboard Example: yellow.
        created_at (datetime.datetime): When this type was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        icon (CatalogTypeV2ResponseBodyIcon): Sets the display icon of this type in the dashboard Example: bolt.
        id (str): ID of this catalog type Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        is_editable (bool): Catalog types that are synced with external resources can't be edited
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        ranked (bool): If this type should be ranked Example: True.
        schema (CatalogTypeSchemaV2ResponseBody):  Example: {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'mode': 'manual', 'name': 'tier', 'type': 'Custom["Service"]'}], 'version': 1}.
        semantic_type (str): Semantic type of this resource (unused) Example: custom.
        type_name (str): The type name of this catalog type, to be used when defining attributes. This is immutable once
            a CatalogType has been created. For non-externally sync types, it must follow the pattern Custom["SomeName "]
            Example: Custom["BackstageGroup"].
        updated_at (datetime.datetime): When this type was last updated Example: 2021-08-17T13:28:57.801578Z.
        dynamic_resource_parameter (Union[Unset, str]): If this is a dynamic catalog type, this will be the unique
            parameter for identitfying this resource externally. Example: abc123.
        estimated_count (Union[Unset, int]): If populated, gives an estimated count of entries for this type Example: 7.
        last_synced_at (Union[Unset, datetime.datetime]): When this type was last synced (if it's ever been sync'd)
            Example: 2021-08-17T13:28:57.801578Z.
        registry_type (Union[Unset, str]): The registry resource this type is synced from, if any Example:
            PagerDutyService.
        required_integrations (Union[Unset, List[str]]): If populated, the integrations required for this type Example:
            ['pager_duty'].
        source_repo_url (Union[Unset, str]): The url of the external repository where this type is managed Example:
            https://github.com/my-company/incident-io-catalog.
    """

    annotations: "CatalogTypeV2ResponseBodyAnnotations"
    color: CatalogTypeV2ResponseBodyColor
    created_at: datetime.datetime
    description: str
    icon: CatalogTypeV2ResponseBodyIcon
    id: str
    is_editable: bool
    name: str
    ranked: bool
    schema: "CatalogTypeSchemaV2ResponseBody"
    semantic_type: str
    type_name: str
    updated_at: datetime.datetime
    dynamic_resource_parameter: Union[Unset, str] = UNSET
    estimated_count: Union[Unset, int] = UNSET
    last_synced_at: Union[Unset, datetime.datetime] = UNSET
    registry_type: Union[Unset, str] = UNSET
    required_integrations: Union[Unset, List[str]] = UNSET
    source_repo_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annotations = self.annotations.to_dict()

        color = self.color.value

        created_at = self.created_at.isoformat()

        description = self.description

        icon = self.icon.value

        id = self.id

        is_editable = self.is_editable

        name = self.name

        ranked = self.ranked

        schema = self.schema.to_dict()

        semantic_type = self.semantic_type

        type_name = self.type_name

        updated_at = self.updated_at.isoformat()

        dynamic_resource_parameter = self.dynamic_resource_parameter

        estimated_count = self.estimated_count

        last_synced_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_synced_at, Unset):
            last_synced_at = self.last_synced_at.isoformat()

        registry_type = self.registry_type

        required_integrations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_integrations, Unset):
            required_integrations = self.required_integrations

        source_repo_url = self.source_repo_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotations": annotations,
                "color": color,
                "created_at": created_at,
                "description": description,
                "icon": icon,
                "id": id,
                "is_editable": is_editable,
                "name": name,
                "ranked": ranked,
                "schema": schema,
                "semantic_type": semantic_type,
                "type_name": type_name,
                "updated_at": updated_at,
            }
        )
        if dynamic_resource_parameter is not UNSET:
            field_dict["dynamic_resource_parameter"] = dynamic_resource_parameter
        if estimated_count is not UNSET:
            field_dict["estimated_count"] = estimated_count
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if registry_type is not UNSET:
            field_dict["registry_type"] = registry_type
        if required_integrations is not UNSET:
            field_dict["required_integrations"] = required_integrations
        if source_repo_url is not UNSET:
            field_dict["source_repo_url"] = source_repo_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_type_schema_v2_response_body import (
            CatalogTypeSchemaV2ResponseBody,
        )
        from ..models.catalog_type_v2_response_body_annotations import (
            CatalogTypeV2ResponseBodyAnnotations,
        )

        d = src_dict.copy()
        annotations = CatalogTypeV2ResponseBodyAnnotations.from_dict(d.pop("annotations"))

        color = CatalogTypeV2ResponseBodyColor(d.pop("color"))

        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        icon = CatalogTypeV2ResponseBodyIcon(d.pop("icon"))

        id = d.pop("id")

        is_editable = d.pop("is_editable")

        name = d.pop("name")

        ranked = d.pop("ranked")

        schema = CatalogTypeSchemaV2ResponseBody.from_dict(d.pop("schema"))

        semantic_type = d.pop("semantic_type")

        type_name = d.pop("type_name")

        updated_at = isoparse(d.pop("updated_at"))

        dynamic_resource_parameter = d.pop("dynamic_resource_parameter", UNSET)

        estimated_count = d.pop("estimated_count", UNSET)

        _last_synced_at = d.pop("last_synced_at", UNSET)
        last_synced_at: Union[Unset, datetime.datetime]
        if isinstance(_last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = isoparse(_last_synced_at)

        registry_type = d.pop("registry_type", UNSET)

        required_integrations = cast(List[str], d.pop("required_integrations", UNSET))

        source_repo_url = d.pop("source_repo_url", UNSET)

        catalog_type_v2_response_body = cls(
            annotations=annotations,
            color=color,
            created_at=created_at,
            description=description,
            icon=icon,
            id=id,
            is_editable=is_editable,
            name=name,
            ranked=ranked,
            schema=schema,
            semantic_type=semantic_type,
            type_name=type_name,
            updated_at=updated_at,
            dynamic_resource_parameter=dynamic_resource_parameter,
            estimated_count=estimated_count,
            last_synced_at=last_synced_at,
            registry_type=registry_type,
            required_integrations=required_integrations,
            source_repo_url=source_repo_url,
        )

        catalog_type_v2_response_body.additional_properties = d
        return catalog_type_v2_response_body

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
