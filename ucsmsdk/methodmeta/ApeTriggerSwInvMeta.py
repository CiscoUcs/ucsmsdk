"""This module contains the meta information of ApeTriggerSwInv ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeTriggerSwInv", "apeTriggerSwInv", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_model": MethodPropertyMeta("InModel", "inModel", "Xs:string", "Version142b", "Input", False),
    "in_serial": MethodPropertyMeta("InSerial", "inSerial", "Xs:string", "Version142b", "Input", False),
    "in_sw_id": MethodPropertyMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
    "in_vendor": MethodPropertyMeta("InVendor", "inVendor", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inModel": "in_model",
    "inSerial": "in_serial",
    "inSwId": "in_sw_id",
    "inVendor": "in_vendor",
}
