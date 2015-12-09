"""This module contains the general information for FsmStatus ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FsmStatusConsts():
    STATE_FAIL = "fail"
    STATE_IN_PROGRESS = "inProgress"
    STATE_NOP = "nop"
    STATE_PENDING = "pending"
    STATE_SKIP = "skip"
    STATE_SUCCESS = "success"
    STATE_THROTTLED = "throttled"


class FsmStatus(ManagedObject):
    """This is FsmStatus class."""

    consts = FsmStatusConsts()
    naming_props = set([u'convertedEpRef'])

    mo_meta = MoMeta("FsmStatus", "fsmStatus", "status-[converted_ep_ref]", VersionMeta.Version211a, "InputOutput", 0xffL, [], ["read-only"], [u'topSystem'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "converted_ep_ref": MoPropertyMeta("converted_ep_ref", "convertedEpRef", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x4L, 1, 510, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "object_class_name": MoPropertyMeta("object_class_name", "objectClassName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "remote_ep_ref": MoPropertyMeta("remote_ep_ref", "remoteEpRef", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "convertedEpRef": "converted_ep_ref", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "objectClassName": "object_class_name", 
        "remoteEpRef": "remote_ep_ref", 
        "rn": "rn", 
        "sacl": "sacl", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, converted_ep_ref, **kwargs):
        self._dirty_mask = 0
        self.converted_ep_ref = converted_ep_ref
        self.child_action = None
        self.descr = None
        self.name = None
        self.object_class_name = None
        self.remote_ep_ref = None
        self.sacl = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "FsmStatus", parent_mo_or_dn, **kwargs)

