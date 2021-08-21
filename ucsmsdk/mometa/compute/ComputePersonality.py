"""This module contains the general information for ComputePersonality ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePersonalityConsts:
    pass


class ComputePersonality(ManagedObject):
    """This is ComputePersonality class."""

    consts = ComputePersonalityConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputePersonality", "computePersonality", "personality-[id]", VersionMeta.Version421a, "InputOutput", 0xff, [], ["admin"], ['computeBlade', 'computeRackUnit'], [], [None])

    prop_meta = {
        "additional_info": MoPropertyMeta("additional_info", "additionalInfo", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 2000, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version421a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-1"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, 0, 100, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "additionalInfo": "additional_info", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.additional_info = None
        self.child_action = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePersonality", parent_mo_or_dn, **kwargs)
