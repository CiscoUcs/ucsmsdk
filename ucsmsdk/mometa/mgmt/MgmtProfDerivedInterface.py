"""This module contains the general information for MgmtProfDerivedInterface ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class MgmtProfDerivedInterfaceConsts():
    CONFIG_STATE_INCOMPLETE = "incomplete"
    CONFIG_STATE_INVALID_PINNING = "invalidPinning"
    CONFIG_STATE_UNRESOLVED_VLAN = "unresolvedVlan"
    CONFIG_STATE_UNSUPPORTED_FIRMWARE = "unsupportedFirmware"
    CONFIG_STATE_UNSUPPORTED_SERVER = "unsupportedServer"
    CONFIG_STATE_UNSUPPORTED_VLAN = "unsupportedVlan"
    CONFIG_STATE_VALID = "valid"
    IP_V4_STATE_NONE = "none"
    IP_V4_STATE_POOLED = "pooled"
    IP_V4_STATE_STATIC = "static"
    IP_V6_STATE_NONE = "none"
    IP_V6_STATE_POOLED = "pooled"
    IP_V6_STATE_STATIC = "static"
    MODE_IN_BAND = "in-band"
    OPER_STATE_DEPLOYED = "deployed"
    OPER_STATE_DOWN = "down"
    OPER_STATE_NOT_DEPLOYED = "notDeployed"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UP = "up"


class MgmtProfDerivedInterface(ManagedObject):
    """This is MgmtProfDerivedInterface class."""

    consts = MgmtProfDerivedInterfaceConsts()
    naming_props = set([u'mode'])

    mo_meta = MoMeta("MgmtProfDerivedInterface", "mgmtProfDerivedInterface", "spiface-[mode]", VersionMeta.Version221b, "InputOutput", 0xffL, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], [u'mgmtController'], [u'mgmtVnet'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_message": MoPropertyMeta("config_message", "configMessage", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["incomplete", "invalidPinning", "unresolvedVlan", "unsupportedFirmware", "unsupportedServer", "unsupportedVlan", "valid"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "ip_v4_state": MoPropertyMeta("ip_v4_state", "ipV4State", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["none", "pooled", "static"], []), 
        "ip_v6_state": MoPropertyMeta("ip_v6_state", "ipV6State", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["none", "pooled", "static"], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x20L, None, None, None, ["in-band"], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deployed", "down", "notDeployed", "unknown", "up"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configMessage": "config_message", 
        "configState": "config_state", 
        "dn": "dn", 
        "ipV4State": "ip_v4_state", 
        "ipV6State": "ip_v6_state", 
        "mode": "mode", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, mode, **kwargs):
        self._dirty_mask = 0
        self.mode = mode
        self.child_action = None
        self.config_message = None
        self.config_state = None
        self.ip_v4_state = None
        self.ip_v6_state = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtProfDerivedInterface", parent_mo_or_dn, **kwargs)

