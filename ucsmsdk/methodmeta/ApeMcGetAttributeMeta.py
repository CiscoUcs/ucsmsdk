"""This module contains the meta information of ApeMcGetAttribute ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeMcGetAttribute", "apeMcGetAttribute", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_attribute_ids": MethodPropertyMeta("InAttributeIds", "inAttributeIds", "IdSet", "Version142b", "Input", True),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
    "out_attribute_vals": MethodPropertyMeta("OutAttributeVals", "outAttributeVals", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inAttributeIds": "in_attribute_ids",
    "inMcIp": "in_mc_ip",
    "outAttributeVals": "out_attribute_vals",
}

