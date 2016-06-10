"""This module contains the meta information of ApeIssueChassisId ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeIssueChassisId", "apeIssueChassisId", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_sw_id": MethodPropertyMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inSwId": "in_sw_id",
}
