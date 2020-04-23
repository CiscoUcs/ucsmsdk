"""This module contains the general information for BiosVfPCHSATAMode ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfPCHSATAModeConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_SATAMODE_AHCI = "ahci"
    VP_SATAMODE_DISABLED = "disabled"
    VP_SATAMODE_LSI_SW_RAID = "lsi-sw-raid"
    VP_SATAMODE_PLATFORM_DEFAULT = "platform-default"
    VP_SATAMODE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfPCHSATAMode(ManagedObject):
    """This is BiosVfPCHSATAMode class."""

    consts = BiosVfPCHSATAModeConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfPCHSATAMode", "biosVfPCHSATAMode", "PCH-SATA-Mode", VersionMeta.Version224b, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_sata_mode": MoPropertyMeta("vp_sata_mode", "vpSATAMode", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ahci", "disabled", "lsi-sw-raid", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpSATAMode": "vp_sata_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_sata_mode = None

        ManagedObject.__init__(self, "BiosVfPCHSATAMode", parent_mo_or_dn, **kwargs)
