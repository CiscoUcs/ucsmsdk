"""This module contains the meta information of ApeMcGetSdr ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMcGetSdr", "apeMcGetSdr", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
    "in_sdr_ids": MethodPropertyMeta("InSdrIds", "inSdrIds", "IdSet", "Version142b", "Input", True),
    "out_sdr_vals": MethodPropertyMeta("OutSdrVals", "outSdrVals", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inMcIp": "in_mc_ip",
    "inSdrIds": "in_sdr_ids",
    "outSdrVals": "out_sdr_vals",
}
