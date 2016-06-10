"""This module contains the meta information of ApeMcGetBiosTokens ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMcGetBiosTokens", "apeMcGetBiosTokens", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_chassis_id": MethodPropertyMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_instance_id": MethodPropertyMeta("InInstanceId", "inInstanceId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_slot_id": MethodPropertyMeta("InSlotId", "inSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
    "out_file_path": MethodPropertyMeta("OutFilePath", "outFilePath", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inChassisId": "in_chassis_id",
    "inInstanceId": "in_instance_id",
    "inSlotId": "in_slot_id",
    "outFilePath": "out_file_path",
}
