"""This module contains the general information for OsMiiLinkMonitoringPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsMiiLinkMonitoringPolicyConsts:
    LINK_STATUS_QUERY_TYPE_ETHTOOL = "ethtool"
    LINK_STATUS_QUERY_TYPE_NETIF = "netif"


class OsMiiLinkMonitoringPolicy(ManagedObject):
    """This is OsMiiLinkMonitoringPolicy class."""

    consts = OsMiiLinkMonitoringPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsMiiLinkMonitoringPolicy", "osMiiLinkMonitoringPolicy", "link-mon-pol", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], ['osEthBondIntf'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "frequency": MoPropertyMeta("frequency", "frequency", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "link_down_delay": MoPropertyMeta("link_down_delay", "linkDownDelay", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "link_status_query_type": MoPropertyMeta("link_status_query_type", "linkStatusQueryType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ethtool", "netif"], []),
        "link_up_delay": MoPropertyMeta("link_up_delay", "linkUpDelay", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "frequency": "frequency", 
        "linkDownDelay": "link_down_delay", 
        "linkStatusQueryType": "link_status_query_type", 
        "linkUpDelay": "link_up_delay", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.frequency = None
        self.link_down_delay = None
        self.link_status_query_type = None
        self.link_up_delay = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "OsMiiLinkMonitoringPolicy", parent_mo_or_dn, **kwargs)
