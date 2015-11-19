"""This module contains the general information for AaaUserLocale ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AaaUserLocaleConsts():
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"


class AaaUserLocale(ManagedObject):
    """This is AaaUserLocale class."""

    consts = AaaUserLocaleConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AaaUserLocale", "aaaUserLocale", "locale-[name]", VersionMeta.Version101e, "InputOutput", 0x3fL, [], ["aaa", "admin"], [u'aaaLdapGroup', u'aaaRemoteUser', u'aaaUser'], [u'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []), 
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "descr": "descr", 
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
        self.config_state = None
        self.config_status_message = None
        self.descr = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AaaUserLocale", parent_mo_or_dn, **kwargs)

