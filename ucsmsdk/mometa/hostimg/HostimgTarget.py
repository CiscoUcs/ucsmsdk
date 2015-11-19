"""This module contains the general information for HostimgTarget ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class HostimgTargetConsts():
    ORDER_UNSPECIFIED = "unspecified"
    TYPE_COMPLETE = "complete"
    TYPE_FILE_SYSTEM = "file-system"
    TYPE_GPXE_SCRIPT = "gpxe-script"
    TYPE_KERNEL = "kernel"
    TYPE_MODULE = "module"


class HostimgTarget(ManagedObject):
    """This is HostimgTarget class."""

    consts = HostimgTargetConsts()
    naming_props = set([u'type', u'name'])

    mo_meta = MoMeta("HostimgTarget", "hostimgTarget", "target-[type]-comp-[name]", VersionMeta.Version141i, "InputOutput", 0xffL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server"], [u'hostimgPolicy'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x40L, None, None, None, ["complete", "file-system", "gpxe-script", "kernel", "module"], []), 
        "uri": MoPropertyMeta("uri", "uri", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "uri": "uri", 
    }

    def __init__(self, parent_mo_or_dn, type, name, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.name = name
        self.child_action = None
        self.order = None
        self.sacl = None
        self.status = None
        self.uri = None

        ManagedObject.__init__(self, "HostimgTarget", parent_mo_or_dn, **kwargs)

