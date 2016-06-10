"""This module contains the meta information of ApeRemoveDevice ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeRemoveDevice", "apeRemoveDevice", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_serial": MethodPropertyMeta("InSerial", "inSerial", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inSerial": "in_serial",
}
