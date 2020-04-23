"""This module contains the general information for FabricFcSan ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricFcSanConsts:
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    UPLINK_TRUNKING_DISABLED = "disabled"
    UPLINK_TRUNKING_ENABLED = "enabled"


class FabricFcSan(ManagedObject):
    """This is FabricFcSan class."""

    consts = FabricFcSanConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FabricFcSan", "fabricFcSan", "[id]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin", "ext-san-config", "ext-san-policy"], ['fabricSanCloud'], ['fabricFcSanEp', 'fabricFcSanPc', 'fabricFcoeSanEp', 'fabricFcoeSanPc', 'fabricSubGroup', 'fabricVsan', 'faultInst'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|vsan-count-exceeds-limit),){0,2}(defaultValue|not-applicable|vsan-count-exceeds-limit){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, ["A", "B", "NONE"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "uplink_trunking": MoPropertyMeta("uplink_trunking", "uplinkTrunking", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "dn": "dn", 
        "id": "id", 
        "locale": "locale", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
        "uplinkTrunking": "uplink_trunking", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.config_qualifier = None
        self.locale = None
        self.name = None
        self.sacl = None
        self.status = None
        self.transport = None
        self.type = None
        self.uplink_trunking = None

        ManagedObject.__init__(self, "FabricFcSan", parent_mo_or_dn, **kwargs)
