"""This module contains the general information for NetworkLimit ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NetworkLimitConsts:
    LIMIT_STATUS_ABOVE_LIMIT = "above-limit"
    LIMIT_STATUS_ABOVE_THRESHOLD_LIMIT = "above-threshold-limit"
    LIMIT_STATUS_WITHIN_LIMIT = "within-limit"
    TYPE_DVIF = "Dvif"
    TYPE_IFTMC_PV = "IftmcPv"
    TYPE_IGMP_GROUP = "IgmpGroup"
    TYPE_MULTICAST_MAC = "MulticastMac"
    TYPE_PV_LIF_VLAN_MBR = "PvLifVlanMbr"
    TYPE_PV_SYSTEM = "PvSystem"
    TYPE_UNICAST_MAC = "UnicastMac"
    TYPE_UNICAST_MAC_LIMIT = "UnicastMacLimit"


class NetworkLimit(ManagedObject):
    """This is NetworkLimit class."""

    consts = NetworkLimitConsts()
    naming_props = set(['type', 'asicNumber'])

    mo_meta = MoMeta("NetworkLimit", "networkLimit", "limit-type-[type]-asic-[asic_number]", VersionMeta.Version321d, "InputOutput", 0x7f, [], ["admin"], ['networkElement'], ['faultInst'], [None])

    prop_meta = {
        "actual_count": MoPropertyMeta("actual_count", "actualCount", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "asic_number": MoPropertyMeta("asic_number", "asicNumber", "uint", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x2, None, None, None, [], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "end_port_number": MoPropertyMeta("end_port_number", "endPortNumber", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "limit_status": MoPropertyMeta("limit_status", "limitStatus", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["above-limit", "above-threshold-limit", "within-limit"], []),
        "lower_limit": MoPropertyMeta("lower_limit", "lowerLimit", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_number": MoPropertyMeta("slot_number", "slotNumber", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "start_port_number": MoPropertyMeta("start_port_number", "startPortNumber", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x40, None, None, None, ["Dvif", "IftmcPv", "IgmpGroup", "MulticastMac", "PvLifVlanMbr", "PvSystem", "UnicastMac", "UnicastMacLimit"], []),
        "upper_limit": MoPropertyMeta("upper_limit", "upperLimit", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
    }

    prop_map = {
        "actualCount": "actual_count", 
        "asicNumber": "asic_number", 
        "childAction": "child_action", 
        "dn": "dn", 
        "endPortNumber": "end_port_number", 
        "limitStatus": "limit_status", 
        "lowerLimit": "lower_limit", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotNumber": "slot_number", 
        "startPortNumber": "start_port_number", 
        "status": "status", 
        "type": "type", 
        "upperLimit": "upper_limit", 
    }

    def __init__(self, parent_mo_or_dn, type, asic_number, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.asic_number = asic_number
        self.actual_count = None
        self.child_action = None
        self.end_port_number = None
        self.limit_status = None
        self.lower_limit = None
        self.sacl = None
        self.slot_number = None
        self.start_port_number = None
        self.status = None
        self.upper_limit = None

        ManagedObject.__init__(self, "NetworkLimit", parent_mo_or_dn, **kwargs)
