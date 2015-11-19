"""This module contains the general information for ApeAttribute ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeAttributeConsts():
    pass


class ApeAttribute(ManagedObject):
    """This is ApeAttribute class."""

    consts = ApeAttributeConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ApeAttribute", "apeAttribute", "attribute-[id]", VersionMeta.Version224a, "InputOutput", 0x7fL, [], ["read-only"], [u'apeMcTable'], [], [None])

    prop_meta = {
        "attrib_type": MoPropertyMeta("attrib_type", "attribType", "uint", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version224a, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "attribType": "attrib_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "ip": "ip", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.attrib_type = None
        self.child_action = None
        self.ip = None
        self.status = None

        ManagedObject.__init__(self, "ApeAttribute", parent_mo_or_dn, **kwargs)

