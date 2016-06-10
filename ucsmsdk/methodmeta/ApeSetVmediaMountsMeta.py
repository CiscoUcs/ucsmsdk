"""This module contains the meta information of ApeSetVmediaMounts ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeSetVmediaMounts", "apeSetVmediaMounts", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_chassis_id": MethodPropertyMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_count": MethodPropertyMeta("InCount", "inCount", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_server_instance_id": MethodPropertyMeta("InServerInstanceId", "inServerInstanceId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_slot_id": MethodPropertyMeta("InSlotId", "inSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_v_media_set": MethodPropertyMeta("InVMediaSet", "inVMediaSet", "ConfigSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inChassisId": "in_chassis_id",
    "inCount": "in_count",
    "inServerInstanceId": "in_server_instance_id",
    "inSlotId": "in_slot_id",
    "inVMediaSet": "in_v_media_set",
}
