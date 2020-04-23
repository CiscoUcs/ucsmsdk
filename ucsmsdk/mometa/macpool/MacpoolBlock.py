"""This module contains the general information for MacpoolBlock ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MacpoolBlockConsts:
    pass


class MacpoolBlock(ManagedObject):
    """This is MacpoolBlock class."""

    consts = MacpoolBlockConsts()
    naming_props = set(['from', 'to'])

    mo_meta = MoMeta("MacpoolBlock", "macpoolBlock", "block-[r_from]-[to]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "ls-network-policy"], ['macpoolPool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "to": MoPropertyMeta("to", "to", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "from": "r_from", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "to": "to", 
    }

    def __init__(self, parent_mo_or_dn, r_from, to, **kwargs):
        self._dirty_mask = 0
        self.r_from = r_from
        self.to = to
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MacpoolBlock", parent_mo_or_dn, **kwargs)
