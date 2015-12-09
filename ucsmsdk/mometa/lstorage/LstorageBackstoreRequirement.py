"""This module contains the general information for LstorageBackstoreRequirement ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageBackstoreRequirementConsts():
    pass


class LstorageBackstoreRequirement(ManagedObject):
    """This is LstorageBackstoreRequirement class."""

    consts = LstorageBackstoreRequirementConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageBackstoreRequirement", "lstorageBackstoreRequirement", "backstore-req", VersionMeta.Version302c, "InputOutput", 0x7fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage", "ls-storage-policy", "read-only"], [u'lstorageSanScsiLun'], [u'faultInst'], [None])

    prop_meta = {
        "backstore_dn": MoPropertyMeta("backstore_dn", "backstoreDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "backstoreDn": "backstore_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "operName": "oper_name", 
        "operQualifier": "oper_qualifier", 
        "qualifier": "qualifier", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.backstore_dn = None
        self.child_action = None
        self.name = None
        self.oper_name = None
        self.oper_qualifier = None
        self.qualifier = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageBackstoreRequirement", parent_mo_or_dn, **kwargs)

