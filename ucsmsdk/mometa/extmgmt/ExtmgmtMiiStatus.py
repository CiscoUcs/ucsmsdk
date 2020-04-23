"""This module contains the general information for ExtmgmtMiiStatus ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtmgmtMiiStatusConsts:
    pass


class ExtmgmtMiiStatus(ManagedObject):
    """This is ExtmgmtMiiStatus class."""

    consts = ExtmgmtMiiStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtMiiStatus", "extmgmtMiiStatus", "mii-status-policy", VersionMeta.Version141i, "InputOutput", 0x7f, [], ["admin", "ext-lan-config"], ['extmgmtIfMonPolicy'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "max_retry_count": MoPropertyMeta("max_retry_count", "maxRetryCount", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-3"]),
        "retry_interval": MoPropertyMeta("retry_interval", "retryInterval", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["3-10"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxRetryCount": "max_retry_count", 
        "retryInterval": "retry_interval", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.max_retry_count = None
        self.retry_interval = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtmgmtMiiStatus", parent_mo_or_dn, **kwargs)
