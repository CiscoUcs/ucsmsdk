"""This module contains the general information for PolicySourceApp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicySourceAppConsts:
    pass


class PolicySourceApp(ManagedObject):
    """This is PolicySourceApp class."""

    consts = PolicySourceAppConsts()
    naming_props = set(['sourceDme'])

    mo_meta = MoMeta("PolicySourceApp", "policySourceApp", "source-[source_dme]", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["read-only"], ['policyControlEp'], ['policyContext'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source_dme": MoPropertyMeta("source_dme", "sourceDme", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceDme": "source_dme", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, source_dme, **kwargs):
        self._dirty_mask = 0
        self.source_dme = source_dme
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicySourceApp", parent_mo_or_dn, **kwargs)
