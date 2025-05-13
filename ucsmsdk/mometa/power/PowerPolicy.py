"""This module contains the general information for PowerPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerPolicyConsts:
    AGGRESSIVE_COOLING_DISABLE = "Disable"
    AGGRESSIVE_COOLING_ENABLE = "Enable"
    CONFIGURED_PPL_DEFAULT = "Default"
    CONFIGURED_PPL_MAX = "Max"
    CONFIGURED_PPL_MIN = "Min"
    FAN_SPEED_ACOUSTIC = "acoustic"
    FAN_SPEED_ANY = "any"
    FAN_SPEED_BALANCED = "balanced"
    FAN_SPEED_ERR = "err"
    FAN_SPEED_HIGH_POWER = "high-power"
    FAN_SPEED_LOW_POWER = "low-power"
    FAN_SPEED_MAX_COOLING = "max-cooling"
    FAN_SPEED_MAX_POWER = "max-power"
    FAN_SPEED_NA = "na"
    FAN_SPEED_NO_UPDATE = "no-update"
    FAN_SPEED_NOT_SUPPORTED = "not-supported"
    FAN_SPEED_PERFORMANCE = "performance"
    INT_ID_NONE = "none"
    OPER_PRIO_NO_CAP = "no-cap"
    OPER_PRIO_UTILITY = "utility"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PRIO_NO_CAP = "no-cap"
    PRIO_UTILITY = "utility"


class PowerPolicy(ManagedObject):
    """This is PowerPolicy class."""

    consts = PowerPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PowerPolicy", "powerPolicy", "power-policy-[name]", VersionMeta.Version141i, "InputOutput", 0xfff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy"], ['orgOrg', 'policySystemEp'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "aggressive_cooling": MoPropertyMeta("aggressive_cooling", "aggressiveCooling", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disable", "Enable"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "configured_ppl": MoPropertyMeta("configured_ppl", "configuredPpl", "string", VersionMeta.Version436a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Default", "Max", "Min"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "fan_speed": MoPropertyMeta("fan_speed", "fanSpeed", "string", VersionMeta.Version226c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["acoustic", "any", "balanced", "err", "high-power", "low-power", "max-cooling", "max-power", "na", "no-update", "not-supported", "performance"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_prio": MoPropertyMeta("oper_prio", "operPrio", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-cap", "utility"], ["1-10"]),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["no-cap", "utility"], ["1-10"]),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "aggressiveCooling": "aggressive_cooling", 
        "childAction": "child_action", 
        "configuredPpl": "configured_ppl", 
        "descr": "descr", 
        "dn": "dn", 
        "fanSpeed": "fan_speed", 
        "intId": "int_id", 
        "name": "name", 
        "operPrio": "oper_prio", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "prio": "prio", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.aggressive_cooling = None
        self.child_action = None
        self.configured_ppl = None
        self.descr = None
        self.fan_speed = None
        self.int_id = None
        self.oper_prio = None
        self.policy_level = None
        self.policy_owner = None
        self.prio = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PowerPolicy", parent_mo_or_dn, **kwargs)
