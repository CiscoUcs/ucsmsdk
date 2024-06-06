"""This module contains the general information for AdaptorFamilyTypeDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFamilyTypeDefConsts:
    BOOT_MODE_SECURE = "secure"
    BOOT_MODE_UNSECURE = "unsecure"
    CPLD_SUPPORT_NO = "no"
    CPLD_SUPPORT_YES = "yes"
    IS_MULTI_PORT_FALSE = "false"
    IS_MULTI_PORT_NO = "no"
    IS_MULTI_PORT_TRUE = "true"
    IS_MULTI_PORT_YES = "yes"
    IS_PASSTHROUGH_FALSE = "false"
    IS_PASSTHROUGH_NO = "no"
    IS_PASSTHROUGH_TRUE = "true"
    IS_PASSTHROUGH_YES = "yes"
    IS_RETIMER_REQUIRED_FALSE = "false"
    IS_RETIMER_REQUIRED_NO = "no"
    IS_RETIMER_REQUIRED_TRUE = "true"
    IS_RETIMER_REQUIRED_YES = "yes"
    PCIE_NODE_SUPPORT_NO = "no"
    PCIE_NODE_SUPPORT_YES = "yes"
    UBM_SUPPORT_NO = "no"
    UBM_SUPPORT_YES = "yes"


class AdaptorFamilyTypeDef(ManagedObject):
    """This is AdaptorFamilyTypeDef class."""

    consts = AdaptorFamilyTypeDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFamilyTypeDef", "adaptorFamilyTypeDef", "family-type", VersionMeta.Version202m, "InputOutput", 0xfff, [], ["read-only"], ['adaptorFruCapProvider', 'equipmentLocalDiskControllerCapProvider'], [], ["Get"])

    prop_meta = {
        "boot_mode": MoPropertyMeta("boot_mode", "bootMode", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["secure", "unsecure"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cpld_support": MoPropertyMeta("cpld_support", "cpldSupport", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "is_multi_port": MoPropertyMeta("is_multi_port", "isMultiPort", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "is_passthrough": MoPropertyMeta("is_passthrough", "isPassthrough", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "is_retimer_required": MoPropertyMeta("is_retimer_required", "isRetimerRequired", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "num_dce_ports": MoPropertyMeta("num_dce_ports", "numDcePorts", "uint", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-4294967295"]),
        "pcie_node_support": MoPropertyMeta("pcie_node_support", "pcieNodeSupport", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "port_family": MoPropertyMeta("port_family", "portFamily", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []),
        "ubm_support": MoPropertyMeta("ubm_support", "ubmSupport", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
    }

    prop_map = {
        "bootMode": "boot_mode", 
        "childAction": "child_action", 
        "cpldSupport": "cpld_support", 
        "dn": "dn", 
        "isMultiPort": "is_multi_port", 
        "isPassthrough": "is_passthrough", 
        "isRetimerRequired": "is_retimer_required", 
        "numDcePorts": "num_dce_ports", 
        "pcieNodeSupport": "pcie_node_support", 
        "portFamily": "port_family", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "ubmSupport": "ubm_support", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.boot_mode = None
        self.child_action = None
        self.cpld_support = None
        self.is_multi_port = None
        self.is_passthrough = None
        self.is_retimer_required = None
        self.num_dce_ports = None
        self.pcie_node_support = None
        self.port_family = None
        self.sacl = None
        self.status = None
        self.type = None
        self.ubm_support = None

        ManagedObject.__init__(self, "AdaptorFamilyTypeDef", parent_mo_or_dn, **kwargs)
