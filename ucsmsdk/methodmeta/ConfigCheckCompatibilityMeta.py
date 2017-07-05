"""This module contains the meta information of ConfigCheckCompatibility ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigCheckCompatibility", "configCheckCompatibility", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_blade_pack_version": MethodPropertyMeta("InBladePackVersion", "inBladePackVersion", "Xs:string", "Version142b", "Input", False),
    "in_detail_result": MethodPropertyMeta("InDetailResult", "inDetailResult", "Xs:string", "Version142b", "Input", False),
    "in_infra_pack_version": MethodPropertyMeta("InInfraPackVersion", "inInfraPackVersion", "Xs:string", "Version142b", "Input", False),
    "in_rack_pack_version": MethodPropertyMeta("InRackPackVersion", "inRackPackVersion", "Xs:string", "Version142b", "Input", False),
    "in_service_pack_bundle_version": MethodPropertyMeta("InServicePackBundleVersion", "inServicePackBundleVersion", "Xs:string", "Version142b", "Input", False),
    "out_config_set": MethodPropertyMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inBladePackVersion": "in_blade_pack_version",
    "inDetailResult": "in_detail_result",
    "inInfraPackVersion": "in_infra_pack_version",
    "inRackPackVersion": "in_rack_pack_version",
    "inServicePackBundleVersion": "in_service_pack_bundle_version",
    "outConfigSet": "out_config_set",
}
