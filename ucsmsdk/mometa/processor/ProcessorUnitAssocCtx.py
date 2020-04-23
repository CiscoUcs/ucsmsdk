"""This module contains the general information for ProcessorUnitAssocCtx ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorUnitAssocCtxConsts:
    STEPPING_UNSPECIFIED = "unspecified"


class ProcessorUnitAssocCtx(ManagedObject):
    """This is ProcessorUnitAssocCtx class."""

    consts = ProcessorUnitAssocCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorUnitAssocCtx", "processorUnitAssocCtx", "procunit-assoc-ctx", VersionMeta.Version141i, "InputOutput", 0x1f, [], ["read-only"], ['lsServerAssocCtx'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fru_cap_dn": MoPropertyMeta("fru_cap_dn", "fruCapDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "stepping": MoPropertyMeta("stepping", "stepping", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fruCapDn": "fru_cap_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "stepping": "stepping", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fru_cap_dn = None
        self.sacl = None
        self.status = None
        self.stepping = None

        ManagedObject.__init__(self, "ProcessorUnitAssocCtx", parent_mo_or_dn, **kwargs)
