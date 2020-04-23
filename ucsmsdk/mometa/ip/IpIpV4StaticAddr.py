"""This module contains the general information for IpIpV4StaticAddr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IpIpV4StaticAddrConsts:
    PREF_ALTERNATE = "alternate"
    PREF_PREFERRED = "preferred"


class IpIpV4StaticAddr(ManagedObject):
    """This is IpIpV4StaticAddr class."""

    consts = IpIpV4StaticAddrConsts()
    naming_props = set(['addr'])

    mo_meta = MoMeta("IpIpV4StaticAddr", "ipIpV4StaticAddr", "addr-[addr]", VersionMeta.Version211a, "InputOutput", 0x1ff, [], ["admin"], [], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "pref": MoPropertyMeta("pref", "pref", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["alternate", "preferred"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "pref": "pref", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, addr, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.child_action = None
        self.def_gw = None
        self.pref = None
        self.sacl = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "IpIpV4StaticAddr", parent_mo_or_dn, **kwargs)
