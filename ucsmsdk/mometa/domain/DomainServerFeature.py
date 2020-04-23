"""This module contains the general information for DomainServerFeature ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DomainServerFeatureConsts:
    FUNCTIONAL_STATE_DISABLED = "disabled"
    FUNCTIONAL_STATE_ENABLED = "enabled"
    TYPE_MAJOR = "major"
    TYPE_MINOR = "minor"


class DomainServerFeature(ManagedObject):
    """This is DomainServerFeature class."""

    consts = DomainServerFeatureConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("DomainServerFeature", "domainServerFeature", "server-feature-[name]", VersionMeta.Version221b, "InputOutput", 0x7f, [], ["admin"], ['domainChassisFeatureCont', 'domainEnvironmentFeatureCont', 'domainNetworkFeatureCont', 'domainServerFeatureCont', 'domainStorageFeatureCont'], ['domainChassisParam', 'domainEnvironmentParam', 'domainNetworkParam', 'domainServerParam', 'domainStorageParam'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "functional_state": MoPropertyMeta("functional_state", "functionalState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["major", "minor"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "functionalState": "functional_state", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.flt_aggr = None
        self.functional_state = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "DomainServerFeature", parent_mo_or_dn, **kwargs)
