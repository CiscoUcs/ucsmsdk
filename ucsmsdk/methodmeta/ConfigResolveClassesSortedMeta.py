"""This module contains the meta information of ConfigResolveClassesSorted ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveClassesSorted", "configResolveClassesSorted", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_ids": MethodPropertyMeta("InIds", "inIds", "ClassIdSet", "Version142b", "Input", True),
    "in_size": MethodPropertyMeta("InSize", "inSize", "Xs:unsignedShort", "Version142b", "Input", False),
    "out_context": MethodPropertyMeta("OutContext", "outContext", "Xs:unsignedLong", "Version142b", "Output", False),
    "out_total_size": MethodPropertyMeta("OutTotalSize", "outTotalSize", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inHierarchical": "in_hierarchical",
    "inIds": "in_ids",
    "inSize": "in_size",
    "outContext": "out_context",
    "outTotalSize": "out_total_size",
}
