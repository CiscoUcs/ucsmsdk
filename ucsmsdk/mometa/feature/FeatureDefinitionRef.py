"""This module contains the general information for FeatureDefinitionRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FeatureDefinitionRefConsts():
    SUPPORTABILITY_DEPRECATED = "deprecated"
    SUPPORTABILITY_NOT_SUPPORTED = "not-supported"
    SUPPORTABILITY_SUPPORTED = "supported"


class FeatureDefinitionRef(ManagedObject):
    """This is FeatureDefinitionRef class."""

    consts = FeatureDefinitionRefConsts()
    naming_props = set([u'name', u'revision'])

    mo_meta = MoMeta("FeatureDefinitionRef", "featureDefinitionRef", "feature-[name]-revision-[revision]", VersionMeta.Version302c, "InputOutput", 0x7fL, [], [""], [u'featureProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x10L, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supportability": MoPropertyMeta("supportability", "supportability", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deprecated", "not-supported", "supported"], []), 
        "target_dn": MoPropertyMeta("target_dn", "targetDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportability": "supportability", 
        "targetDn": "target_dn", 
    }

    def __init__(self, parent_mo_or_dn, name, revision, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.revision = revision
        self.child_action = None
        self.sacl = None
        self.status = None
        self.supportability = None
        self.target_dn = None

        ManagedObject.__init__(self, "FeatureDefinitionRef", parent_mo_or_dn, **kwargs)

