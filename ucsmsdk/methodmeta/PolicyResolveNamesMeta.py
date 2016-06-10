"""This module contains the meta information of PolicyResolveNames ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("PolicyResolveNames", "policyResolveNames", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_client_connector_dn": MethodPropertyMeta("InClientConnectorDn", "inClientConnectorDn", "ReferenceObject", "Version142b", "Input", False),
    "in_context": MethodPropertyMeta("InContext", "inContext", "ReferenceObject", "Version142b", "Input", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_policy_type": MethodPropertyMeta("InPolicyType", "inPolicyType", "Xs:string", "Version142b", "Input", False),
    "out_policy_names": MethodPropertyMeta("OutPolicyNames", "outPolicyNames", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inClientConnectorDn": "in_client_connector_dn",
    "inContext": "in_context",
    "inFilter": "in_filter",
    "inPolicyType": "in_policy_type",
    "outPolicyNames": "out_policy_names",
}
