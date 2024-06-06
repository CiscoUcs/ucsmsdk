"""This module contains the general information for FabricMonOriginSVI ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricMonOriginSVIConsts:
    pass


class FabricMonOriginSVI(ManagedObject):
    """This is FabricMonOriginSVI class."""

    consts = FabricMonOriginSVIConsts()
    naming_props = set(['sourceVlan'])

    mo_meta = MoMeta("FabricMonOriginSVI", "fabricMonOriginSVI", "vlan-[source_vlan]", VersionMeta.Version434a, "InputOutput", 0x3f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricRMonEp'], ['fabricMonOriginIP', 'faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_fail_reason": MoPropertyMeta("config_fail_reason", "configFailReason", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|source-vlan-unresolved),){0,2}(defaultValue|not-applicable|source-vlan-unresolved){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source_vlan": MoPropertyMeta("source_vlan", "sourceVlan", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "source_vlan_dn": MoPropertyMeta("source_vlan_dn", "sourceVlanDn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configFailReason": "config_fail_reason", 
        "configQualifier": "config_qualifier", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceVlan": "source_vlan", 
        "sourceVlanDn": "source_vlan_dn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, source_vlan, **kwargs):
        self._dirty_mask = 0
        self.source_vlan = source_vlan
        self.child_action = None
        self.config_fail_reason = None
        self.config_qualifier = None
        self.sacl = None
        self.source_vlan_dn = None
        self.status = None

        ManagedObject.__init__(self, "FabricMonOriginSVI", parent_mo_or_dn, **kwargs)
