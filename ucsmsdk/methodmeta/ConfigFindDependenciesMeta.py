"""This module contains the meta information of ConfigFindDependencies ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigFindDependencies", "configFindDependencies", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_return_configs": MethodPropertyMeta("InReturnConfigs", "inReturnConfigs", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
    "out_has_dep": MethodPropertyMeta("OutHasDep", "outHasDep", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inReturnConfigs": "in_return_configs",
    "outConfigs": "out_configs",
    "outHasDep": "out_has_dep",
}
