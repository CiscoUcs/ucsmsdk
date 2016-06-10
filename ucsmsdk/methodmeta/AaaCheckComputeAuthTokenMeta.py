"""This module contains the meta information of AaaCheckComputeAuthToken ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaCheckComputeAuthToken", "aaaCheckComputeAuthToken", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_token": MethodPropertyMeta("InToken", "inToken", "Xs:string", "Version142b", "Input", False),
    "in_user": MethodPropertyMeta("InUser", "inUser", "Xs:string", "Version142b", "Input", False),
    "out_allow": MethodPropertyMeta("OutAllow", "outAllow", "Xs:string", "Version142b", "Output", False),
    "out_auth_domain": MethodPropertyMeta("OutAuthDomain", "outAuthDomain", "Xs:string", "Version142b", "Output", False),
    "out_auth_user": MethodPropertyMeta("OutAuthUser", "outAuthUser", "Xs:string", "Version142b", "Output", False),
    "out_kvm_priv": MethodPropertyMeta("OutKvmPriv", "outKvmPriv", "Xs:string", "Version142b", "Output", False),
    "out_locales": MethodPropertyMeta("OutLocales", "outLocales", "Xs:string", "Version142b", "Output", False),
    "out_priv": MethodPropertyMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
    "out_remote": MethodPropertyMeta("OutRemote", "outRemote", "Xs:string", "Version142b", "Output", False),
    "out_v_media_priv": MethodPropertyMeta("OutVMediaPriv", "outVMediaPriv", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inToken": "in_token",
    "inUser": "in_user",
    "outAllow": "out_allow",
    "outAuthDomain": "out_auth_domain",
    "outAuthUser": "out_auth_user",
    "outKvmPriv": "out_kvm_priv",
    "outLocales": "out_locales",
    "outPriv": "out_priv",
    "outRemote": "out_remote",
    "outVMediaPriv": "out_v_media_priv",
}
