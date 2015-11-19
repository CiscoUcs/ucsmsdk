"""This module contains the general information for BiosVfDDR3VoltageSelection ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfDDR3VoltageSelectionConsts():
    VP_DDR3_VOLTAGE_SELECTION_DDR3_1350MV = "ddr3-1350mv"
    VP_DDR3_VOLTAGE_SELECTION_DDR3_1500MV = "ddr3-1500mv"
    VP_DDR3_VOLTAGE_SELECTION_PLATFORM_DEFAULT = "platform-default"
    VP_DDR3_VOLTAGE_SELECTION_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfDDR3VoltageSelection(ManagedObject):
    """This is BiosVfDDR3VoltageSelection class."""

    consts = BiosVfDDR3VoltageSelectionConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfDDR3VoltageSelection", "biosVfDDR3VoltageSelection", "DDR3-Voltage-Selection", VersionMeta.Version251a, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vp_dd_r3_voltage_selection": MoPropertyMeta("vp_dd_r3_voltage_selection", "vpDDR3VoltageSelection", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["ddr3-1350mv", "ddr3-1500mv", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpDDR3VoltageSelection": "vp_dd_r3_voltage_selection", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_dd_r3_voltage_selection = None

        ManagedObject.__init__(self, "BiosVfDDR3VoltageSelection", parent_mo_or_dn, **kwargs)

