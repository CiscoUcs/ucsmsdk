"""This module contains the general information for PciEquipSlot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PciEquipSlotConsts:
    DISCOVERY_STATE_AUTO_UPGRADING = "auto-upgrading"
    DISCOVERY_STATE_DISCOVERED = "discovered"
    DISCOVERY_STATE_OFFLINE = "offline"
    DISCOVERY_STATE_ONLINE = "online"
    DISCOVERY_STATE_PINGLOST = "pinglost"
    DISCOVERY_STATE_UNKNOWN = "unknown"
    DISCOVERY_STATE_UNSECURE = "unsecure"
    DISCOVERY_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    SPDM_FAULT_FALSE = "false"
    SPDM_FAULT_NO = "no"
    SPDM_FAULT_TRUE = "true"
    SPDM_FAULT_YES = "yes"


class PciEquipSlot(ManagedObject):
    """This is PciEquipSlot class."""

    consts = PciEquipSlotConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("PciEquipSlot", "pciEquipSlot", "equipped-slot-[id]", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "controller_reported": MoPropertyMeta("controller_reported", "controllerReported", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "discovery_state": MoPropertyMeta("discovery_state", "discoveryState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto-upgrading", "discovered", "offline", "online", "pinglost", "unknown", "unsecure", "unsupported-connectivity"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "host_reported": MoPropertyMeta("host_reported", "hostReported", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-5000"]),
        "mac_left": MoPropertyMeta("mac_left", "macLeft", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "mac_right": MoPropertyMeta("mac_right", "macRight", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "smbios_id": MoPropertyMeta("smbios_id", "smbiosId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "spdm_fault": MoPropertyMeta("spdm_fault", "spdmFault", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "spdm_fault_desc": MoPropertyMeta("spdm_fault_desc", "spdmFaultDesc", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerReported": "controller_reported", 
        "discoveryState": "discovery_state", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "hostReported": "host_reported", 
        "id": "id", 
        "macLeft": "mac_left", 
        "macRight": "mac_right", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "smbiosId": "smbios_id", 
        "spdmFault": "spdm_fault", 
        "spdmFaultDesc": "spdm_fault_desc", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.controller_reported = None
        self.discovery_state = None
        self.flt_aggr = None
        self.host_reported = None
        self.mac_left = None
        self.mac_right = None
        self.model = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.smbios_id = None
        self.spdm_fault = None
        self.spdm_fault_desc = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "PciEquipSlot", parent_mo_or_dn, **kwargs)
