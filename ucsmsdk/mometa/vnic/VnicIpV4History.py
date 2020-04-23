"""This module contains the general information for VnicIpV4History ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIpV4HistoryConsts:
    pass


class VnicIpV4History(ManagedObject):
    """This is VnicIpV4History class."""

    consts = VnicIpV4HistoryConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIpV4History", "vnicIpV4History", "ipv4-history", VersionMeta.Version212a, "InputOutput", 0x1f, [], ["read-only"], ['vnicIPv4PooledIscsiAddr', 'vnicIpV4MgmtPooledAddr', 'vnicIpV4PooledAddr'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "old_ip_v4_addr": MoPropertyMeta("old_ip_v4_addr", "oldIpV4Addr", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "oldIpV4Addr": "old_ip_v4_addr", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.old_ip_v4_addr = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicIpV4History", parent_mo_or_dn, **kwargs)
