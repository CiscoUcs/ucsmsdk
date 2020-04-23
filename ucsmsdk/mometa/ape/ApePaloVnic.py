"""This module contains the general information for ApePaloVnic ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApePaloVnicConsts:
    FAILOVER_FALSE = "false"
    FAILOVER_NO = "no"
    FAILOVER_TRUE = "true"
    FAILOVER_YES = "yes"
    PASS_THRU_FALSE = "false"
    PASS_THRU_NO = "no"
    PASS_THRU_TRUE = "true"
    PASS_THRU_YES = "yes"
    STATE_CREATE_PEND = "CreatePend"
    STATE_CREATING = "Creating"
    STATE_DESTROY_PEND = "DestroyPend"
    STATE_DESTROYING = "Destroying"
    STATE_MODIFY_PEND = "ModifyPend"
    STATE_MODIFYING = "Modifying"
    STATE_PRESENT = "Present"
    STATE_UNKNOWN = "Unknown"
    TYPE_ETH = "Eth"
    TYPE_FC = "Fc"
    TYPE_SCSI = "Scsi"
    TYPE_UNKNOWN = "Unknown"
    VM_WARE_FALSE = "false"
    VM_WARE_NO = "no"
    VM_WARE_TRUE = "true"
    VM_WARE_YES = "yes"


class ApePaloVnic(ManagedObject):
    """This is ApePaloVnic class."""

    consts = ApePaloVnicConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ApePaloVnic", "apePaloVnic", "AdapterVnic-[name]", VersionMeta.Version211a, "InputOutput", 0x1fffff, [], ["read-only"], ['apeMenlo', 'apePalo'], ['apeMenloVnicStats', 'apePaloVnicStats'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cookie": MoPropertyMeta("cookie", "cookie", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
        "cos": MoPropertyMeta("cos", "cos", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "failover": MoPropertyMeta("failover", "failover", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "mtu": MoPropertyMeta("mtu", "mtu", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "nic_dn": MoPropertyMeta("nic_dn", "nicDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "pass_thru": MoPropertyMeta("pass_thru", "passThru", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["CreatePend", "Creating", "DestroyPend", "Destroying", "ModifyPend", "Modifying", "Present", "Unknown"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "stdby_vif_id": MoPropertyMeta("stdby_vif_id", "stdbyVifId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Eth", "Fc", "Scsi", "Unknown"], []),
        "uplink_port_id": MoPropertyMeta("uplink_port_id", "uplinkPortId", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []),
        "vif_id": MoPropertyMeta("vif_id", "vifId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], []),
        "vif_type": MoPropertyMeta("vif_type", "vifType", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], []),
        "vlan_id": MoPropertyMeta("vlan_id", "vlanId", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, [], []),
        "vm_ware": MoPropertyMeta("vm_ware", "vmWare", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["false", "no", "true", "yes"], []),
        "vntag": MoPropertyMeta("vntag", "vntag", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, [], []),
        "wwnn": MoPropertyMeta("wwnn", "wwnn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100000, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "cookie": "cookie", 
        "cos": "cos", 
        "dn": "dn", 
        "failover": "failover", 
        "mac": "mac", 
        "mtu": "mtu", 
        "name": "name", 
        "nicDn": "nic_dn", 
        "passThru": "pass_thru", 
        "rn": "rn", 
        "sacl": "sacl", 
        "state": "state", 
        "status": "status", 
        "stdbyVifId": "stdby_vif_id", 
        "type": "type", 
        "uplinkPortId": "uplink_port_id", 
        "vifId": "vif_id", 
        "vifType": "vif_type", 
        "vlanId": "vlan_id", 
        "vmWare": "vm_ware", 
        "vntag": "vntag", 
        "wwnn": "wwnn", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.cookie = None
        self.cos = None
        self.failover = None
        self.mac = None
        self.mtu = None
        self.nic_dn = None
        self.pass_thru = None
        self.sacl = None
        self.state = None
        self.status = None
        self.stdby_vif_id = None
        self.type = None
        self.uplink_port_id = None
        self.vif_id = None
        self.vif_type = None
        self.vlan_id = None
        self.vm_ware = None
        self.vntag = None
        self.wwnn = None

        ManagedObject.__init__(self, "ApePaloVnic", parent_mo_or_dn, **kwargs)
