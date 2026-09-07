import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_page_retrospective_incident_update_v2_incident_status import (
    StatusPageRetrospectiveIncidentUpdateV2IncidentStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_incident_affected_component_v2 import (
        StatusPageIncidentAffectedComponentV2,
    )


T = TypeVar("T", bound="StatusPageRetrospectiveIncidentUpdateV2")


@_attrs_define
class StatusPageRetrospectiveIncidentUpdateV2:
    """A single update in the reconstructed timeline of a retrospective status page incident.

    Example:
        {'component_statuses': [{'component_id': '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}],
            'incident_status': 'investigating', 'message': 'We are currently investigating reports of elevated error rates
            affecting our API.', 'published_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        incident_status (StatusPageRetrospectiveIncidentUpdateV2IncidentStatus): Current status for this incident
            Example: investigating.
        message (str): Markdown update on what's changed about this status page incident Example: We are currently
            investigating reports of elevated error rates affecting our API..
        published_at (datetime.datetime): When this update was published. Must be in the past. Example:
            2021-08-17T13:28:57.801578Z.
        component_statuses (Union[Unset, List['StatusPageIncidentAffectedComponentV2']]): An array of mappings from
            component ID to component status at the time this update was published Example: [{'component_id':
            '01FCNDV6P870EA6S7TK1DSYDG2', 'component_status': 'operational'}].
    """

    incident_status: StatusPageRetrospectiveIncidentUpdateV2IncidentStatus
    message: str
    published_at: datetime.datetime
    component_statuses: Union[
        Unset, List["StatusPageIncidentAffectedComponentV2"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_status = self.incident_status.value

        message = self.message

        published_at = self.published_at.isoformat()

        component_statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.component_statuses, Unset):
            component_statuses = []
            for component_statuses_item_data in self.component_statuses:
                component_statuses_item = component_statuses_item_data.to_dict()
                component_statuses.append(component_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_status": incident_status,
                "message": message,
                "published_at": published_at,
            }
        )
        if component_statuses is not UNSET:
            field_dict["component_statuses"] = component_statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.status_page_incident_affected_component_v2 import (
            StatusPageIncidentAffectedComponentV2,
        )

        d = src_dict.copy()
        incident_status = StatusPageRetrospectiveIncidentUpdateV2IncidentStatus(
            d.pop("incident_status")
        )

        message = d.pop("message")

        published_at = isoparse(d.pop("published_at"))

        component_statuses = []
        _component_statuses = d.pop("component_statuses", UNSET)
        for component_statuses_item_data in _component_statuses or []:
            component_statuses_item = StatusPageIncidentAffectedComponentV2.from_dict(
                component_statuses_item_data
            )

            component_statuses.append(component_statuses_item)

        status_page_retrospective_incident_update_v2 = cls(
            incident_status=incident_status,
            message=message,
            published_at=published_at,
            component_statuses=component_statuses,
        )

        status_page_retrospective_incident_update_v2.additional_properties = d
        return status_page_retrospective_incident_update_v2

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
