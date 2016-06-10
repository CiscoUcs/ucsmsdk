"""This module contains the meta information of EquipmentTemplatise ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EquipmentTemplatise", "equipmentTemplatise", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_target_org": MethodPropertyMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
    "in_template_name": MethodPropertyMeta("InTemplateName", "inTemplateName", "Xs:string", "Version142b", "Input", False),
    "in_template_type": MethodPropertyMeta("InTemplateType", "inTemplateType", "Xs:string", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inHierarchical": "in_hierarchical",
    "inTargetOrg": "in_target_org",
    "inTemplateName": "in_template_name",
    "inTemplateType": "in_template_type",
    "outConfig": "out_config",
}
