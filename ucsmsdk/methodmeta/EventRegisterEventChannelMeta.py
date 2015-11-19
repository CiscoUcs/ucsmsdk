"""This module contains the meta information of EventRegisterEventChannel ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

