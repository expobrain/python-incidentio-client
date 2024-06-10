from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_v2_response_body import (
        EngineParamBindingV2ResponseBody,
    )


T = TypeVar("T", bound="StepConfigResponseBody")


@_attrs_define
class StepConfigResponseBody:
    """
    Example:
        {'for_each': 'abc123', 'id': 'abc123', 'label': 'PagerDuty Escalate', 'name': 'pagerduty.escalate',
            'param_bindings': [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference':
            'incident.severity'}}]}

    Attributes:
        id (str): Unique ID of this step in a workflow Example: abc123.
        label (str): Human readable identifier for this step Example: PagerDuty Escalate.
        name (str): Unique name of the step in the engine Example: pagerduty.escalate.
        param_bindings (List['EngineParamBindingV2ResponseBody']): Bindings for the step parameters Example:
            [{'array_value': [{'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}], 'value':
            {'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity'}}].
        for_each (Union[Unset, str]): Reference to the loop variable to run this step over Example: abc123.
    """

    id: str
    label: str
    name: str
    param_bindings: List["EngineParamBindingV2ResponseBody"]
    for_each: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        label = self.label

        name = self.name

        param_bindings = []
        for param_bindings_item_data in self.param_bindings:
            param_bindings_item = param_bindings_item_data.to_dict()
            param_bindings.append(param_bindings_item)

        for_each = self.for_each

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "name": name,
                "param_bindings": param_bindings,
            }
        )
        if for_each is not UNSET:
            field_dict["for_each"] = for_each

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding_v2_response_body import (
            EngineParamBindingV2ResponseBody,
        )

        d = src_dict.copy()
        id = d.pop("id")

        label = d.pop("label")

        name = d.pop("name")

        param_bindings = []
        _param_bindings = d.pop("param_bindings")
        for param_bindings_item_data in _param_bindings:
            param_bindings_item = EngineParamBindingV2ResponseBody.from_dict(
                param_bindings_item_data
            )

            param_bindings.append(param_bindings_item)

        for_each = d.pop("for_each", UNSET)

        step_config_response_body = cls(
            id=id,
            label=label,
            name=name,
            param_bindings=param_bindings,
            for_each=for_each,
        )

        step_config_response_body.additional_properties = d
        return step_config_response_body

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
