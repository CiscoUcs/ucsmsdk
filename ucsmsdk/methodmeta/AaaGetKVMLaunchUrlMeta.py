"""This module contains the meta information of AaaGetKVMLaunchUrl ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetKVMLaunchUrl", "aaaGetKVMLaunchUrl", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_cookie": MethodPropertyMeta("InCookie", "inCookie", "Xs:string", "Version142b", "Input", False),
    "in_ipv4": MethodPropertyMeta("InIpv4", "inIpv4", "Xs:string", "Version142b", "Input", False),
    "out_url": MethodPropertyMeta("OutUrl", "outUrl", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inCookie": "in_cookie",
    "inIpv4": "in_ipv4",
    "outUrl": "out_url",
}
