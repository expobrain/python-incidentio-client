from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_events_v2_create_http_request_body_status import (
    AlertEventsV2CreateHTTPRequestBodyStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_events_v2_create_http_request_body_metadata import (
        AlertEventsV2CreateHTTPRequestBodyMetadata,
    )


T = TypeVar("T", bound="AlertEventsV2CreateHTTPRequestBody")


@_attrs_define
class AlertEventsV2CreateHTTPRequestBody:
    """
    Example:
        {'deduplication_key': '4293868629', 'description': "We've detected a number of timeouts on hello.world.com, the
            service may be down. To fix...", 'metadata': {'service': 'hello.world.com', 'team': ['my-team']}, 'source_url':
            'https://www.my-alerting-platform.com/alerts/my-alert-123', 'status': 'firing', 'title': '*errors.withMessage:
            PG::Error failed to connect'}

    Attributes:
        status (AlertEventsV2CreateHTTPRequestBodyStatus): Current status of this alert Example: firing.
        title (str): Alert title which is used when summarising the alert Example: *errors.withMessage: PG::Error failed
            to connect.
        deduplication_key (Union[Unset, str]): A deduplication key can be provided to uniquely reference this alert from
            your alert source. If you send an event with the same deduplication_key multiple times, only one alert will be
            created in incident.io for this alert source config. Example: 4293868629.
        description (Union[Unset, str]): Description that optionally adds more detail to title. Supports markdown.
            Example: We've detected a number of timeouts on hello.world.com, the service may be down. To fix....
        metadata (Union[Unset, AlertEventsV2CreateHTTPRequestBodyMetadata]): Any additional metadata that you've
            configured your alert source to parse Example: {'service': 'hello.world.com', 'team': ['my-team']}.
        source_url (Union[Unset, str]): If applicable, a link to the alert in the upstream system Example:
            https://www.my-alerting-platform.com/alerts/my-alert-123.
    """

    status: AlertEventsV2CreateHTTPRequestBodyStatus
    title: str
    deduplication_key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, "AlertEventsV2CreateHTTPRequestBodyMetadata"] = UNSET
    source_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        title = self.title

        deduplication_key = self.deduplication_key

        description = self.description

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        source_url = self.source_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "title": title,
            }
        )
        if deduplication_key is not UNSET:
            field_dict["deduplication_key"] = deduplication_key
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_events_v2_create_http_request_body_metadata import (
            AlertEventsV2CreateHTTPRequestBodyMetadata,
        )

        d = src_dict.copy()
        status = AlertEventsV2CreateHTTPRequestBodyStatus(d.pop("status"))

        title = d.pop("title")

        deduplication_key = d.pop("deduplication_key", UNSET)

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AlertEventsV2CreateHTTPRequestBodyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AlertEventsV2CreateHTTPRequestBodyMetadata.from_dict(_metadata)

        source_url = d.pop("source_url", UNSET)

        alert_events_v2_create_http_request_body = cls(
            status=status,
            title=title,
            deduplication_key=deduplication_key,
            description=description,
            metadata=metadata,
            source_url=source_url,
        )

        alert_events_v2_create_http_request_body.additional_properties = d
        return alert_events_v2_create_http_request_body

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
