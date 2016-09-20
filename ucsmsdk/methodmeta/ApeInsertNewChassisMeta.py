"""This module contains the meta information of ApeInsertNewChassis ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeInsertNewChassis", "apeInsertNewChassis", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_device_primary_key": MethodPropertyMeta("InDevicePrimaryKey", "inDevicePrimaryKey", "Xs:string", "Version142b", "Input", False),
    "in_model": MethodPropertyMeta("InModel", "inModel", "Xs:string", "Version142b", "Input", False),
    "in_peer_type": MethodPropertyMeta("InPeerType", "inPeerType", "Xs:string", "Version142b", "Input", False),
    "in_serial": MethodPropertyMeta("InSerial", "inSerial", "Xs:string", "Version142b", "Input", False),
    "in_vendor": MethodPropertyMeta("InVendor", "inVendor", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inDevicePrimaryKey": "in_device_primary_key",
    "inModel": "in_model",
    "inPeerType": "in_peer_type",
    "inSerial": "in_serial",
    "inVendor": "in_vendor",
}
