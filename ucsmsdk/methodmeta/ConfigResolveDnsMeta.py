"""This module contains the meta information of ConfigResolveDns ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveDns", "configResolveDns", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dns": MethodPropertyMeta("InDns", "inDns", "DnSet", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
    "out_unresolved": MethodPropertyMeta("OutUnresolved", "outUnresolved", "DnSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inDns": "in_dns",
    "inHierarchical": "in_hierarchical",
    "outConfigs": "out_configs",
    "outUnresolved": "out_unresolved",
}
