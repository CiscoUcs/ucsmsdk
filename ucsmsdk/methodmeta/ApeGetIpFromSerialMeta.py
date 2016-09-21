"""This module contains the meta information of ApeGetIpFromSerial ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeGetIpFromSerial", "apeGetIpFromSerial", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_equipment_serial": MethodPropertyMeta("InEquipmentSerial", "inEquipmentSerial", "Xs:string", "Version142b", "Input", False),
    "out_ip_addr": MethodPropertyMeta("OutIpAddr", "outIpAddr", "AddressIPv4", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inEquipmentSerial": "in_equipment_serial",
    "outIpAddr": "out_ip_addr",
}
