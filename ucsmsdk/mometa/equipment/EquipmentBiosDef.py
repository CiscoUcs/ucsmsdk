"""This module contains the general information for EquipmentBiosDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentBiosDefConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    RESET_ON_ACTIVATE = "Activate"
    RESET_ON_UNKNOWN = "Unknown"
    RESET_ON_UPDATE = "Update"
    SECURE_BIOS_NOT_SUPPORTED = "Not supported"
    SECURE_BIOS_SUPPORTED = "Supported"
    SECURE_BIOS_UNKNOWN = "Unknown"
    STORAGE_METHOD_DUAL_FLASH = "Dual Flash"
    STORAGE_METHOD_SINGLE_FLASH = "Single Flash"
    STORAGE_METHOD_UNKNOWN = "Unknown"
    TPM_CONFIG_SUPPORT_SUPPORTED = "Supported"
    TPM_CONFIG_SUPPORT_UNSUPPORTED = "Unsupported"
    UPDATE_METHOD_MANAGEMENT_CONTROLLER = "Management Controller"
    UPDATE_METHOD_PNUOS = "Pnuos"
    UPDATE_METHOD_UNKNOWN = "Unknown"


class EquipmentBiosDef(ManagedObject):
    """This is EquipmentBiosDef class."""

    consts = EquipmentBiosDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentBiosDef", "equipmentBiosDef", "bios-def", VersionMeta.Version202m, "InputOutput", 0xff, [], [""], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "reset_on": MoPropertyMeta("reset_on", "resetOn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Activate", "Unknown", "Update"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "secure_bios": MoPropertyMeta("secure_bios", "secureBios", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Not supported", "Supported", "Unknown"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "storage_method": MoPropertyMeta("storage_method", "storageMethod", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Dual Flash", "Single Flash", "Unknown"], []),
        "tpm_config_support": MoPropertyMeta("tpm_config_support", "tpmConfigSupport", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Supported", "Unsupported"], []),
        "update_method": MoPropertyMeta("update_method", "updateMethod", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Management Controller", "Pnuos", "Unknown"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "resetOn": "reset_on", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secureBios": "secure_bios", 
        "status": "status", 
        "storageMethod": "storage_method", 
        "tpmConfigSupport": "tpm_config_support", 
        "updateMethod": "update_method", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.reset_on = None
        self.sacl = None
        self.secure_bios = None
        self.status = None
        self.storage_method = None
        self.tpm_config_support = None
        self.update_method = None

        ManagedObject.__init__(self, "EquipmentBiosDef", parent_mo_or_dn, **kwargs)
