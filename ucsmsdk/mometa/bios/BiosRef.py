"""This module contains the general information for BiosRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosRefConsts:
    FORCE_OVERRIDE_ON_LOAD_NO = "no"
    FORCE_OVERRIDE_ON_LOAD_YES = "yes"
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class BiosRef(ManagedObject):
    """This is BiosRef class."""

    consts = BiosRefConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosRef", "biosRef", "bios-ref", VersionMeta.Version131c, "InputOutput", 0x1f, [], [""], ['equipmentBladeBiosCapProvider'], ['biosFeatureRef', 'biosTokenParam'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "force_override_on_load": MoPropertyMeta("force_override_on_load", "forceOverrideOnLoad", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "forceOverrideOnLoad": "force_override_on_load", 
        "isSupported": "is_supported", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.force_override_on_load = None
        self.is_supported = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "BiosRef", parent_mo_or_dn, **kwargs)
