"""This module contains the general information for FirmwareModule ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareModuleConsts:
    pass


class FirmwareModule(ManagedObject):
    """This is FirmwareModule class."""

    consts = FirmwareModuleConsts()
    naming_props = set(['name', 'type'])

    mo_meta = MoMeta("FirmwareModule", "firmwareModule", "module-[name]|[type]", VersionMeta.Version321d, "InputOutput", 0x7f, [], ["admin"], ['firmwareImage'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "model": "model", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, name, type, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.type = type
        self.child_action = None
        self.description = None
        self.model = None
        self.sacl = None
        self.status = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareModule", parent_mo_or_dn, **kwargs)
