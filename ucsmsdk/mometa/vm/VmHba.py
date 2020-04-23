"""This module contains the general information for VmHba ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VmHbaConsts:
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    PH_SWITCH_ID_A = "A"
    PH_SWITCH_ID_B = "B"
    PH_SWITCH_ID_NONE = "NONE"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"
    V_STATUS_OFFLINE = "offline"
    V_STATUS_ONLINE = "online"
    V_STATUS_UNKNOWN = "unknown"


class VmHba(ManagedObject):
    """This is VmHba class."""

    consts = VmHbaConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VmHba", "vmHba", "hba-[name]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["admin", "read-only"], ['vmComputeEp', 'vmHv', 'vmInstance'], ['vmVsan'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "dvs_gen_port_id": MoPropertyMeta("dvs_gen_port_id", "dvsGenPortId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "dvs_port_id": MoPropertyMeta("dvs_port_id", "dvsPortId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dvs_switch_id": MoPropertyMeta("dvs_switch_id", "dvsSwitchId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "host_if_dn": MoPropertyMeta("host_if_dn", "hostIfDn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, 1, 31, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []),
        "ph_switch_id": MoPropertyMeta("ph_switch_id", "phSwitchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "profile_id": MoPropertyMeta("profile_id", "profileId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "profile_name": MoPropertyMeta("profile_name", "profileName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "status_change_ts": MoPropertyMeta("status_change_ts", "statusChangeTs", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []),
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "v_status": MoPropertyMeta("v_status", "vStatus", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["offline", "online", "unknown"], []),
        "vc_dn": MoPropertyMeta("vc_dn", "vcDn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "vif_id": MoPropertyMeta("vif_id", "vifId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "vmnd_guid": MoPropertyMeta("vmnd_guid", "vmndGuid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "vmnd_name": MoPropertyMeta("vmnd_name", "vmndName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "vnic_dn": MoPropertyMeta("vnic_dn", "vnicDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "wwnn": MoPropertyMeta("wwnn", "wwnn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "dvsGenPortId": "dvs_gen_port_id", 
        "dvsPortId": "dvs_port_id", 
        "dvsSwitchId": "dvs_switch_id", 
        "hostIfDn": "host_if_dn", 
        "name": "name", 
        "owner": "owner", 
        "phSwitchId": "ph_switch_id", 
        "profileId": "profile_id", 
        "profileName": "profile_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "statusChangeTs": "status_change_ts", 
        "switchId": "switch_id", 
        "type": "type", 
        "uuid": "uuid", 
        "vStatus": "v_status", 
        "vcDn": "vc_dn", 
        "vifId": "vif_id", 
        "vmndGuid": "vmnd_guid", 
        "vmndName": "vmnd_name", 
        "vnicDn": "vnic_dn", 
        "wwnn": "wwnn", 
        "wwpn": "wwpn", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.dvs_gen_port_id = None
        self.dvs_port_id = None
        self.dvs_switch_id = None
        self.host_if_dn = None
        self.owner = None
        self.ph_switch_id = None
        self.profile_id = None
        self.profile_name = None
        self.sacl = None
        self.status = None
        self.status_change_ts = None
        self.switch_id = None
        self.type = None
        self.uuid = None
        self.v_status = None
        self.vc_dn = None
        self.vif_id = None
        self.vmnd_guid = None
        self.vmnd_name = None
        self.vnic_dn = None
        self.wwnn = None
        self.wwpn = None

        ManagedObject.__init__(self, "VmHba", parent_mo_or_dn, **kwargs)
