"""This module contains the general information for IppoolIpV6Block ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IppoolIpV6BlockConsts:
    pass


class IppoolIpV6Block(ManagedObject):
    """This is IppoolIpV6Block class."""

    consts = IppoolIpV6BlockConsts()
    naming_props = set(['from', 'to'])

    mo_meta = MoMeta("IppoolIpV6Block", "ippoolIpV6Block", "v6block-[r_from]-[to]", VersionMeta.Version221b, "InputOutput", 0x7ff, [], ["admin", "ls-network-policy"], ['ippoolPool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version221b, MoPropertyMeta.CREATE_ONLY, 0x4, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x10, 0, 256, None, [], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version221b, MoPropertyMeta.CREATE_ONLY, 0x20, None, None, None, [], ["1-127"]),
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version221b, MoPropertyMeta.CREATE_ONLY, 0x40, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version221b, MoPropertyMeta.CREATE_ONLY, 0x100, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "to": MoPropertyMeta("to", "to", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x400, 0, 256, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "from": "r_from", 
        "prefix": "prefix", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secDns": "sec_dns", 
        "status": "status", 
        "to": "to", 
    }

    def __init__(self, parent_mo_or_dn, r_from, to, **kwargs):
        self._dirty_mask = 0
        self.r_from = r_from
        self.to = to
        self.child_action = None
        self.def_gw = None
        self.prefix = None
        self.prim_dns = None
        self.sacl = None
        self.sec_dns = None
        self.status = None

        ManagedObject.__init__(self, "IppoolIpV6Block", parent_mo_or_dn, **kwargs)
