"""This module contains the general information for EquipmentPOSTCodeTemplate ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPOSTCodeTemplateConsts:
    pass


class EquipmentPOSTCodeTemplate(ManagedObject):
    """This is EquipmentPOSTCodeTemplate class."""

    consts = EquipmentPOSTCodeTemplateConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentPOSTCodeTemplate", "equipmentPOSTCodeTemplate", "POST-[name]", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["read-only"], ['capabilityCatalogue'], ['equipmentPOSTCode'], ["Get"])

    prop_meta = {
        "base_container": MoPropertyMeta("base_container", "baseContainer", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{1,64}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "baseContainer": "base_container", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.base_container = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPOSTCodeTemplate", parent_mo_or_dn, **kwargs)
