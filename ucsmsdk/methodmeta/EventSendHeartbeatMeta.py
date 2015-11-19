"""This module contains the meta information of EventSendHeartbeat ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("EventSendHeartbeat", "eventSendHeartbeat", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "out_system_time": MethodPropertyMeta("OutSystemTime", "outSystemTime", "DateTime", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "outSystemTime": "out_system_time",
}

