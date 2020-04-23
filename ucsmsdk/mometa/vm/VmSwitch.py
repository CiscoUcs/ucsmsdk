"""This module contains the general information for VmSwitch ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VmSwitchConsts:
    ADMIN_STATE_DISABLE = "disable"
    ADMIN_STATE_ENABLE = "enable"
    INT_ID_NONE = "none"
    MANAGER_RHEV_M = "rhev-m"
    MANAGER_SCVMM = "scvmm"
    MANAGER_UNMANAGED = "unmanaged"
    MANAGER_VCENTER = "vcenter"
    OWN_DISCOVERED = "discovered"
    OWN_MANAGED = "managed"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    VENDOR_MICROSOFT = "microsoft"
    VENDOR_UNDETERMINED = "undetermined"
    VENDOR_VMWARE = "vmware"


class VmSwitch(ManagedObject):
    """This is VmSwitch class."""

    consts = VmSwitchConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VmSwitch", "vmSwitch", "switch-[name]", VersionMeta.Version111j, "InputOutput", 0xfff, [], ["admin", "ls-config", "ls-config-policy", "ls-network", "pn-policy"], ['extvmmProvider', 'extvmmSwitchSet', 'vmOrg'], ['extvmmUpLinkPP', 'vmVnicProfInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disable", "enable"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "ext_key": MoPropertyMeta("ext_key", "extKey", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 1, 33, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,40}""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "key_inst": MoPropertyMeta("key_inst", "keyInst", "ushort", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "manager": MoPropertyMeta("manager", "manager", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["rhev-m", "scvmm", "unmanaged", "vcenter"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "own": MoPropertyMeta("own", "own", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["discovered", "managed"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["microsoft", "undetermined", "vmware"], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "extKey": "ext_key", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "intId": "int_id", 
        "keyInst": "key_inst", 
        "manager": "manager", 
        "name": "name", 
        "own": "own", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "uuid": "uuid", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.ext_key = None
        self.flt_aggr = None
        self.id = None
        self.int_id = None
        self.key_inst = None
        self.manager = None
        self.own = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.uuid = None
        self.vendor = None

        ManagedObject.__init__(self, "VmSwitch", parent_mo_or_dn, **kwargs)
