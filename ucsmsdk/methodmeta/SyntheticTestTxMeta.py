"""This module contains the meta information of SyntheticTestTx ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("SyntheticTestTx", "syntheticTestTx", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigSet", "Version142b", "Input", True),
    "in_test": MethodPropertyMeta("InTest", "inTest", "Xs:string", "Version142b", "Input", False),
    "in_what": MethodPropertyMeta("InWhat", "inWhat", "Xs:string", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inTest": "in_test",
    "inWhat": "in_what",
    "outConfig": "out_config",
}

