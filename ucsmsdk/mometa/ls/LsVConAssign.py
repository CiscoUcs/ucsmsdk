"""This module contains the general information for LsVConAssign ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsVConAssignConsts:
    ADMIN_HOST_PORT_1 = "1"
    ADMIN_HOST_PORT_2 = "2"
    ADMIN_HOST_PORT_ANY = "ANY"
    ADMIN_HOST_PORT_NONE = "NONE"
    ADMIN_VCON_1 = "1"
    ADMIN_VCON_2 = "2"
    ADMIN_VCON_3 = "3"
    ADMIN_VCON_4 = "4"
    ADMIN_VCON_ANY = "any"
    ORDER_UNSPECIFIED = "unspecified"


class LsVConAssign(ManagedObject):
    """This is LsVConAssign class."""

    consts = LsVConAssignConsts()
    naming_props = set(['transport', 'vnicName'])

    mo_meta = MoMeta("LsVConAssign", "lsVConAssign", "assign-[transport]-vnic-[vnic_name]", VersionMeta.Version211a, "InputOutput", 0x3ff, [], ["admin", "ls-compute", "ls-config", "ls-server"], ['lsServer'], [], ["Get", "Set"])

    prop_meta = {
        "admin_host_port": MoPropertyMeta("admin_host_port", "adminHostPort", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["1", "2", "ANY", "NONE"], []),
        "admin_vcon": MoPropertyMeta("admin_vcon", "adminVcon", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["1", "2", "3", "4", "any"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["unspecified"], ["0-256"]),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x100, None, None, r"""((fc|ethernet|defaultValue),){0,2}(fc|ethernet|defaultValue){0,1}""", [], []),
        "vnic_name": MoPropertyMeta("vnic_name", "vnicName", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
    }

    prop_map = {
        "adminHostPort": "admin_host_port", 
        "adminVcon": "admin_vcon", 
        "childAction": "child_action", 
        "dn": "dn", 
        "order": "order", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
        "vnicName": "vnic_name", 
    }

    def __init__(self, parent_mo_or_dn, transport, vnic_name, **kwargs):
        self._dirty_mask = 0
        self.transport = transport
        self.vnic_name = vnic_name
        self.admin_host_port = None
        self.admin_vcon = None
        self.child_action = None
        self.order = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LsVConAssign", parent_mo_or_dn, **kwargs)
