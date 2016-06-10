"""This module contains the meta information of ConfigGetXmlFile ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetXmlFile", "configGetXmlFile", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_file_path": MethodPropertyMeta("InFilePath", "inFilePath", "Xs:string", "Version142b", "Input", False),
    "out_config": MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inFilePath": "in_file_path",
    "outConfig": "out_config",
}
