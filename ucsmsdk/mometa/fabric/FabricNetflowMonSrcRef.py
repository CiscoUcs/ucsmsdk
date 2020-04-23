"""This module contains the general information for FabricNetflowMonSrcRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricNetflowMonSrcRefConsts:
    PROTOCOL_NETFLOW = "netflow"
    SOURCE_TYPE_PORT_PROFILE = "port-profile"
    SOURCE_TYPE_VNIC = "vnic"


class FabricNetflowMonSrcRef(ManagedObject):
    """This is FabricNetflowMonSrcRef class."""

    consts = FabricNetflowMonSrcRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FabricNetflowMonSrcRef", "fabricNetflowMonSrcRef", "flow-mon-src-ref-[id]", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricNetflowMonSession'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source_dn": MoPropertyMeta("source_dn", "sourceDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "source_type": MoPropertyMeta("source_type", "sourceType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["port-profile", "vnic"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceDn": "source_dn", 
        "sourceType": "source_type", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.protocol = None
        self.sacl = None
        self.source_dn = None
        self.source_type = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FabricNetflowMonSrcRef", parent_mo_or_dn, **kwargs)
