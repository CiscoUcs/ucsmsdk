"""This module contains the general information for LsbootVirtualMedia ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsbootVirtualMediaConsts:
    ACCESS_READ_ONLY = "read-only"
    ACCESS_READ_ONLY_LOCAL = "read-only-local"
    ACCESS_READ_ONLY_REMOTE = "read-only-remote"
    ACCESS_READ_ONLY_REMOTE_CIMC = "read-only-remote-cimc"
    ACCESS_READ_WRITE = "read-write"
    ACCESS_READ_WRITE_DRIVE = "read-write-drive"
    ACCESS_READ_WRITE_LOCAL = "read-write-local"
    ACCESS_READ_WRITE_REMOTE = "read-write-remote"
    ACCESS_READ_WRITE_REMOTE_CIMC = "read-write-remote-cimc"
    LUN_ID_UNSPECIFIED = "unspecified"
    TYPE_EFI_SHELL = "efi-shell"
    TYPE_ISCSI = "iscsi"
    TYPE_LAN = "lan"
    TYPE_SAN = "san"
    TYPE_STORAGE = "storage"
    TYPE_VIRTUAL_MEDIA = "virtual-media"


class LsbootVirtualMedia(ManagedObject):
    """This is LsbootVirtualMedia class."""

    consts = LsbootVirtualMediaConsts()
    naming_props = set(['access'])

    mo_meta = MoMeta("LsbootVirtualMedia", "lsbootVirtualMedia", "[access]-vm", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootDef', 'lsbootPolicy'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x2, None, None, None, ["read-only", "read-only-local", "read-only-remote", "read-only-remote-cimc", "read-write", "read-write-drive", "read-write-local", "read-write-remote", "read-write-remote-cimc"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "lun_id": MoPropertyMeta("lun_id", "lunId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["unspecified"], ["0-4294967295"]),
        "mapping_name": MoPropertyMeta("mapping_name", "mappingName", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-16"]),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["efi-shell", "iscsi", "lan", "san", "storage", "virtual-media"], []),
    }

    prop_map = {
        "access": "access", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lunId": "lun_id", 
        "mappingName": "mapping_name", 
        "order": "order", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, access, **kwargs):
        self._dirty_mask = 0
        self.access = access
        self.child_action = None
        self.lun_id = None
        self.mapping_name = None
        self.order = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootVirtualMedia", parent_mo_or_dn, **kwargs)
