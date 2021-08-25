"""This module contains the meta information of AaaLogin ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaLogin", "aaaLogin", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_name": MethodPropertyMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
    "in_password": MethodPropertyMeta("InPassword", "inPassword", "Xs:string", "Version142b", "Input", False),
    "out_channel": MethodPropertyMeta("OutChannel", "outChannel", "Xs:string", "Version142b", "Output", False),
    "out_cookie": MethodPropertyMeta("OutCookie", "outCookie", "Xs:string", "Version142b", "Output", False),
    "out_domains": MethodPropertyMeta("OutDomains", "outDomains", "Xs:string", "Version142b", "Output", False),
    "out_evt_channel": MethodPropertyMeta("OutEvtChannel", "outEvtChannel", "Xs:string", "Version142b", "Output", False),
    "out_name": MethodPropertyMeta("OutName", "outName", "Xs:string", "Version142b", "Output", False),
    "out_passwd_expiry_duration": MethodPropertyMeta("OutPasswdExpiryDuration", "outPasswdExpiryDuration", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_passwd_expiry_status": MethodPropertyMeta("OutPasswdExpiryStatus", "outPasswdExpiryStatus", "Xs:string", "Version142b", "Output", False),
    "out_priv": MethodPropertyMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
    "out_refresh_period": MethodPropertyMeta("OutRefreshPeriod", "outRefreshPeriod", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_session_id": MethodPropertyMeta("OutSessionId", "outSessionId", "Xs:string", "Version142b", "Output", False),
    "out_version": MethodPropertyMeta("OutVersion", "outVersion", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inName": "in_name",
    "inPassword": "in_password",
    "outChannel": "out_channel",
    "outCookie": "out_cookie",
    "outDomains": "out_domains",
    "outEvtChannel": "out_evt_channel",
    "outName": "out_name",
    "outPasswdExpiryDuration": "out_passwd_expiry_duration",
    "outPasswdExpiryStatus": "out_passwd_expiry_status",
    "outPriv": "out_priv",
    "outRefreshPeriod": "out_refresh_period",
    "outSessionId": "out_session_id",
    "outVersion": "out_version",
}
