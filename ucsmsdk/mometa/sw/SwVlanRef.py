"""This module contains the general information for SwVlanRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwVlanRefConsts:
    COMPRESSION_TYPE_EXCLUDED = "excluded"
    COMPRESSION_TYPE_INCLUDED = "included"
    CONFIG_STATUS_APPLIED = "applied"
    CONFIG_STATUS_UN_APPLIED = "unApplied"


class SwVlanRef(ManagedObject):
    """This is SwVlanRef class."""

    consts = SwVlanRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("SwVlanRef", "swVlanRef", "vlanref-[id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["read-only"], ['swVlanGroup'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "compression_type": MoPropertyMeta("compression_type", "compressionType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["excluded", "included"], []),
        "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "unApplied"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-4093"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "compressionType": "compression_type", 
        "configStatus": "config_status", 
        "dn": "dn", 
        "id": "id", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.compression_type = None
        self.config_status = None
        self.peer_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SwVlanRef", parent_mo_or_dn, **kwargs)
