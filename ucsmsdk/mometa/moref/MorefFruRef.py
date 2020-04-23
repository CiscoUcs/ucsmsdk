"""This module contains the general information for MorefFruRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MorefFruRefConsts:
    pass


class MorefFruRef(ManagedObject):
    """This is MorefFruRef class."""

    consts = MorefFruRefConsts()
    naming_props = set(['className', 'vendor', 'model', 'serial'])

    mo_meta = MoMeta("MorefFruRef", "morefFruRef", "[class_name]-vendor-[vendor]-model-[model]-serial-[serial]", VersionMeta.Version227b, "InputOutput", 0x1ff, [], ["admin"], ['morefImportRoot'], ['morefProp', 'morefRef'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "class_name": MoPropertyMeta("class_name", "className", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "className": "class_name", 
        "dn": "dn", 
        "model": "model", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, class_name, vendor, model, serial, **kwargs):
        self._dirty_mask = 0
        self.class_name = class_name
        self.vendor = vendor
        self.model = model
        self.serial = serial
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MorefFruRef", parent_mo_or_dn, **kwargs)
