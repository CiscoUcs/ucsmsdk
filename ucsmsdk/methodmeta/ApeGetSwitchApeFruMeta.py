"""This module contains the meta information of ApeGetSwitchApeFru ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeGetSwitchApeFru", "apeGetSwitchApeFru", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_sw_id": MethodPropertyMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
    "out_controller_id": MethodPropertyMeta("OutControllerId", "outControllerId", "Xs:string", "Version142b", "Output", False),
    "out_controller_type": MethodPropertyMeta("OutControllerType", "outControllerType", "Xs:string", "Version142b", "Output", False),
    "out_controller_vendor": MethodPropertyMeta("OutControllerVendor", "outControllerVendor", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inSwId": "in_sw_id",
    "outControllerId": "out_controller_id",
    "outControllerType": "out_controller_type",
    "outControllerVendor": "out_controller_vendor",
}
