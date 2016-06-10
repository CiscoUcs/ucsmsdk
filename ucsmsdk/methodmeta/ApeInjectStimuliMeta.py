"""This module contains the meta information of ApeInjectStimuli ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeInjectStimuli", "apeInjectStimuli", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_from_svc": MethodPropertyMeta("InFromSvc", "inFromSvc", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_stimuli": MethodPropertyMeta("InStimuli", "inStimuli", "MethodSet", "Version142b", "Input", True),
    "in_to_svc": MethodPropertyMeta("InToSvc", "inToSvc", "Xs:unsignedInt", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inFromSvc": "in_from_svc",
    "inStimuli": "in_stimuli",
    "inToSvc": "in_to_svc",
}
