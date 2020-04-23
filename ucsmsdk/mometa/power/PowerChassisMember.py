"""This module contains the general information for PowerChassisMember ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerChassisMemberConsts:
    OPER_STATE_CAP_INSUFFICIENT = "cap-insufficient"
    OPER_STATE_CAP_OK = "cap-ok"
    OPER_STATE_FW_MISMATCH = "fw-mismatch"
    OPER_STATE_PSU_INSUFFICIENT = "psu-insufficient"
    OPER_STATE_PSU_REDUNDANCY_FAILED = "psu-redundancy-failed"
    OPER_STATE_UNINITIALIZED = "uninitialized"


class PowerChassisMember(ManagedObject):
    """This is PowerChassisMember class."""

    consts = PowerChassisMemberConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("PowerChassisMember", "powerChassisMember", "ch-member-[id]", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["admin", "power-mgmt", "read-only"], ['powerGroup'], ['faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cap-insufficient", "cap-ok", "fw-mismatch", "psu-insufficient", "psu-redundancy-failed", "uninitialized"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
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
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PowerChassisMember", parent_mo_or_dn, **kwargs)
