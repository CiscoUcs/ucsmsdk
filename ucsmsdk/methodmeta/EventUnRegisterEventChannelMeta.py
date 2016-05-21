"""This module contains the meta information of EventUnRegisterEventChannel ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventUnRegisterEventChannel", "eventUnRegisterEventChannel", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dn": MethodPropertyMeta("InDn", "inDn", "Xs:string", "Version142b", "Input", False),
    "in_req_id": MethodPropertyMeta("InReqID", "inReqID", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inDn": "in_dn",
    "inReqID": "in_req_id",
}
