"""This module contains the meta information of ConfigRefreshIdentity ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigRefreshIdentity", "configRefreshIdentity", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_id_type": MethodPropertyMeta("InIdType", "inIdType", "Xs:string", "Version142b", "Input", False),
    "in_is_discard_mode": MethodPropertyMeta("InIsDiscardMode", "inIsDiscardMode", "Xs:string", "Version142b", "Input", False),
    "out_ackables": MethodPropertyMeta("OutAckables", "outAckables", "ConfigMap", "Version142b", "Output", True),
    "out_affected": MethodPropertyMeta("OutAffected", "outAffected", "ConfigMap", "Version142b", "Output", True),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
    "out_old_ackables": MethodPropertyMeta("OutOldAckables", "outOldAckables", "ConfigMap", "Version142b", "Output", True),
    "out_old_affected": MethodPropertyMeta("OutOldAffected", "outOldAffected", "ConfigMap", "Version142b", "Output", True),
    "out_retry": MethodPropertyMeta("OutRetry", "outRetry", "Xs:unsignedShort", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inHierarchical": "in_hierarchical",
    "inIdType": "in_id_type",
    "inIsDiscardMode": "in_is_discard_mode",
    "outAckables": "out_ackables",
    "outAffected": "out_affected",
    "outConfig": "out_config",
    "outOldAckables": "out_old_ackables",
    "outOldAffected": "out_old_affected",
    "outRetry": "out_retry",
}
