"""This module contains the general information for CallhomeSmtp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CallhomeSmtpConsts:
    SMTP_AUTHENTICATION_OFF = "off"
    SMTP_AUTHENTICATION_ON = "on"


class CallhomeSmtp(ManagedObject):
    """This is CallhomeSmtp class."""

    consts = CallhomeSmtpConsts()
    naming_props = set([])

    mo_meta = MoMeta("CallhomeSmtp", "callhomeSmtp", "smtp", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["admin", "operations"], ['callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []),
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version423b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[!#%\*\+,\-\./:=@\\\^_\{\}~a-zA-Z0-9]{0,56}""", [], []),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "smtp_authentication": MoPropertyMeta("smtp_authentication", "smtpAuthentication", "string", VersionMeta.Version423b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["off", "on"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version423b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[a-zA-Z0-9_.-]{0,255}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "host": "host", 
        "password": "password", 
        "port": "port", 
        "rn": "rn", 
        "sacl": "sacl", 
        "smtpAuthentication": "smtp_authentication", 
        "status": "status", 
        "username": "username", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.host = None
        self.password = None
        self.port = None
        self.sacl = None
        self.smtp_authentication = None
        self.status = None
        self.username = None

        ManagedObject.__init__(self, "CallhomeSmtp", parent_mo_or_dn, **kwargs)
