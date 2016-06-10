"""This module contains the meta information of ConfigGetRemotePolicies ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetRemotePolicies", "configGetRemotePolicies", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_context": MethodPropertyMeta("InContext", "inContext", "ReferenceObject", "Version142b", "Input", False),
    "in_policy_digests": MethodPropertyMeta("InPolicyDigests", "inPolicyDigests", "ConfigSet", "Version142b", "Input", True),
    "in_stimulus_id": MethodPropertyMeta("InStimulusId", "inStimulusId", "Xs:unsignedLong", "Version142b", "Input", False),
    "out_policies": MethodPropertyMeta("OutPolicies", "outPolicies", "ConfigSet", "Version142b", "Output", True),
    "out_stimulus_id": MethodPropertyMeta("OutStimulusId", "outStimulusId", "Xs:unsignedLong", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inContext": "in_context",
    "inPolicyDigests": "in_policy_digests",
    "inStimulusId": "in_stimulus_id",
    "outPolicies": "out_policies",
    "outStimulusId": "out_stimulus_id",
}
