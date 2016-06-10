"""This module contains the general information for OsPrimarySlave ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsPrimarySlaveConsts:
    RESELECT_POLICY_ALWAYS = "always"
    RESELECT_POLICY_BETTER = "better"
    RESELECT_POLICY_FAILURE = "failure"


class OsPrimarySlave(ManagedObject):
    """This is OsPrimarySlave class."""

    consts = OsPrimarySlaveConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("OsPrimarySlave", "osPrimarySlave", "slave-intf-[name]", VersionMeta.Version302a, "InputOutput", 0x3f, [], ["read-only"], [u'osEthBondModeActiveBackup', u'osEthBondModeBalancedALB', u'osEthBondModeBalancedRR', u'osEthBondModeBalancedTLB', u'osEthBondModeBalancedXOR', u'osEthBondModeBroadcast'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "reselect_policy": MoPropertyMeta("reselect_policy", "reselectPolicy", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["always", "better", "failure"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "reselectPolicy": "reselect_policy", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.reselect_policy = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "OsPrimarySlave", parent_mo_or_dn, **kwargs)
