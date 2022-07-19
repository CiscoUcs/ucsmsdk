"""This module contains the general information for LsPower ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsPowerConsts:
    SOFT_SHUTDOWN_TIMER_150_SECS = "150-secs"
    SOFT_SHUTDOWN_TIMER_300_SECS = "300-secs"
    SOFT_SHUTDOWN_TIMER_600_SECS = "600-secs"
    SOFT_SHUTDOWN_TIMER_NEVER = "never"
    STATE_ADMIN_DOWN = "admin-down"
    STATE_ADMIN_UP = "admin-up"
    STATE_BIOS_PASSWORD_RESET_IMMEDIATE = "bios-password-reset-immediate"
    STATE_BMC_RESET_IMMEDIATE = "bmc-reset-immediate"
    STATE_BMC_RESET_WAIT = "bmc-reset-wait"
    STATE_CMOS_RESET_IMMEDIATE = "cmos-reset-immediate"
    STATE_CYCLE_IMMEDIATE = "cycle-immediate"
    STATE_CYCLE_WAIT = "cycle-wait"
    STATE_DIAGNOSTIC_INTERRUPT = "diagnostic-interrupt"
    STATE_DOWN = "down"
    STATE_HARD_RESET_IMMEDIATE = "hard-reset-immediate"
    STATE_HARD_RESET_WAIT = "hard-reset-wait"
    STATE_IPMI_RESET = "ipmi-reset"
    STATE_KVM_RESET = "kvm-reset"
    STATE_SOFT_SHUT_DOWN = "soft-shut-down"
    STATE_SOFT_SHUT_DOWN_ONLY = "soft-shut-down-only"
    STATE_UP = "up"


class LsPower(ManagedObject):
    """This is LsPower class."""

    consts = LsPowerConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsPower", "lsPower", "power", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-oper", "ls-server-policy", "pn-equipment", "pn-maintenance", "pn-policy"], ['lsServer'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "soft_shutdown_timer": MoPropertyMeta("soft_shutdown_timer", "softShutdownTimer", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["150-secs", "300-secs", "600-secs", "never"], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["admin-down", "admin-up", "bios-password-reset-immediate", "bmc-reset-immediate", "bmc-reset-wait", "cmos-reset-immediate", "cycle-immediate", "cycle-wait", "diagnostic-interrupt", "down", "hard-reset-immediate", "hard-reset-wait", "ipmi-reset", "kvm-reset", "soft-shut-down", "soft-shut-down-only", "up"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "softShutdownTimer": "soft_shutdown_timer", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.soft_shutdown_timer = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "LsPower", parent_mo_or_dn, **kwargs)
