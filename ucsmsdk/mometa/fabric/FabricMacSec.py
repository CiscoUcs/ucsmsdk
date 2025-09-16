"""This module contains the general information for FabricMacSec ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricMacSecConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    HIDE_KEY_HEX_STRING_IN_FI_NO = "no"
    HIDE_KEY_HEX_STRING_IN_FI_YES = "yes"


class FabricMacSec(ManagedObject):
    """This is FabricMacSec class."""

    consts = FabricMacSecConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricMacSec", "fabricMacSec", "macsec", VersionMeta.Version434a, "InputOutput", 0x7f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricLanCloud', 'swEthLanBorder'], ['fabricMacSecEapol', 'fabricMacSecIfConfig', 'fabricMacSecKeyChain', 'fabricMacSecPolicy'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "hide_key_hex_string_in_fi": MoPropertyMeta("hide_key_hex_string_in_fi", "hideKeyHexStringInFI", "string", VersionMeta.Version601b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["no", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "hideKeyHexStringInFI": "hide_key_hex_string_in_fi", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.hide_key_hex_string_in_fi = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricMacSec", parent_mo_or_dn, **kwargs)
