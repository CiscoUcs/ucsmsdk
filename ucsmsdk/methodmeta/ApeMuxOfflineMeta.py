"""This module contains the meta information of ApeMuxOffline ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMuxOffline", "apeMuxOffline", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_ch_id": MethodPropertyMeta("InChId", "inChId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_mux_slot_id": MethodPropertyMeta("InMuxSlotId", "inMuxSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inChId": "in_ch_id",
    "inMuxSlotId": "in_mux_slot_id",
}
