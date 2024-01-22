from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_statuses_v1_create_request_body_category import (
    IncidentStatusesV1CreateRequestBodyCategory,
)

T = TypeVar("T", bound="IncidentStatusesV1CreateRequestBody")


@_attrs_define
class IncidentStatusesV1CreateRequestBody:
    """
    Example:
        {'category': 'live', 'description': "Impact has been **fully mitigated**, and we're ready to learn from this
            incident.", 'name': 'Closed'}

    Attributes:
        category (IncidentStatusesV1CreateRequestBodyCategory): Whether the status should be considered 'live' (now
            renamed to active), 'learning' (now renamed to post-incident) or 'closed'. The triage and declined statuses
            cannot be created or modified. Example: live.
        description (str): Rich text description of the incident status Example: Impact has been **fully mitigated**,
            and we're ready to learn from this incident..
        name (str): Unique name of this status Example: Closed.
    """

    category: IncidentStatusesV1CreateRequestBodyCategory
    description: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.value

        description = self.description

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "description": description,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = IncidentStatusesV1CreateRequestBodyCategory(d.pop("category"))

        description = d.pop("description")

        name = d.pop("name")

        incident_statuses_v1_create_request_body = cls(
            category=category,
            description=description,
            name=name,
        )

        incident_statuses_v1_create_request_body.additional_properties = d
        return incident_statuses_v1_create_request_body

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
