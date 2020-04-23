"""This module contains the general information for VnicIScsiConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIScsiConfigConsts:
    IP_POOL_TYPE_SPECIFIC = "specific"
    IP_POOL_TYPE_TARGET = "target"


class VnicIScsiConfig(ManagedObject):
    """This is VnicIScsiConfig class."""

    consts = VnicIScsiConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIScsiConfig", "vnicIScsiConfig", "iscsi-vnic", VersionMeta.Version302c, "InputOutput", 0x3ff, [], ["admin", "ls-config", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['vnicIScsiInitAutoConfigPolicy'], ['faultInst'], [None])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ip_pool_name": MoPropertyMeta("ip_pool_name", "ipPoolName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "ip_pool_name_fabric_b": MoPropertyMeta("ip_pool_name_fabric_b", "ipPoolNameFabricB", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "ip_pool_type": MoPropertyMeta("ip_pool_type", "ipPoolType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["specific", "target"], []),
        "iqn_pool_name": MoPropertyMeta("iqn_pool_name", "iqnPoolName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "oper_adaptor_profile_name": MoPropertyMeta("oper_adaptor_profile_name", "operAdaptorProfileName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_ip_pool_name": MoPropertyMeta("oper_ip_pool_name", "operIpPoolName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_ip_pool_name_fabric_b": MoPropertyMeta("oper_ip_pool_name_fabric_b", "operIpPoolNameFabricB", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_iqn_pool_name": MoPropertyMeta("oper_iqn_pool_name", "operIqnPoolName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "ipPoolName": "ip_pool_name", 
        "ipPoolNameFabricB": "ip_pool_name_fabric_b", 
        "ipPoolType": "ip_pool_type", 
        "iqnPoolName": "iqn_pool_name", 
        "operAdaptorProfileName": "oper_adaptor_profile_name", 
        "operIpPoolName": "oper_ip_pool_name", 
        "operIpPoolNameFabricB": "oper_ip_pool_name_fabric_b", 
        "operIqnPoolName": "oper_iqn_pool_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_profile_name = None
        self.child_action = None
        self.ip_pool_name = None
        self.ip_pool_name_fabric_b = None
        self.ip_pool_type = None
        self.iqn_pool_name = None
        self.oper_adaptor_profile_name = None
        self.oper_ip_pool_name = None
        self.oper_ip_pool_name_fabric_b = None
        self.oper_iqn_pool_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicIScsiConfig", parent_mo_or_dn, **kwargs)
