"""This module contains the meta information of MethodResolveVessel ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("MethodResolveVessel", "methodResolveVessel", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_stimuli": MethodPropertyMeta("InStimuli", "inStimuli", "MethodSet", "Version142b", "Input", True),
    "out_stimuli": MethodPropertyMeta("OutStimuli", "outStimuli", "MethodSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inStimuli": "in_stimuli",
    "outStimuli": "out_stimuli",
}
