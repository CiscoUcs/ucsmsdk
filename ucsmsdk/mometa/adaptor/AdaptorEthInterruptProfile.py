"""This module contains the general information for AdaptorEthInterruptProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthInterruptProfileConsts:
    COALESCING_TYPE_IDLE = "idle"
    COALESCING_TYPE_MIN = "min"
    MODE_INTX = "intx"
    MODE_MSI = "msi"
    MODE_MSI_X = "msi-x"


class AdaptorEthInterruptProfile(ManagedObject):
    """This is AdaptorEthInterruptProfile class."""

    consts = AdaptorEthInterruptProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthInterruptProfile", "adaptorEthInterruptProfile", "eth-int", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIf', 'adaptorHostEthIfProfile', 'adaptorUsnicConnDef', 'adaptorVmmqConnDef'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "coalescing_time": MoPropertyMeta("coalescing_time", "coalescingTime", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-65535"]),
        "coalescing_type": MoPropertyMeta("coalescing_type", "coalescingType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["idle", "min"], []),
        "count": MoPropertyMeta("count", "count", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-1024"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["intx", "msi", "msi-x"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "coalescingTime": "coalescing_time", 
        "coalescingType": "coalescing_type", 
        "count": "count", 
        "dn": "dn", 
        "mode": "mode", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.coalescing_time = None
        self.coalescing_type = None
        self.count = None
        self.mode = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthInterruptProfile", parent_mo_or_dn, **kwargs)
