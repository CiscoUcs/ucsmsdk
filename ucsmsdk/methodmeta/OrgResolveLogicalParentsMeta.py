"""This module contains the meta information of OrgResolveLogicalParents ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("OrgResolveLogicalParents", "orgResolveLogicalParents", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_single_level": MethodPropertyMeta("InSingleLevel", "inSingleLevel", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigMap", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inHierarchical": "in_hierarchical",
    "inSingleLevel": "in_single_level",
    "outConfigs": "out_configs",
}

