from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entry_reference_v2_response_body import (
        CatalogEntryReferenceV2ResponseBody,
    )


T = TypeVar("T", bound="EngineParamBindingValueV2ResponseBody")


@_attrs_define
class EngineParamBindingValueV2ResponseBody:
    """
    Example:
        {'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'Collection of standalone automations like auto-closing incidents.',
            'image_url': 'https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg',
            'is_image_slack_icon': False, 'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity',
            'sort_key': '000020', 'unavailable': False, 'value': 'abc123'}

    Attributes:
        label (str): Human readable label to be displayed for user to select Example: Lawrence Jones.
        sort_key (str): Gives an indication of how to sort the options when displayed to the user Example: 000020.
        catalog_entry (Union[Unset, CatalogEntryReferenceV2ResponseBody]):  Example: {'archived_at':
            '2021-08-17T14:28:57.801578Z', 'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary
            escalation', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        helptext (Union[Unset, str]): Gives a description of the option to the user Example: Collection of standalone
            automations like auto-closing incidents..
        image_url (Union[Unset, str]): If appropriate, URL to an image that can be displayed alongside the option
            Example: https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg.
        is_image_slack_icon (Union[Unset, bool]): If true, the image_url is a Slack icon and should be displayed as such
        literal (Union[Unset, str]): If set, this is the literal value of the step parameter Example: SEV123.
        reference (Union[Unset, str]): If set, this is the reference into the trigger scope that is the value of this
            parameter Example: incident.severity.
        unavailable (Union[Unset, bool]): Unavailable is true if we've failed to build the value for this binding
        value (Union[Unset, str]): Either the reference or the literal: this field is designed purely to make working
            with react-select easier Example: abc123.
    """

    label: str
    sort_key: str
    catalog_entry: Union[Unset, "CatalogEntryReferenceV2ResponseBody"] = UNSET
    helptext: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    is_image_slack_icon: Union[Unset, bool] = UNSET
    literal: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    unavailable: Union[Unset, bool] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        sort_key = self.sort_key
        catalog_entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.catalog_entry, Unset):
            catalog_entry = self.catalog_entry.to_dict()

        helptext = self.helptext
        image_url = self.image_url
        is_image_slack_icon = self.is_image_slack_icon
        literal = self.literal
        reference = self.reference
        unavailable = self.unavailable
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "sort_key": sort_key,
            }
        )
        if catalog_entry is not UNSET:
            field_dict["catalog_entry"] = catalog_entry
        if helptext is not UNSET:
            field_dict["helptext"] = helptext
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if is_image_slack_icon is not UNSET:
            field_dict["is_image_slack_icon"] = is_image_slack_icon
        if literal is not UNSET:
            field_dict["literal"] = literal
        if reference is not UNSET:
            field_dict["reference"] = reference
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_entry_reference_v2_response_body import (
            CatalogEntryReferenceV2ResponseBody,
        )

        d = src_dict.copy()
        label = d.pop("label")

        sort_key = d.pop("sort_key")

        _catalog_entry = d.pop("catalog_entry", UNSET)
        catalog_entry: Union[Unset, CatalogEntryReferenceV2ResponseBody]
        if isinstance(_catalog_entry, Unset):
            catalog_entry = UNSET
        else:
            catalog_entry = CatalogEntryReferenceV2ResponseBody.from_dict(_catalog_entry)

        helptext = d.pop("helptext", UNSET)

        image_url = d.pop("image_url", UNSET)

        is_image_slack_icon = d.pop("is_image_slack_icon", UNSET)

        literal = d.pop("literal", UNSET)

        reference = d.pop("reference", UNSET)

        unavailable = d.pop("unavailable", UNSET)

        value = d.pop("value", UNSET)

        engine_param_binding_value_v2_response_body = cls(
            label=label,
            sort_key=sort_key,
            catalog_entry=catalog_entry,
            helptext=helptext,
            image_url=image_url,
            is_image_slack_icon=is_image_slack_icon,
            literal=literal,
            reference=reference,
            unavailable=unavailable,
            value=value,
        )

        engine_param_binding_value_v2_response_body.additional_properties = d
        return engine_param_binding_value_v2_response_body

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
