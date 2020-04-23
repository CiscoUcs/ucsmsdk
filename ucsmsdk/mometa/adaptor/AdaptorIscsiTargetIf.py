"""This module contains the general information for AdaptorIscsiTargetIf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorIscsiTargetIfConsts:
    pass


class AdaptorIscsiTargetIf(ManagedObject):
    """This is AdaptorIscsiTargetIf class."""

    consts = AdaptorIscsiTargetIfConsts()
    naming_props = set(['priority'])

    mo_meta = MoMeta("AdaptorIscsiTargetIf", "adaptorIscsiTargetIf", "iscsi-target[priority]", VersionMeta.Version201m, "InputOutput", 0x3f, [], ["read-only"], ['adaptorHostIscsiIf'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dhcp_vendor_id": MoPropertyMeta("dhcp_vendor_id", "dhcpVendorId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "lun": MoPropertyMeta("lun", "lun", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "port_number": MoPropertyMeta("port_number", "portNumber", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority": MoPropertyMeta("priority", "priority", "ushort", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dhcpVendorId": "dhcp_vendor_id", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "ipAddress": "ip_address", 
        "lun": "lun", 
        "name": "name", 
        "portNumber": "port_number", 
        "priority": "priority", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, priority, **kwargs):
        self._dirty_mask = 0
        self.priority = priority
        self.child_action = None
        self.dhcp_vendor_id = None
        self.flt_aggr = None
        self.ip_address = None
        self.lun = None
        self.name = None
        self.port_number = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorIscsiTargetIf", parent_mo_or_dn, **kwargs)
