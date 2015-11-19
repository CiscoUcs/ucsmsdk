"""This module contains the meta information of FaultResolveFault ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

