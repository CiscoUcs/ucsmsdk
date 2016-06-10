"""This module contains the general information for FirmwareVicSlotConstraint ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareVicSlotConstraintConsts:
    pass


class FirmwareVicSlotConstraint(ManagedObject):
    """This is FirmwareVicSlotConstraint class."""

    consts = FirmwareVicSlotConstraintConsts()
    naming_props = set([u'vicSlot'])

    mo_meta = MoMeta("FirmwareVicSlotConstraint", "firmwareVicSlotConstraint", "constraint-vic-slot-[vic_slot]", VersionMeta.Version227b, "InputOutput", 0x3f, [], [""], [u'firmwareConstraints'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "min_bios_version": MoPropertyMeta("min_bios_version", "minBiosVersion", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vic_slot": MoPropertyMeta("vic_slot", "vicSlot", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "minBiosVersion": "min_bios_version", 
        "minCimcVersion": "min_cimc_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vicSlot": "vic_slot", 
    }

    def __init__(self, parent_mo_or_dn, vic_slot, **kwargs):
        self._dirty_mask = 0
        self.vic_slot = vic_slot
        self.child_action = None
        self.min_bios_version = None
        self.min_cimc_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareVicSlotConstraint", parent_mo_or_dn, **kwargs)
