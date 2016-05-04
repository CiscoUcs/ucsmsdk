"""This module contains the meta information of ConfigEstimateImpact ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigEstimateImpact", "configEstimateImpact", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_configs": MethodPropertyMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
    "out_ackables": MethodPropertyMeta("OutAckables", "outAckables", "ConfigMap", "Version142b", "Output", True),
    "out_affected": MethodPropertyMeta("OutAffected", "outAffected", "ConfigMap", "Version142b", "Output", True),
    "out_old_ackables": MethodPropertyMeta("OutOldAckables", "outOldAckables", "ConfigMap", "Version142b", "Output", True),
    "out_old_affected": MethodPropertyMeta("OutOldAffected", "outOldAffected", "ConfigMap", "Version142b", "Output", True),
    "out_retry": MethodPropertyMeta("OutRetry", "outRetry", "Xs:unsignedShort", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfigs": "in_configs",
    "outAckables": "out_ackables",
    "outAffected": "out_affected",
    "outOldAckables": "out_old_ackables",
    "outOldAffected": "out_old_affected",
    "outRetry": "out_retry",
}
