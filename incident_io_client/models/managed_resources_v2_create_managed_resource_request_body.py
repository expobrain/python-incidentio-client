from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_resources_v2_create_managed_resource_request_body_resource_type import (
    ManagedResourcesV2CreateManagedResourceRequestBodyResourceType,
)

if TYPE_CHECKING:
    from ..models.managed_resources_v2_create_managed_resource_request_body_annotations import (
        ManagedResourcesV2CreateManagedResourceRequestBodyAnnotations,
    )


T = TypeVar("T", bound="ManagedResourcesV2CreateManagedResourceRequestBody")


@_attrs_define
class ManagedResourcesV2CreateManagedResourceRequestBody:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'resource_id': 'abc123', 'resource_type':
            'schedule'}

    Attributes:
        annotations (ManagedResourcesV2CreateManagedResourceRequestBodyAnnotations): Annotations that track metadata
            about this resource Example: {'incident.io/terraform/version': '3.0.0'}.
        resource_id (str): The ID of the related resource Example: abc123.
        resource_type (ManagedResourcesV2CreateManagedResourceRequestBodyResourceType): The type of the related resource
            Example: schedule.
    """

    annotations: "ManagedResourcesV2CreateManagedResourceRequestBodyAnnotations"
    resource_id: str
    resource_type: ManagedResourcesV2CreateManagedResourceRequestBodyResourceType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annotations = self.annotations.to_dict()

        resource_id = self.resource_id

        resource_type = self.resource_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotations": annotations,
                "resource_id": resource_id,
                "resource_type": resource_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_resources_v2_create_managed_resource_request_body_annotations import (
            ManagedResourcesV2CreateManagedResourceRequestBodyAnnotations,
        )

        d = src_dict.copy()
        annotations = ManagedResourcesV2CreateManagedResourceRequestBodyAnnotations.from_dict(
            d.pop("annotations")
        )

        resource_id = d.pop("resource_id")

        resource_type = ManagedResourcesV2CreateManagedResourceRequestBodyResourceType(
            d.pop("resource_type")
        )

        managed_resources_v2_create_managed_resource_request_body = cls(
            annotations=annotations,
            resource_id=resource_id,
            resource_type=resource_type,
        )

        managed_resources_v2_create_managed_resource_request_body.additional_properties = d
        return managed_resources_v2_create_managed_resource_request_body

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
