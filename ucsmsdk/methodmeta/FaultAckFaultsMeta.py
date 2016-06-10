"""This module contains the meta information of FaultAckFaults ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FaultAckFaults", "faultAckFaults", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_ids": MethodPropertyMeta("InIds", "inIds", "IdSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inIds": "in_ids",
}
