"""This module contains the meta information of ConfigResolveContext ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveContext", "configResolveContext", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_context": MethodPropertyMeta("InContext", "inContext", "Xs:unsignedLong", "Version142b", "Input", False),
    "in_size": MethodPropertyMeta("InSize", "inSize", "Xs:unsignedShort", "Version142b", "Input", False),
    "out_context": MethodPropertyMeta("OutContext", "outContext", "Xs:unsignedLong", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inContext": "in_context",
    "inSize": "in_size",
    "outContext": "out_context",
}
