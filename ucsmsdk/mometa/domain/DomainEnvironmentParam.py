"""This module contains the general information for DomainEnvironmentParam ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DomainEnvironmentParamConsts:
    pass


class DomainEnvironmentParam(ManagedObject):
    """This is DomainEnvironmentParam class."""

    consts = DomainEnvironmentParamConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("DomainEnvironmentParam", "domainEnvironmentParam", "env-param-[name]", VersionMeta.Version221b, "InputOutput", 0x7f, [], ["admin"], [u'domainChassisFeature', u'domainEnvironmentFeature', u'domainNetworkFeature', u'domainServerFeature', u'domainStorageFeature'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.flt_aggr = None
        self.sacl = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "DomainEnvironmentParam", parent_mo_or_dn, **kwargs)
