"""This module contains the meta information of EventSendEvent ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventSendEvent", "eventSendEvent", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dn": MethodPropertyMeta("InDn", "inDn", "Xs:string", "Version142b", "Input", False),
    "in_event": MethodPropertyMeta("InEvent", "inEvent", "Method", "Version142b", "Input", True),
    "in_req_id": MethodPropertyMeta("InReqId", "inReqId", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inDn": "in_dn",
    "inEvent": "in_event",
    "inReqId": "in_req_id",
}
