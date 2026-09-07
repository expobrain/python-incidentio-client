from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_v2_outcome import WebhookDeliveryV2Outcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_delivery_request_v2 import WebhookDeliveryRequestV2
    from ..models.webhook_delivery_response_v2 import WebhookDeliveryResponseV2


T = TypeVar("T", bound="WebhookDeliveryV2")


@_attrs_define
class WebhookDeliveryV2:
    """
    Example:
        {'duration_ms': 412, 'endpoint': 'https://example.com/hooks/incident', 'method': 'POST', 'outcome': 'non_2xx',
            'request': {'body': '{"incident_id":"01FCNDV6P870EA6S7TK1DSYDG0"}', 'body_truncated': False, 'headers':
            {'Content-Type': 'application/json'}}, 'response': {'body': '{"error":"unprocessable"}', 'body_truncated':
            False, 'headers': {'Content-Type': 'application/json'}}, 'status_code': 500}

    Attributes:
        endpoint (str): The interpolated URL the request was sent to. Redirects are followed, so this is the URL
            requested rather than the URL that ultimately served it Example: https://example.com/hooks/incident.
        method (str): HTTP method used for the request Example: POST.
        outcome (WebhookDeliveryV2Outcome): The result of the delivery attempt. Only success and non_2xx have a response
            Example: non_2xx.
        request (WebhookDeliveryRequestV2):  Example: {'body': '{"incident_id":"01FCNDV6P870EA6S7TK1DSYDG0"}',
            'body_truncated': False, 'headers': {'Content-Type': 'application/json'}}.
        duration_ms (Union[Unset, int]): Time taken by the request, in milliseconds Example: 412.
        response (Union[Unset, WebhookDeliveryResponseV2]):  Example: {'body': '{"error":"unprocessable"}',
            'body_truncated': False, 'headers': {'Content-Type': 'application/json'}}.
        status_code (Union[Unset, int]): HTTP status code returned by the endpoint. Absent when no response was received
            Example: 500.
    """

    endpoint: str
    method: str
    outcome: WebhookDeliveryV2Outcome
    request: "WebhookDeliveryRequestV2"
    duration_ms: Union[Unset, int] = UNSET
    response: Union[Unset, "WebhookDeliveryResponseV2"] = UNSET
    status_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint

        method = self.method

        outcome = self.outcome.value

        request = self.request.to_dict()

        duration_ms = self.duration_ms

        response: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "method": method,
                "outcome": outcome,
                "request": request,
            }
        )
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if response is not UNSET:
            field_dict["response"] = response
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_delivery_request_v2 import WebhookDeliveryRequestV2
        from ..models.webhook_delivery_response_v2 import WebhookDeliveryResponseV2

        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        method = d.pop("method")

        outcome = WebhookDeliveryV2Outcome(d.pop("outcome"))

        request = WebhookDeliveryRequestV2.from_dict(d.pop("request"))

        duration_ms = d.pop("duration_ms", UNSET)

        _response = d.pop("response", UNSET)
        response: Union[Unset, WebhookDeliveryResponseV2]
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = WebhookDeliveryResponseV2.from_dict(_response)

        status_code = d.pop("status_code", UNSET)

        webhook_delivery_v2 = cls(
            endpoint=endpoint,
            method=method,
            outcome=outcome,
            request=request,
            duration_ms=duration_ms,
            response=response,
            status_code=status_code,
        )

        webhook_delivery_v2.additional_properties = d
        return webhook_delivery_v2

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
