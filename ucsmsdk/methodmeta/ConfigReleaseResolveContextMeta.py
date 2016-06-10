"""This module contains the meta information of ConfigReleaseResolveContext ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigReleaseResolveContext", "configReleaseResolveContext", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_context": MethodPropertyMeta("InContext", "inContext", "Xs:unsignedLong", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inContext": "in_context",
}
