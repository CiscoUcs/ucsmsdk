"""This module contains the general information for LsbootStorage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsbootStorageConsts:
    ACCESS_READ_ONLY = "read-only"
    ACCESS_READ_ONLY_LOCAL = "read-only-local"
    ACCESS_READ_ONLY_REMOTE = "read-only-remote"
    ACCESS_READ_ONLY_REMOTE_CIMC = "read-only-remote-cimc"
    ACCESS_READ_WRITE = "read-write"
    ACCESS_READ_WRITE_DRIVE = "read-write-drive"
    ACCESS_READ_WRITE_LOCAL = "read-write-local"
    ACCESS_READ_WRITE_REMOTE = "read-write-remote"
    ACCESS_READ_WRITE_REMOTE_CIMC = "read-write-remote-cimc"
    TYPE_EFI_SHELL = "efi-shell"
    TYPE_ISCSI = "iscsi"
    TYPE_LAN = "lan"
    TYPE_SAN = "san"
    TYPE_STORAGE = "storage"
    TYPE_VIRTUAL_MEDIA = "virtual-media"


class LsbootStorage(ManagedObject):
    """This is LsbootStorage class."""

    consts = LsbootStorageConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootStorage", "lsbootStorage", "storage", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootDef', 'lsbootPolicy'], ['lsbootLocalStorage', 'lsbootSanImage'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["read-only", "read-only-local", "read-only-remote", "read-only-remote-cimc", "read-write", "read-write-drive", "read-write-local", "read-write-remote", "read-write-remote-cimc"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-16"]),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["efi-shell", "iscsi", "lan", "san", "storage", "virtual-media"], []),
    }

    prop_map = {
        "access": "access", 
        "childAction": "child_action", 
        "dn": "dn", 
        "order": "order", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access = None
        self.child_action = None
        self.order = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootStorage", parent_mo_or_dn, **kwargs)
