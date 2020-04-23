"""This module contains the general information for LsVersionBeh ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsVersionBehConsts:
    PCI_ENUM_MULTI_FUNC_ALL = "multi-func-all"
    PCI_ENUM_STATIC_ZERO_FUNC = "static-zero-func"
    PCI_ENUM_ZERO_FUNC_ALL = "zero-func-all"
    VCON_MAP_LINEAR_ORDERED = "linear-ordered"
    VCON_MAP_LINEAR_ORDERED_TO_ROUND_ROBIN = "linear-ordered-to-round-robin"
    VCON_MAP_ROUND_ROBIN = "round-robin"
    VCON_MAP_ROUND_ROBIN_TO_LINEAR_ORDERED = "round-robin-to-linear-ordered"
    VNIC_MAP_CAP_LOAD_DISTRIBUTE = "cap-load-distribute"
    VNIC_MAP_PHYSICAL_CAP_FIRST = "physical-cap-first"
    VNIC_ORDER_ALL_VNIC = "all-vnic"
    VNIC_ORDER_DYNAMIC_ALL_LAST = "dynamic-all-last"
    VNIC_ORDER_STATIC_ALL_FIRST = "static-all-first"


class LsVersionBeh(ManagedObject):
    """This is LsVersionBeh class."""

    consts = LsVersionBehConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsVersionBeh", "lsVersionBeh", "ls-vers-beh", VersionMeta.Version201q, "InputOutput", 0x1ff, [], ["admin"], ['lsServer'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201q, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201q, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "pci_enum": MoPropertyMeta("pci_enum", "pciEnum", "string", VersionMeta.Version201q, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["multi-func-all", "static-zero-func", "zero-func-all"], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201q, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201q, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vcon_map": MoPropertyMeta("vcon_map", "vconMap", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["linear-ordered", "linear-ordered-to-round-robin", "round-robin", "round-robin-to-linear-ordered"], []),
        "vnic_map": MoPropertyMeta("vnic_map", "vnicMap", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["cap-load-distribute", "physical-cap-first"], []),
        "vnic_order": MoPropertyMeta("vnic_order", "vnicOrder", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["all-vnic", "dynamic-all-last", "static-all-first"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "pciEnum": "pci_enum", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vconMap": "vcon_map", 
        "vnicMap": "vnic_map", 
        "vnicOrder": "vnic_order", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.pci_enum = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.vcon_map = None
        self.vnic_map = None
        self.vnic_order = None

        ManagedObject.__init__(self, "LsVersionBeh", parent_mo_or_dn, **kwargs)
