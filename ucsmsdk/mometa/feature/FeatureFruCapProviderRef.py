"""This module contains the general information for FeatureFruCapProviderRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FeatureFruCapProviderRefConsts:
    SUPPORTABILITY_DEPRECATED = "deprecated"
    SUPPORTABILITY_NOT_SUPPORTED = "not-supported"
    SUPPORTABILITY_SUPPORTED = "supported"


class FeatureFruCapProviderRef(ManagedObject):
    """This is FeatureFruCapProviderRef class."""

    consts = FeatureFruCapProviderRefConsts()
    naming_props = set(['vendor', 'model', 'revision'])

    mo_meta = MoMeta("FeatureFruCapProviderRef", "featureFruCapProviderRef", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version302c, "InputOutput", 0xff, [], [""], ['featureProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supportability": MoPropertyMeta("supportability", "supportability", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deprecated", "not-supported", "supported"], []),
        "target_dn": MoPropertyMeta("target_dn", "targetDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportability": "supportability", 
        "targetDn": "target_dn", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.sacl = None
        self.status = None
        self.supportability = None
        self.target_dn = None

        ManagedObject.__init__(self, "FeatureFruCapProviderRef", parent_mo_or_dn, **kwargs)
