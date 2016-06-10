"""This module contains the meta information of ApeMcGetSmbios ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ApeMcGetSmbios", "apeMcGetSmbios", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_ip_addr": MethodPropertyMeta("InIpAddr", "inIpAddr", "AddressIPv4", "Version142b", "Input", False),
    "in_update_cnt": MethodPropertyMeta("InUpdateCnt", "inUpdateCnt", "Xs:int", "Version142b", "Input", False),
    "out_file_path": MethodPropertyMeta("OutFilePath", "outFilePath", "Xs:string", "Version142b", "Output", False),
    "out_update_cnt": MethodPropertyMeta("OutUpdateCnt", "outUpdateCnt", "Xs:int", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inIpAddr": "in_ip_addr",
    "inUpdateCnt": "in_update_cnt",
    "outFilePath": "out_file_path",
    "outUpdateCnt": "out_update_cnt",
}
