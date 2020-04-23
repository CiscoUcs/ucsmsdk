"""This module contains the general information for SwNetflowRecordDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwNetflowRecordDefConsts:
    KEY_TYPE_IPV4KEYS = "ipv4keys"
    KEY_TYPE_IPV6KEYS = "ipv6keys"
    KEY_TYPE_L2KEYS = "l2keys"
    LIFE_CYCLE_DELETED = "deleted"
    LIFE_CYCLE_NEW = "new"
    LIFE_CYCLE_NORMAL = "normal"
    PROTOCOL_NETFLOW = "netflow"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwNetflowRecordDef(ManagedObject):
    """This is SwNetflowRecordDef class."""

    consts = SwNetflowRecordDefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SwNetflowRecordDef", "swNetflowRecordDef", "flowrecord-netflow-[name]", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["read-only"], ['swEthLanFlowMon'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ipv4keys": MoPropertyMeta("ipv4keys", "ipv4keys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|src-port|ipv4-src-address|ipv4-dest-address|dest-port|ip-protocol|ip-tos),){0,7}(defaultValue|none|src-port|ipv4-src-address|ipv4-dest-address|dest-port|ip-protocol|ip-tos){0,1}""", [], []),
        "ipv6keys": MoPropertyMeta("ipv6keys", "ipv6keys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|src-port|ipv6-src-address|ipv6-dest-address|dest-port|ip-protocol),){0,6}(defaultValue|none|src-port|ipv6-src-address|ipv6-dest-address|dest-port|ip-protocol){0,1}""", [], []),
        "key_type": MoPropertyMeta("key_type", "keyType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4keys", "ipv6keys", "l2keys"], []),
        "l2keys": MoPropertyMeta("l2keys", "l2keys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|ethertype|dest-mac-address|src-mac-address),){0,4}(defaultValue|none|ethertype|dest-mac-address|src-mac-address){0,1}""", [], []),
        "life_cycle": MoPropertyMeta("life_cycle", "lifeCycle", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deleted", "new", "normal"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "nonkeys": MoPropertyMeta("nonkeys", "nonkeys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|counter-packets-long|counter-bytes-long|sys-uptime-first|sys-uptime-last),){0,5}(defaultValue|none|counter-packets-long|counter-bytes-long|sys-uptime-first|sys-uptime-last){0,1}""", [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ipv4keys": "ipv4keys", 
        "ipv6keys": "ipv6keys", 
        "keyType": "key_type", 
        "l2keys": "l2keys", 
        "lifeCycle": "life_cycle", 
        "name": "name", 
        "nonkeys": "nonkeys", 
        "peerDn": "peer_dn", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.ipv4keys = None
        self.ipv6keys = None
        self.key_type = None
        self.l2keys = None
        self.life_cycle = None
        self.nonkeys = None
        self.peer_dn = None
        self.protocol = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "SwNetflowRecordDef", parent_mo_or_dn, **kwargs)
