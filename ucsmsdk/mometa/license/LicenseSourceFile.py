"""This module contains the general information for LicenseSourceFile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LicenseSourceFileConsts:
    EXP_NEVER = "never"
    TYPE_FEATURE = "feature"
    TYPE_INCREMENT = "increment"
    TYPE_UPGRADE = "upgrade"


class LicenseSourceFile(ManagedObject):
    """This is LicenseSourceFile class."""

    consts = LicenseSourceFileConsts()
    naming_props = set(['id', 'line'])

    mo_meta = MoMeta("LicenseSourceFile", "licenseSourceFile", "src-[id]:[line]", VersionMeta.Version141i, "InputOutput", 0x7f, [], ["read-only"], ['licenseInstance'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "exp": MoPropertyMeta("exp", "exp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "host_id": MoPropertyMeta("host_id", "hostId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, 1, 32, None, [], []),
        "line": MoPropertyMeta("line", "line", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "pak": MoPropertyMeta("pak", "pak", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "quant": MoPropertyMeta("quant", "quant", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sig": MoPropertyMeta("sig", "sig", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["feature", "increment", "upgrade"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "exp": "exp", 
        "hostId": "host_id", 
        "id": "id", 
        "line": "line", 
        "pak": "pak", 
        "quant": "quant", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sig": "sig", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, line, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.line = line
        self.child_action = None
        self.exp = None
        self.host_id = None
        self.pak = None
        self.quant = None
        self.sacl = None
        self.sig = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LicenseSourceFile", parent_mo_or_dn, **kwargs)
