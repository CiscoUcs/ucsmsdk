"""This module contains the meta information of StatsClearInterval ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("StatsClearInterval", "statsClearInterval", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dns": MethodPropertyMeta("InDns", "inDns", "DnSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inDns": "in_dns",
}

