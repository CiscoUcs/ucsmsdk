"""This module contains the meta information of ApeDeleteSfish ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeDeleteSfish", "apeDeleteSfish", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_vm_switch_dn": MethodPropertyMeta("InVmSwitchDn", "inVmSwitchDn", "ReferenceObject", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inVmSwitchDn": "in_vm_switch_dn",
}

