"""This module contains the general information for FabricRemoteConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricRemoteConfigConsts:
    IS_MTU_FALSE = "false"
    IS_MTU_NO = "no"
    IS_MTU_TRUE = "true"
    IS_MTU_YES = "yes"


class FabricRemoteConfig(ManagedObject):
    """This is FabricRemoteConfig class."""

    consts = FabricRemoteConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricRemoteConfig", "fabricRemoteConfig", "remote", VersionMeta.Version434a, "InputOutput", 0xfff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthMon', 'fabricFcMon'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dest_ip": MoPropertyMeta("dest_ip", "destIP", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "erspan_id": MoPropertyMeta("erspan_id", "erspanID", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-1023"]),
        "ip_dscp": MoPropertyMeta("ip_dscp", "ipDscp", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-63"]),
        "ip_ttl": MoPropertyMeta("ip_ttl", "ipTtl", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-255"]),
        "is_mtu": MoPropertyMeta("is_mtu", "isMtu", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []),
        "mtu": MoPropertyMeta("mtu", "mtu", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["64-1518"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "destIP": "dest_ip", 
        "dn": "dn", 
        "erspanID": "erspan_id", 
        "ipDscp": "ip_dscp", 
        "ipTtl": "ip_ttl", 
        "isMtu": "is_mtu", 
        "mtu": "mtu", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.dest_ip = None
        self.erspan_id = None
        self.ip_dscp = None
        self.ip_ttl = None
        self.is_mtu = None
        self.mtu = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricRemoteConfig", parent_mo_or_dn, **kwargs)
