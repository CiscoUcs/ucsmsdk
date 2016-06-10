"""This module contains the meta information of FaultAckFault ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FaultAckFault", "faultAckFault", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_id": MethodPropertyMeta("InId", "inId", "Xs:unsignedLong", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inId": "in_id",
}
