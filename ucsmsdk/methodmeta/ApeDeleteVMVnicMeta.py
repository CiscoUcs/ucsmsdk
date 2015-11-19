"""This module contains the meta information of ApeDeleteVMVnic ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeDeleteVMVnic", "apeDeleteVMVnic", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_vnic_dn": MethodPropertyMeta("InVnicDn", "inVnicDn", "ReferenceObject", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inVnicDn": "in_vnic_dn",
}

