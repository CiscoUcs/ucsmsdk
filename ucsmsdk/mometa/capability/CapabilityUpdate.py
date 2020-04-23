"""This module contains the general information for CapabilityUpdate ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CapabilityUpdateConsts:
    pass


class CapabilityUpdate(ManagedObject):
    """This is CapabilityUpdate class."""

    consts = CapabilityUpdateConsts()
    naming_props = set(['version'])

    mo_meta = MoMeta("CapabilityUpdate", "capabilityUpdate", "update-[version]", VersionMeta.Version131c, "InputOutput", 0x3f, [], ["admin"], ['capabilityEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "image_name": MoPropertyMeta("image_name", "imageName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 1, 64, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "update_ts": MoPropertyMeta("update_ts", "updateTs", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "imageName": "image_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "updateTs": "update_ts", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, version, **kwargs):
        self._dirty_mask = 0
        self.version = version
        self.child_action = None
        self.image_name = None
        self.sacl = None
        self.status = None
        self.update_ts = None

        ManagedObject.__init__(self, "CapabilityUpdate", parent_mo_or_dn, **kwargs)
