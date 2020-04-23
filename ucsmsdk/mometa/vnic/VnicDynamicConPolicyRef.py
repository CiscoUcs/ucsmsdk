"""This module contains the general information for VnicDynamicConPolicyRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicDynamicConPolicyRefConsts:
    pass


class VnicDynamicConPolicyRef(ManagedObject):
    """This is VnicDynamicConPolicyRef class."""

    consts = VnicDynamicConPolicyRefConsts()
    naming_props = set(['conPolicyName'])

    mo_meta = MoMeta("VnicDynamicConPolicyRef", "vnicDynamicConPolicyRef", "con-ref-[con_policy_name]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin", "ls-config", "ls-network", "ls-server"], ['vnicEther', 'vnicLanConnTempl'], ['faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "oper_con_policy_name": MoPropertyMeta("oper_con_policy_name", "operConPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "operConPolicyName": "oper_con_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, con_policy_name, **kwargs):
        self._dirty_mask = 0
        self.con_policy_name = con_policy_name
        self.child_action = None
        self.oper_con_policy_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicDynamicConPolicyRef", parent_mo_or_dn, **kwargs)
