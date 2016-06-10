"""This module contains the meta information of ApeUpdateApeFirmwareActiveSide ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeUpdateApeFirmwareActiveSide", "apeUpdateApeFirmwareActiveSide", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_field_name": MethodPropertyMeta("InFieldName", "inFieldName", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_ip_addr": MethodPropertyMeta("InIpAddr", "inIpAddr", "AddressIPv4", "Version142b", "Input", False),
    "in_side": MethodPropertyMeta("InSide", "inSide", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inFieldName": "in_field_name",
    "inIpAddr": "in_ip_addr",
    "inSide": "in_side",
}
