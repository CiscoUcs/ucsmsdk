"""This module contains the general information for DhcpAcquired ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DhcpAcquiredConsts:
    pass


class DhcpAcquired(ManagedObject):
    """This is DhcpAcquired class."""

    consts = DhcpAcquiredConsts()
    naming_props = set([])

    mo_meta = MoMeta("DhcpAcquired", "dhcpAcquired", "lease", VersionMeta.Version141i, "InputOutput", 0x1f, [], ["read-only"], ['adaptorHostEthIf', 'mgmtIf'], [], ["Get"])

    prop_meta = {
        "acqts": MoPropertyMeta("acqts", "acqts", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cookie": MoPropertyMeta("cookie", "cookie", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ends": MoPropertyMeta("ends", "ends", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sys_id": MoPropertyMeta("sys_id", "sysId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "acqts": "acqts", 
        "childAction": "child_action", 
        "cookie": "cookie", 
        "dn": "dn", 
        "ends": "ends", 
        "ip": "ip", 
        "mac": "mac", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "sysId": "sys_id", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.acqts = None
        self.child_action = None
        self.cookie = None
        self.ends = None
        self.ip = None
        self.mac = None
        self.sacl = None
        self.status = None
        self.sys_id = None

        ManagedObject.__init__(self, "DhcpAcquired", parent_mo_or_dn, **kwargs)
