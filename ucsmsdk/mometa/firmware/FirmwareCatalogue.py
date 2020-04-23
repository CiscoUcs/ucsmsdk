"""This module contains the general information for FirmwareCatalogue ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareCatalogueConsts:
    SYNC_TRIGGER_FALSE = "false"
    SYNC_TRIGGER_NO = "no"
    SYNC_TRIGGER_TRUE = "true"
    SYNC_TRIGGER_YES = "yes"


class FirmwareCatalogue(ManagedObject):
    """This is FirmwareCatalogue class."""

    consts = FirmwareCatalogueConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareCatalogue", "firmwareCatalogue", "fw-catalogue", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["read-only"], ['topSystem'], ['firmwareCompSource', 'firmwareDistributable', 'firmwareDownloader', 'firmwareImage', 'firmwareUcscInfo'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sync_trigger": MoPropertyMeta("sync_trigger", "syncTrigger", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "syncTrigger": "sync_trigger", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.sync_trigger = None

        ManagedObject.__init__(self, "FirmwareCatalogue", parent_mo_or_dn, **kwargs)
