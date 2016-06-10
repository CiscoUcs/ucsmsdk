"""This module contains the meta information of LstorageCreateZoningFromInv ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("LstorageCreateZoningFromInv", "lstorageCreateZoningFromInv", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_chassis_dn": MethodPropertyMeta("InChassisDn", "inChassisDn", "ReferenceObject", "Version142b", "Input", False),
    "in_disk_zoning_policy_name": MethodPropertyMeta("InDiskZoningPolicyName", "inDiskZoningPolicyName", "Xs:string", "Version142b", "Input", False),
    "in_target_org": MethodPropertyMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inChassisDn": "in_chassis_dn",
    "inDiskZoningPolicyName": "in_disk_zoning_policy_name",
    "inTargetOrg": "in_target_org",
    "outConfig": "out_config",
}
