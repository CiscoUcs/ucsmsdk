"""This module contains the meta information of ConfigResolveClasses ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveClasses", "configResolveClasses", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_ids": MethodPropertyMeta("InIds", "inIds", "ClassIdSet", "Version142b", "Input", True),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inHierarchical": "in_hierarchical",
    "inIds": "in_ids",
    "outConfigs": "out_configs",
}
