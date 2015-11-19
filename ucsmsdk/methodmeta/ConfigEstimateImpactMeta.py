"""This module contains the meta information of ConfigEstimateImpact ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

