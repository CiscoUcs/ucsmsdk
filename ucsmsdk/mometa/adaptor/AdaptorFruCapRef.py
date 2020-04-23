"""This module contains the general information for AdaptorFruCapRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFruCapRefConsts:
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class AdaptorFruCapRef(ManagedObject):
    """This is AdaptorFruCapRef class."""

    consts = AdaptorFruCapRefConsts()
    naming_props = set(['vendor', 'model', 'revision'])

    mo_meta = MoMeta("AdaptorFruCapRef", "adaptorFruCapRef", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version141i, "InputOutput", 0xff, [], [""], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSupported": "is_supported", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.is_supported = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFruCapRef", parent_mo_or_dn, **kwargs)
