"""This module contains the meta information of ConfigCheckConformance ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigCheckConformance", "configCheckConformance", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "out_conf_dns": MethodPropertyMeta("OutConfDns", "outConfDns", "DnSet", "Version142b", "Output", True),
    "out_in_progress_dns": MethodPropertyMeta("OutInProgressDns", "outInProgressDns", "DnSet", "Version142b", "Output", True),
    "out_non_conf_dns": MethodPropertyMeta("OutNonConfDns", "outNonConfDns", "DnSet", "Version142b", "Output", True),
    "out_non_upgradable_dns": MethodPropertyMeta("OutNonUpgradableDns", "outNonUpgradableDns", "DnSet", "Version142b", "Output", True),
    "out_to_reset_dns": MethodPropertyMeta("OutToResetDns", "outToResetDns", "DnSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "outConfDns": "out_conf_dns",
    "outInProgressDns": "out_in_progress_dns",
    "outNonConfDns": "out_non_conf_dns",
    "outNonUpgradableDns": "out_non_upgradable_dns",
    "outToResetDns": "out_to_reset_dns",
}
