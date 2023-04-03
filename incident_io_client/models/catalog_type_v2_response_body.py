import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

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
            of GKE.', 'estimated_count': 7, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Kubernetes Cluster', 'ranked':
            True, 'required_integrations': ['pager_duty'], 'schema': {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]'}], 'version':
            1}, 'semantic_type': 'custom', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When this type was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        id (str): ID of this resource Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        ranked (bool): If this type should be ranked Example: True.
        schema (CatalogTypeSchemaV2ResponseBody):  Example: {'attributes': [{'array': False, 'id':
            '01GW2G3V0S59R238FAHPDS1R66', 'name': 'tier', 'type': 'CatalogEntry["01GVGYJSD39FRKVDWACK9NDS4E"]'}], 'version':
            1}.
        semantic_type (str): Semantic type of this resource Example: custom.
        updated_at (datetime.datetime): When this type was last updated Example: 2021-08-17T13:28:57.801578Z.
        estimated_count (Union[Unset, int]): If populated, gives an estimated count of entries for this type Example: 7.
        required_integrations (Union[Unset, List[str]]): If populated, the integrations required for this type Example:
            ['pager_duty'].
    """

    created_at: datetime.datetime
    description: str
    id: str
    name: str
    ranked: bool
    schema: "CatalogTypeSchemaV2ResponseBody"
    semantic_type: str
    updated_at: datetime.datetime
    estimated_count: Union[Unset, int] = UNSET
    required_integrations: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        id = self.id
        name = self.name
        ranked = self.ranked
        schema = self.schema.to_dict()

        semantic_type = self.semantic_type
        updated_at = self.updated_at.isoformat()

        estimated_count = self.estimated_count
        required_integrations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_integrations, Unset):
            required_integrations = self.required_integrations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "ranked": ranked,
                "schema": schema,
                "semantic_type": semantic_type,
                "updated_at": updated_at,
            }
        )
        if estimated_count is not UNSET:
            field_dict["estimated_count"] = estimated_count
        if required_integrations is not UNSET:
            field_dict["required_integrations"] = required_integrations

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

        ranked = d.pop("ranked")

        schema = CatalogTypeSchemaV2ResponseBody.from_dict(d.pop("schema"))

        semantic_type = d.pop("semantic_type")

        updated_at = isoparse(d.pop("updated_at"))

        estimated_count = d.pop("estimated_count", UNSET)

        required_integrations = cast(List[str], d.pop("required_integrations", UNSET))

        catalog_type_v2_response_body = cls(
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            ranked=ranked,
            schema=schema,
            semantic_type=semantic_type,
            updated_at=updated_at,
            estimated_count=estimated_count,
            required_integrations=required_integrations,
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
