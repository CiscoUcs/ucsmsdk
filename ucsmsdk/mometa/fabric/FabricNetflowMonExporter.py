"""This module contains the general information for FabricNetflowMonExporter ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricNetflowMonExporterConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTOCOL_NETFLOW = "netflow"
    TRANSPORT_PROTOCOL_SCTP = "sctp"
    TRANSPORT_PROTOCOL_UDP = "udp"
    VERSION_IPFIX = "ipfix"
    VERSION_V9 = "v9"


class FabricNetflowMonExporter(ManagedObject):
    """This is FabricNetflowMonExporter class."""

    consts = FabricNetflowMonExporterConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricNetflowMonExporter", "fabricNetflowMonExporter", "lanFlowMonExporter-eth-netflow-[name]", VersionMeta.Version221b, "InputOutput", 0x3fff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthLanFlowMonitoring'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "dscp": MoPropertyMeta("dscp", "dscp", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-63"]),
        "export_internal": MoPropertyMeta("export_internal", "exportInternal", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "exporter_stats_timeout": MoPropertyMeta("exporter_stats_timeout", "exporterStatsTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["60-86400"]),
        "flow_exp_profile": MoPropertyMeta("flow_exp_profile", "flowExpProfile", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "flow_mon_collector": MoPropertyMeta("flow_mon_collector", "flowMonCollector", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "interface_table_timeout": MoPropertyMeta("interface_table_timeout", "interfaceTableTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["60-86400"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_flow_exp_profile": MoPropertyMeta("oper_flow_exp_profile", "operFlowExpProfile", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["local", "pending-policy", "policy"], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "template_data_timeout": MoPropertyMeta("template_data_timeout", "templateDataTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], ["60-86400"]),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "transport_protocol": MoPropertyMeta("transport_protocol", "transportProtocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["sctp", "udp"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipfix", "v9"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "dscp": "dscp", 
        "exportInternal": "export_internal", 
        "exporterStatsTimeout": "exporter_stats_timeout", 
        "flowExpProfile": "flow_exp_profile", 
        "flowMonCollector": "flow_mon_collector", 
        "intId": "int_id", 
        "interfaceTableTimeout": "interface_table_timeout", 
        "name": "name", 
        "operFlowExpProfile": "oper_flow_exp_profile", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
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
        self.descr = None
        self.dscp = None
        self.export_internal = None
        self.exporter_stats_timeout = None
        self.flow_exp_profile = None
        self.flow_mon_collector = None
        self.int_id = None
        self.interface_table_timeout = None
        self.oper_flow_exp_profile = None
        self.policy_level = None
        self.policy_owner = None
        self.protocol = None
        self.sacl = None
        self.status = None
        self.template_data_timeout = None
        self.transport = None
        self.transport_protocol = None
        self.type = None
        self.version = None

        ManagedObject.__init__(self, "FabricNetflowMonExporter", parent_mo_or_dn, **kwargs)
