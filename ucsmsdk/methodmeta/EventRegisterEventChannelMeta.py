"""This module contains the meta information of EventRegisterEventChannel ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventRegisterEventChannel", "eventRegisterEventChannel", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dn": MethodPropertyMeta("InDn", "inDn", "Xs:string", "Version142b", "Input", False),
    "out_req_id": MethodPropertyMeta("OutReqID", "outReqID", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inDn": "in_dn",
    "outReqID": "out_req_id",
}
