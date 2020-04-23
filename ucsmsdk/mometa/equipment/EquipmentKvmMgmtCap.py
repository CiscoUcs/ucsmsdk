"""This module contains the general information for EquipmentKvmMgmtCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentKvmMgmtCapConsts:
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class EquipmentKvmMgmtCap(ManagedObject):
    """This is EquipmentKvmMgmtCap class."""

    consts = EquipmentKvmMgmtCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentKvmMgmtCap", "equipmentKvmMgmtCap", "kvm-mgmt-cap", VersionMeta.Version222c, "InputOutput", 0x1f, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_kvm_cert_supported_cimc_ver": MoPropertyMeta("min_kvm_cert_supported_cimc_ver", "minKvmCertSupportedCimcVer", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_web_ui_supported_cimc_ver": MoPropertyMeta("min_web_ui_supported_cimc_ver", "minWebUISupportedCimcVer", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSupported": "is_supported", 
        "minCimcVersion": "min_cimc_version", 
        "minKvmCertSupportedCimcVer": "min_kvm_cert_supported_cimc_ver", 
        "minWebUISupportedCimcVer": "min_web_ui_supported_cimc_ver", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_supported = None
        self.min_cimc_version = None
        self.min_kvm_cert_supported_cimc_ver = None
        self.min_web_ui_supported_cimc_ver = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentKvmMgmtCap", parent_mo_or_dn, **kwargs)
