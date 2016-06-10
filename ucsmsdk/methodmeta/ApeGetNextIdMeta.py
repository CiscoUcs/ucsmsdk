"""This module contains the meta information of ApeGetNextId ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeGetNextId", "apeGetNextId", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_chassis_id": MethodPropertyMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_mo_type": MethodPropertyMeta("InMoType", "inMoType", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_server_instance_id": MethodPropertyMeta("InServerInstanceId", "inServerInstanceId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_slot_id": MethodPropertyMeta("InSlotId", "inSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
    "out_next_id": MethodPropertyMeta("OutNextId", "outNextId", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inChassisId": "in_chassis_id",
    "inMoType": "in_mo_type",
    "inServerInstanceId": "in_server_instance_id",
    "inSlotId": "in_slot_id",
    "outNextId": "out_next_id",
}
