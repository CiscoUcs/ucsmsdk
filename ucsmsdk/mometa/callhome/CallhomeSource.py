"""This module contains the general information for CallhomeSource ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CallhomeSourceConsts():
    URGENCY_ALERT = "alert"
    URGENCY_CRITICAL = "critical"
    URGENCY_DEBUG = "debug"
    URGENCY_EMERGENCY = "emergency"
    URGENCY_ERROR = "error"
    URGENCY_INFO = "info"
    URGENCY_NOTICE = "notice"
    URGENCY_WARNING = "warning"


class CallhomeSource(ManagedObject):
    """This is CallhomeSource class."""

    consts = CallhomeSourceConsts()
    naming_props = set([])

    mo_meta = MoMeta("CallhomeSource", "callhomeSource", "source", VersionMeta.Version101e, "InputOutput", 0x7fffL, [], ["admin", "operations"], [u'callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, 1, 255, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "contact": MoPropertyMeta("contact", "contact", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[^<>""'&]*""", [], []), 
        "contract": MoPropertyMeta("contract", "contract", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, 1, 64, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []), 
        "customer": MoPropertyMeta("customer", "customer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], []), 
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, [], []), 
        "phone": MoPropertyMeta("phone", "phone", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, [], []), 
        "reply_to": MoPropertyMeta("reply_to", "replyTo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x800L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 510, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "urgency": MoPropertyMeta("urgency", "urgency", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, ["alert", "critical", "debug", "emergency", "error", "info", "notice", "warning"], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "contact": "contact", 
        "contract": "contract", 
        "customer": "customer", 
        "dn": "dn", 
        "email": "email", 
        "from": "r_from", 
        "phone": "phone", 
        "replyTo": "reply_to", 
        "rn": "rn", 
        "sacl": "sacl", 
        "site": "site", 
        "status": "status", 
        "urgency": "urgency", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.contact = None
        self.contract = None
        self.customer = None
        self.email = None
        self.r_from = None
        self.phone = None
        self.reply_to = None
        self.sacl = None
        self.site = None
        self.status = None
        self.urgency = None

        ManagedObject.__init__(self, "CallhomeSource", parent_mo_or_dn, **kwargs)

