"""This module contains the meta information of AaaGetAuthTokenClient ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetAuthTokenClient", "aaaGetAuthTokenClient", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_cookie": MethodPropertyMeta("InCookie", "inCookie", "Xs:string", "Version142b", "Input", False),
    "out_tokens": MethodPropertyMeta("OutTokens", "outTokens", "Xs:string", "Version142b", "Output", False),
    "out_user": MethodPropertyMeta("OutUser", "outUser", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inCookie": "in_cookie",
    "outTokens": "out_tokens",
    "outUser": "out_user",
}
