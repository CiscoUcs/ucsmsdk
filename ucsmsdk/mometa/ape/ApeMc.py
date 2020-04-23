"""This module contains the general information for ApeMc ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeMcConsts:
    UPDATE_TYPE_DELTA = "delta"
    UPDATE_TYPE_PERIODIC = "periodic"
    UPDATE_TYPE_SYNC = "sync"


class ApeMc(ManagedObject):
    """This is ApeMc class."""

    consts = ApeMcConsts()
    naming_props = set(['ip'])

    mo_meta = MoMeta("ApeMc", "apeMc", "mc-[ip]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["read-only"], ['apeManager'], ['apeMcTable'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
        "update_type": MoPropertyMeta("update_type", "updateType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["delta", "periodic", "sync"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ip": "ip", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "updateType": "update_type", 
    }

    def __init__(self, parent_mo_or_dn, ip, **kwargs):
        self._dirty_mask = 0
        self.ip = ip
        self.child_action = None
        self.sacl = None
        self.status = None
        self.type = None
        self.update_type = None

        ManagedObject.__init__(self, "ApeMc", parent_mo_or_dn, **kwargs)
