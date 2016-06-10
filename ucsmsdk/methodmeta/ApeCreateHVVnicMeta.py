"""This module contains the meta information of ApeCreateHVVnic ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeCreateHVVnic", "apeCreateHVVnic", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_blade_slot_id": MethodPropertyMeta("InBladeSlotId", "inBladeSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_chassis_id": MethodPropertyMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_sw_id": MethodPropertyMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inBladeSlotId": "in_blade_slot_id",
    "inChassisId": "in_chassis_id",
    "inConfig": "in_config",
    "inSwId": "in_sw_id",
}
