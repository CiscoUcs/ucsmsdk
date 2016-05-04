"""This module contains the general information for LsIdentityInfo ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsIdentityInfoConsts:
    UUID_IDENTITY_STATE_CONSISTENT = "consistent"
    UUID_IDENTITY_STATE_MISMATCH = "mismatch"


class LsIdentityInfo(ManagedObject):
    """This is LsIdentityInfo class."""

    consts = LsIdentityInfoConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsIdentityInfo", "lsIdentityInfo", "ls-identity-info", VersionMeta.Version224a, "InputOutput", 0x1f, [], ["read-only"], [u'lsServer'], [u'faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uuid_identity_state": MoPropertyMeta("uuid_identity_state", "uuidIdentityState", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["consistent", "mismatch"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "uuidIdentityState": "uuid_identity_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.uuid_identity_state = None

        ManagedObject.__init__(self, "LsIdentityInfo", parent_mo_or_dn, **kwargs)
