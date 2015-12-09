"""This module contains the general information for EquipmentSlotArrayRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentSlotArrayRefConsts():
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
    naming_props = set([u'name'])

    mo_meta = MoMeta("EquipmentSlotArrayRef", "equipmentSlotArrayRef", "ref-[name]", VersionMeta.Version101e, "InputOutput", 0xffL, [], ["read-only"], [u'adaptorFruCapProvider', u'diagSrvCapProvider', u'equipmentBaseBoardCapProvider', u'equipmentBladeBiosCapProvider', u'equipmentBladeCapProvider', u'equipmentCatalogCapProvider', u'equipmentChassisCapProvider', u'equipmentDbgPluginCapProvider', u'equipmentFanModuleCapProvider', u'equipmentFexCapProvider', u'equipmentGemCapProvider', u'equipmentGraphicsCardCapProvider', u'equipmentHostIfCapProvider', u'equipmentIOCardCapProvider', u'equipmentLocalDiskCapProvider', u'equipmentLocalDiskControllerCapProvider', u'equipmentMemoryUnitCapProvider', u'equipmentMgmtCapProvider', u'equipmentMgmtExtCapProvider', u'equipmentProcessorUnitCapProvider', u'equipmentPsuCapProvider', u'equipmentRackUnitCapProvider', u'equipmentSecurityUnitCapProvider', u'equipmentServerUnitCapProvider', u'equipmentStorageDevBridgeCapProvider', u'equipmentStorageSasExpanderCapProvider', u'equipmentSwitchCapProvider', u'equipmentSwitchIOCardCapProvider', u'equipmentSystemFruCapProvider', u'equipmentTpmCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10L, 1, 512, None, [], []), 
        "number_of_slots_spanned": MoPropertyMeta("number_of_slots_spanned", "numberOfSlotsSpanned", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "slot_span_orientation": MoPropertyMeta("slot_span_orientation", "slotSpanOrientation", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["inline", "transverse", "unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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

