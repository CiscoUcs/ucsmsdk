"""This module contains the general information for FirmwareExcludeChassisComponent ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareExcludeChassisComponentConsts:
    CHASSIS_COMPONENT_CHASSIS_BOARD_CONTROLLER = "chassis-board-controller"
    CHASSIS_COMPONENT_CMC = "cmc"
    CHASSIS_COMPONENT_IOCARD = "iocard"
    CHASSIS_COMPONENT_LOCAL_DISK = "local-disk"
    CHASSIS_COMPONENT_SAS_EXPANDER = "sas-expander"
    CHASSIS_COMPONENT_UNSPECIFIED = "unspecified"


class FirmwareExcludeChassisComponent(ManagedObject):
    """This is FirmwareExcludeChassisComponent class."""

    consts = FirmwareExcludeChassisComponentConsts()
    naming_props = set(['chassisComponent'])

    mo_meta = MoMeta("FirmwareExcludeChassisComponent", "firmwareExcludeChassisComponent", "exclude-chassis-component-[chassis_component]", VersionMeta.Version312b, "InputOutput", 0x3f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['firmwareChassisPack'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "chassis_component": MoPropertyMeta("chassis_component", "chassisComponent", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x2, None, None, None, ["chassis-board-controller", "cmc", "iocard", "local-disk", "sas-expander", "unspecified"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "chassisComponent": "chassis_component", 
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, chassis_component, **kwargs):
        self._dirty_mask = 0
        self.chassis_component = chassis_component
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareExcludeChassisComponent", parent_mo_or_dn, **kwargs)
