"""This module contains the meta information of ConfigGetRemotePolicies ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

