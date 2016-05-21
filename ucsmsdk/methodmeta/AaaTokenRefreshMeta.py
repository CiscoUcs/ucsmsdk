"""This module contains the meta information of AaaTokenRefresh ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaTokenRefresh", "aaaTokenRefresh", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_cookie": MethodPropertyMeta("InCookie", "inCookie", "Xs:string", "Version142b", "Input", False),
    "in_name": MethodPropertyMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
    "out_channel": MethodPropertyMeta("OutChannel", "outChannel", "Xs:string", "Version142b", "Output", False),
    "out_cookie": MethodPropertyMeta("OutCookie", "outCookie", "Xs:string", "Version142b", "Output", False),
    "out_domains": MethodPropertyMeta("OutDomains", "outDomains", "Xs:string", "Version142b", "Output", False),
    "out_evt_channel": MethodPropertyMeta("OutEvtChannel", "outEvtChannel", "Xs:string", "Version142b", "Output", False),
    "out_priv": MethodPropertyMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
    "out_refresh_period": MethodPropertyMeta("OutRefreshPeriod", "outRefreshPeriod", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inCookie": "in_cookie",
    "inName": "in_name",
    "outChannel": "out_channel",
    "outCookie": "out_cookie",
    "outDomains": "out_domains",
    "outEvtChannel": "out_evt_channel",
    "outPriv": "out_priv",
    "outRefreshPeriod": "out_refresh_period",
}
