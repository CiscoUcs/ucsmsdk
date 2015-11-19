"""This module contains the meta information of EventUnRegisterEventChannel ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

