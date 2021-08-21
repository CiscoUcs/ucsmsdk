"""This module contains the general information for FcpoolOui ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FcpoolOuiConsts:
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "None"


class FcpoolOui(ManagedObject):
    """This is FcpoolOui class."""

    consts = FcpoolOuiConsts()
    naming_props = set(['oui'])

    mo_meta = MoMeta("FcpoolOui", "fcpoolOui", "oui-[oui]", VersionMeta.Version413a, "InputOutput", 0x3f, [], ["admin"], ['fcpoolOuis'], [], [None])

    prop_meta = {
        "switch_id": MoPropertyMeta("switch_id", "SwitchId", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "None"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "oui": MoPropertyMeta("oui", "oui", "string", VersionMeta.Version413a, MoPropertyMeta.NAMING, 0x8, None, None, r"""^0x([a-f0-9]{6})$""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "SwitchId": "switch_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "oui": "oui", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, oui, **kwargs):
        self._dirty_mask = 0
        self.oui = oui
        self.switch_id = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolOui", parent_mo_or_dn, **kwargs)
