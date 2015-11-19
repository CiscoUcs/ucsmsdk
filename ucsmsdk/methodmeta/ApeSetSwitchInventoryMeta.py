"""This module contains the meta information of ApeSetSwitchInventory ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeSetSwitchInventory", "apeSetSwitchInventory", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_sw_id": MethodPropertyMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inSwId": "in_sw_id",
}

