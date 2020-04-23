"""This module contains the general information for FirmwareChassisComponentSpec ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareChassisComponentSpecConsts:
    EXCLUDE_BY_DEFAULT_FALSE = "false"
    EXCLUDE_BY_DEFAULT_NO = "no"
    EXCLUDE_BY_DEFAULT_TRUE = "true"
    EXCLUDE_BY_DEFAULT_YES = "yes"
    TYPE_CHASSIS_BOARD_CONTROLLER = "chassis-board-controller"
    TYPE_CMC = "cmc"
    TYPE_IOCARD = "iocard"
    TYPE_LOCAL_DISK = "local-disk"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_UNSPECIFIED = "unspecified"


class FirmwareChassisComponentSpec(ManagedObject):
    """This is FirmwareChassisComponentSpec class."""

    consts = FirmwareChassisComponentSpecConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FirmwareChassisComponentSpec", "firmwareChassisComponentSpec", "chassis-component-spec-[type]", VersionMeta.Version312b, "InputOutput", 0x3f, [], [""], ['firmwareBundleTypeCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "exclude_by_default": MoPropertyMeta("exclude_by_default", "excludeByDefault", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x20, None, None, None, ["chassis-board-controller", "cmc", "iocard", "local-disk", "sas-expander", "unspecified"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "excludeByDefault": "exclude_by_default", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.exclude_by_default = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareChassisComponentSpec", parent_mo_or_dn, **kwargs)
