"""This module contains the meta information of ApeInsertNewRack ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeInsertNewRack", "apeInsertNewRack", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_fx_id": MethodPropertyMeta("InFxId", "inFxId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_fx_port_id": MethodPropertyMeta("InFxPortId", "inFxPortId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_fx_slot_id": MethodPropertyMeta("InFxSlotId", "inFxSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_is_refresh": MethodPropertyMeta("InIsRefresh", "inIsRefresh", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inFxId": "in_fx_id",
    "inFxPortId": "in_fx_port_id",
    "inFxSlotId": "in_fx_slot_id",
    "inIsRefresh": "in_is_refresh",
}
