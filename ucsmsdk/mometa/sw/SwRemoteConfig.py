"""This module contains the general information for SwRemoteConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwRemoteConfigConsts:
    IS_MTU_FALSE = "false"
    IS_MTU_NO = "no"
    IS_MTU_TRUE = "true"
    IS_MTU_YES = "yes"
    LIFE_CYCLE_DELETED = "deleted"
    LIFE_CYCLE_NEW = "new"
    LIFE_CYCLE_NORMAL = "normal"


class SwRemoteConfig(ManagedObject):
    """This is SwRemoteConfig class."""

    consts = SwRemoteConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwRemoteConfig", "swRemoteConfig", "remote", VersionMeta.Version434a, "InputOutput", 0x7fff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['swEthMon', 'swFcMon'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dest_ip": MoPropertyMeta("dest_ip", "destIP", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dest_i_pv6": MoPropertyMeta("dest_i_pv6", "destIPv6", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "erspan_id": MoPropertyMeta("erspan_id", "erspanID", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-1023"]),
        "ip_dscp": MoPropertyMeta("ip_dscp", "ipDscp", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-63"]),
        "ip_ttl": MoPropertyMeta("ip_ttl", "ipTtl", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-255"]),
        "is_mtu": MoPropertyMeta("is_mtu", "isMtu", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []),
        "life_cycle": MoPropertyMeta("life_cycle", "lifeCycle", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deleted", "new", "normal"], []),
        "mtu": MoPropertyMeta("mtu", "mtu", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["64-1518"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source_ip": MoPropertyMeta("source_ip", "sourceIP", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "source_i_pv6": MoPropertyMeta("source_i_pv6", "sourceIPv6", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x2000, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "destIP": "dest_ip", 
        "destIPv6": "dest_i_pv6", 
        "dn": "dn", 
        "erspanID": "erspan_id", 
        "ipDscp": "ip_dscp", 
        "ipTtl": "ip_ttl", 
        "isMtu": "is_mtu", 
        "lifeCycle": "life_cycle", 
        "mtu": "mtu", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceIP": "source_ip", 
        "sourceIPv6": "source_i_pv6", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.dest_ip = None
        self.dest_i_pv6 = None
        self.erspan_id = None
        self.ip_dscp = None
        self.ip_ttl = None
        self.is_mtu = None
        self.life_cycle = None
        self.mtu = None
        self.name = None
        self.sacl = None
        self.source_ip = None
        self.source_i_pv6 = None
        self.status = None

        ManagedObject.__init__(self, "SwRemoteConfig", parent_mo_or_dn, **kwargs)
