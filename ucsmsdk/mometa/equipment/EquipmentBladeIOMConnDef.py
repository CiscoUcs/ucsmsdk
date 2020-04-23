"""This module contains the general information for EquipmentBladeIOMConnDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentBladeIOMConnDefConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PORT_BANDWIDTH_100GBPS = "100gbps"
    PORT_BANDWIDTH_10GBPS = "10gbps"
    PORT_BANDWIDTH_1GBPS = "1gbps"
    PORT_BANDWIDTH_20GBPS = "20gbps"
    PORT_BANDWIDTH_25GBPS = "25gbps"
    PORT_BANDWIDTH_40GBPS = "40gbps"
    PORT_BANDWIDTH_AUTO = "auto"
    PORT_BANDWIDTH_INDETERMINATE = "indeterminate"


class EquipmentBladeIOMConnDef(ManagedObject):
    """This is EquipmentBladeIOMConnDef class."""

    consts = EquipmentBladeIOMConnDefConsts()
    naming_props = set(['iocardType'])

    mo_meta = MoMeta("EquipmentBladeIOMConnDef", "equipmentBladeIOMConnDef", "-iom-type-[iocard_type]", VersionMeta.Version203a, "InputOutput", 0x1ff, [], [""], ['equipmentBladeConnDef'], ['equipmentAdaptorConnDef'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version203a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version203a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "iocard_type": MoPropertyMeta("iocard_type", "iocardType", "string", VersionMeta.Version203a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "port_bandwidth": MoPropertyMeta("port_bandwidth", "portBandwidth", "string", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "iocardType": "iocard_type", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "portBandwidth": "port_bandwidth", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, iocard_type, **kwargs):
        self._dirty_mask = 0
        self.iocard_type = iocard_type
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.port_bandwidth = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBladeIOMConnDef", parent_mo_or_dn, **kwargs)
