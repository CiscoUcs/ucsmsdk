"""This module contains the general information for FcpoolInitiatorEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FcpoolInitiatorEpConsts:
    PURPOSE_NODE_WWN = "node-wwn"
    PURPOSE_PORT_WWN = "port-wwn"


class FcpoolInitiatorEp(ManagedObject):
    """This is FcpoolInitiatorEp class."""

    consts = FcpoolInitiatorEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FcpoolInitiatorEp", "fcpoolInitiatorEp", "[id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["read-only"], ['fcpoolInitiator'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        "initiator_dn": MoPropertyMeta("initiator_dn", "initiatorDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["node-wwn", "port-wwn"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "initiatorDn": "initiator_dn", 
        "purpose": "purpose", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.initiator_dn = None
        self.purpose = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolInitiatorEp", parent_mo_or_dn, **kwargs)
