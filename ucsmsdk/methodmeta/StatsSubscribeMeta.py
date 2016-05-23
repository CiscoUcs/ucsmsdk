"""This module contains the meta information of StatsSubscribe ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("StatsSubscribe", "statsSubscribe", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_category": MethodPropertyMeta("InCategory", "inCategory", "Xs:string", "Version142b", "Input", False),
    "in_provider": MethodPropertyMeta("InProvider", "inProvider", "Xs:string", "Version142b", "Input", False),
    "in_schema_info": MethodPropertyMeta("InSchemaInfo", "inSchemaInfo", "ConfigSet", "Version142b", "Input", True),
    "in_time_interval": MethodPropertyMeta("InTimeInterval", "inTimeInterval", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inCategory": "in_category",
    "inProvider": "in_provider",
    "inSchemaInfo": "in_schema_info",
    "inTimeInterval": "in_time_interval",
}
