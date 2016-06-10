"""This module contains the meta information of ApeSetMcStats ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeSetMcStats", "apeSetMcStats", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_equipment_serial": MethodPropertyMeta("InEquipmentSerial", "inEquipmentSerial", "Xs:string", "Version142b", "Input", False),
    "in_mc_stats": MethodPropertyMeta("InMcStats", "inMcStats", "ConfigSet", "Version142b", "Input", True),
    "in_stat_ids": MethodPropertyMeta("InStatIds", "inStatIds", "IdSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inEquipmentSerial": "in_equipment_serial",
    "inMcStats": "in_mc_stats",
    "inStatIds": "in_stat_ids",
}
