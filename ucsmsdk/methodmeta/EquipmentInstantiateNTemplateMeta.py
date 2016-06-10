"""This module contains the meta information of EquipmentInstantiateNTemplate ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EquipmentInstantiateNTemplate", "equipmentInstantiateNTemplate", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_chassis_profile_name_prefix_or_empty": MethodPropertyMeta("InChassisProfileNamePrefixOrEmpty", "inChassisProfileNamePrefixOrEmpty", "Xs:string", "Version142b", "Input", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_number_of": MethodPropertyMeta("InNumberOf", "inNumberOf", "Xs:unsignedByte", "Version142b", "Input", False),
    "in_target_org": MethodPropertyMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inChassisProfileNamePrefixOrEmpty": "in_chassis_profile_name_prefix_or_empty",
    "inHierarchical": "in_hierarchical",
    "inNumberOf": "in_number_of",
    "inTargetOrg": "in_target_org",
    "outConfigs": "out_configs",
}
