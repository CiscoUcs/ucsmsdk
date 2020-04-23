"""This module contains the general information for ExtvmmKeyRing ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtvmmKeyRingConsts:
    LOCATION_FTP = "ftp"
    LOCATION_NONE = "none"
    LOCATION_SCP = "scp"
    LOCATION_SFTP = "sftp"
    LOCATION_TFTP = "tftp"
    LOCATION_USB_A = "usbA"
    LOCATION_USB_B = "usbB"
    LOCATION_USBDRIVE = "usbdrive"
    LOCATION_VOLATILE = "volatile"
    LOCATION_WORKSPACE = "workspace"


class ExtvmmKeyRing(ManagedObject):
    """This is ExtvmmKeyRing class."""

    consts = ExtvmmKeyRingConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ExtvmmKeyRing", "extvmmKeyRing", "keyring-[name]", VersionMeta.Version111j, "InputOutput", 0x1ff, [], ["admin", "ls-config", "ls-config-policy", "pn-policy"], ['extvmmKeyStore'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "cert_file": MoPropertyMeta("cert_file", "certFile", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ftp", "none", "scp", "sftp", "tftp", "usbA", "usbB", "usbdrive", "volatile", "workspace"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
        "path": MoPropertyMeta("path", "path", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "certFile": "cert_file", 
        "childAction": "child_action", 
        "dn": "dn", 
        "location": "location", 
        "name": "name", 
        "path": "path", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.cert_file = None
        self.child_action = None
        self.location = None
        self.path = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtvmmKeyRing", parent_mo_or_dn, **kwargs)
