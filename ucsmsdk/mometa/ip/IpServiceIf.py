"""This module contains the general information for IpServiceIf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IpServiceIfConsts:
    PREF_ALTERNATE = "alternate"
    PREF_PREFERRED = "preferred"


class IpServiceIf(ManagedObject):
    """This is IpServiceIf class."""

    consts = IpServiceIfConsts()
    naming_props = set(['addr', 'port'])

    mo_meta = MoMeta("IpServiceIf", "ipServiceIf", "serv-ip-[addr]-port-[port]", VersionMeta.Version211a, "InputOutput", 0xff, [], ["admin"], ['storageEtherIf'], [], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-65535"]),
        "pref": MoPropertyMeta("pref", "pref", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["alternate", "preferred"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "port": "port", 
        "pref": "pref", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, addr, port, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.port = port
        self.child_action = None
        self.def_gw = None
        self.pref = None
        self.sacl = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "IpServiceIf", parent_mo_or_dn, **kwargs)
