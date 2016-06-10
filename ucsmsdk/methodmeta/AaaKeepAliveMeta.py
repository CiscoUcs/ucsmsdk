"""This module contains the meta information of AaaKeepAlive ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaKeepAlive", "aaaKeepAlive", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
}

prop_map = {
    "cookie": "cookie",
}
