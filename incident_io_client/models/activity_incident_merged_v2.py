from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2 import ActorV2
    from ..models.incident_slim_v2 import IncidentSlimV2


T = TypeVar("T", bound="ActivityIncidentMergedV2")


@_attrs_define
class ActivityIncidentMergedV2:
    """
    Example:
        {'incident_update_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'merger': {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66',
            'title': '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name':
            'Lisa Karlin Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My little workflow'}}, 'source_incident': {'external_id': 123, 'id':
            '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad', 'reference': 'INC-123', 'status_category':
            'triage', 'summary': "Our database is really really sad, and we don't know why yet.", 'visibility': 'public'}}

    Attributes:
        incident_update_id (Union[Unset, str]): The incident update that carried the merge. Absent on merges recorded
            before December 2025. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        merger (Union[Unset, ActorV2]):  Example: {'alert': {'id': '01GW2G3V0S59R238FAHPDS1R66', 'title':
            '*errors.withMessage: PG::Error failed to connect'}, 'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My
            test API key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'owner', 'slack_user_id': 'U02AYNF2XJM'}, 'workflow': {'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'My little workflow'}}.
        source_incident (Union[Unset, IncidentSlimV2]): Incident slim is a subset of the full incident object, listing
            key fields. Example: {'external_id': 123, 'id': '01FDAG4SAP5TYPT98WGR2N7W91', 'name': 'Our database is sad',
            'reference': 'INC-123', 'status_category': 'triage', 'summary': "Our database is really really sad, and we don't
            know why yet.", 'visibility': 'public'}.
    """

    incident_update_id: Union[Unset, str] = UNSET
    merger: Union[Unset, "ActorV2"] = UNSET
    source_incident: Union[Unset, "IncidentSlimV2"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_update_id = self.incident_update_id

        merger: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.merger, Unset):
            merger = self.merger.to_dict()

        source_incident: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_incident, Unset):
            source_incident = self.source_incident.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incident_update_id is not UNSET:
            field_dict["incident_update_id"] = incident_update_id
        if merger is not UNSET:
            field_dict["merger"] = merger
        if source_incident is not UNSET:
            field_dict["source_incident"] = source_incident

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.actor_v2 import ActorV2
        from ..models.incident_slim_v2 import IncidentSlimV2

        d = src_dict.copy()
        incident_update_id = d.pop("incident_update_id", UNSET)

        _merger = d.pop("merger", UNSET)
        merger: Union[Unset, ActorV2]
        if isinstance(_merger, Unset):
            merger = UNSET
        else:
            merger = ActorV2.from_dict(_merger)

        _source_incident = d.pop("source_incident", UNSET)
        source_incident: Union[Unset, IncidentSlimV2]
        if isinstance(_source_incident, Unset):
            source_incident = UNSET
        else:
            source_incident = IncidentSlimV2.from_dict(_source_incident)

        activity_incident_merged_v2 = cls(
            incident_update_id=incident_update_id,
            merger=merger,
            source_incident=source_incident,
        )

        activity_incident_merged_v2.additional_properties = d
        return activity_incident_merged_v2

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
