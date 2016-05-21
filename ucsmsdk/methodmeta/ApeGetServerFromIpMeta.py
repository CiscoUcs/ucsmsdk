"""This module contains the meta information of ApeGetServerFromIp ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeGetServerFromIp", "apeGetServerFromIp", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_ip_addr": MethodPropertyMeta("InIpAddr", "inIpAddr", "AddressIPv4", "Version142b", "Input", False),
    "out_chassis_id": MethodPropertyMeta("OutChassisId", "outChassisId", "Xs:string", "Version142b", "Output", False),
    "out_server_instance_id": MethodPropertyMeta("OutServerInstanceId", "outServerInstanceId", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_slot_id": MethodPropertyMeta("OutSlotId", "outSlotId", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inIpAddr": "in_ip_addr",
    "outChassisId": "out_chassis_id",
    "outServerInstanceId": "out_server_instance_id",
    "outSlotId": "out_slot_id",
}
