"""This module contains the general information for IppoolBlock ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IppoolBlockConsts:
    pass


class IppoolBlock(ManagedObject):
    """This is IppoolBlock class."""

    consts = IppoolBlockConsts()
    naming_props = set(['from', 'to'])

    mo_meta = MoMeta("IppoolBlock", "ippoolBlock", "block-[r_from]-[to]", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "ls-network-policy"], ['ippoolPool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version201m, MoPropertyMeta.CREATE_ONLY, 0x20, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version201m, MoPropertyMeta.CREATE_ONLY, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x200, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "to": MoPropertyMeta("to", "to", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x400, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "from": "r_from", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secDns": "sec_dns", 
        "status": "status", 
        "subnet": "subnet", 
        "to": "to", 
    }

    def __init__(self, parent_mo_or_dn, r_from, to, **kwargs):
        self._dirty_mask = 0
        self.r_from = r_from
        self.to = to
        self.child_action = None
        self.def_gw = None
        self.prim_dns = None
        self.sacl = None
        self.sec_dns = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "IppoolBlock", parent_mo_or_dn, **kwargs)
