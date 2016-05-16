"""This module contains the meta information of ApeDeleteHVVnic ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeDeleteHVVnic", "apeDeleteHVVnic", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_vnic_dn": MethodPropertyMeta("InVnicDn", "inVnicDn", "ReferenceObject", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inVnicDn": "in_vnic_dn",
}
