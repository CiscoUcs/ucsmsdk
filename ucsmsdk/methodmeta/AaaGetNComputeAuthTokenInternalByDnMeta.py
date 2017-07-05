"""This module contains the meta information of AaaGetNComputeAuthTokenInternalByDn ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetNComputeAuthTokenInternalByDn", "aaaGetNComputeAuthTokenInternalByDn", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dn": MethodPropertyMeta("InDn", "inDn", "Xs:string", "Version142b", "Input", False),
    "in_id": MethodPropertyMeta("InId", "inId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_ipv4": MethodPropertyMeta("InIpv4", "inIpv4", "Xs:string", "Version142b", "Input", False),
    "in_locales": MethodPropertyMeta("InLocales", "inLocales", "Xs:string", "Version142b", "Input", False),
    "in_number_of": MethodPropertyMeta("InNumberOf", "inNumberOf", "Xs:unsignedByte", "Version142b", "Input", False),
    "in_parent_sess": MethodPropertyMeta("InParentSess", "inParentSess", "Xs:string", "Version142b", "Input", False),
    "in_priv": MethodPropertyMeta("InPriv", "inPriv", "Xs:string", "Version142b", "Input", False),
    "in_remote": MethodPropertyMeta("InRemote", "inRemote", "Xs:string", "Version142b", "Input", False),
    "in_role_list": MethodPropertyMeta("InRoleList", "inRoleList", "Xs:string", "Version142b", "Input", False),
    "in_user": MethodPropertyMeta("InUser", "inUser", "Xs:string", "Version142b", "Input", False),
    "out_out_user": MethodPropertyMeta("OutOutUser", "outOutUser", "Xs:string", "Version142b", "Output", False),
    "out_tokens": MethodPropertyMeta("OutTokens", "outTokens", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inDn": "in_dn",
    "inId": "in_id",
    "inIpv4": "in_ipv4",
    "inLocales": "in_locales",
    "inNumberOf": "in_number_of",
    "inParentSess": "in_parent_sess",
    "inPriv": "in_priv",
    "inRemote": "in_remote",
    "inRoleList": "in_role_list",
    "inUser": "in_user",
    "outOutUser": "out_out_user",
    "outTokens": "out_tokens",
}
