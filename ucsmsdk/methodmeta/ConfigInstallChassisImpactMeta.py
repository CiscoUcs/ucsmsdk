"""This module contains the meta information of ConfigInstallChassisImpact ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigInstallChassisImpact", "configInstallChassisImpact", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_chassis_pack_dns": MethodPropertyMeta("InChassisPackDns", "inChassisPackDns", "DnSet", "Version142b", "Input", True),
    "in_rack_pack_version": MethodPropertyMeta("InRackPackVersion", "inRackPackVersion", "Xs:string", "Version142b", "Input", False),
    "in_service_pack_bundle_version": MethodPropertyMeta("InServicePackBundleVersion", "inServicePackBundleVersion", "Xs:string", "Version142b", "Input", False),
    "out_config_set": MethodPropertyMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inChassisPackDns": "in_chassis_pack_dns",
    "inRackPackVersion": "in_rack_pack_version",
    "inServicePackBundleVersion": "in_service_pack_bundle_version",
    "outConfigSet": "out_config_set",
}
