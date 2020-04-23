"""This module contains the general information for FabricSanGroupRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricSanGroupRefConsts:
    OWNER_POLICY_EXTERNAL = "policy-external"
    OWNER_POLICY_GLOBAL = "policy-global"
    OWNER_POLICY_LOCAL = "policy-local"


class FabricSanGroupRef(ManagedObject):
    """This is FabricSanGroupRef class."""

    consts = FabricSanGroupRefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricSanGroupRef", "fabricSanGroupRef", "san-group-ref-[name]", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["admin", "ls-config", "ls-network", "ls-server"], ['dcxVc', 'vnicFc', 'vnicLanConnTempl', 'vnicSanConnTempl'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["policy-external", "policy-global", "policy-local"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "operName": "oper_name", 
        "owner": "owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.oper_name = None
        self.owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricSanGroupRef", parent_mo_or_dn, **kwargs)
