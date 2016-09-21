"""This module contains the meta information of ApeGetInventoryFromStorageRegistrar ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeGetInventoryFromStorageRegistrar", "apeGetInventoryFromStorageRegistrar", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_disk_model": MethodPropertyMeta("InDiskModel", "inDiskModel", "Xs:string", "Version142b", "Input", False),
    "in_disk_serial": MethodPropertyMeta("InDiskSerial", "inDiskSerial", "Xs:string", "Version142b", "Input", False),
    "in_disk_vendor": MethodPropertyMeta("InDiskVendor", "inDiskVendor", "Xs:string", "Version142b", "Input", False),
    "out_controllers_assigned": MethodPropertyMeta("OutControllersAssigned", "outControllersAssigned", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inDiskModel": "in_disk_model",
    "inDiskSerial": "in_disk_serial",
    "inDiskVendor": "in_disk_vendor",
    "outControllersAssigned": "out_controllers_assigned",
}
