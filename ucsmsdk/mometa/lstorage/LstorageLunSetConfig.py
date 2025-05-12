"""This module contains the general information for LstorageLunSetConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageLunSetConfigConsts:
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_UNDEPLOYED = "undeployed"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_OK = "ok"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"
    RAID_LEVEL_JBOD = "jbod"
    RAID_LEVEL_SIMPLE = "simple"
    RAID_LEVEL_STRIPE = "stripe"
    RAID_LEVEL_UNSPECIFIED = "unspecified"


class LstorageLunSetConfig(ManagedObject):
    """This is LstorageLunSetConfig class."""

    consts = LstorageLunSetConfigConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("LstorageLunSetConfig", "lstorageLunSetConfig", "lun-set-config-[name]", VersionMeta.Version402a, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage", "ls-storage-policy"], ['lstorageProfile', 'lstorageProfileDef'], ['lstorageLunSetDiskSlot', 'lstorageVirtualDriveDef'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["offline", "online", "undeployed"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable),){0,10}(defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "ok"], []),
        "disk_slot_range": MoPropertyMeta("disk_slot_range", "diskSlotRange", "string", VersionMeta.Version402a, MoPropertyMeta.CREATE_ONLY, 0x8, None, None, r"""[,\-0-9]{1,104}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version402a, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,10}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute-degraded", "compute-inoperable", "offline", "online", "undefined"], []),
        "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["jbod", "simple", "stripe", "unspecified"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "diskSlotRange": "disk_slot_range", 
        "dn": "dn", 
        "name": "name", 
        "operState": "oper_state", 
        "raidLevel": "raid_level", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.disk_slot_range = None
        self.oper_state = None
        self.raid_level = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLunSetConfig", parent_mo_or_dn, **kwargs)
