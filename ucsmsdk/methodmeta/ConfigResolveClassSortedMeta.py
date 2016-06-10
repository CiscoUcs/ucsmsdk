"""This module contains the meta information of ConfigResolveClassSorted ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveClassSorted", "configResolveClassSorted", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_size": MethodPropertyMeta("InSize", "inSize", "Xs:unsignedShort", "Version142b", "Input", False),
    "out_context": MethodPropertyMeta("OutContext", "outContext", "Xs:unsignedLong", "Version142b", "Output", False),
    "out_total_size": MethodPropertyMeta("OutTotalSize", "outTotalSize", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "inFilter": "in_filter",
    "inHierarchical": "in_hierarchical",
    "inSize": "in_size",
    "outContext": "out_context",
    "outTotalSize": "out_total_size",
}
