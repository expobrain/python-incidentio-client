from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding import EngineParamBinding


T = TypeVar("T", bound="EngineParam")


@_attrs_define
class EngineParam:
    """
    Example:
        {'array': True, 'default_value': {'array_value': [{'catalog_entry': {'archived_at':
            '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary
            escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations
            like auto-closing incidents.', 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': '000020', 'unavailable':
            False, 'value': 'abc123'}], 'value': {'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z',
            'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations like auto-closing incidents.',
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': '000020', 'unavailable': False, 'value': 'abc123'}}, 'description': 'What slack channel should we
            send the message to?', 'infer_reference': True, 'label': 'To date', 'name': 'severity', 'optional': True,
            'type': 'IncidentSeverity'}

    Attributes:
        array (bool): Whether this parameter is an array Example: True.
        description (str): A string describing the param Example: What slack channel should we send the message to?.
        infer_reference (bool): Whether this parameter should be inferred as a reference from the scope Example: True.
        label (str): Human readable label for this parameter Example: To date.
        name (str): The unique identifier for the parameter Example: severity.
        optional (bool): Whether this parameter is optional Example: True.
        type (str): The type of the parameter Example: IncidentSeverity.
        default_value (Union[Unset, EngineParamBinding]):  Example: {'array_value': [{'catalog_entry': {'archived_at':
            '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary
            escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations
            like auto-closing incidents.', 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': '000020', 'unavailable':
            False, 'value': 'abc123'}], 'value': {'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z',
            'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations like auto-closing incidents.',
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': '000020', 'unavailable': False, 'value': 'abc123'}}.
    """

    array: bool
    description: str
    infer_reference: bool
    label: str
    name: str
    optional: bool
    type: str
    default_value: Union[Unset, "EngineParamBinding"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array

        description = self.description

        infer_reference = self.infer_reference

        label = self.label

        name = self.name

        optional = self.optional

        type = self.type

        default_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "description": description,
                "infer_reference": infer_reference,
                "label": label,
                "name": name,
                "optional": optional,
                "type": type,
            }
        )
        if default_value is not UNSET:
            field_dict["default_value"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding import EngineParamBinding

        d = src_dict.copy()
        array = d.pop("array")

        description = d.pop("description")

        infer_reference = d.pop("infer_reference")

        label = d.pop("label")

        name = d.pop("name")

        optional = d.pop("optional")

        type = d.pop("type")

        _default_value = d.pop("default_value", UNSET)
        default_value: Union[Unset, EngineParamBinding]
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = EngineParamBinding.from_dict(_default_value)

        engine_param = cls(
            array=array,
            description=description,
            infer_reference=infer_reference,
            label=label,
            name=name,
            optional=optional,
            type=type,
            default_value=default_value,
        )

        engine_param.additional_properties = d
        return engine_param

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
