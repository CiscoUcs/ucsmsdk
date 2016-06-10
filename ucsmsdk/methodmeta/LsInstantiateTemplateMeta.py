"""This module contains the meta information of LsInstantiateTemplate ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("LsInstantiateTemplate", "lsInstantiateTemplate", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_error_on_existing": MethodPropertyMeta("InErrorOnExisting", "inErrorOnExisting", "Xs:string", "Version142b", "Input", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_server_name": MethodPropertyMeta("InServerName", "inServerName", "Xs:string", "Version142b", "Input", False),
    "in_target_org": MethodPropertyMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inErrorOnExisting": "in_error_on_existing",
    "inHierarchical": "in_hierarchical",
    "inServerName": "in_server_name",
    "inTargetOrg": "in_target_org",
    "outConfig": "out_config",
}
