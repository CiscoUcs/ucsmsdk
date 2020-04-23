"""This module contains the general information for MgmtConnection ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtConnectionConsts:
    ACK_ACKNOWLEDGED = "acknowledged"
    ACK_UN_INITIALIZED = "un-initialized"
    ACK_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    IS_LLDP_DISCOVERY_POLICY_FALSE = "false"
    IS_LLDP_DISCOVERY_POLICY_NO = "no"
    IS_LLDP_DISCOVERY_POLICY_TRUE = "true"
    IS_LLDP_DISCOVERY_POLICY_YES = "yes"
    OPER_STATE_ACKNOWLEDGED = "acknowledged"
    OPER_STATE_UN_INITIALIZED = "un-initialized"
    OPER_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    TYPE_SHARED_LOM = "shared-lom"
    TYPE_SIDEBAND = "sideband"
    TYPE_UNSPECIFIED = "unspecified"


class MgmtConnection(ManagedObject):
    """This is MgmtConnection class."""

    consts = MgmtConnectionConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("MgmtConnection", "mgmtConnection", "mgmt-connection-[type]", VersionMeta.Version211a, "InputOutput", 0x7f, [], ["admin"], ['mgmtController'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "ack": MoPropertyMeta("ack", "ack", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["acknowledged", "un-initialized", "unsupported-connectivity"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "connection_serial": MoPropertyMeta("connection_serial", "connectionSerial", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "is_lldp_discovery_policy": MoPropertyMeta("is_lldp_discovery_policy", "isLldpDiscoveryPolicy", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["acknowledged", "un-initialized", "unsupported-connectivity"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x40, None, None, None, ["shared-lom", "sideband", "unspecified"], []),
    }

    prop_map = {
        "ack": "ack", 
        "childAction": "child_action", 
        "connectionSerial": "connection_serial", 
        "dn": "dn", 
        "isLldpDiscoveryPolicy": "is_lldp_discovery_policy", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.ack = None
        self.child_action = None
        self.connection_serial = None
        self.is_lldp_discovery_policy = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtConnection", parent_mo_or_dn, **kwargs)
