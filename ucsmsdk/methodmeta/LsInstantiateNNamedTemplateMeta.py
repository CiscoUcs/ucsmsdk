"""This module contains the meta information of LsInstantiateNNamedTemplate ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("LsInstantiateNNamedTemplate", "lsInstantiateNNamedTemplate", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_error_on_existing": MethodPropertyMeta("InErrorOnExisting", "inErrorOnExisting", "Xs:string", "Version142b", "Input", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_name_set": MethodPropertyMeta("InNameSet", "inNameSet", "DnSet", "Version142b", "Input", True),
    "in_target_org": MethodPropertyMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inErrorOnExisting": "in_error_on_existing",
    "inHierarchical": "in_hierarchical",
    "inNameSet": "in_name_set",
    "inTargetOrg": "in_target_org",
    "outConfigs": "out_configs",
}

