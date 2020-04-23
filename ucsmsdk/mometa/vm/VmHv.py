"""This module contains the general information for VmHv ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VmHvConsts:
    CL_INST_TYPE_COMPUTE_EP = "compute-ep"
    CL_INST_TYPE_HV = "hv"
    CL_INST_TYPE_VM = "vm"
    HV_TYPE_ESX = "esx"
    HV_TYPE_HYPERV = "hyperv"
    HV_TYPE_KVM = "kvm"
    HV_TYPE_UNSPECIFIED = "unspecified"
    HV_TYPE_XEN = "xen"
    INT_ID_NONE = "none"
    MODEL_LINUX = "Linux"
    MODEL_PNU_OS = "PnuOS"
    MODEL_SOLARIS = "Solaris"
    MODEL_VMWARE_ESX = "VMWareESX"
    MODEL_WINDOWS = "Windows"
    MODEL_UNSPECIFIED = "unspecified"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    V_STATUS_OFFLINE = "offline"
    V_STATUS_ONLINE = "online"
    V_STATUS_UNKNOWN = "unknown"
    VENDOR_CITRIX = "citrix"
    VENDOR_MICROSOFT = "microsoft"
    VENDOR_NOVELL = "novell"
    VENDOR_ORACLE = "oracle"
    VENDOR_REDHAT = "redhat"
    VENDOR_UNSPECIFIED = "unspecified"
    VENDOR_VMWARE = "vmware"


class VmHv(ManagedObject):
    """This is VmHv class."""

    consts = VmHvConsts()
    naming_props = set(['uuid'])

    mo_meta = MoMeta("VmHv", "vmHv", "hv-[uuid]", VersionMeta.Version111j, "InputOutput", 0xff, [], ["admin", "read-only"], ['vmEp'], ['vmHba', 'vmNic'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cl_inst_type": MoPropertyMeta("cl_inst_type", "clInstType", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute-ep", "hv", "vm"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "dvs_dn": MoPropertyMeta("dvs_dn", "dvsDn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "dvs_name": MoPropertyMeta("dvs_name", "dvsName", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "hv_type": MoPropertyMeta("hv_type", "hvType", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["esx", "hyperv", "kvm", "unspecified", "xen"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Linux", "PnuOS", "Solaris", "VMWareESX", "Windows", "unspecified"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "status_change_ts": MoPropertyMeta("status_change_ts", "statusChangeTs", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x80, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "v_status": MoPropertyMeta("v_status", "vStatus", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["offline", "online", "unknown"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["citrix", "microsoft", "novell", "oracle", "redhat", "unspecified", "vmware"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "clInstType": "cl_inst_type", 
        "descr": "descr", 
        "dn": "dn", 
        "dvsDn": "dvs_dn", 
        "dvsName": "dvs_name", 
        "fltAggr": "flt_aggr", 
        "hvType": "hv_type", 
        "intId": "int_id", 
        "lsDn": "ls_dn", 
        "model": "model", 
        "name": "name", 
        "pnDn": "pn_dn", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "statusChangeTs": "status_change_ts", 
        "uuid": "uuid", 
        "vStatus": "v_status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, uuid, **kwargs):
        self._dirty_mask = 0
        self.uuid = uuid
        self.child_action = None
        self.cl_inst_type = None
        self.descr = None
        self.dvs_dn = None
        self.dvs_name = None
        self.flt_aggr = None
        self.hv_type = None
        self.int_id = None
        self.ls_dn = None
        self.model = None
        self.name = None
        self.pn_dn = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.status_change_ts = None
        self.v_status = None
        self.vendor = None

        ManagedObject.__init__(self, "VmHv", parent_mo_or_dn, **kwargs)
