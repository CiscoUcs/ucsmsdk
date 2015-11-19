"""This module contains the meta information of ConfigResolveDn ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ConfigResolveDn", "configResolveDn", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inHierarchical": "in_hierarchical",
    "outConfig": "out_config",
}

