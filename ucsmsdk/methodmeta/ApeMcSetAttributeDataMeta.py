"""This module contains the meta information of ApeMcSetAttributeData ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMcSetAttributeData", "apeMcSetAttributeData", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_action": MethodPropertyMeta("InAction", "inAction", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inAction": "in_action",
    "inConfig": "in_config",
    "inMcIp": "in_mc_ip",
}
