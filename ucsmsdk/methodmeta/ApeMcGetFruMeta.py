"""This module contains the meta information of ApeMcGetFru ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeMcGetFru", "apeMcGetFru", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_fru_ids": MethodPropertyMeta("InFruIds", "inFruIds", "IdSet", "Version142b", "Input", True),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
    "out_fru_vals": MethodPropertyMeta("OutFruVals", "outFruVals", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inFruIds": "in_fru_ids",
    "inMcIp": "in_mc_ip",
    "outFruVals": "out_fru_vals",
}

