"""This module contains the meta information of EquipmentClone ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EquipmentClone", "equipmentClone", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_chassis_profile_name": MethodPropertyMeta("InChassisProfileName", "inChassisProfileName", "Xs:string", "Version142b", "Input", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_target_org": MethodPropertyMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inChassisProfileName": "in_chassis_profile_name",
    "inHierarchical": "in_hierarchical",
    "inTargetOrg": "in_target_org",
    "outConfig": "out_config",
}
