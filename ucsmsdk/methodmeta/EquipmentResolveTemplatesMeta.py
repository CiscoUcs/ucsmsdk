"""This module contains the meta information of EquipmentResolveTemplates ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EquipmentResolveTemplates", "equipmentResolveTemplates", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_exclude_if_bound": MethodPropertyMeta("InExcludeIfBound", "inExcludeIfBound", "Xs:string", "Version142b", "Input", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_type": MethodPropertyMeta("InType", "inType", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigMap", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inExcludeIfBound": "in_exclude_if_bound",
    "inFilter": "in_filter",
    "inHierarchical": "in_hierarchical",
    "inType": "in_type",
    "outConfigs": "out_configs",
}
