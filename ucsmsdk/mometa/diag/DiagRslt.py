"""This module contains the general information for DiagRslt ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DiagRsltConsts:
    RESULT_FAIL = "fail"
    RESULT_NA = "na"
    RESULT_PASS = "pass"
    RESULT_UNKNOWN = "unknown"
    RSLT_STATUS_CANCELLED = "cancelled"
    RSLT_STATUS_COMPLETED = "completed"
    RSLT_STATUS_FAILED = "failed"
    RSLT_STATUS_IDLE = "idle"
    RSLT_STATUS_IN_PROGRESS = "in-progress"
    RSLT_STATUS_UNKNOWN = "unknown"
    TEST_TYPE_DISK = "disk"
    TEST_TYPE_MEMTEST = "memtest"
    TEST_TYPE_PCI = "pci"
    TEST_TYPE_PMEM2 = "pmem2"
    TEST_TYPE_PROCESSOR = "processor"
    TEST_TYPE_STRESS = "stress"


class DiagRslt(ManagedObject):
    """This is DiagRslt class."""

    consts = DiagRsltConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("DiagRslt", "diagRslt", "rslt-[id]", VersionMeta.Version111j, "InputOutput", 0x3f, [], [""], ['diagSrvCtrl'], ['diagLogEp'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "end_ts": MoPropertyMeta("end_ts", "endTs", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "est_prog_weight": MoPropertyMeta("est_prog_weight", "estProgWeight", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "byte", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "progress": MoPropertyMeta("progress", "progress", "byte", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]),
        "result": MoPropertyMeta("result", "result", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "na", "pass", "unknown"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "rslt_status": MoPropertyMeta("rslt_status", "rsltStatus", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cancelled", "completed", "failed", "idle", "in-progress", "unknown"], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "start_ts": MoPropertyMeta("start_ts", "startTs", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "test_dn": MoPropertyMeta("test_dn", "testDn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "test_type": MoPropertyMeta("test_type", "testType", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disk", "memtest", "pci", "pmem2", "processor", "stress"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "endTs": "end_ts", 
        "estProgWeight": "est_prog_weight", 
        "id": "id", 
        "progress": "progress", 
        "result": "result", 
        "rn": "rn", 
        "rsltStatus": "rslt_status", 
        "sacl": "sacl", 
        "startTs": "start_ts", 
        "status": "status", 
        "testDn": "test_dn", 
        "testType": "test_type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.descr = None
        self.end_ts = None
        self.est_prog_weight = None
        self.progress = None
        self.result = None
        self.rslt_status = None
        self.sacl = None
        self.start_ts = None
        self.status = None
        self.test_dn = None
        self.test_type = None

        ManagedObject.__init__(self, "DiagRslt", parent_mo_or_dn, **kwargs)
