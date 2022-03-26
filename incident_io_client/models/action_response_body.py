import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.action_response_body_status import ActionResponseBodyStatus
from ..models.external_issue_reference_response_body import (
    ExternalIssueReferenceResponseBody,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionResponseBody")


@attr.s(auto_attribs=True)
class ActionResponseBody:
    """
    Example:
        {'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            'Call the fire brigade', 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink':
            'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'linear'}, 'follow_up':
            True, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding',
            'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        description (str): Description of the action Example: Call the fire brigade.
        follow_up (bool): Whether an action is marked as follow-up Example: True.
        id (str): Unique identifier for the action Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): Unique identifier of the incident the action belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (ActionResponseBodyStatus): Status of the action Example: outstanding.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
        completed_at (Union[Unset, datetime.datetime]): When the action was completed Example:
            2021-08-17T13:28:57.801578Z.
        external_issue_reference (Union[Unset, ExternalIssueReferenceResponseBody]):  Example: {'issue_name': 'INC-123',
            'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider':
            'linear'}.
    """

    created_at: datetime.datetime
    description: str
    follow_up: bool
    id: str
    incident_id: str
    status: ActionResponseBodyStatus
    updated_at: datetime.datetime
    completed_at: Union[Unset, datetime.datetime] = UNSET
    external_issue_reference: Union[Unset, ExternalIssueReferenceResponseBody] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        follow_up = self.follow_up
        id = self.id
        incident_id = self.incident_id
        status = self.status.value

        updated_at = self.updated_at.isoformat()

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        external_issue_reference: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_issue_reference, Unset):
            external_issue_reference = self.external_issue_reference.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "follow_up": follow_up,
                "id": id,
                "incident_id": incident_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if external_issue_reference is not UNSET:
            field_dict["external_issue_reference"] = external_issue_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        follow_up = d.pop("follow_up")

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        status = ActionResponseBodyStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _external_issue_reference = d.pop("external_issue_reference", UNSET)
        external_issue_reference: Union[Unset, ExternalIssueReferenceResponseBody]
        if isinstance(_external_issue_reference, Unset):
            external_issue_reference = UNSET
        else:
            external_issue_reference = ExternalIssueReferenceResponseBody.from_dict(
                _external_issue_reference
            )

        action_response_body = cls(
            created_at=created_at,
            description=description,
            follow_up=follow_up,
            id=id,
            incident_id=incident_id,
            status=status,
            updated_at=updated_at,
            completed_at=completed_at,
            external_issue_reference=external_issue_reference,
        )

        action_response_body.additional_properties = d
        return action_response_body

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
