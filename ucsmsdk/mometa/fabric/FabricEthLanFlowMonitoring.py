"""This module contains the general information for FabricEthLanFlowMonitoring ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricEthLanFlowMonitoringConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    TYPE_ETH_FLOW_MONITORING = "eth-flow-monitoring"
    TYPE_SPAN = "span"
    TYPE_UNKNOWN = "unknown"


class FabricEthLanFlowMonitoring(ManagedObject):
    """This is FabricEthLanFlowMonitoring class."""

    consts = FabricEthLanFlowMonitoringConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricEthLanFlowMonitoring", "fabricEthLanFlowMonitoring", "eth-flow-monitoring", VersionMeta.Version221b, "InputOutput", 0x3fL, [], ["admin", "ext-lan-config", "ext-lan-policy"], [u'fabricLanMonCloud'], [u'fabricEthFlowMonLan', u'fabricFlowMonDefinition', u'fabricFlowMonExporterProfile', u'fabricNetflowCollector', u'fabricNetflowMonExporter', u'fabricNetflowMonSession', u'fabricNetflowMonitor', u'fabricNetflowTimeoutPolicy'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["eth-flow-monitoring", "span", "unknown"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FabricEthLanFlowMonitoring", parent_mo_or_dn, **kwargs)

