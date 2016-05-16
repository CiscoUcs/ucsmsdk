"""This module contains the meta information of ApeMcGetAttributeData ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMcGetAttributeData", "apeMcGetAttributeData", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_attribute_id": MethodPropertyMeta("InAttributeId", "inAttributeId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
    "out_attribute_vals": MethodPropertyMeta("OutAttributeVals", "outAttributeVals", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inAttributeId": "in_attribute_id",
    "inMcIp": "in_mc_ip",
    "outAttributeVals": "out_attribute_vals",
}
