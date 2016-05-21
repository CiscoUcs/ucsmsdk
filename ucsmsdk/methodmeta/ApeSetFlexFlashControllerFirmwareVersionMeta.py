"""This module contains the meta information of ApeSetFlexFlashControllerFirmwareVersion ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeSetFlexFlashControllerFirmwareVersion", "apeSetFlexFlashControllerFirmwareVersion", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_ip_addr": MethodPropertyMeta("InIpAddr", "inIpAddr", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_version": MethodPropertyMeta("InVersion", "inVersion", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inIpAddr": "in_ip_addr",
    "inVersion": "in_version",
}
