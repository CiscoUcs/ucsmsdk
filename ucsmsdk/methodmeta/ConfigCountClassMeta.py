"""This module contains the meta information of ConfigCountClass ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigCountClass", "configCountClass", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "out_count": MethodPropertyMeta("OutCount", "outCount", "Xs:unsignedLong", "Version142b", "Output", False),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "inFilter": "in_filter",
    "inHierarchical": "in_hierarchical",
    "outCount": "out_count",
}
