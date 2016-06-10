"""This module contains the meta information of MethodVessel ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("MethodVessel", "methodVessel", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_stimuli": MethodPropertyMeta("InStimuli", "inStimuli", "MethodSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inStimuli": "in_stimuli",
}
