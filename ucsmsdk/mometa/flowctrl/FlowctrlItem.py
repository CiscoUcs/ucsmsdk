"""This module contains the general information for FlowctrlItem ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FlowctrlItemConsts:
    CONFIG_NOT_SUPPORTED = "not-supported"
    CONFIG_OK = "ok"
    PRIO_AUTO = "auto"
    PRIO_ON = "on"
    RCV_OFF = "off"
    RCV_ON = "on"
    SND_OFF = "off"
    SND_ON = "on"


class FlowctrlItem(ManagedObject):
    """This is FlowctrlItem class."""

    consts = FlowctrlItemConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FlowctrlItem", "flowctrlItem", "policy-[name]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "ls-network", "ls-network-policy", "ls-qos-policy"], ['flowctrlDefinition'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config": MoPropertyMeta("config", "config", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-supported", "ok"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "on"], []),
        "rcv": MoPropertyMeta("rcv", "rcv", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["off", "on"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "snd": MoPropertyMeta("snd", "snd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["off", "on"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "config": "config", 
        "dn": "dn", 
        "name": "name", 
        "prio": "prio", 
        "rcv": "rcv", 
        "rn": "rn", 
        "sacl": "sacl", 
        "snd": "snd", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config = None
        self.prio = None
        self.rcv = None
        self.sacl = None
        self.snd = None
        self.status = None

        ManagedObject.__init__(self, "FlowctrlItem", parent_mo_or_dn, **kwargs)
