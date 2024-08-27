from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entry_reference_v2 import CatalogEntryReferenceV2


T = TypeVar("T", bound="CatalogEntryEngineParamBindingValueV2")


@_attrs_define
class CatalogEntryEngineParamBindingValueV2:
    """
    Example:
        {'catalog_entry': {'archived_at': '2021-08-17T14:28:57.801578Z', 'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'helptext': 'abc123', 'image_url': 'abc123', 'is_image_slack_icon': False,
            'label': 'Lawrence Jones', 'literal': 'SEV123', 'reference': 'incident.severity', 'sort_key': 'abc123',
            'unavailable': False, 'value': 'abc123'}

    Attributes:
        label (str): Human readable label to be displayed for user to select Example: Lawrence Jones.
        sort_key (str): This field is deprecated. It will not be present in any responses, and will be removed in a
            future version Example: abc123.
        catalog_entry (Union[Unset, CatalogEntryReferenceV2]):  Example: {'archived_at': '2021-08-17T14:28:57.801578Z',
            'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_entry_name': 'Primary escalation', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}.
        helptext (Union[Unset, str]): This field is deprecated. It will not be present in any responses, and will be
            removed in a future version Example: abc123.
        image_url (Union[Unset, str]): This field is deprecated. It will not be present in any responses, and will be
            removed in a future version Example: abc123.
        is_image_slack_icon (Union[Unset, bool]): This field is deprecated. It will not be present in any responses, and
            will be removed in a future version
        literal (Union[Unset, str]): If set, this is the literal value of the step parameter Example: SEV123.
        reference (Union[Unset, str]): This field is deprecated. It will not be present in any responses, and will be
            removed in a future version Example: incident.severity.
        unavailable (Union[Unset, bool]): This field is deprecated. It will not be present in any responses, and will be
            removed in a future version
        value (Union[Unset, str]): This field is deprecated. It will not be present in any responses, and will be
            removed in a future version Example: abc123.
    """

    label: str
    sort_key: str
    catalog_entry: Union[Unset, "CatalogEntryReferenceV2"] = UNSET
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
        from ..models.catalog_entry_reference_v2 import CatalogEntryReferenceV2

        d = src_dict.copy()
        label = d.pop("label")

        sort_key = d.pop("sort_key")

        _catalog_entry = d.pop("catalog_entry", UNSET)
        catalog_entry: Union[Unset, CatalogEntryReferenceV2]
        if isinstance(_catalog_entry, Unset):
            catalog_entry = UNSET
        else:
            catalog_entry = CatalogEntryReferenceV2.from_dict(_catalog_entry)

        helptext = d.pop("helptext", UNSET)

        image_url = d.pop("image_url", UNSET)

        is_image_slack_icon = d.pop("is_image_slack_icon", UNSET)

        literal = d.pop("literal", UNSET)

        reference = d.pop("reference", UNSET)

        unavailable = d.pop("unavailable", UNSET)

        value = d.pop("value", UNSET)

        catalog_entry_engine_param_binding_value_v2 = cls(
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

        catalog_entry_engine_param_binding_value_v2.additional_properties = d
        return catalog_entry_engine_param_binding_value_v2

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
