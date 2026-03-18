"""This module contains the general information for FirmwareSfpFirmwareInfo ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareSfpFirmwareInfoConsts:
    UPGRADE_NEEDED_FALSE = "false"
    UPGRADE_NEEDED_NO = "no"
    UPGRADE_NEEDED_TRUE = "true"
    UPGRADE_NEEDED_YES = "yes"


class FirmwareSfpFirmwareInfo(ManagedObject):
    """This is FirmwareSfpFirmwareInfo class."""

    consts = FirmwareSfpFirmwareInfoConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareSfpFirmwareInfo", "firmwareSfpFirmwareInfo", "sfp-fw-info", VersionMeta.Version602a, "InputOutput", 0x1f, [], ["admin"], ['fcPIo'], [], [None])

    prop_meta = {
        "available_version": MoPropertyMeta("available_version", "availableVersion", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version602a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "running_version": MoPropertyMeta("running_version", "runningVersion", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "upgrade_needed": MoPropertyMeta("upgrade_needed", "upgradeNeeded", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "availableVersion": "available_version", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "runningVersion": "running_version", 
        "sacl": "sacl", 
        "status": "status", 
        "upgradeNeeded": "upgrade_needed", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.available_version = None
        self.child_action = None
        self.running_version = None
        self.sacl = None
        self.status = None
        self.upgrade_needed = None

        ManagedObject.__init__(self, "FirmwareSfpFirmwareInfo", parent_mo_or_dn, **kwargs)
