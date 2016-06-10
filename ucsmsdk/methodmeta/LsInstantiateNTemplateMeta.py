"""This module contains the meta information of LsInstantiateNTemplate ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("LsInstantiateNTemplate", "lsInstantiateNTemplate", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_number_of": MethodPropertyMeta("InNumberOf", "inNumberOf", "Xs:unsignedByte", "Version142b", "Input", False),
    "in_server_name_prefix_or_empty": MethodPropertyMeta("InServerNamePrefixOrEmpty", "inServerNamePrefixOrEmpty", "Xs:string", "Version142b", "Input", False),
    "in_target_org": MethodPropertyMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inHierarchical": "in_hierarchical",
    "inNumberOf": "in_number_of",
    "inServerNamePrefixOrEmpty": "in_server_name_prefix_or_empty",
    "inTargetOrg": "in_target_org",
    "outConfigs": "out_configs",
}
