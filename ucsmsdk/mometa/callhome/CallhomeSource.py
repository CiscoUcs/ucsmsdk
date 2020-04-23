"""This module contains the general information for CallhomeSource ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CallhomeSourceConsts:
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

    mo_meta = MoMeta("CallhomeSource", "callhomeSource", "source", VersionMeta.Version101e, "InputOutput", 0x7fff, [], ["admin", "operations"], ['callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "contact": MoPropertyMeta("contact", "contact", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`^]*""", [], []),
        "contract": MoPropertyMeta("contract", "contract", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []),
        "customer": MoPropertyMeta("customer", "customer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
        "phone": MoPropertyMeta("phone", "phone", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []),
        "reply_to": MoPropertyMeta("reply_to", "replyTo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?`<>""'&^]+""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "urgency": MoPropertyMeta("urgency", "urgency", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["alert", "critical", "debug", "emergency", "error", "info", "notice", "warning"], []),
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
