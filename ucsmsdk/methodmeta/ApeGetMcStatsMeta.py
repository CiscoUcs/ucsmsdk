"""This module contains the meta information of ApeGetMcStats ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeGetMcStats", "apeGetMcStats", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_equipment_serial": MethodPropertyMeta("InEquipmentSerial", "inEquipmentSerial", "Xs:string", "Version142b", "Input", False),
    "out_mc_stats": MethodPropertyMeta("OutMcStats", "outMcStats", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inEquipmentSerial": "in_equipment_serial",
    "outMcStats": "out_mc_stats",
}
