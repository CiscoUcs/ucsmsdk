"""This module contains the meta information of ConfigCheckFirmwareUpdatable ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigCheckFirmwareUpdatable", "configCheckFirmwareUpdatable", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_updatable_dns": MethodPropertyMeta("InUpdatableDns", "inUpdatableDns", "DnSet", "Version142b", "Input", True),
    "out_fail_dns": MethodPropertyMeta("OutFailDns", "outFailDns", "DnSet", "Version142b", "Output", True),
    "out_invalid_dns": MethodPropertyMeta("OutInvalidDns", "outInvalidDns", "DnSet", "Version142b", "Output", True),
    "out_pass_dns": MethodPropertyMeta("OutPassDns", "outPassDns", "DnSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inUpdatableDns": "in_updatable_dns",
    "outFailDns": "out_fail_dns",
    "outInvalidDns": "out_invalid_dns",
    "outPassDns": "out_pass_dns",
}
