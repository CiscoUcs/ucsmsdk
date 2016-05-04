"""This module contains the meta information of ApeMcGetParam ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMcGetParam", "apeMcGetParam", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
    "in_param_ids": MethodPropertyMeta("InParamIds", "inParamIds", "IdSet", "Version142b", "Input", True),
    "out_param_vals": MethodPropertyMeta("OutParamVals", "outParamVals", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inMcIp": "in_mc_ip",
    "inParamIds": "in_param_ids",
    "outParamVals": "out_param_vals",
}
