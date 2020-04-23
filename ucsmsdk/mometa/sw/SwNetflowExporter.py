"""This module contains the general information for SwNetflowExporter ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwNetflowExporterConsts:
    IS_VALID_CONFIG_INCOMPLETE = "incomplete"
    IS_VALID_CONFIG_OK = "ok"
    LIFE_CYCLE_DELETED = "deleted"
    LIFE_CYCLE_NEW = "new"
    LIFE_CYCLE_NORMAL = "normal"
    PROTOCOL_NETFLOW = "netflow"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TRANSPORT_PROTOCOL_SCTP = "sctp"
    TRANSPORT_PROTOCOL_UDP = "udp"
    VERSION_IPFIX = "ipfix"
    VERSION_V9 = "v9"


class SwNetflowExporter(ManagedObject):
    """This is SwNetflowExporter class."""

    consts = SwNetflowExporterConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SwNetflowExporter", "swNetflowExporter", "flowexporter-netflow-[name]", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["read-only"], ['swEthLanFlowMon'], ['swVlan'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "destination_ip_address": MoPropertyMeta("destination_ip_address", "destinationIpAddress", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "destination_port": MoPropertyMeta("destination_port", "destinationPort", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "dscp": MoPropertyMeta("dscp", "dscp", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "export_internal": MoPropertyMeta("export_internal", "exportInternal", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "exporter_stats_timeout": MoPropertyMeta("exporter_stats_timeout", "exporterStatsTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "interface_table_timeout": MoPropertyMeta("interface_table_timeout", "interfaceTableTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "is_valid_config": MoPropertyMeta("is_valid_config", "isValidConfig", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["incomplete", "ok"], []),
        "life_cycle": MoPropertyMeta("life_cycle", "lifeCycle", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deleted", "new", "normal"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source_vlan": MoPropertyMeta("source_vlan", "sourceVlan", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "template_data_timeout": MoPropertyMeta("template_data_timeout", "templateDataTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "transport_protocol": MoPropertyMeta("transport_protocol", "transportProtocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["sctp", "udp"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipfix", "v9"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "destinationIpAddress": "destination_ip_address", 
        "destinationPort": "destination_port", 
        "dn": "dn", 
        "dscp": "dscp", 
        "exportInternal": "export_internal", 
        "exporterStatsTimeout": "exporter_stats_timeout", 
        "interfaceTableTimeout": "interface_table_timeout", 
        "isValidConfig": "is_valid_config", 
        "lifeCycle": "life_cycle", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceVlan": "source_vlan", 
        "status": "status", 
        "switchId": "switch_id", 
        "templateDataTimeout": "template_data_timeout", 
        "transport": "transport", 
        "transportProtocol": "transport_protocol", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.destination_ip_address = None
        self.destination_port = None
        self.dscp = None
        self.export_internal = None
        self.exporter_stats_timeout = None
        self.interface_table_timeout = None
        self.is_valid_config = None
        self.life_cycle = None
        self.peer_dn = None
        self.protocol = None
        self.sacl = None
        self.source_vlan = None
        self.status = None
        self.switch_id = None
        self.template_data_timeout = None
        self.transport = None
        self.transport_protocol = None
        self.type = None
        self.version = None

        ManagedObject.__init__(self, "SwNetflowExporter", parent_mo_or_dn, **kwargs)
