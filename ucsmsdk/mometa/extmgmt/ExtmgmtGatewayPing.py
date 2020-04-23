"""This module contains the general information for ExtmgmtGatewayPing ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtmgmtGatewayPingConsts:
    pass


class ExtmgmtGatewayPing(ManagedObject):
    """This is ExtmgmtGatewayPing class."""

    consts = ExtmgmtGatewayPingConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtGatewayPing", "extmgmtGatewayPing", "gw-ping-policy", VersionMeta.Version141i, "InputOutput", 0x7f, [], ["admin", "ext-lan-config"], ['extmgmtIfMonPolicy'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "max_deadline_timeout": MoPropertyMeta("max_deadline_timeout", "maxDeadlineTimeout", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["5-15"]),
        "number_of_ping_requests": MoPropertyMeta("number_of_ping_requests", "numberOfPingRequests", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-5"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxDeadlineTimeout": "max_deadline_timeout", 
        "numberOfPingRequests": "number_of_ping_requests", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.max_deadline_timeout = None
        self.number_of_ping_requests = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtmgmtGatewayPing", parent_mo_or_dn, **kwargs)
