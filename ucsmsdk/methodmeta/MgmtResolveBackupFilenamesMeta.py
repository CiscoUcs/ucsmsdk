"""This module contains the meta information of MgmtResolveBackupFilenames ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("MgmtResolveBackupFilenames", "mgmtResolveBackupFilenames", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_backup_source": MethodPropertyMeta("InBackupSource", "inBackupSource", "Xs:string", "Version142b", "Input", False),
    "in_type": MethodPropertyMeta("InType", "inType", "Xs:string", "Version142b", "Input", False),
    "out_backups": MethodPropertyMeta("OutBackups", "outBackups", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inBackupSource": "in_backup_source",
    "inType": "in_type",
    "outBackups": "out_backups",
}
