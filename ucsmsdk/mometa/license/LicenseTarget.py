"""This module contains the general information for LicenseTarget ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LicenseTargetConsts:
    IS_RACK_PRESENT_FALSE = "false"
    IS_RACK_PRESENT_NO = "no"
    IS_RACK_PRESENT_TRUE = "true"
    IS_RACK_PRESENT_YES = "yes"


class LicenseTarget(ManagedObject):
    """This is LicenseTarget class."""

    consts = LicenseTargetConsts()
    naming_props = set(['slotId', 'aggrPortId', 'portId'])

    mo_meta = MoMeta("LicenseTarget", "licenseTarget", "slot-[slot_id]-aggr-port-[aggr_port_id]-port-[port_id]", VersionMeta.Version223a, "InputOutput", 0xff, [], ["admin"], ['licenseInstance'], [], [None])

    prop_meta = {
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version311e, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "is_rack_present": MoPropertyMeta("is_rack_present", "isRackPresent", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version223a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version223a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "aggrPortId": "aggr_port_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "isRackPresent": "is_rack_present", 
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
        self.is_rack_present = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LicenseTarget", parent_mo_or_dn, **kwargs)
