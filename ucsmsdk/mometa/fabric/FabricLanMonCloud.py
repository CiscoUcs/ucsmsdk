"""This module contains the general information for FabricLanMonCloud ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricLanMonCloudConsts:
    MODE_END_HOST = "end-host"
    MODE_SWITCH = "switch"


class FabricLanMonCloud(ManagedObject):
    """This is FabricLanMonCloud class."""

    consts = FabricLanMonCloudConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricLanMonCloud", "fabricLanMonCloud", "lanmon", VersionMeta.Version141i, "InputOutput", 0x1f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEp'], ['fabricEthLanFlowMonitoring', 'fabricEthMonLan', 'statsThresholdPolicy'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["end-host", "switch"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "mode": "mode", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mode = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricLanMonCloud", parent_mo_or_dn, **kwargs)
