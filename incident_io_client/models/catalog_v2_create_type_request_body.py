from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CatalogV2CreateTypeRequestBody")


@attr.s(auto_attribs=True)
class CatalogV2CreateTypeRequestBody:
    """
    Example:
        {'description': 'Represents Kubernetes clusters that we run inside of GKE.', 'name': 'Kubernetes Cluster',
            'semantic_type': 'custom'}

    Attributes:
        description (str): Human readble description of this type Example: Represents Kubernetes clusters that we run
            inside of GKE..
        name (str): Name is the human readable name of this type Example: Kubernetes Cluster.
        semantic_type (str): Semantic type of this resource Example: custom.
    """

    description: str
    name: str
    semantic_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        semantic_type = self.semantic_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "semantic_type": semantic_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        name = d.pop("name")

        semantic_type = d.pop("semantic_type")

        catalog_v2_create_type_request_body = cls(
            description=description,
            name=name,
            semantic_type=semantic_type,
        )

        catalog_v2_create_type_request_body.additional_properties = d
        return catalog_v2_create_type_request_body

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
