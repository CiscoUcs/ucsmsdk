"""This module contains the general information for EquipmentLocalDiskControllerDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentLocalDiskControllerDefConsts:
    AUTO_CONFIG_MODE_SUPPORTED_FALSE = "false"
    AUTO_CONFIG_MODE_SUPPORTED_NO = "no"
    AUTO_CONFIG_MODE_SUPPORTED_TRUE = "true"
    AUTO_CONFIG_MODE_SUPPORTED_YES = "yes"
    CONFIG_PARM_MOD_SUPPORTED_FALSE = "false"
    CONFIG_PARM_MOD_SUPPORTED_NO = "no"
    CONFIG_PARM_MOD_SUPPORTED_TRUE = "true"
    CONFIG_PARM_MOD_SUPPORTED_YES = "yes"
    CONTROLLER_DEF_TYPE_DUAL = "dual"
    CONTROLLER_DEF_TYPE_EMBEDDED = "embedded"
    CONTROLLER_DEF_TYPE_M2 = "m2"
    CONTROLLER_DEF_TYPE_NONE = "none"
    CONTROLLER_DEF_TYPE_NVME = "nvme"
    CONTROLLER_DEF_TYPE_NVME_HHHL = "nvme-hhhl"
    CONTROLLER_DEF_TYPE_NVME_MEZZ = "nvme-mezz"
    CONTROLLER_DEF_TYPE_PT = "pt"
    CONTROLLER_DEF_TYPE_SLOT_BASED = "slot-based"
    CONTROLLER_SUB_TYPE_NONE = "none"
    CONTROLLER_SUB_TYPE_PSATA = "psata"
    CONTROLLER_SUB_TYPE_SSATA = "ssata"
    DISK_SHARING_SUPPORTED_FALSE = "false"
    DISK_SHARING_SUPPORTED_NO = "no"
    DISK_SHARING_SUPPORTED_TRUE = "true"
    DISK_SHARING_SUPPORTED_YES = "yes"
    FORCE_UPDATE_VERSION_FALSE = "false"
    FORCE_UPDATE_VERSION_NO = "no"
    FORCE_UPDATE_VERSION_TRUE = "true"
    FORCE_UPDATE_VERSION_YES = "yes"
    HOT_PLUG_SUPPORTED_FALSE = "false"
    HOT_PLUG_SUPPORTED_NO = "no"
    HOT_PLUG_SUPPORTED_TRUE = "true"
    HOT_PLUG_SUPPORTED_YES = "yes"
    INT_ID_NONE = "none"
    JBOD_SHARING_SUPPORTED_FALSE = "false"
    JBOD_SHARING_SUPPORTED_NO = "no"
    JBOD_SHARING_SUPPORTED_TRUE = "true"
    JBOD_SHARING_SUPPORTED_YES = "yes"
    ON_BOARD_MEMORY_CHECK_NEEDED_FALSE = "false"
    ON_BOARD_MEMORY_CHECK_NEEDED_NO = "no"
    ON_BOARD_MEMORY_CHECK_NEEDED_TRUE = "true"
    ON_BOARD_MEMORY_CHECK_NEEDED_YES = "yes"
    OOB_CONTROLLER_CLASS_IDENTIFIER_AERO_MR = "aero-mr"
    OOB_CONTROLLER_CLASS_IDENTIFIER_AVENGER_RIO = "avenger-rio"
    OOB_CONTROLLER_CLASS_IDENTIFIER_AVILA_ROCK = "avila-rock"
    OOB_CONTROLLER_CLASS_IDENTIFIER_NONE = "none"
    OOB_CONTROLLER_CLASS_IDENTIFIER_NVME = "nvme"
    OOB_INTERFACE_SUPPORTED_FALSE = "false"
    OOB_INTERFACE_SUPPORTED_NO = "no"
    OOB_INTERFACE_SUPPORTED_TRUE = "true"
    OOB_INTERFACE_SUPPORTED_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    TFM_SUPPORTED_FALSE = "false"
    TFM_SUPPORTED_NO = "no"
    TFM_SUPPORTED_TRUE = "true"
    TFM_SUPPORTED_YES = "yes"
    ZONING_SUPPORTED_FALSE = "false"
    ZONING_SUPPORTED_NO = "no"
    ZONING_SUPPORTED_TRUE = "true"
    ZONING_SUPPORTED_YES = "yes"


class EquipmentLocalDiskControllerDef(ManagedObject):
    """This is EquipmentLocalDiskControllerDef class."""

    consts = EquipmentLocalDiskControllerDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentLocalDiskControllerDef", "equipmentLocalDiskControllerDef", "disk-controller", VersionMeta.Version131c, "InputOutput", 0xff, [], [""], ['equipmentLocalDiskControllerCapProvider'], [], ["Get"])

    prop_meta = {
        "auto_config_mode_supported": MoPropertyMeta("auto_config_mode_supported", "autoConfigModeSupported", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_parm_mod_supported": MoPropertyMeta("config_parm_mod_supported", "configParmModSupported", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "controller_def_type": MoPropertyMeta("controller_def_type", "controllerDefType", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["dual", "embedded", "m2", "none", "nvme", "nvme-hhhl", "nvme-mezz", "pt", "slot-based"], []),
        "controller_sub_type": MoPropertyMeta("controller_sub_type", "controllerSubType", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "psata", "ssata"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "disk_sharing_supported": MoPropertyMeta("disk_sharing_supported", "diskSharingSupported", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "force_update_version": MoPropertyMeta("force_update_version", "forceUpdateVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "hot_plug_supported": MoPropertyMeta("hot_plug_supported", "hotPlugSupported", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "jbod_sharing_supported": MoPropertyMeta("jbod_sharing_supported", "jbodSharingSupported", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "max_restricted_drives_for_raid1": MoPropertyMeta("max_restricted_drives_for_raid1", "maxRestrictedDrivesForRaid1", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "on_board_memory_check_needed": MoPropertyMeta("on_board_memory_check_needed", "onBoardMemoryCheckNeeded", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "oob_controller_class_identifier": MoPropertyMeta("oob_controller_class_identifier", "oobControllerClassIdentifier", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aero-mr", "avenger-rio", "avila-rock", "none", "nvme"], []),
        "oob_interface_supported": MoPropertyMeta("oob_interface_supported", "oobInterfaceSupported", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "tfm_supported": MoPropertyMeta("tfm_supported", "tfmSupported", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "zoning_supported": MoPropertyMeta("zoning_supported", "zoningSupported", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "autoConfigModeSupported": "auto_config_mode_supported", 
        "childAction": "child_action", 
        "configParmModSupported": "config_parm_mod_supported", 
        "controllerDefType": "controller_def_type", 
        "controllerSubType": "controller_sub_type", 
        "descr": "descr", 
        "diskSharingSupported": "disk_sharing_supported", 
        "dn": "dn", 
        "forceUpdateVersion": "force_update_version", 
        "hotPlugSupported": "hot_plug_supported", 
        "intId": "int_id", 
        "jbodSharingSupported": "jbod_sharing_supported", 
        "maxRestrictedDrivesForRaid1": "max_restricted_drives_for_raid1", 
        "name": "name", 
        "onBoardMemoryCheckNeeded": "on_board_memory_check_needed", 
        "oobControllerClassIdentifier": "oob_controller_class_identifier", 
        "oobInterfaceSupported": "oob_interface_supported", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tfmSupported": "tfm_supported", 
        "zoningSupported": "zoning_supported", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.auto_config_mode_supported = None
        self.child_action = None
        self.config_parm_mod_supported = None
        self.controller_def_type = None
        self.controller_sub_type = None
        self.descr = None
        self.disk_sharing_supported = None
        self.force_update_version = None
        self.hot_plug_supported = None
        self.int_id = None
        self.jbod_sharing_supported = None
        self.max_restricted_drives_for_raid1 = None
        self.name = None
        self.on_board_memory_check_needed = None
        self.oob_controller_class_identifier = None
        self.oob_interface_supported = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.tfm_supported = None
        self.zoning_supported = None

        ManagedObject.__init__(self, "EquipmentLocalDiskControllerDef", parent_mo_or_dn, **kwargs)
