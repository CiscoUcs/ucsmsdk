"""This module contains the general information for ExtmgmtIfMonPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtmgmtIfMonPolicyConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ENABLE_HAFAILOVER_FALSE = "false"
    ENABLE_HAFAILOVER_NO = "no"
    ENABLE_HAFAILOVER_TRUE = "true"
    ENABLE_HAFAILOVER_YES = "yes"
    INT_ID_NONE = "none"
    MONITOR_MECHANISM_ARP_TARGET_PING = "arpTargetPing"
    MONITOR_MECHANISM_GATEWAY_PING = "gatewayPing"
    MONITOR_MECHANISM_MII_STATUS = "miiStatus"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class ExtmgmtIfMonPolicy(ManagedObject):
    """This is ExtmgmtIfMonPolicy class."""

    consts = ExtmgmtIfMonPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtIfMonPolicy", "extmgmtIfMonPolicy", "extmgmt-intf-monitor-policy", VersionMeta.Version141i, "InputOutput", 0x1fff, [], ["admin", "ext-lan-config"], ['topSystem'], ['extmgmtArpTargets', 'extmgmtGatewayPing', 'extmgmtMiiStatus', 'extmgmtNdiscTargets'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "enable_ha_failover": MoPropertyMeta("enable_ha_failover", "enableHAFailover", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "max_fail_report_count": MoPropertyMeta("max_fail_report_count", "maxFailReportCount", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["2-5"]),
        "monitor_mechanism": MoPropertyMeta("monitor_mechanism", "monitorMechanism", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["arpTargetPing", "gatewayPing", "miiStatus"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "poll_interval": MoPropertyMeta("poll_interval", "pollInterval", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["90-300"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "enableHAFailover": "enable_ha_failover", 
        "intId": "int_id", 
        "maxFailReportCount": "max_fail_report_count", 
        "monitorMechanism": "monitor_mechanism", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "pollInterval": "poll_interval", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.enable_ha_failover = None
        self.int_id = None
        self.max_fail_report_count = None
        self.monitor_mechanism = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.poll_interval = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtmgmtIfMonPolicy", parent_mo_or_dn, **kwargs)
