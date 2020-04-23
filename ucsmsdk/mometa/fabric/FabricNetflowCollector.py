"""This module contains the general information for FabricNetflowCollector ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricNetflowCollectorConsts:
    FLOW_PROTOCOL_NETFLOW = "netflow"
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"


class FabricNetflowCollector(ManagedObject):
    """This is FabricNetflowCollector class."""

    consts = FabricNetflowCollectorConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricNetflowCollector", "fabricNetflowCollector", "flow-collector-[name]", VersionMeta.Version221b, "InputOutput", 0x3ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthLanFlowMonitoring'], ['ipIpV4StaticTargetAddr'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "flow_protocol": MoPropertyMeta("flow_protocol", "flowProtocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version221b, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, None, ["A", "B", "NONE"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source_vlan": MoPropertyMeta("source_vlan", "sourceVlan", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []),
        "source_vlan_dn": MoPropertyMeta("source_vlan_dn", "sourceVlanDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "flowProtocol": "flow_protocol", 
        "id": "id", 
        "locale": "locale", 
        "name": "name", 
        "port": "port", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceVlan": "source_vlan", 
        "sourceVlanDn": "source_vlan_dn", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.flow_protocol = None
        self.id = None
        self.locale = None
        self.port = None
        self.sacl = None
        self.source_vlan = None
        self.source_vlan_dn = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricNetflowCollector", parent_mo_or_dn, **kwargs)
