"""This module contains the meta information of FaultResolveFault ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FaultResolveFault", "faultResolveFault", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_id": MethodPropertyMeta("InId", "inId", "Xs:unsignedLong", "Version142b", "Input", False),
    "out_fault": MethodPropertyMeta("OutFault", "outFault", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inId": "in_id",
    "outFault": "out_fault",
}
