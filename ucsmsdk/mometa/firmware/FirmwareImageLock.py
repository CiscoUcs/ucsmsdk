"""This module contains the general information for FirmwareImageLock ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareImageLockConsts:
    pass


class FirmwareImageLock(ManagedObject):
    """This is FirmwareImageLock class."""

    consts = FirmwareImageLockConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareImageLock", "firmwareImageLock", "fw-imagelock[name]", VersionMeta.Version222c, "InputOutput", 0x3f, [], ["admin"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'equipmentChassis'], [], ["Get"])

    prop_meta = {
        "image_name_dn": MoPropertyMeta("image_name_dn", "ImageNameDn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version222c, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "ImageNameDn": "image_name_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.image_name_dn = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareImageLock", parent_mo_or_dn, **kwargs)
