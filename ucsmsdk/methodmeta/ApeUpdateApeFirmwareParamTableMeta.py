"""This module contains the meta information of ApeUpdateApeFirmwareParamTable ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeUpdateApeFirmwareParamTable", "apeUpdateApeFirmwareParamTable", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_field_name": MethodPropertyMeta("InFieldName", "inFieldName", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_ip_addr": MethodPropertyMeta("InIpAddr", "inIpAddr", "AddressIPv4", "Version142b", "Input", False),
    "in_version": MethodPropertyMeta("InVersion", "inVersion", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inFieldName": "in_field_name",
    "inIpAddr": "in_ip_addr",
    "inVersion": "in_version",
}
