import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.catalog_type_schema_v2_response_body import (
        CatalogTypeSchemaV2ResponseBody,
    )


T = TypeVar("T", bound="CatalogTypeV2ResponseBody")


@attr.s(auto_attribs=True)
class CatalogTypeV2ResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Represents Kubernetes clusters that we run inside
            of GKE.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Kubernetes Cluster', 'schema': {'attributes': [{'array':
            False, 'id': '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}], 'version': 1}, 'semantic_type':
            'service', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When this type was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        id (str): ID of this resource Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        schema (CatalogTypeSchemaV2ResponseBody):  Example: {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'tier'}], 'version': 1}.
        semantic_type (str): Semantic type of this resource Example: service.
        updated_at (datetime.datetime): When this type was last updated Example: 2021-08-17T13:28:57.801578Z.
    """

    created_at: datetime.datetime
    description: str
    id: str
    name: str
    schema: "CatalogTypeSchemaV2ResponseBody"
    semantic_type: str
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        id = self.id
        name = self.name
        schema = self.schema.to_dict()

        semantic_type = self.semantic_type
        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "schema": schema,
                "semantic_type": semantic_type,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_type_schema_v2_response_body import (
            CatalogTypeSchemaV2ResponseBody,
        )

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        schema = CatalogTypeSchemaV2ResponseBody.from_dict(d.pop("schema"))

        semantic_type = d.pop("semantic_type")

        updated_at = isoparse(d.pop("updated_at"))

        catalog_type_v2_response_body = cls(
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            schema=schema,
            semantic_type=semantic_type,
            updated_at=updated_at,
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
