"""This module contains the general information for FirmwareCatalogPack ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareCatalogPackConsts:
    CONFIG_STATE_FAILED = "failed"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    INT_ID_NONE = "none"
    MODE_ONE_SHOT = "one-shot"
    MODE_STAGED = "staged"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareCatalogPack(ManagedObject):
    """This is FirmwareCatalogPack class."""

    consts = FirmwareCatalogPackConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareCatalogPack", "firmwareCatalogPack", "fw-catalog-pack-[name]", VersionMeta.Version211a, "InputOutput", 0xfff, [], ["admin", "operations"], ['orgOrg'], ['firmwareBackupVersionHolder', 'firmwarePackItem'], ["Get", "Set"])

    prop_meta = {
        "catalog_name": MoPropertyMeta("catalog_name", "catalogName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "catalog_version": MoPropertyMeta("catalog_version", "catalogVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "not-applied", "ok"], []),
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["one-shot", "staged"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []),
    }

    prop_map = {
        "catalogName": "catalog_name", 
        "catalogVersion": "catalog_version", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageSize": "stage_size", 
        "status": "status", 
        "updateTrigger": "update_trigger", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.catalog_name = None
        self.catalog_version = None
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.descr = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareCatalogPack", parent_mo_or_dn, **kwargs)
