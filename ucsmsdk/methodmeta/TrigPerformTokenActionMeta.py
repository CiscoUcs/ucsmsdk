"""This module contains the meta information of TrigPerformTokenAction ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("TrigPerformTokenAction", "trigPerformTokenAction", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_context": MethodPropertyMeta("InContext", "inContext", "ReferenceObject", "Version142b", "Input", False),
    "in_ownership": MethodPropertyMeta("InOwnership", "inOwnership", "Xs:string", "Version142b", "Input", False),
    "in_sched_name": MethodPropertyMeta("InSchedName", "inSchedName", "Xs:string", "Version142b", "Input", False),
    "in_token_action": MethodPropertyMeta("InTokenAction", "inTokenAction", "Xs:string", "Version142b", "Input", False),
    "in_token_id": MethodPropertyMeta("InTokenId", "inTokenId", "Xs:unsignedLong", "Version142b", "Input", False),
    "in_triggerable_dn": MethodPropertyMeta("InTriggerableDn", "inTriggerableDn", "ReferenceObject", "Version142b", "Input", False),
    "in_window_name": MethodPropertyMeta("InWindowName", "inWindowName", "Xs:string", "Version142b", "Input", False),
    "in_window_type": MethodPropertyMeta("InWindowType", "inWindowType", "Xs:string", "Version142b", "Input", False),
    "out_last_token_operation": MethodPropertyMeta("OutLastTokenOperation", "outLastTokenOperation", "Xs:string", "Version142b", "Output", False),
    "out_new_token_id": MethodPropertyMeta("OutNewTokenId", "outNewTokenId", "Xs:unsignedLong", "Version142b", "Output", False),
    "out_old_token_id": MethodPropertyMeta("OutOldTokenId", "outOldTokenId", "Xs:unsignedLong", "Version142b", "Output", False),
    "out_old_triggerable_dn": MethodPropertyMeta("OutOldTriggerableDn", "outOldTriggerableDn", "ReferenceObject", "Version142b", "Output", False),
    "out_ownership": MethodPropertyMeta("OutOwnership", "outOwnership", "Xs:string", "Version142b", "Output", False),
    "out_window_name": MethodPropertyMeta("OutWindowName", "outWindowName", "Xs:string", "Version142b", "Output", False),
    "out_window_type": MethodPropertyMeta("OutWindowType", "outWindowType", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inContext": "in_context",
    "inOwnership": "in_ownership",
    "inSchedName": "in_sched_name",
    "inTokenAction": "in_token_action",
    "inTokenId": "in_token_id",
    "inTriggerableDn": "in_triggerable_dn",
    "inWindowName": "in_window_name",
    "inWindowType": "in_window_type",
    "outLastTokenOperation": "out_last_token_operation",
    "outNewTokenId": "out_new_token_id",
    "outOldTokenId": "out_old_token_id",
    "outOldTriggerableDn": "out_old_triggerable_dn",
    "outOwnership": "out_ownership",
    "outWindowName": "out_window_name",
    "outWindowType": "out_window_type",
}
