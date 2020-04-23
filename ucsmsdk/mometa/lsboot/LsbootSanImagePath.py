"""This module contains the general information for LsbootSanImagePath ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsbootSanImagePathConsts:
    IP_ADDR_TYPE_IPV4 = "ipv4"
    IP_ADDR_TYPE_IPV6 = "ipv6"
    IP_ADDR_TYPE_NONE = "none"
    LUN_UNSPECIFIED = "unspecified"
    TYPE_PRIMARY = "primary"
    TYPE_SECONDARY = "secondary"


class LsbootSanImagePath(ManagedObject):
    """This is LsbootSanImagePath class."""

    consts = LsbootSanImagePathConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("LsbootSanImagePath", "lsbootSanImagePath", "path-[type]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootSanImage'], ['lsbootUEFIBootParam'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ip_addr_type": MoPropertyMeta("ip_addr_type", "ipAddrType", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ipv4", "ipv6", "none"], []),
        "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["unspecified"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, None, ["primary", "secondary"], []),
        "vnic_name": MoPropertyMeta("vnic_name", "vnicName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "wwn": MoPropertyMeta("wwn", "wwn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ipAddrType": "ip_addr_type", 
        "lun": "lun", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "vnicName": "vnic_name", 
        "wwn": "wwn", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.ip_addr_type = None
        self.lun = None
        self.sacl = None
        self.status = None
        self.vnic_name = None
        self.wwn = None

        ManagedObject.__init__(self, "LsbootSanImagePath", parent_mo_or_dn, **kwargs)
