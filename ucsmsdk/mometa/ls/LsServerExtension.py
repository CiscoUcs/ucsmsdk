"""This module contains the general information for LsServerExtension ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsServerExtensionConsts:
    pass


class LsServerExtension(ManagedObject):
    """This is LsServerExtension class."""

    consts = LsServerExtensionConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsServerExtension", "lsServerExtension", "extension", VersionMeta.Version212a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server"], [u'lsServer'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "version": MoPropertyMeta("version", "version", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_grp_request_compute_time": MoPropertyMeta("vlan_grp_request_compute_time", "vlanGrpRequestComputeTime", "string", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "guid": "guid", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "version": "version", 
        "vlanGrpRequestComputeTime": "vlan_grp_request_compute_time", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.guid = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.version = None
        self.vlan_grp_request_compute_time = None

        ManagedObject.__init__(self, "LsServerExtension", parent_mo_or_dn, **kwargs)
