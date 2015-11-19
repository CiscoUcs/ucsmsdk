"""This module contains the meta information of ApeInsertNewFex ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeInsertNewFex", "apeInsertNewFex", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_is_refresh": MethodPropertyMeta("InIsRefresh", "inIsRefresh", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_sw_id": MethodPropertyMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
    "in_sw_port_id": MethodPropertyMeta("InSwPortId", "inSwPortId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_sw_slot_id": MethodPropertyMeta("InSwSlotId", "inSwSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inIsRefresh": "in_is_refresh",
    "inSwId": "in_sw_id",
    "inSwPortId": "in_sw_port_id",
    "inSwSlotId": "in_sw_slot_id",
}

