"""This module contains the meta information of ApeMcGet ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMcGet", "apeMcGet", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_mc_address": MethodPropertyMeta("InMcAddress", "inMcAddress", "AddressIPv4", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inMcAddress": "in_mc_address",
    "outConfigs": "out_configs",
}
