"""This module contains the meta information of ConfigEstimateConfMos ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ConfigEstimateConfMos", "configEstimateConfMos", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_configs": MethodPropertyMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigMap", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inConfigs": "in_configs",
    "inHierarchical": "in_hierarchical",
    "outConfigs": "out_configs",
}

