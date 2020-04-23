"""This module contains the general information for StorageIniGroup ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageIniGroupConsts:
    INT_ID_NONE = "none"
    OPER_PROTOCOL_DERIVED = "derived"
    OPER_PROTOCOL_FC = "fc"
    OPER_PROTOCOL_ISCSI = "iscsi"
    OPER_STATE_MISCONFIGURED = "misconfigured"
    OPER_STATE_OK = "ok"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTOCOL_DERIVED = "derived"
    PROTOCOL_FC = "fc"
    PROTOCOL_ISCSI = "iscsi"


class StorageIniGroup(ManagedObject):
    """This is StorageIniGroup class."""

    consts = StorageIniGroupConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageIniGroup", "storageIniGroup", "grp-[name]", VersionMeta.Version211a, "InputOutput", 0xfff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['lsServer', 'vnicSanConnPolicy'], ['faultInst', 'storageInitiator', 'vnicFcGroupDef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "group_policy_name": MoPropertyMeta("group_policy_name", "groupPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_protocol": MoPropertyMeta("oper_protocol", "operProtocol", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["derived", "fc", "iscsi"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["misconfigured", "ok"], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_name": MoPropertyMeta("policy_name", "policyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version211a, MoPropertyMeta.CREATE_ONLY, 0x100, None, None, None, ["derived", "fc", "iscsi"], []),
        "rmt_disk_cfg_name": MoPropertyMeta("rmt_disk_cfg_name", "rmtDiskCfgName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "groupPolicyName": "group_policy_name", 
        "intId": "int_id", 
        "name": "name", 
        "operProtocol": "oper_protocol", 
        "operState": "oper_state", 
        "owner": "owner", 
        "policyLevel": "policy_level", 
        "policyName": "policy_name", 
        "policyOwner": "policy_owner", 
        "protocol": "protocol", 
        "rmtDiskCfgName": "rmt_disk_cfg_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.group_policy_name = None
        self.int_id = None
        self.oper_protocol = None
        self.oper_state = None
        self.owner = None
        self.policy_level = None
        self.policy_name = None
        self.policy_owner = None
        self.protocol = None
        self.rmt_disk_cfg_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageIniGroup", parent_mo_or_dn, **kwargs)
