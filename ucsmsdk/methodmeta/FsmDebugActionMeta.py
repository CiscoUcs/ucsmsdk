"""This module contains the meta information of FsmDebugAction ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FsmDebugAction", "fsmDebugAction", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_directive": MethodPropertyMeta("InDirective", "inDirective", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inDirective": "in_directive",
}
