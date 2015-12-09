"""This module contains the general information for LstorageControllerDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageControllerDefConsts():
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_UNDEPLOYED = "undeployed"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_OK = "ok"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"


class LstorageControllerDef(ManagedObject):
    """This is LstorageControllerDef class."""

    consts = LstorageControllerDefConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LstorageControllerDef", "lstorageControllerDef", "controller-def-[name]", None, "InputOutput", 0x7fL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], [u'lstorageProfile', u'lstorageProfileDef', u'storageController'], [u'lstorageControllerModeConfig', u'lstorageControllerQualifier'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", None, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["offline", "online", "undeployed"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable),){0,10}(defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "ok"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.NAMING, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute-degraded", "compute-inoperable", "offline", "online", "undefined"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "dn": "dn", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageControllerDef", parent_mo_or_dn, **kwargs)

