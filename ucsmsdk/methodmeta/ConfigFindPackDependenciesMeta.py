"""This module contains the meta information of ConfigFindPackDependencies ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigFindPackDependencies", "configFindPackDependencies", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_chassis_pack_dns": MethodPropertyMeta("InChassisPackDns", "inChassisPackDns", "DnSet", "Version142b", "Input", True),
    "in_host_pack_dns": MethodPropertyMeta("InHostPackDns", "inHostPackDns", "DnSet", "Version142b", "Input", True),
    "out_config_set": MethodPropertyMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inChassisPackDns": "in_chassis_pack_dns",
    "inHostPackDns": "in_host_pack_dns",
    "outConfigSet": "out_config_set",
}
