"""This module contains the meta information of ApeDeleteSfish ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeDeleteSfish", "apeDeleteSfish", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_vm_switch_dn": MethodPropertyMeta("InVmSwitchDn", "inVmSwitchDn", "ReferenceObject", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inVmSwitchDn": "in_vm_switch_dn",
}
