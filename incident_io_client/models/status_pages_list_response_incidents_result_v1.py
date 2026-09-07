from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_page_linked_response_incident_v1 import (
        StatusPageLinkedResponseIncidentV1,
    )


T = TypeVar("T", bound="StatusPagesListResponseIncidentsResultV1")


@_attrs_define
class StatusPagesListResponseIncidentsResultV1:
    """
    Example:
        {'incidents': [{'id': '01FDAG4SAH3GYPT98WGR2N7W91', 'linked_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        incidents (List['StatusPageLinkedResponseIncidentV1']):  Example: [{'id': '01FDAG4SAH3GYPT98WGR2N7W91',
            'linked_at': '2021-08-17T13:28:57.801578Z'}].
    """

    incidents: List["StatusPageLinkedResponseIncidentV1"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incidents = []
        for incidents_item_data in self.incidents:
            incidents_item = incidents_item_data.to_dict()
            incidents.append(incidents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incidents": incidents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.status_page_linked_response_incident_v1 import (
            StatusPageLinkedResponseIncidentV1,
        )

        d = src_dict.copy()
        incidents = []
        _incidents = d.pop("incidents")
        for incidents_item_data in _incidents:
            incidents_item = StatusPageLinkedResponseIncidentV1.from_dict(
                incidents_item_data
            )

            incidents.append(incidents_item)

        status_pages_list_response_incidents_result_v1 = cls(
            incidents=incidents,
        )

        status_pages_list_response_incidents_result_v1.additional_properties = d
        return status_pages_list_response_incidents_result_v1

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
