"""This module contains the general information for PowerFIMember ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerFIMemberConsts:
    FI_ID_A = "A"
    FI_ID_B = "B"
    FI_ID_NONE = "NONE"
    OPER_STATE_CAP_INSUFFICIENT = "cap-insufficient"
    OPER_STATE_CAP_OK = "cap-ok"
    OPER_STATE_FW_MISMATCH = "fw-mismatch"
    OPER_STATE_PSU_INSUFFICIENT = "psu-insufficient"
    OPER_STATE_PSU_REDUNDANCY_FAILED = "psu-redundancy-failed"
    OPER_STATE_UNINITIALIZED = "uninitialized"


class PowerFIMember(ManagedObject):
    """This is PowerFIMember class."""

    consts = PowerFIMemberConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("PowerFIMember", "powerFIMember", "fi-member-[id]", VersionMeta.Version312b, "InputOutput", 0x7f, [], ["admin", "power-mgmt", "read-only"], ['powerGroup'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fi_id": MoPropertyMeta("fi_id", "fiId", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["A", "B", "NONE"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cap-insufficient", "cap-ok", "fw-mismatch", "psu-insufficient", "psu-redundancy-failed", "uninitialized"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fiId": "fi_id", 
        "id": "id", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.fi_id = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PowerFIMember", parent_mo_or_dn, **kwargs)
