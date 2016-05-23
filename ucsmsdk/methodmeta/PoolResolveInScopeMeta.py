"""This module contains the meta information of PoolResolveInScope ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("PoolResolveInScope", "poolResolveInScope", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_class": MethodPropertyMeta("InClass", "inClass", "NamingClassId", "Version142b", "Input", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_single_level": MethodPropertyMeta("InSingleLevel", "inSingleLevel", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigMap", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inClass": "in_class",
    "inFilter": "in_filter",
    "inHierarchical": "in_hierarchical",
    "inSingleLevel": "in_single_level",
    "outConfigs": "out_configs",
}
