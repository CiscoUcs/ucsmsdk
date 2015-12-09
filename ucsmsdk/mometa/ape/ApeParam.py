"""This module contains the general information for ApeParam ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeParamConsts():
    KEY_ACTIVE_IMAGE = "ACTIVE_IMAGE"
    KEY_BIOS_ACTIVATE_STATUS = "BIOS_ACTIVATE_STATUS"
    KEY_BIOS_ACTIVE_IMAGE = "BIOS_ACTIVE_IMAGE"
    KEY_BIOS_ALTERNATE_IMAGE = "BIOS_ALTERNATE_IMAGE"
    KEY_BIOS_POWER_LOCK = "BIOS_POWER_LOCK"
    KEY_BIOS_RECOVERY_STATUS = "BIOS_RECOVERY_STATUS"
    KEY_BIOS_STARTUP_IMAGE = "BIOS_STARTUP_IMAGE"
    KEY_BIOS_UPDATE_STATUS = "BIOS_UPDATE_STATUS"
    KEY_BLADE_POWER_BUDGET = "BLADE_POWER_BUDGET"
    KEY_BLADE_UCSM_STATE = "BLADE_UCSM_STATE"
    KEY_BOOT_INSTANCE_ID = "BOOT_INSTANCE_ID"
    KEY_CAPABILITIES = "CAPABILITIES"
    KEY_CARD_BYPASS_RESET = "CARD_BYPASS_RESET"
    KEY_CHASSIS_POWER_BUDGET = "CHASSIS_POWER_BUDGET"
    KEY_CIMC_FRU_INV_VALID = "CIMC_FRU_INV_VALID"
    KEY_CIMC_SOFTWARE_VALID = "CIMC_SOFTWARE_VALID"
    KEY_CLUSTER_ID = "CLUSTER_ID"
    KEY_CMC_MODEL = "CMC_MODEL"
    KEY_COMM_STATUS = "COMM_STATUS"
    KEY_FLEX_FLASH_CAPABLE = "FLEX_FLASH_CAPABLE"
    KEY_FLEX_FLASH_CONTROLLER = "FLEX_FLASH_CONTROLLER"
    KEY_FLEX_FLASH_ENABLE_STATE = "FLEX_FLASH_ENABLE_STATE"
    KEY_FLEX_FLASH_PHY_DRIVE = "FLEX_FLASH_PHY_DRIVE"
    KEY_FLEX_FLASH_VIRT_DRIVE = "FLEX_FLASH_VIRT_DRIVE"
    KEY_FP_BUTTON_LOCK = "FP_BUTTON_LOCK"
    KEY_GET_POWER_CAP_STATUS = "GET_POWER_CAP_STATUS"
    KEY_HEALTH_STATUS = "HEALTH_STATUS"
    KEY_HOST_BIST = "HOST_BIST"
    KEY_IMAGE1_STATUS = "IMAGE1_STATUS"
    KEY_IMAGE2_STATUS = "IMAGE2_STATUS"
    KEY_LOCATE_LED_STATE = "LOCATE_LED_STATE"
    KEY_LOW_POWER_USB = "LOW_POWER_USB"
    KEY_LPC_RESET_INFO = "LPC_RESET_INFO"
    KEY_MAX_POWER_USAGE = "MAX_POWER_USAGE"
    KEY_MEZZ_POST = "MEZZ_POST"
    KEY_MIN_CHASSIS_BUDGET = "MIN_CHASSIS_BUDGET"
    KEY_MONTEREY_PARK_MODE = "MONTEREY_PARK_MODE"
    KEY_NVRAM_WORN = "NVRAM_WORN"
    KEY_PECI_TCONTROL = "PECI_TCONTROL"
    KEY_PEER_POST_STATUS = "PEER_POST_STATUS"
    KEY_PLD_UPDATE_STATUS = "PLD_UPDATE_STATUS"
    KEY_PLD_VER = "PLD_VER"
    KEY_POST_STATUS = "POST_STATUS"
    KEY_POWER_AND_BIOS_COMPLETE = "POWER_AND_BIOS_COMPLETE"
    KEY_POWER_CAP_REPORT = "POWER_CAP_REPORT"
    KEY_POWER_POLICY = "POWER_POLICY"
    KEY_POWER_POLICY_PEER = "POWER_POLICY_PEER"
    KEY_POWER_REBALANCING_ENABLE = "POWER_REBALANCING_ENABLE"
    KEY_POWER_STATUS = "POWER_STATUS"
    KEY_PROFILE_THERMAL = "PROFILE_THERMAL"
    KEY_PSU_INFO = "PSU_INFO"
    KEY_RACK_POWER_CAP_REPORT = "RACK_POWER_CAP_REPORT"
    KEY_RUNNING_IMAGE = "RUNNING_IMAGE"
    KEY_SEL_CNTRS = "SEL_CNTRS"
    KEY_SERVER_ALARMS = "SERVER_ALARMS"
    KEY_SERVER_DISCOV_CAPABLE = "SERVER_DISCOV_CAPABLE"
    KEY_SERVER_HEALTH = "SERVER_HEALTH"
    KEY_SERVER_HW_CFG_VALID = "SERVER_HW_CFG_VALID"
    KEY_SERVER_PWR_PERMISSIONS = "SERVER_PWR_PERMISSIONS"
    KEY_SESSION_INFO = "SESSION_INFO"
    KEY_SINGLE_MP_CARD_MODE = "SINGLE_MP_CARD_MODE"
    KEY_SW_BOOT_ORDER = "SW_BOOT_ORDER"
    KEY_SW_UPDATE_STATUS = "SW_UPDATE_STATUS"
    KEY_SW_VER_IMAGE_1 = "SW_VER_IMAGE_1"
    KEY_SW_VER_IMAGE_2 = "SW_VER_IMAGE_2"
    KEY_THERMAL_INFO = "THERMAL_INFO"
    KEY_TIMESTAMPS = "TIMESTAMPS"
    KEY_UBOOT_VERSION = "UBOOT_VERSION"
    KEY_UCSM_FLAG = "UCSM_FLAG"
    KEY_UCSM_MODE = "UCSM_MODE"
    KEY_UNKNOWN = "UNKNOWN"


class ApeParam(ManagedObject):
    """This is ApeParam class."""

    consts = ApeParamConsts()
    naming_props = set([u'key'])

    mo_meta = MoMeta("ApeParam", "apeParam", "param-[key]", VersionMeta.Version101e, "InputOutput", 0x7fL, [], ["read-only"], [u'apeMcTable'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8L, None, None, None, ["ACTIVE_IMAGE", "BIOS_ACTIVATE_STATUS", "BIOS_ACTIVE_IMAGE", "BIOS_ALTERNATE_IMAGE", "BIOS_POWER_LOCK", "BIOS_RECOVERY_STATUS", "BIOS_STARTUP_IMAGE", "BIOS_UPDATE_STATUS", "BLADE_POWER_BUDGET", "BLADE_UCSM_STATE", "BOOT_INSTANCE_ID", "CAPABILITIES", "CARD_BYPASS_RESET", "CHASSIS_POWER_BUDGET", "CIMC_FRU_INV_VALID", "CIMC_SOFTWARE_VALID", "CLUSTER_ID", "CMC_MODEL", "COMM_STATUS", "FLEX_FLASH_CAPABLE", "FLEX_FLASH_CONTROLLER", "FLEX_FLASH_ENABLE_STATE", "FLEX_FLASH_PHY_DRIVE", "FLEX_FLASH_VIRT_DRIVE", "FP_BUTTON_LOCK", "GET_POWER_CAP_STATUS", "HEALTH_STATUS", "HOST_BIST", "IMAGE1_STATUS", "IMAGE2_STATUS", "LOCATE_LED_STATE", "LOW_POWER_USB", "LPC_RESET_INFO", "MAX_POWER_USAGE", "MEZZ_POST", "MIN_CHASSIS_BUDGET", "MONTEREY_PARK_MODE", "NVRAM_WORN", "PECI_TCONTROL", "PEER_POST_STATUS", "PLD_UPDATE_STATUS", "PLD_VER", "POST_STATUS", "POWER_AND_BIOS_COMPLETE", "POWER_CAP_REPORT", "POWER_POLICY", "POWER_POLICY_PEER", "POWER_REBALANCING_ENABLE", "POWER_STATUS", "PROFILE_THERMAL", "PSU_INFO", "RACK_POWER_CAP_REPORT", "RUNNING_IMAGE", "SEL_CNTRS", "SERVER_ALARMS", "SERVER_DISCOV_CAPABLE", "SERVER_HEALTH", "SERVER_HW_CFG_VALID", "SERVER_PWR_PERMISSIONS", "SESSION_INFO", "SINGLE_MP_CARD_MODE", "SW_BOOT_ORDER", "SW_UPDATE_STATUS", "SW_VER_IMAGE_1", "SW_VER_IMAGE_2", "THERMAL_INFO", "TIMESTAMPS", "UBOOT_VERSION", "UCSM_FLAG", "UCSM_MODE", "UNKNOWN"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "key": "key", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, key, **kwargs):
        self._dirty_mask = 0
        self.key = key
        self.child_action = None
        self.sacl = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "ApeParam", parent_mo_or_dn, **kwargs)

