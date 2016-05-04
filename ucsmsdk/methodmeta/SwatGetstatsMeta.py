"""This module contains the meta information of SwatGetstats ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("SwatGetstats", "swatGetstats", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "outConfigs": "out_configs",
}
