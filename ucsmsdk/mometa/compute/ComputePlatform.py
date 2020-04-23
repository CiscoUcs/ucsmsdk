"""This module contains the general information for ComputePlatform ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePlatformConsts:
    pass


class ComputePlatform(ManagedObject):
    """This is ComputePlatform class."""

    consts = ComputePlatformConsts()
    naming_props = set(['vendor', 'model', 'revision'])

    mo_meta = MoMeta("ComputePlatform", "computePlatform", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version131c, "InputOutput", 0xff, [], [""], ['computeDefaults'], ['biosSettings'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "model": "model", 
        "productName": "product_name", 
        "propAcl": "prop_acl", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.product_name = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePlatform", parent_mo_or_dn, **kwargs)
