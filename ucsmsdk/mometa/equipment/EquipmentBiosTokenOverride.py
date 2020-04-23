"""This module contains the general information for EquipmentBiosTokenOverride ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentBiosTokenOverrideConsts:
    BIOS_TOKEN_ID_BIOS_VFTPM = "bios-vftpm"
    BIOS_TOKEN_ID_MEMORY_MAPPED_ABOVE_4GB = "memory-mapped-above-4gb"
    BIOS_TOKEN_ID_NONE = "none"
    BIOS_TOKEN_ID_OPTION_ROM = "option-rom"
    BIOS_TOKEN_ID_PSATA = "psata"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentBiosTokenOverride(ManagedObject):
    """This is EquipmentBiosTokenOverride class."""

    consts = EquipmentBiosTokenOverrideConsts()
    naming_props = set(['biosTokenId'])

    mo_meta = MoMeta("EquipmentBiosTokenOverride", "equipmentBiosTokenOverride", "bios-token-override-[bios_token_id]", VersionMeta.Version321d, "InputOutput", 0x1ff, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get", "Set"])

    prop_meta = {
        "bios_token_id": MoPropertyMeta("bios_token_id", "biosTokenId", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x2, None, None, None, ["bios-vftpm", "memory-mapped-above-4gb", "none", "option-rom", "psata"], []),
        "bios_token_name": MoPropertyMeta("bios_token_name", "biosTokenName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "bios_token_value": MoPropertyMeta("bios_token_value", "biosTokenValue", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "biosTokenId": "bios_token_id", 
        "biosTokenName": "bios_token_name", 
        "biosTokenValue": "bios_token_value", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, bios_token_id, **kwargs):
        self._dirty_mask = 0
        self.bios_token_id = bios_token_id
        self.bios_token_name = None
        self.bios_token_value = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBiosTokenOverride", parent_mo_or_dn, **kwargs)
