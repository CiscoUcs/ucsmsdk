"""This module contains the general information for AdaptorIpV6RssHashProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorIpV6RssHashProfileConsts:
    IP_HASH_DISABLED = "disabled"
    IP_HASH_ENABLED = "enabled"
    TCP_HASH_DISABLED = "disabled"
    TCP_HASH_ENABLED = "enabled"


class AdaptorIpV6RssHashProfile(ManagedObject):
    """This is AdaptorIpV6RssHashProfile class."""

    consts = AdaptorIpV6RssHashProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorIpV6RssHashProfile", "adaptorIpV6RssHashProfile", "ipv6-rss-hash", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIf', 'adaptorHostEthIfProfile', 'adaptorUsnicConnDef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ip_hash": MoPropertyMeta("ip_hash", "ipHash", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "tcp_hash": MoPropertyMeta("tcp_hash", "tcpHash", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ipHash": "ip_hash", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tcpHash": "tcp_hash", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.ip_hash = None
        self.sacl = None
        self.status = None
        self.tcp_hash = None

        ManagedObject.__init__(self, "AdaptorIpV6RssHashProfile", parent_mo_or_dn, **kwargs)
