"""This module contains the meta information of ConfigMoChangeEvent ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigMoChangeEvent", "configMoChangeEvent", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_eid": MethodPropertyMeta("InEid", "inEid", "Xs:unsignedLong", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inEid": "in_eid",
}
