"""This module contains the meta information of ConfigGetEstimateImpact ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetEstimateImpact", "configGetEstimateImpact", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_configs": MethodPropertyMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
    "in_deleted_dns": MethodPropertyMeta("InDeletedDns", "inDeletedDns", "DnSet", "Version142b", "Input", True),
    "in_impact_analyzer_id": MethodPropertyMeta("InImpactAnalyzerId", "inImpactAnalyzerId", "DateTime", "Version142b", "Input", False),
    "in_is_policy_full_config": MethodPropertyMeta("InIsPolicyFullConfig", "inIsPolicyFullConfig", "Xs:string", "Version142b", "Input", False),
    "in_source_connector_id": MethodPropertyMeta("InSourceConnectorId", "inSourceConnectorId", "Xs:unsignedInt", "Version142b", "Input", False),
    "out_app_impact_response": MethodPropertyMeta("OutAppImpactResponse", "outAppImpactResponse", "ConfigConfig", "Version142b", "Output", True),
    "out_retry": MethodPropertyMeta("OutRetry", "outRetry", "Xs:unsignedShort", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfigs": "in_configs",
    "inDeletedDns": "in_deleted_dns",
    "inImpactAnalyzerId": "in_impact_analyzer_id",
    "inIsPolicyFullConfig": "in_is_policy_full_config",
    "inSourceConnectorId": "in_source_connector_id",
    "outAppImpactResponse": "out_app_impact_response",
    "outRetry": "out_retry",
}
