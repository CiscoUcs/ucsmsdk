"""This module contains the general information for VnicEthConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicEthConfigConsts:
    pass


class VnicEthConfig(ManagedObject):
    """This is VnicEthConfig class."""

    consts = VnicEthConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicEthConfig", "vnicEthConfig", "eth-vnic", VersionMeta.Version302c, "InputOutput", 0x1ff, [], ["admin", "ls-config", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['vnicIScsiInitAutoConfigPolicy'], ['faultInst'], [None])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "mac_pool_name": MoPropertyMeta("mac_pool_name", "macPoolName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "nw_ctrl_policy_name": MoPropertyMeta("nw_ctrl_policy_name", "nwCtrlPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_adaptor_profile_name": MoPropertyMeta("oper_adaptor_profile_name", "operAdaptorProfileName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_mac_pool_name": MoPropertyMeta("oper_mac_pool_name", "operMacPoolName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_nw_ctrl_policy_name": MoPropertyMeta("oper_nw_ctrl_policy_name", "operNwCtrlPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "macPoolName": "mac_pool_name", 
        "nwCtrlPolicyName": "nw_ctrl_policy_name", 
        "operAdaptorProfileName": "oper_adaptor_profile_name", 
        "operMacPoolName": "oper_mac_pool_name", 
        "operNwCtrlPolicyName": "oper_nw_ctrl_policy_name", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_profile_name = None
        self.child_action = None
        self.mac_pool_name = None
        self.nw_ctrl_policy_name = None
        self.oper_adaptor_profile_name = None
        self.oper_mac_pool_name = None
        self.oper_nw_ctrl_policy_name = None
        self.oper_stats_policy_name = None
        self.sacl = None
        self.stats_policy_name = None
        self.status = None

        ManagedObject.__init__(self, "VnicEthConfig", parent_mo_or_dn, **kwargs)
