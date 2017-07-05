"""This module contains the meta information of AaaGetKVMLaunchUrlInternal ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetKVMLaunchUrlInternal", "aaaGetKVMLaunchUrlInternal", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_cimc_ipv4": MethodPropertyMeta("InCimcIpv4", "inCimcIpv4", "Xs:string", "Version142b", "Input", False),
    "in_ipv4": MethodPropertyMeta("InIpv4", "inIpv4", "Xs:string", "Version142b", "Input", False),
    "in_ipv6": MethodPropertyMeta("InIpv6", "inIpv6", "Xs:string", "Version142b", "Input", False),
    "in_locales": MethodPropertyMeta("InLocales", "inLocales", "Xs:string", "Version142b", "Input", False),
    "in_parent_sess": MethodPropertyMeta("InParentSess", "inParentSess", "Xs:string", "Version142b", "Input", False),
    "in_priv": MethodPropertyMeta("InPriv", "inPriv", "Xs:string", "Version142b", "Input", False),
    "in_remote": MethodPropertyMeta("InRemote", "inRemote", "Xs:string", "Version142b", "Input", False),
    "in_role_list": MethodPropertyMeta("InRoleList", "inRoleList", "Xs:string", "Version142b", "Input", False),
    "in_user": MethodPropertyMeta("InUser", "inUser", "Xs:string", "Version142b", "Input", False),
    "out_url": MethodPropertyMeta("OutUrl", "outUrl", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inCimcIpv4": "in_cimc_ipv4",
    "inIpv4": "in_ipv4",
    "inIpv6": "in_ipv6",
    "inLocales": "in_locales",
    "inParentSess": "in_parent_sess",
    "inPriv": "in_priv",
    "inRemote": "in_remote",
    "inRoleList": "in_role_list",
    "inUser": "in_user",
    "outUrl": "out_url",
}
