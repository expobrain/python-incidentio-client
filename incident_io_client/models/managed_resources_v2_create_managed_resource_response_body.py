from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.managed_resource_v2 import ManagedResourceV2


T = TypeVar("T", bound="ManagedResourcesV2CreateManagedResourceResponseBody")


@_attrs_define
class ManagedResourcesV2CreateManagedResourceResponseBody:
    """
    Example:
        {'managed_resource': {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'managed_by': 'dashboard',
            'resource_id': 'abc123', 'resource_type': 'schedule', 'source_url': 'https://github.com/my-
            company/infrastructure'}}

    Attributes:
        managed_resource (ManagedResourceV2):  Example: {'annotations': {'incident.io/terraform/version': '3.0.0'},
            'managed_by': 'dashboard', 'resource_id': 'abc123', 'resource_type': 'schedule', 'source_url':
            'https://github.com/my-company/infrastructure'}.
    """

    managed_resource: "ManagedResourceV2"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        managed_resource = self.managed_resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "managed_resource": managed_resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.managed_resource_v2 import ManagedResourceV2

        d = src_dict.copy()
        managed_resource = ManagedResourceV2.from_dict(d.pop("managed_resource"))

        managed_resources_v2_create_managed_resource_response_body = cls(
            managed_resource=managed_resource,
        )

        managed_resources_v2_create_managed_resource_response_body.additional_properties = d
        return managed_resources_v2_create_managed_resource_response_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
