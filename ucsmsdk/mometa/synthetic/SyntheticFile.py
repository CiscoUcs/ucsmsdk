"""This module contains the general information for SyntheticFile ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SyntheticFileConsts():
    pass


class SyntheticFile(ManagedObject):
    """This is SyntheticFile class."""

    consts = SyntheticFileConsts()
    naming_props = set([u'ino'])

    mo_meta = MoMeta("SyntheticFile", "syntheticFile", "file-[ino]", VersionMeta.Version101e, "InputOutput", 0xfffffL, [], ["admin"], [u'syntheticDirectory'], [], ["Get"])

    prop_meta = {
        "atime": MoPropertyMeta("atime", "atime", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], []), 
        "blksize": MoPropertyMeta("blksize", "blksize", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], []), 
        "blocks": MoPropertyMeta("blocks", "blocks", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x10L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "ctime": MoPropertyMeta("ctime", "ctime", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], []), 
        "dev": MoPropertyMeta("dev", "dev", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "gid": MoPropertyMeta("gid", "gid", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, [], []), 
        "ino": MoPropertyMeta("ino", "ino", "ulong", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x200L, None, None, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], []), 
        "mtime": MoPropertyMeta("mtime", "mtime", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 510, None, [], []), 
        "nlink": MoPropertyMeta("nlink", "nlink", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, [], []), 
        "path": MoPropertyMeta("path", "path", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, 0, 510, None, [], []), 
        "rdev": MoPropertyMeta("rdev", "rdev", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10000L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uid": MoPropertyMeta("uid", "uid", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80000L, None, None, None, [], []), 
    }

    prop_map = {
        "atime": "atime", 
        "blksize": "blksize", 
        "blocks": "blocks", 
        "childAction": "child_action", 
        "ctime": "ctime", 
        "dev": "dev", 
        "dn": "dn", 
        "gid": "gid", 
        "ino": "ino", 
        "mode": "mode", 
        "mtime": "mtime", 
        "name": "name", 
        "nlink": "nlink", 
        "path": "path", 
        "rdev": "rdev", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "uid": "uid", 
    }

    def __init__(self, parent_mo_or_dn, ino, **kwargs):
        self._dirty_mask = 0
        self.ino = ino
        self.atime = None
        self.blksize = None
        self.blocks = None
        self.child_action = None
        self.ctime = None
        self.dev = None
        self.gid = None
        self.mode = None
        self.mtime = None
        self.name = None
        self.nlink = None
        self.path = None
        self.rdev = None
        self.sacl = None
        self.size = None
        self.status = None
        self.uid = None

        ManagedObject.__init__(self, "SyntheticFile", parent_mo_or_dn, **kwargs)
