"""This module contains the meta information of LoggingSyncOcns ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("LoggingSyncOcns", "loggingSyncOcns", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_from_or_zero": MethodPropertyMeta("InFromOrZero", "inFromOrZero", "Xs:unsignedLong", "Version142b", "Input", False),
    "in_to_or_zero": MethodPropertyMeta("InToOrZero", "inToOrZero", "Xs:unsignedLong", "Version142b", "Input", False),
    "out_stimuli": MethodPropertyMeta("OutStimuli", "outStimuli", "MethodSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inFromOrZero": "in_from_or_zero",
    "inToOrZero": "in_to_or_zero",
    "outStimuli": "out_stimuli",
}
