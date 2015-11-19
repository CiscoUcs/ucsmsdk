"""This module contains the meta information of PolicySetCentraleStorage ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("PolicySetCentraleStorage", "policySetCentraleStorage", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_data": MethodPropertyMeta("InData", "inData", "Xs:string", "Version142b", "Input", False),
    "in_oper": MethodPropertyMeta("InOper", "inOper", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_side": MethodPropertyMeta("InSide", "inSide", "Xs:string", "Version142b", "Input", False),
    "out_data": MethodPropertyMeta("OutData", "outData", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inData": "in_data",
    "inOper": "in_oper",
    "inSide": "in_side",
    "outData": "out_data",
}

