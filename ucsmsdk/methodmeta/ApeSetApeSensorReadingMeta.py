"""This module contains the meta information of ApeSetApeSensorReading ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeSetApeSensorReading", "apeSetApeSensorReading", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_chassis_id": MethodPropertyMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_fault_level": MethodPropertyMeta("InFaultLevel", "inFaultLevel", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_instance_id": MethodPropertyMeta("InInstanceId", "inInstanceId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_operation": MethodPropertyMeta("InOperation", "inOperation", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_sensor_name": MethodPropertyMeta("InSensorName", "inSensorName", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_slot_id": MethodPropertyMeta("InSlotId", "inSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inChassisId": "in_chassis_id",
    "inFaultLevel": "in_fault_level",
    "inInstanceId": "in_instance_id",
    "inOperation": "in_operation",
    "inSensorName": "in_sensor_name",
    "inSlotId": "in_slot_id",
}
