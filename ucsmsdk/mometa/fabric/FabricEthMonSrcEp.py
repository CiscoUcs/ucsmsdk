"""This module contains the general information for FabricEthMonSrcEp ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricEthMonSrcEpConsts():
    DIRECTION_BOTH = "both"
    DIRECTION_RX = "rx"
    DIRECTION_TX = "tx"


class FabricEthMonSrcEp(ManagedObject):
    """This is FabricEthMonSrcEp class."""

    consts = FabricEthMonSrcEpConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FabricEthMonSrcEp", "fabricEthMonSrcEp", "mon-src-[name]", VersionMeta.Version141i, "InputOutput", 0xffL, [], ["admin", "ext-lan-config", "ext-lan-policy"], [u'adaptorExtEthIf', u'fabricDceSwSrvEp', u'fabricEthEstcEp', u'fabricEthEstcPc', u'fabricEthLanEp', u'fabricEthLanPc', u'fabricFcoeEstcEp', u'fabricFcoeSanEp', u'fabricFcoeSanPc', u'fabricVlan', u'vmNic', u'vnicEther', u'vnicFc', u'vnicIScsi', u'vnicIScsiLCP', u'vnicIpc', u'vnicScsi'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "direction": MoPropertyMeta("direction", "direction", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["both", "rx", "tx"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "session": MoPropertyMeta("session", "session", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["1-255"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "direction": "direction", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "session": "session", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.direction = None
        self.sacl = None
        self.session = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricEthMonSrcEp", parent_mo_or_dn, **kwargs)

