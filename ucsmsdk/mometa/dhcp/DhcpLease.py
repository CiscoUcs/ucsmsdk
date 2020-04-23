"""This module contains the general information for DhcpLease ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DhcpLeaseConsts:
    pass


class DhcpLease(ManagedObject):
    """This is DhcpLease class."""

    consts = DhcpLeaseConsts()
    naming_props = set(['ip'])

    mo_meta = MoMeta("DhcpLease", "dhcpLease", "lease-[ip]", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["read-only"], ['dhcpInst'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cli_id": MoPropertyMeta("cli_id", "cliId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 1, 128, None, [], []),
        "cookie": MoPropertyMeta("cookie", "cookie", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ends": MoPropertyMeta("ends", "ends", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "intf": MoPropertyMeta("intf", "intf", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "starts": MoPropertyMeta("starts", "starts", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "cliId": "cli_id", 
        "cookie": "cookie", 
        "dn": "dn", 
        "ends": "ends", 
        "hostname": "hostname", 
        "intf": "intf", 
        "ip": "ip", 
        "mac": "mac", 
        "rn": "rn", 
        "sacl": "sacl", 
        "starts": "starts", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, ip, **kwargs):
        self._dirty_mask = 0
        self.ip = ip
        self.child_action = None
        self.cli_id = None
        self.cookie = None
        self.ends = None
        self.hostname = None
        self.intf = None
        self.mac = None
        self.sacl = None
        self.starts = None
        self.status = None

        ManagedObject.__init__(self, "DhcpLease", parent_mo_or_dn, **kwargs)
