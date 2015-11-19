"""This module contains the meta information of ConfigInstallStorageAllImpact ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ConfigInstallStorageAllImpact", "configInstallStorageAllImpact", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_storage_pack_dns": MethodPropertyMeta("InStoragePackDns", "inStoragePackDns", "DnSet", "Version142b", "Input", True),
    "in_storage_pack_version": MethodPropertyMeta("InStoragePackVersion", "inStoragePackVersion", "Xs:string", "Version142b", "Input", False),
    "out_config_set": MethodPropertyMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inStoragePackDns": "in_storage_pack_dns",
    "inStoragePackVersion": "in_storage_pack_version",
    "outConfigSet": "out_config_set",
}

