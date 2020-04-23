"""This module contains the general information for EquipmentNvmeDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentNvmeDefConsts:
    INT_ID_NONE = "none"
    M_SWITCH_SAS_MIXING_SUPPORTED_FALSE = "false"
    M_SWITCH_SAS_MIXING_SUPPORTED_NO = "no"
    M_SWITCH_SAS_MIXING_SUPPORTED_TRUE = "true"
    M_SWITCH_SAS_MIXING_SUPPORTED_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentNvmeDef(ManagedObject):
    """This is EquipmentNvmeDef class."""

    consts = EquipmentNvmeDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentNvmeDef", "equipmentNvmeDef", "nvme-def", VersionMeta.Version321d, "InputOutput", 0xff, [], [""], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "front_disk_slots": MoPropertyMeta("front_disk_slots", "frontDiskSlots", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "m_switch_drive_index": MoPropertyMeta("m_switch_drive_index", "mSwitchDriveIndex", "ushort", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "m_switch_sas_mixing_supported": MoPropertyMeta("m_switch_sas_mixing_supported", "mSwitchSasMixingSupported", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "max_number_of_m_switch": MoPropertyMeta("max_number_of_m_switch", "maxNumberOfMSwitch", "ushort", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "pci_slots": MoPropertyMeta("pci_slots", "pciSlots", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rear_disk_slots": MoPropertyMeta("rear_disk_slots", "rearDiskSlots", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "frontDiskSlots": "front_disk_slots", 
        "intId": "int_id", 
        "mSwitchDriveIndex": "m_switch_drive_index", 
        "mSwitchSasMixingSupported": "m_switch_sas_mixing_supported", 
        "maxNumberOfMSwitch": "max_number_of_m_switch", 
        "name": "name", 
        "pciSlots": "pci_slots", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rearDiskSlots": "rear_disk_slots", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.front_disk_slots = None
        self.int_id = None
        self.m_switch_drive_index = None
        self.m_switch_sas_mixing_supported = None
        self.max_number_of_m_switch = None
        self.name = None
        self.pci_slots = None
        self.policy_level = None
        self.policy_owner = None
        self.rear_disk_slots = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentNvmeDef", parent_mo_or_dn, **kwargs)
