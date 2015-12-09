"""This module contains the general information for ApeControllerEeprom ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeControllerEepromConsts():
    SIDE_LEFT = "Left"
    SIDE_RIGHT = "Right"
    SIDE_UNKNOWN = "Unknown"


class ApeControllerEeprom(ManagedObject):
    """This is ApeControllerEeprom class."""

    consts = ApeControllerEepromConsts()
    naming_props = set([u'side'])

    mo_meta = MoMeta("ApeControllerEeprom", "apeControllerEeprom", "Eeprom-[side]", VersionMeta.Version101e, "InputOutput", 0x1ffL, [], ["read-only"], [u'apeControllerChassis'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "database_version": MoPropertyMeta("database_version", "databaseVersion", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "heartbeat_request": MoPropertyMeta("heartbeat_request", "heartbeatRequest", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "heartbeat_response": MoPropertyMeta("heartbeat_response", "heartbeatResponse", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "side": MoPropertyMeta("side", "side", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80L, None, None, None, ["Left", "Right", "Unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "databaseVersion": "database_version", 
        "dn": "dn", 
        "heartbeatRequest": "heartbeat_request", 
        "heartbeatResponse": "heartbeat_response", 
        "rn": "rn", 
        "sacl": "sacl", 
        "side": "side", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, side, **kwargs):
        self._dirty_mask = 0
        self.side = side
        self.child_action = None
        self.database_version = None
        self.heartbeat_request = None
        self.heartbeat_response = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ApeControllerEeprom", parent_mo_or_dn, **kwargs)

