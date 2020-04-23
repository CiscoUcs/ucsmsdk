"""This module contains the general information for FabricVlanPermit ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricVlanPermitConsts:
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_DUAL = "dual"


class FabricVlanPermit(ManagedObject):
    """This is FabricVlanPermit class."""

    consts = FabricVlanPermitConsts()
    naming_props = set(['cloud', 'switchId', 'name'])

    mo_meta = MoMeta("FabricVlanPermit", "fabricVlanPermit", "perm-[cloud]sw-[switch_id]net-[name]", VersionMeta.Version211a, "InputOutput", 0xff, [], [""], ['orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cloud": MoPropertyMeta("cloud", "cloud", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x4, None, None, r"""((defaultValue|unknown|fcsanmon|ethlan|ethestclan|fcestc|ethlanmon|fcsan),){0,7}(defaultValue|unknown|fcsanmon|ethlan|ethestclan|fcestc|ethlanmon|fcsan){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x80, None, None, None, ["A", "B", "NONE", "dual"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "cloud": "cloud", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, cloud, switch_id, name, **kwargs):
        self._dirty_mask = 0
        self.cloud = cloud
        self.switch_id = switch_id
        self.name = name
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricVlanPermit", parent_mo_or_dn, **kwargs)
