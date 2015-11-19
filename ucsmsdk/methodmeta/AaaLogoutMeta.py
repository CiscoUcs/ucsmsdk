"""This module contains the meta information of AaaLogout ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("AaaLogout", "aaaLogout", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_cookie": MethodPropertyMeta("InCookie", "inCookie", "Xs:string", "Version142b", "Input", False),
    "in_delay_secs": MethodPropertyMeta("InDelaySecs", "inDelaySecs", "Xs:unsignedInt", "Version142b", "Input", False),
    "out_status": MethodPropertyMeta("OutStatus", "outStatus", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inCookie": "in_cookie",
    "inDelaySecs": "in_delay_secs",
    "outStatus": "out_status",
}

