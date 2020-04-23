"""This module contains the general information for SysfileDigest ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SysfileDigestConsts:
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SysfileDigest(ManagedObject):
    """This is SysfileDigest class."""

    consts = SysfileDigestConsts()
    naming_props = set(['name', 'creationTS'])

    mo_meta = MoMeta("SysfileDigest", "sysfileDigest", "filedigest-[name]-[creation_ts]", VersionMeta.Version211a, "InputOutput", 0xff, [], ["read-only"], [], [], [None])

    prop_meta = {
        "checksum": MoPropertyMeta("checksum", "checksum", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "creation_ts": MoPropertyMeta("creation_ts", "creationTS", "ulong", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x20, 1, 128, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "source": MoPropertyMeta("source", "source", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "ts": MoPropertyMeta("ts", "ts", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "uri": MoPropertyMeta("uri", "uri", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "checksum": "checksum", 
        "childAction": "child_action", 
        "creationTS": "creation_ts", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "source": "source", 
        "status": "status", 
        "switchId": "switch_id", 
        "ts": "ts", 
        "uri": "uri", 
    }

    def __init__(self, parent_mo_or_dn, name, creation_ts, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.creation_ts = creation_ts
        self.checksum = None
        self.child_action = None
        self.descr = None
        self.sacl = None
        self.size = None
        self.source = None
        self.status = None
        self.switch_id = None
        self.ts = None
        self.uri = None

        ManagedObject.__init__(self, "SysfileDigest", parent_mo_or_dn, **kwargs)
