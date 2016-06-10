"""This module contains the meta information of ConfigFindHostPackDependencies ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigFindHostPackDependencies", "configFindHostPackDependencies", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_host_pack_dns": MethodPropertyMeta("InHostPackDns", "inHostPackDns", "DnSet", "Version142b", "Input", True),
    "out_config_set": MethodPropertyMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inHostPackDns": "in_host_pack_dns",
    "outConfigSet": "out_config_set",
}
