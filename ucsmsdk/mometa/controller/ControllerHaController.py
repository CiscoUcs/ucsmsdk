"""This module contains the general information for ControllerHaController ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ControllerHaControllerConsts:
    TRIG_ELECTION_FLAG_FALSE = "false"
    TRIG_ELECTION_FLAG_NO = "no"
    TRIG_ELECTION_FLAG_TRUE = "true"
    TRIG_ELECTION_FLAG_YES = "yes"


class ControllerHaController(ManagedObject):
    """This is ControllerHaController class."""

    consts = ControllerHaControllerConsts()
    naming_props = set([])

    mo_meta = MoMeta("ControllerHaController", "controllerHaController", "HaController", VersionMeta.Version911z, "InputOutput", 0x3f, [], ["admin"], [u'topSystem'], [u'controllerOperationalVersionHolder', u'controllerPreferedVersionHolder'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version911z, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version911z, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trig_election_flag": MoPropertyMeta("trig_election_flag", "trigElectionFlag", "string", VersionMeta.Version911z, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "trigElectionFlag": "trig_election_flag", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.trig_election_flag = None

        ManagedObject.__init__(self, "ControllerHaController", parent_mo_or_dn, **kwargs)
