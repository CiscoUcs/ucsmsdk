"""This module contains the general information for MgmtSwPersonality ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtSwPersonalityConsts:
    pass


class MgmtSwPersonality(ManagedObject):
    """This is MgmtSwPersonality class."""

    consts = MgmtSwPersonalityConsts()
    naming_props = set(['Id'])

    mo_meta = MoMeta("MgmtSwPersonality", "mgmtSwPersonality", "sw-personality-[id]", VersionMeta.Version421a, "InputOutput", 0xff, [], ["admin"], ['mgmtSwPersonalities', 'mgmtSwPersonalitiesInventory'], [], [None])

    prop_meta = {
        "addl_info": MoPropertyMeta("addl_info", "AddlInfo", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 1, 100, None, [], []),
        "id": MoPropertyMeta("id", "Id", "uint", VersionMeta.Version421a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], ["1-1"]),
        "name": MoPropertyMeta("name", "Name", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, 1, 100, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "AddlInfo": "addl_info", 
        "Id": "id", 
        "Name": "name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.addl_info = None
        self.name = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtSwPersonality", parent_mo_or_dn, **kwargs)
