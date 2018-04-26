"""This module contains the general information for DiagLogEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DiagLogEpConsts:
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class DiagLogEp(ManagedObject):
    """This is DiagLogEp class."""

    consts = DiagLogEpConsts()
    naming_props = set([u'switchId'])

    mo_meta = MoMeta("DiagLogEp", "diagLogEp", "logep-[switch_id]", VersionMeta.Version321d, "InputOutput", 0x3f, [], [""], [u'diagRslt'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "log_dn": MoPropertyMeta("log_dn", "logDn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x20, None, None, None, ["A", "B", "NONE"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "logDn": "log_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, switch_id, **kwargs):
        self._dirty_mask = 0
        self.switch_id = switch_id
        self.child_action = None
        self.log_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "DiagLogEp", parent_mo_or_dn, **kwargs)
