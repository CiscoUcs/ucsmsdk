"""This module contains the general information for SwVirtL3Intf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwVirtL3IntfConsts:
    pass


class SwVirtL3Intf(ManagedObject):
    """This is SwVirtL3Intf class."""

    consts = SwVirtL3IntfConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SwVirtL3Intf", "swVirtL3Intf", "l3-vlan-[name]", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["read-only"], ['swEthLanFlowMon'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "netmask": MoPropertyMeta("netmask", "netmask", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vlan_id": MoPropertyMeta("vlan_id", "vlanId", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ipAddress": "ip_address", 
        "name": "name", 
        "netmask": "netmask", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vlanId": "vlan_id", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.ip_address = None
        self.netmask = None
        self.sacl = None
        self.status = None
        self.vlan_id = None

        ManagedObject.__init__(self, "SwVirtL3Intf", parent_mo_or_dn, **kwargs)
