"""This module contains the meta information of ApeSetFlexFlashVirtualRaidInformation ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeSetFlexFlashVirtualRaidInformation", "apeSetFlexFlashVirtualRaidInformation", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_conrtoller_id": MethodPropertyMeta("InConrtollerId", "inConrtollerId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_ip_addr": MethodPropertyMeta("InIpAddr", "inIpAddr", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_raid_health": MethodPropertyMeta("InRaidHealth", "inRaidHealth", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_raid_state": MethodPropertyMeta("InRaidState", "inRaidState", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inConrtollerId": "in_conrtoller_id",
    "inIpAddr": "in_ip_addr",
    "inRaidHealth": "in_raid_health",
    "inRaidState": "in_raid_state",
}
