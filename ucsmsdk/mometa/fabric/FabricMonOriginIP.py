"""This module contains the general information for FabricMonOriginIP ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricMonOriginIPConsts:
    FABRIC_ID_A = "A"
    FABRIC_ID_B = "B"
    FABRIC_ID_NONE = "NONE"


class FabricMonOriginIP(ManagedObject):
    """This is FabricMonOriginIP class."""

    consts = FabricMonOriginIPConsts()
    naming_props = set(['fabricId'])

    mo_meta = MoMeta("FabricMonOriginIP", "fabricMonOriginIP", "origin-[fabric_id]", VersionMeta.Version434a, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['adaptorHostIscsiIf', 'adaptorVlan', 'fabricMonOriginSVI', 'vnicIPv4If'], [], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "fabric_id": MoPropertyMeta("fabric_id", "fabricId", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["A", "B", "NONE"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "fabricId": "fabric_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, fabric_id, **kwargs):
        self._dirty_mask = 0
        self.fabric_id = fabric_id
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.sacl = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "FabricMonOriginIP", parent_mo_or_dn, **kwargs)
