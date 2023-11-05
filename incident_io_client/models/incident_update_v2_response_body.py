import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_v2_response_body import ActorV2ResponseBody
    from ..models.incident_status_v2_response_body import IncidentStatusV2ResponseBody
    from ..models.severity_v2_response_body import SeverityV2ResponseBody


T = TypeVar("T", bound="IncidentUpdateV2ResponseBody")


@_attrs_define
class IncidentUpdateV2ResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'message': "We're working on a fix, hoping to ship in the next 30 minutes",
            'new_incident_status': {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            "Impact has been **fully mitigated**, and we're ready to learn from this incident.", 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'new_severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'},
            'updater': {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}, 'user': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}}}

    Attributes:
        created_at (datetime.datetime): When the update was created Example: 2021-08-17T13:28:57.801578Z.
        id (str): Unique identifier for this incident update Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): The incident this update relates to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        new_incident_status (IncidentStatusV2ResponseBody):  Example: {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
        updater (ActorV2ResponseBody):  Example: {'api_key': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API
            key'}, 'user': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}}.
        message (Union[Unset, str]): Message that explains the context behind the update Example: We're working on a
            fix, hoping to ship in the next 30 minutes.
        new_severity (Union[Unset, SeverityV2ResponseBody]):  Example: {'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Issues with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    created_at: datetime.datetime
    id: str
    incident_id: str
    new_incident_status: "IncidentStatusV2ResponseBody"
    updater: "ActorV2ResponseBody"
    message: Union[Unset, str] = UNSET
    new_severity: Union[Unset, "SeverityV2ResponseBody"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id
        incident_id = self.incident_id
        new_incident_status = self.new_incident_status.to_dict()

        updater = self.updater.to_dict()

        message = self.message
        new_severity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_severity, Unset):
            new_severity = self.new_severity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "incident_id": incident_id,
                "new_incident_status": new_incident_status,
                "updater": updater,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if new_severity is not UNSET:
            field_dict["new_severity"] = new_severity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.actor_v2_response_body import ActorV2ResponseBody
        from ..models.incident_status_v2_response_body import (
            IncidentStatusV2ResponseBody,
        )
        from ..models.severity_v2_response_body import SeverityV2ResponseBody

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        new_incident_status = IncidentStatusV2ResponseBody.from_dict(d.pop("new_incident_status"))

        updater = ActorV2ResponseBody.from_dict(d.pop("updater"))

        message = d.pop("message", UNSET)

        _new_severity = d.pop("new_severity", UNSET)
        new_severity: Union[Unset, SeverityV2ResponseBody]
        if isinstance(_new_severity, Unset):
            new_severity = UNSET
        else:
            new_severity = SeverityV2ResponseBody.from_dict(_new_severity)

        incident_update_v2_response_body = cls(
            created_at=created_at,
            id=id,
            incident_id=incident_id,
            new_incident_status=new_incident_status,
            updater=updater,
            message=message,
            new_severity=new_severity,
        )

        incident_update_v2_response_body.additional_properties = d
        return incident_update_v2_response_body

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
