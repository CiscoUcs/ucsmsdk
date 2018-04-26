"""This module contains the general information for DomainChassisFeature ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DomainChassisFeatureConsts:
    FUNCTIONAL_STATE_DISABLED = "disabled"
    FUNCTIONAL_STATE_ENABLED = "enabled"
    TYPE_MAJOR = "major"
    TYPE_MINOR = "minor"


class DomainChassisFeature(ManagedObject):
    """This is DomainChassisFeature class."""

    consts = DomainChassisFeatureConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("DomainChassisFeature", "domainChassisFeature", "chassis-feature-[name]", VersionMeta.Version321d, "InputOutput", 0x7f, [], ["admin"], [u'domainChassisFeatureCont', u'domainEnvironmentFeatureCont', u'domainNetworkFeatureCont', u'domainServerFeatureCont', u'domainStorageFeatureCont'], [u'domainChassisParam', u'domainEnvironmentParam', u'domainNetworkParam', u'domainServerParam', u'domainStorageParam'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "functional_state": MoPropertyMeta("functional_state", "functionalState", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["major", "minor"], []), 
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

        ManagedObject.__init__(self, "DomainChassisFeature", parent_mo_or_dn, **kwargs)
