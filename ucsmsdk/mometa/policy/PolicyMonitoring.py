"""This module contains the general information for PolicyMonitoring ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyMonitoringConsts:
    SOURCE_LOCAL = "local"
    SOURCE_PENDING_POLICY = "pending-policy"
    SOURCE_POLICY = "policy"


class PolicyMonitoring(ManagedObject):
    """This is PolicyMonitoring class."""

    consts = PolicyMonitoringConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyMonitoring", "policyMonitoring", "monitoring-ctrl", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin", "operations"], ['policyControlEp'], ['policyControlledInstance', 'policyControlledType'], ["Add", "Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source": MoPropertyMeta("source", "source", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["local", "pending-policy", "policy"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "source": "source", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.source = None
        self.status = None

        ManagedObject.__init__(self, "PolicyMonitoring", parent_mo_or_dn, **kwargs)
