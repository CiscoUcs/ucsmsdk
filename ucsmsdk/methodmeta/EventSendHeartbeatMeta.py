"""This module contains the meta information of EventSendHeartbeat ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventSendHeartbeat", "eventSendHeartbeat", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "out_system_time": MethodPropertyMeta("OutSystemTime", "outSystemTime", "DateTime", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "outSystemTime": "out_system_time",
}
