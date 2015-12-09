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

    mo_meta = MoMeta("ApeAttribute", "apeAttribute", "attribute-[id]", VersionMeta.Version224b, "InputOutput", 0xffL, [], ["read-only"], [u'apeMcTable'], [u'storageLocalDisk'], [None])

    prop_meta = {
        "attrib_type": MoPropertyMeta("attrib_type", "attribType", "uint", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x10L, None, None, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20L, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "attribType": "attrib_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "ip": "ip", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.attrib_type = None
        self.child_action = None
        self.ip = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ApeAttribute", parent_mo_or_dn, **kwargs)

