import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.incident_timestamp_v2_response_body_required import (
    IncidentTimestampV2ResponseBodyRequired,
)
from ..models.incident_timestamp_v2_response_body_set_on_transition import (
    IncidentTimestampV2ResponseBodySetOnTransition,
)
from ..models.incident_timestamp_v2_response_body_set_on_visit import (
    IncidentTimestampV2ResponseBodySetOnVisit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentTimestampV2ResponseBody")


@attr.s(auto_attribs=True)
class IncidentTimestampV2ResponseBody:
    """
    Example:
        {'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'When this incident started impacting customers.',
            'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Impact started', 'rank': 1, 'required': 'never', 'set_on_creation':
            True, 'set_on_status_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'set_on_transition': 'enter', 'set_on_visit': 'first',
            'show_before_closure': True, 'show_before_creation': True, 'show_in_announcement_post': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        description (str): Rich text description of the incident timestamp Example: When this incident started impacting
            customers..
        id (str): Unique ID of this incident timestamp Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        name (str): Unique name of this timestamp Example: Impact started.
        rank (int): Order in which this timestamp should be shown Example: 1.
        required (IncidentTimestampV2ResponseBodyRequired): When this incident timestamp must be set during the incident
            lifecycle. Example: never.
        set_on_creation (bool): Whether this incident timestamp should be set on incident creation. Example: True.
        set_on_transition (IncidentTimestampV2ResponseBodySetOnTransition): The transition that this incident timestamp
            should be set on. Example: enter.
        set_on_visit (IncidentTimestampV2ResponseBodySetOnVisit): The visit that this incident timestamp should be set
            on. Example: first.
        show_before_closure (bool): Whether a incident timestamp should be shown in the incident close modal. If this
            incident timestamp is required before closure, but no value has been set for it, the timestamp will be shown in
            the closure modal whatever the value of this setting. Example: True.
        show_before_creation (bool): Whether a incident timestamp should be shown in the incident creation modal. This
            must be true if the timestamp is always required. Example: True.
        show_in_announcement_post (bool): Whether a incident timestamp should be shown in the list of fields as part of
            the announcement post when set. Example: True.
        updated_at (datetime.datetime):  Example: 2021-08-17T13:28:57.801578Z.
        set_on_status_id (Union[Unset, str]): The id of the incident status that this incident timestamp should be set
            on. Example: 01FCNDV6P870EA6S7TK1DSYD5H.
    """

    created_at: datetime.datetime
    description: str
    id: str
    name: str
    rank: int
    required: IncidentTimestampV2ResponseBodyRequired
    set_on_creation: bool
    set_on_transition: IncidentTimestampV2ResponseBodySetOnTransition
    set_on_visit: IncidentTimestampV2ResponseBodySetOnVisit
    show_before_closure: bool
    show_before_creation: bool
    show_in_announcement_post: bool
    updated_at: datetime.datetime
    set_on_status_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        id = self.id
        name = self.name
        rank = self.rank
        required = self.required.value

        set_on_creation = self.set_on_creation
        set_on_transition = self.set_on_transition.value

        set_on_visit = self.set_on_visit.value

        show_before_closure = self.show_before_closure
        show_before_creation = self.show_before_creation
        show_in_announcement_post = self.show_in_announcement_post
        updated_at = self.updated_at.isoformat()

        set_on_status_id = self.set_on_status_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "rank": rank,
                "required": required,
                "set_on_creation": set_on_creation,
                "set_on_transition": set_on_transition,
                "set_on_visit": set_on_visit,
                "show_before_closure": show_before_closure,
                "show_before_creation": show_before_creation,
                "show_in_announcement_post": show_in_announcement_post,
                "updated_at": updated_at,
            }
        )
        if set_on_status_id is not UNSET:
            field_dict["set_on_status_id"] = set_on_status_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        rank = d.pop("rank")

        required = IncidentTimestampV2ResponseBodyRequired(d.pop("required"))

        set_on_creation = d.pop("set_on_creation")

        set_on_transition = IncidentTimestampV2ResponseBodySetOnTransition(
            d.pop("set_on_transition")
        )

        set_on_visit = IncidentTimestampV2ResponseBodySetOnVisit(d.pop("set_on_visit"))

        show_before_closure = d.pop("show_before_closure")

        show_before_creation = d.pop("show_before_creation")

        show_in_announcement_post = d.pop("show_in_announcement_post")

        updated_at = isoparse(d.pop("updated_at"))

        set_on_status_id = d.pop("set_on_status_id", UNSET)

        incident_timestamp_v2_response_body = cls(
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            rank=rank,
            required=required,
            set_on_creation=set_on_creation,
            set_on_transition=set_on_transition,
            set_on_visit=set_on_visit,
            show_before_closure=show_before_closure,
            show_before_creation=show_before_creation,
            show_in_announcement_post=show_in_announcement_post,
            updated_at=updated_at,
            set_on_status_id=set_on_status_id,
        )

        incident_timestamp_v2_response_body.additional_properties = d
        return incident_timestamp_v2_response_body

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
