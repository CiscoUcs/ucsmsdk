"""This module contains the general information for LicenseFeatureLine ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LicenseFeatureLineConsts:
    EXP_NEVER = "never"
    TYPE_FEATURE = "feature"
    TYPE_INCREMENT = "increment"
    TYPE_UPGRADE = "upgrade"


class LicenseFeatureLine(ManagedObject):
    """This is LicenseFeatureLine class."""

    consts = LicenseFeatureLineConsts()
    naming_props = set(['id', 'type'])

    mo_meta = MoMeta("LicenseFeatureLine", "licenseFeatureLine", "FeatureLine-[id]:[type]", VersionMeta.Version141i, "InputOutput", 0x7f, [], ["read-only"], ['licenseContents'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "exp": MoPropertyMeta("exp", "exp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, 1, 32, None, [], []),
        "pak": MoPropertyMeta("pak", "pak", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "quant": MoPropertyMeta("quant", "quant", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sig": MoPropertyMeta("sig", "sig", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x40, None, None, None, ["feature", "increment", "upgrade"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "exp": "exp", 
        "id": "id", 
        "pak": "pak", 
        "quant": "quant", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sig": "sig", 
        "sku": "sku", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, type, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.type = type
        self.child_action = None
        self.exp = None
        self.pak = None
        self.quant = None
        self.sacl = None
        self.sig = None
        self.sku = None
        self.status = None

        ManagedObject.__init__(self, "LicenseFeatureLine", parent_mo_or_dn, **kwargs)
