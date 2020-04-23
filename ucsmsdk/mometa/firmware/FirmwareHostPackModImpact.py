"""This module contains the general information for FirmwareHostPackModImpact ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareHostPackModImpactConsts:
    pass


class FirmwareHostPackModImpact(ManagedObject):
    """This is FirmwareHostPackModImpact class."""

    consts = FirmwareHostPackModImpactConsts()
    naming_props = set(['keyDn'])

    mo_meta = MoMeta("FirmwareHostPackModImpact", "firmwareHostPackModImpact", "fw-sys-HostPackModImpact-[key_dn]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-server-policy"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "key_dn": MoPropertyMeta("key_dn", "keyDn", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "maint_policy_dn": MoPropertyMeta("maint_policy_dn", "maintPolicyDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "reboot_policy": MoPropertyMeta("reboot_policy", "rebootPolicy", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "service_profile_dn": MoPropertyMeta("service_profile_dn", "serviceProfileDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "keyDn": "key_dn", 
        "maintPolicyDn": "maint_policy_dn", 
        "pnDn": "pn_dn", 
        "rebootPolicy": "reboot_policy", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serviceProfileDn": "service_profile_dn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, key_dn, **kwargs):
        self._dirty_mask = 0
        self.key_dn = key_dn
        self.child_action = None
        self.maint_policy_dn = None
        self.pn_dn = None
        self.reboot_policy = None
        self.sacl = None
        self.service_profile_dn = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareHostPackModImpact", parent_mo_or_dn, **kwargs)
