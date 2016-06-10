"""This module contains the meta information of EventUnsubscribe ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventUnsubscribe", "eventUnsubscribe", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "out_status": MethodPropertyMeta("OutStatus", "outStatus", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "outStatus": "out_status",
}
