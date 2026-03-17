"""This module contains the general information for PkiNXOSTpDeletion ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PkiNXOSTpDeletionConsts:
    pass


class PkiNXOSTpDeletion(ManagedObject):
    """This is PkiNXOSTpDeletion class."""

    consts = PkiNXOSTpDeletionConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PkiNXOSTpDeletion", "pkiNXOSTpDeletion", "nxosTpDel-[name]", VersionMeta.Version602a, "InputOutput", 0x7f, [], ["aaa", "admin"], ['pkiEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version602a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "del_tp_str": MoPropertyMeta("del_tp_str", "delTPStr", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version602a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "delTPStr": "del_tp_str", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.del_tp_str = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PkiNXOSTpDeletion", parent_mo_or_dn, **kwargs)
