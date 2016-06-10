"""This module contains the meta information of ApeDeleteVMVnic ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeDeleteVMVnic", "apeDeleteVMVnic", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_vnic_dn": MethodPropertyMeta("InVnicDn", "inVnicDn", "ReferenceObject", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inVnicDn": "in_vnic_dn",
}
