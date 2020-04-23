"""This module contains the general information for SesEnclosure ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SesEnclosureConsts:
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"


class SesEnclosure(ManagedObject):
    """This is SesEnclosure class."""

    consts = SesEnclosureConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("SesEnclosure", "sesEnclosure", "ses-enc-[id]", VersionMeta.Version312b, "InputOutput", 0x7f, [], ["read-only"], ['equipmentChassis'], ['sesDiskSlotEp'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "elid": MoPropertyMeta("elid", "elid", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "elid": "elid", 
        "id": "id", 
        "lc": "lc", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.descr = None
        self.elid = None
        self.lc = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SesEnclosure", parent_mo_or_dn, **kwargs)
