"""This module contains the general information for EquipmentLocalDiskControllerDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentLocalDiskControllerDefConsts():
    CONFIG_PARM_MOD_SUPPORTED_FALSE = "false"
    CONFIG_PARM_MOD_SUPPORTED_NO = "no"
    CONFIG_PARM_MOD_SUPPORTED_TRUE = "true"
    CONFIG_PARM_MOD_SUPPORTED_YES = "yes"
    CONTROLLER_DEF_TYPE_EMBEDDED = "embedded"
    CONTROLLER_DEF_TYPE_NONE = "none"
    CONTROLLER_DEF_TYPE_NVME = "nvme"
    CONTROLLER_DEF_TYPE_SLOT_BASED = "slot-based"
    FORCE_UPDATE_VERSION_FALSE = "false"
    FORCE_UPDATE_VERSION_NO = "no"
    FORCE_UPDATE_VERSION_TRUE = "true"
    FORCE_UPDATE_VERSION_YES = "yes"
    INT_ID_NONE = "none"
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


class EquipmentLocalDiskControllerDef(ManagedObject):
    """This is EquipmentLocalDiskControllerDef class."""

    consts = EquipmentLocalDiskControllerDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentLocalDiskControllerDef", "equipmentLocalDiskControllerDef", "disk-controller", VersionMeta.Version131c, "InputOutput", 0xffL, [], [""], [u'equipmentLocalDiskControllerCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_parm_mod_supported": MoPropertyMeta("config_parm_mod_supported", "configParmModSupported", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "controller_def_type": MoPropertyMeta("controller_def_type", "controllerDefType", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["embedded", "none", "nvme", "slot-based"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "force_update_version": MoPropertyMeta("force_update_version", "forceUpdateVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oob_interface_supported": MoPropertyMeta("oob_interface_supported", "oobInterfaceSupported", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tfm_supported": MoPropertyMeta("tfm_supported", "tfmSupported", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configParmModSupported": "config_parm_mod_supported", 
        "controllerDefType": "controller_def_type", 
        "descr": "descr", 
        "dn": "dn", 
        "forceUpdateVersion": "force_update_version", 
        "intId": "int_id", 
        "name": "name", 
        "oobInterfaceSupported": "oob_interface_supported", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tfmSupported": "tfm_supported", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_parm_mod_supported = None
        self.controller_def_type = None
        self.descr = None
        self.force_update_version = None
        self.int_id = None
        self.name = None
        self.oob_interface_supported = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.tfm_supported = None

        ManagedObject.__init__(self, "EquipmentLocalDiskControllerDef", parent_mo_or_dn, **kwargs)

