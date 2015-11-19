"""This module contains the meta information of AaaCheckComputeExtAccess ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("AaaCheckComputeExtAccess", "aaaCheckComputeExtAccess", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dn": MethodPropertyMeta("InDn", "inDn", "ReferenceObject", "Version142b", "Input", False),
    "in_user": MethodPropertyMeta("InUser", "inUser", "Xs:string", "Version142b", "Input", False),
    "out_allow": MethodPropertyMeta("OutAllow", "outAllow", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inDn": "in_dn",
    "inUser": "in_user",
    "outAllow": "out_allow",
}

