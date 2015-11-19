"""This module contains the meta information of FaultAckFault ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("FaultAckFault", "faultAckFault", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_id": MethodPropertyMeta("InId", "inId", "Xs:unsignedLong", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inId": "in_id",
}

