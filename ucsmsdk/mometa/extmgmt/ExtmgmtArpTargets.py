"""This module contains the general information for ExtmgmtArpTargets ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtmgmtArpTargetsConsts:
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"


class ExtmgmtArpTargets(ManagedObject):
    """This is ExtmgmtArpTargets class."""

    consts = ExtmgmtArpTargetsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtArpTargets", "extmgmtArpTargets", "arp-target-policy", VersionMeta.Version141i, "InputOutput", 0x3ff, [], ["admin", "ext-lan-config"], ['extmgmtIfMonPolicy'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []),
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "max_deadline_timeout": MoPropertyMeta("max_deadline_timeout", "maxDeadlineTimeout", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["5-15"]),
        "number_of_arp_requests": MoPropertyMeta("number_of_arp_requests", "numberOfArpRequests", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-5"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "target_ip1": MoPropertyMeta("target_ip1", "targetIp1", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "target_ip2": MoPropertyMeta("target_ip2", "targetIp2", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "target_ip3": MoPropertyMeta("target_ip3", "targetIp3", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "dn": "dn", 
        "maxDeadlineTimeout": "max_deadline_timeout", 
        "numberOfArpRequests": "number_of_arp_requests", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "targetIp1": "target_ip1", 
        "targetIp2": "target_ip2", 
        "targetIp3": "target_ip3", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.max_deadline_timeout = None
        self.number_of_arp_requests = None
        self.sacl = None
        self.status = None
        self.target_ip1 = None
        self.target_ip2 = None
        self.target_ip3 = None

        ManagedObject.__init__(self, "ExtmgmtArpTargets", parent_mo_or_dn, **kwargs)
