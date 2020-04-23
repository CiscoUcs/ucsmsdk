"""This module contains the general information for PortGroup ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PortGroupConsts:
    TYPE_ADAPTOR_EXT = "adaptor-ext"
    TYPE_ADAPTOR_PC = "adaptor-pc"
    TYPE_FABRIC = "fabric"
    TYPE_FABRIC_PC = "fabric-pc"
    TYPE_HOST = "host"
    TYPE_HOST_PC = "host-pc"
    TYPE_SERVER_PC = "server-pc"
    TYPE_SWITCH_ETHER = "switch-ether"
    TYPE_SWITCH_FC = "switch-fc"


class PortGroup(ManagedObject):
    """This is PortGroup class."""

    consts = PortGroupConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("PortGroup", "portGroup", "[type]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['equipmentIOCard', 'equipmentSharedIOModule', 'equipmentSwitchCard', 'equipmentSwitchIOCard'], ['etherPIo', 'etherServerIntFIo', 'etherServerIntFIoPc', 'etherSwitchIntFIo', 'etherSwitchIntFIoPc', 'fcPIo', 'portSubGroup'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, ["adaptor-ext", "adaptor-pc", "fabric", "fabric-pc", "host", "host-pc", "server-pc", "switch-ether", "switch-fc"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "locale": "locale", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.locale = None
        self.name = None
        self.sacl = None
        self.status = None
        self.transport = None

        ManagedObject.__init__(self, "PortGroup", parent_mo_or_dn, **kwargs)
