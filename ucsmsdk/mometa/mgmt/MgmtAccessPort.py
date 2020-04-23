"""This module contains the general information for MgmtAccessPort ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtAccessPortConsts:
    PORT_NONE = "none"
    PROTOCOL_TCP = "TCP"
    PROTOCOL_UDP = "UDP"


class MgmtAccessPort(ManagedObject):
    """This is MgmtAccessPort class."""

    consts = MgmtAccessPortConsts()
    naming_props = set(['protocol', 'port'])

    mo_meta = MoMeta("MgmtAccessPort", "mgmtAccessPort", "[protocol]-port-[port]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['mgmtAccessPolicyItem'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, ["none"], ["0-65536"]),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, ["TCP", "UDP"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "port": "port", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, protocol, port, **kwargs):
        self._dirty_mask = 0
        self.protocol = protocol
        self.port = port
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtAccessPort", parent_mo_or_dn, **kwargs)
