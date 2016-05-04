"""This module contains the meta information of ApeBootPnuOs ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeBootPnuOs", "apeBootPnuOs", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
}
