"""This module contains the general information for MgmtIPv6IfAddrFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtIPv6IfAddrFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_BEGIN = "SwMgmtOobIpv6IfConfigBegin"
    NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_FAIL = "SwMgmtOobIpv6IfConfigFail"
    NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_SUCCESS = "SwMgmtOobIpv6IfConfigSuccess"
    NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_SWITCH = "SwMgmtOobIpv6IfConfigSwitch"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class MgmtIPv6IfAddrFsmStage(ManagedObject):
    """This is MgmtIPv6IfAddrFsmStage class."""

    consts = MgmtIPv6IfAddrFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MgmtIPv6IfAddrFsmStage", "mgmtIPv6IfAddrFsmStage", "stage-[name]", VersionMeta.Version221b, "OutputOnly", 0xf, [], [""], ['mgmtIPv6IfAddrFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, None, None, None, None, ["SwMgmtOobIpv6IfConfigBegin", "SwMgmtOobIpv6IfConfigFail", "SwMgmtOobIpv6IfConfigSuccess", "SwMgmtOobIpv6IfConfigSwitch", "nop"], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "MgmtIPv6IfAddrFsmStage", parent_mo_or_dn, **kwargs)
