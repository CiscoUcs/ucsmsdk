"""This module contains the general information for SwEtherPort ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwEtherPortConsts:
    pass


class SwEtherPort(ManagedObject):
    """This is SwEtherPort class."""

    consts = SwEtherPortConsts()
    naming_props = set(['slotId', 'aggrPortId', 'portId'])

    mo_meta = MoMeta("SwEtherPort", "swEtherPort", "slot-[slot_id]-aggrport-[aggr_port_id]-port-[port_id]", VersionMeta.Version321d, "InputOutput", 0xff, [], ["admin"], ['swPortDiscover'], [], [None])

    prop_meta = {
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x2, None, None, None, [], ["1-64"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-64"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-7"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "aggrPortId": "aggr_port_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, aggr_port_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.aggr_port_id = aggr_port_id
        self.port_id = port_id
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SwEtherPort", parent_mo_or_dn, **kwargs)
