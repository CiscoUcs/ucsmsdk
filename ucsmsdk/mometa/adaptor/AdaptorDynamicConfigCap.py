"""This module contains the general information for AdaptorDynamicConfigCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorDynamicConfigCapConsts:
    FW_VERSION_OPER_GT = "gt"
    FW_VERSION_OPER_LT = "lt"
    FW_VERSION_OPER_NONE = "none"
    FW_VERSION_OPER_RANGE = "range"


class AdaptorDynamicConfigCap(ManagedObject):
    """This is AdaptorDynamicConfigCap class."""

    consts = AdaptorDynamicConfigCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorDynamicConfigCap", "adaptorDynamicConfigCap", "cap-dynamic-config", VersionMeta.Version302c, "InputOutput", 0x7f, [], ["admin", "pn-policy", "read-only"], ['adaptorFruCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "dynamic_params": MoPropertyMeta("dynamic_params", "dynamicParams", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((defaultValue|unknown|vlan),){0,2}(defaultValue|unknown|vlan){0,1}""", [], []),
        "fw_version_hi": MoPropertyMeta("fw_version_hi", "fwVersionHi", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fw_version_lo": MoPropertyMeta("fw_version_lo", "fwVersionLo", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fw_version_oper": MoPropertyMeta("fw_version_oper", "fwVersionOper", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["gt", "lt", "none", "range"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "dynamicParams": "dynamic_params", 
        "fwVersionHi": "fw_version_hi", 
        "fwVersionLo": "fw_version_lo", 
        "fwVersionOper": "fw_version_oper", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.dynamic_params = None
        self.fw_version_hi = None
        self.fw_version_lo = None
        self.fw_version_oper = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorDynamicConfigCap", parent_mo_or_dn, **kwargs)
