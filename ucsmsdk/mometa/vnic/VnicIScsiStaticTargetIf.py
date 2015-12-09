"""This module contains the general information for VnicIScsiStaticTargetIf ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicIScsiStaticTargetIfConsts():
    OWNER_TYPE_MANAGED = "managed"
    OWNER_TYPE_UNMANAGED = "unmanaged"
    OWNER_TYPE_UNSPECIFIED = "unspecified"


class VnicIScsiStaticTargetIf(ManagedObject):
    """This is VnicIScsiStaticTargetIf class."""

    consts = VnicIScsiStaticTargetIfConsts()
    naming_props = set([u'priority'])

    mo_meta = MoMeta("VnicIScsiStaticTargetIf", "vnicIScsiStaticTargetIf", "[priority]", VersionMeta.Version201m, "InputOutput", 0x3ffL, [], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"], [u'adaptorVlan', u'vnicIScsi', u'vnicIScsiBootVnic', u'vnicVlan'], [u'faultInst', u'vnicLun'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "auth_profile_name": MoPropertyMeta("auth_profile_name", "authProfileName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[0-9a-zA-Z\.:-]{0,223}""", [], []), 
        "oper_auth_profile_name": MoPropertyMeta("oper_auth_profile_name", "operAuthProfileName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "owner_type": MoPropertyMeta("owner_type", "ownerType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["managed", "unmanaged", "unspecified"], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["1-65535"]), 
        "priority": MoPropertyMeta("priority", "priority", "ushort", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x80L, None, None, None, [], ["1-2"]), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "authProfileName": "auth_profile_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "ipAddress": "ip_address", 
        "name": "name", 
        "operAuthProfileName": "oper_auth_profile_name", 
        "ownerType": "owner_type", 
        "port": "port", 
        "priority": "priority", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, priority, **kwargs):
        self._dirty_mask = 0
        self.priority = priority
        self.auth_profile_name = None
        self.child_action = None
        self.ip_address = None
        self.name = None
        self.oper_auth_profile_name = None
        self.owner_type = None
        self.port = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicIScsiStaticTargetIf", parent_mo_or_dn, **kwargs)

