from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_resource_v2_response_body_managed_by import (
    ManagedResourceV2ResponseBodyManagedBy,
)
from ..models.managed_resource_v2_response_body_resource_type import (
    ManagedResourceV2ResponseBodyResourceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_resource_v2_response_body_annotations import (
        ManagedResourceV2ResponseBodyAnnotations,
    )


T = TypeVar("T", bound="ManagedResourceV2ResponseBody")


@_attrs_define
class ManagedResourceV2ResponseBody:
    """
    Example:
        {'annotations': {'incident.io/terraform/version': '3.0.0'}, 'managed_by': 'dashboard', 'resource_id': 'abc123',
            'resource_type': 'schedule', 'source_url': 'https://github.com/my-company/infrastructure'}

    Attributes:
        annotations (ManagedResourceV2ResponseBodyAnnotations): Annotations that track metadata about this resource
            Example: {'incident.io/terraform/version': '3.0.0'}.
        managed_by (ManagedResourceV2ResponseBodyManagedBy): How is this resource managed Example: dashboard.
        resource_id (str): The ID of the related resource Example: abc123.
        resource_type (ManagedResourceV2ResponseBodyResourceType): The type of the related resource Example: schedule.
        source_url (Union[Unset, str]): The url of the external repository where this resource is managed (if there is
            one) Example: https://github.com/my-company/infrastructure.
    """

    annotations: "ManagedResourceV2ResponseBodyAnnotations"
    managed_by: ManagedResourceV2ResponseBodyManagedBy
    resource_id: str
    resource_type: ManagedResourceV2ResponseBodyResourceType
    source_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annotations = self.annotations.to_dict()

        managed_by = self.managed_by.value

        resource_id = self.resource_id

        resource_type = self.resource_type.value

        source_url = self.source_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotations": annotations,
                "managed_by": managed_by,
                "resource_id": resource_id,
                "resource_type": resource_type,
            }
        )
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_resource_v2_response_body_annotations import (
            ManagedResourceV2ResponseBodyAnnotations,
        )

        d = src_dict.copy()
        annotations = ManagedResourceV2ResponseBodyAnnotations.from_dict(d.pop("annotations"))

        managed_by = ManagedResourceV2ResponseBodyManagedBy(d.pop("managed_by"))

        resource_id = d.pop("resource_id")

        resource_type = ManagedResourceV2ResponseBodyResourceType(d.pop("resource_type"))

        source_url = d.pop("source_url", UNSET)

        managed_resource_v2_response_body = cls(
            annotations=annotations,
            managed_by=managed_by,
            resource_id=resource_id,
            resource_type=resource_type,
            source_url=source_url,
        )

        managed_resource_v2_response_body.additional_properties = d
        return managed_resource_v2_response_body

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
