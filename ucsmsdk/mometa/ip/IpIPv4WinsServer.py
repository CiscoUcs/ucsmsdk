"""This module contains the general information for IpIPv4WinsServer ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IpIPv4WinsServerConsts:
    pass


class IpIPv4WinsServer(ManagedObject):
    """This is IpIPv4WinsServer class."""

    consts = IpIPv4WinsServerConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("IpIPv4WinsServer", "ipIPv4WinsServer", "wins-server-[name]", VersionMeta.Version221b, "InputOutput", 0x1ff, [], ["admin", "ls-network-policy"], ['ippoolPool'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "i_pv4_address": MoPropertyMeta("i_pv4_address", "IPv4Address", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "IPv4Address": "i_pv4_address", 
        "childAction": "child_action", 
        "dn": "dn", 
        "guid": "guid", 
        "host": "host", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.i_pv4_address = None
        self.child_action = None
        self.guid = None
        self.host = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "IpIPv4WinsServer", parent_mo_or_dn, **kwargs)
