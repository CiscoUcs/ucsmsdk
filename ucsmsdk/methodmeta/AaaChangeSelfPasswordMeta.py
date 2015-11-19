"""This module contains the meta information of AaaChangeSelfPassword ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("AaaChangeSelfPassword", "aaaChangeSelfPassword", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_confirm_new_password": MethodPropertyMeta("InConfirmNewPassword", "inConfirmNewPassword", "Xs:string", "Version142b", "Input", False),
    "in_new_password": MethodPropertyMeta("InNewPassword", "inNewPassword", "Xs:string", "Version142b", "Input", False),
    "in_old_password": MethodPropertyMeta("InOldPassword", "inOldPassword", "Xs:string", "Version142b", "Input", False),
    "in_user_name": MethodPropertyMeta("InUserName", "inUserName", "Xs:string", "Version142b", "Input", False),
    "out_status": MethodPropertyMeta("OutStatus", "outStatus", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfirmNewPassword": "in_confirm_new_password",
    "inNewPassword": "in_new_password",
    "inOldPassword": "in_old_password",
    "inUserName": "in_user_name",
    "outStatus": "out_status",
}

