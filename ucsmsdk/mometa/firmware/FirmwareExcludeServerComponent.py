"""This module contains the general information for FirmwareExcludeServerComponent ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FirmwareExcludeServerComponentConsts():
    SERVER_COMPONENT_ADAPTOR = "adaptor"
    SERVER_COMPONENT_BLADE_BIOS = "blade-bios"
    SERVER_COMPONENT_BLADE_CONTROLLER = "blade-controller"
    SERVER_COMPONENT_BOARD_CONTROLLER = "board-controller"
    SERVER_COMPONENT_FLEXFLASH_CONTROLLER = "flexflash-controller"
    SERVER_COMPONENT_GRAPHICS_CARD = "graphics-card"
    SERVER_COMPONENT_HOST_HBA = "host-hba"
    SERVER_COMPONENT_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    SERVER_COMPONENT_HOST_NIC = "host-nic"
    SERVER_COMPONENT_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    SERVER_COMPONENT_LOCAL_DISK = "local-disk"
    SERVER_COMPONENT_PSU = "psu"
    SERVER_COMPONENT_SAS_EXPANDER = "sas-expander"
    SERVER_COMPONENT_STORAGE_CONTROLLER = "storage-controller"
    SERVER_COMPONENT_UNSPECIFIED = "unspecified"


class FirmwareExcludeServerComponent(ManagedObject):
    """This is FirmwareExcludeServerComponent class."""

    consts = FirmwareExcludeServerComponentConsts()
    naming_props = set([u'serverComponent'])

    mo_meta = MoMeta("FirmwareExcludeServerComponent", "firmwareExcludeServerComponent", "exclude-server-component-[server_component]", None, "InputOutput", 0x3fL, [], ["admin", "ls-compute", "ls-config-policy", "ls-server-policy"], [u'firmwareComputeHostPack'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "server_component": MoPropertyMeta("server_component", "serverComponent", "string", None, MoPropertyMeta.NAMING, 0x10L, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "local-disk", "psu", "sas-expander", "storage-controller", "unspecified"], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverComponent": "server_component", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, server_component, **kwargs):
        self._dirty_mask = 0
        self.server_component = server_component
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareExcludeServerComponent", parent_mo_or_dn, **kwargs)

