"""This module contains the general information for ExtpolClient ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtpolClientConsts:
    CONN_PROTOCOL_IPV4 = "ipv4"
    CONN_PROTOCOL_IPV6 = "ipv6"
    CONN_PROTOCOL_UNKNOWN = "unknown"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    OPER_STATE_LOST_VISIBILITY = "lost-visibility"
    OPER_STATE_REGISTERED = "registered"
    OPER_STATE_REGISTERING = "registering"
    OPER_STATE_REGISTRY_NOT_REACHABLE = "registry-not-reachable"
    OPER_STATE_SYNCHRONIZING = "synchronizing"
    OPER_STATE_UNREGISTERED = "unregistered"
    OPER_STATE_VERSION_MISMATCH = "version-mismatch"
    SUSPEND_STATE_OFF = "off"
    SUSPEND_STATE_ON = "on"
    TYPE_APE = "ape"
    TYPE_BOOT_MGR = "boot-mgr"
    TYPE_CENTRAL_MGR = "central-mgr"
    TYPE_IDENTIFIER_MGR = "identifier-mgr"
    TYPE_MANAGED_ENDPOINT = "managed-endpoint"
    TYPE_MGMT_CONTROLLER = "mgmt-controller"
    TYPE_OPERATION_MGR = "operation-mgr"
    TYPE_POLICY_MGR = "policy-mgr"
    TYPE_RESOURCE_AGGR = "resource-aggr"
    TYPE_RESOURCE_MGR = "resource-mgr"
    TYPE_SERVICE_REG = "service-reg"
    TYPE_STATS_MGR = "stats-mgr"
    TYPE_STORAGE_BROKER = "storage-broker"
    TYPE_VIRTUAL_SWITCHING_MGR = "virtual-switching-mgr"
    TYPE_VM_MGR = "vm-mgr"


class ExtpolClient(ManagedObject):
    """This is ExtpolClient class."""

    consts = ExtpolClientConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ExtpolClient", "extpolClient", "client-[id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin"], ['extpolClientCont'], ['faultInst', 'observeObserved', 'policyPolicyScopeCont'], ["Get"])

    prop_meta = {
        "capability": MoPropertyMeta("capability", "capability", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr),){0,28}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr){0,1}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "conn_protocol": MoPropertyMeta("conn_protocol", "connProtocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4", "ipv6", "unknown"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "grace_period_used": MoPropertyMeta("grace_period_used", "gracePeriodUsed", "ulong", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?$|^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*(\.[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$""", [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "interest": MoPropertyMeta("interest", "interest", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr),){0,28}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr){0,1}""", [], []),
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "ipv6": MoPropertyMeta("ipv6", "ipv6", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "last_poll_ts": MoPropertyMeta("last_poll_ts", "lastPollTs", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "registry-not-reachable", "synchronizing", "unregistered", "version-mismatch"], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ape", "boot-mgr", "central-mgr", "identifier-mgr", "managed-endpoint", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-aggr", "resource-mgr", "service-reg", "stats-mgr", "storage-broker", "virtual-switching-mgr", "vm-mgr"], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "capability": "capability", 
        "childAction": "child_action", 
        "connProtocol": "conn_protocol", 
        "descr": "descr", 
        "dn": "dn", 
        "gracePeriodUsed": "grace_period_used", 
        "guid": "guid", 
        "host": "host", 
        "id": "id", 
        "interest": "interest", 
        "ip": "ip", 
        "ipv6": "ipv6", 
        "lastPollTs": "last_poll_ts", 
        "licState": "lic_state", 
        "name": "name", 
        "operState": "oper_state", 
        "owner": "owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "site": "site", 
        "status": "status", 
        "suspendState": "suspend_state", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.capability = None
        self.child_action = None
        self.conn_protocol = None
        self.descr = None
        self.grace_period_used = None
        self.guid = None
        self.host = None
        self.interest = None
        self.ip = None
        self.ipv6 = None
        self.last_poll_ts = None
        self.lic_state = None
        self.name = None
        self.oper_state = None
        self.owner = None
        self.sacl = None
        self.site = None
        self.status = None
        self.suspend_state = None
        self.type = None
        self.version = None

        ManagedObject.__init__(self, "ExtpolClient", parent_mo_or_dn, **kwargs)
