"""This module contains the general information for OsAgent ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsAgentConsts:
    LAST_CMD_NONE = "none"
    LAST_EVT_NONE = "none"
    PREV_CMD_NONE = "none"
    PREV_EVT_NONE = "none"
    TYPE_HOST_AGENT = "hostAgent"
    TYPE_INDETERMINATE = "indeterminate"
    TYPE_PNUOS_AGENT = "pnuosAgent"


class OsAgent(ManagedObject):
    """This is OsAgent class."""

    consts = OsAgentConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsAgent", "osAgent", "agent", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "last_cmd": MoPropertyMeta("last_cmd", "lastCmd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none"], []),
        "last_evt": MoPropertyMeta("last_evt", "lastEvt", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none"], []),
        "last_evt_ts": MoPropertyMeta("last_evt_ts", "lastEvtTs", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "prev_cmd": MoPropertyMeta("prev_cmd", "prevCmd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none"], []),
        "prev_evt": MoPropertyMeta("prev_evt", "prevEvt", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["hostAgent", "indeterminate", "pnuosAgent"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lastCmd": "last_cmd", 
        "lastEvt": "last_evt", 
        "lastEvtTs": "last_evt_ts", 
        "prevCmd": "prev_cmd", 
        "prevEvt": "prev_evt", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.last_cmd = None
        self.last_evt = None
        self.last_evt_ts = None
        self.prev_cmd = None
        self.prev_evt = None
        self.sacl = None
        self.status = None
        self.type = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "OsAgent", parent_mo_or_dn, **kwargs)
