"""This module contains the general information for EquipmentSlotArrayRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentSlotArrayRefConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SLOT_SPAN_ORIENTATION_INLINE = "inline"
    SLOT_SPAN_ORIENTATION_TRANSVERSE = "transverse"
    SLOT_SPAN_ORIENTATION_UNKNOWN = "unknown"


class EquipmentSlotArrayRef(ManagedObject):
    """This is EquipmentSlotArrayRef class."""

    consts = EquipmentSlotArrayRefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentSlotArrayRef", "equipmentSlotArrayRef", "ref-[name]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["read-only"], ['adaptorFruCapProvider', 'diagSrvCapProvider', 'equipmentBaseBoardCapProvider', 'equipmentBladeBiosCapProvider', 'equipmentBladeCapProvider', 'equipmentCatalogCapProvider', 'equipmentChassisCapProvider', 'equipmentCoprocessorUnitCapProvider', 'equipmentCpldCapProvider', 'equipmentCrossFabricModuleCapProvider', 'equipmentDbgPluginCapProvider', 'equipmentFanModuleCapProvider', 'equipmentFexCapProvider', 'equipmentGemCapProvider', 'equipmentGraphicsCardCapProvider', 'equipmentHostIfCapProvider', 'equipmentIOCardCapProvider', 'equipmentIOExpanderCapProvider', 'equipmentIntelAmcCapProvider', 'equipmentLocalDiskCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentMemoryUnitCapProvider', 'equipmentMgmtCapProvider', 'equipmentMgmtExtCapProvider', 'equipmentMiniStorageCapProvider', 'equipmentPciSwitchCapProvider', 'equipmentPcieConnectorCapProvider', 'equipmentPcieNodeCapProvider', 'equipmentPersistentMemoryUnitCapProvider', 'equipmentProcessorUnitCapProvider', 'equipmentPsuCapProvider', 'equipmentRackEnclosureCapProvider', 'equipmentRackUnitCapProvider', 'equipmentRetimerCapProvider', 'equipmentSecurityUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSiocCapProvider', 'equipmentStorageEncCapProvider', 'equipmentStorageNvmeSwitchCapProvider', 'equipmentStorageSasExpanderCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider', 'equipmentTpmCapProvider', 'equipmentUbmCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, 1, 512, None, [], []),
        "number_of_slots_spanned": MoPropertyMeta("number_of_slots_spanned", "numberOfSlotsSpanned", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_span_orientation": MoPropertyMeta("slot_span_orientation", "slotSpanOrientation", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["inline", "transverse", "unknown"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "target_dn": MoPropertyMeta("target_dn", "targetDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "numberOfSlotsSpanned": "number_of_slots_spanned", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotSpanOrientation": "slot_span_orientation", 
        "status": "status", 
        "targetDn": "target_dn", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.number_of_slots_spanned = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.slot_span_orientation = None
        self.status = None
        self.target_dn = None

        ManagedObject.__init__(self, "EquipmentSlotArrayRef", parent_mo_or_dn, **kwargs)
