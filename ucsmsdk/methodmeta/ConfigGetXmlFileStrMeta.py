"""This module contains the meta information of ConfigGetXmlFileStr ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ConfigGetXmlFileStr", "configGetXmlFileStr", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_file_path": MethodPropertyMeta("InFilePath", "inFilePath", "Xs:string", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inFilePath": "in_file_path",
    "outConfig": "out_config",
}

