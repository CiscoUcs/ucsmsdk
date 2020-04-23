"""This module contains the general information for AdaptorUnitAssocCtx ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorUnitAssocCtxConsts:
    pass


class AdaptorUnitAssocCtx(ManagedObject):
    """This is AdaptorUnitAssocCtx class."""

    consts = AdaptorUnitAssocCtxConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorUnitAssocCtx", "adaptorUnitAssocCtx", "adaptorunit-assoc-ctx-[id]", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["read-only"], ['lsServerAssocCtx'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fru_cap_dn": MoPropertyMeta("fru_cap_dn", "fruCapDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fruCapDn": "fru_cap_dn", 
        "id": "id", 
        "pciAddr": "pci_addr", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.fru_cap_dn = None
        self.pci_addr = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorUnitAssocCtx", parent_mo_or_dn, **kwargs)
