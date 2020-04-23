"""This module contains the general information for EquipmentLocalDiskDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentLocalDiskDefConsts:
    FORCE_UPDATE_VERSION_FALSE = "false"
    FORCE_UPDATE_VERSION_NO = "no"
    FORCE_UPDATE_VERSION_TRUE = "true"
    FORCE_UPDATE_VERSION_YES = "yes"
    INT_ID_NONE = "none"
    ME4308_SUPPORTED_FALSE = "false"
    ME4308_SUPPORTED_NO = "no"
    ME4308_SUPPORTED_TRUE = "true"
    ME4308_SUPPORTED_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SELF_ENCRYPTING_DRIVE_FALSE = "false"
    SELF_ENCRYPTING_DRIVE_NO = "no"
    SELF_ENCRYPTING_DRIVE_TRUE = "true"
    SELF_ENCRYPTING_DRIVE_YES = "yes"
    TECHNOLOGY_HDD = "HDD"
    TECHNOLOGY_SSD = "SSD"
    TECHNOLOGY_UNSPECIFIED = "unspecified"


class EquipmentLocalDiskDef(ManagedObject):
    """This is EquipmentLocalDiskDef class."""

    consts = EquipmentLocalDiskDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentLocalDiskDef", "equipmentLocalDiskDef", "disk", VersionMeta.Version101e, "InputOutput", 0xff, [], [""], ['equipmentLocalDiskCapProvider'], [], ["Get"])

    prop_meta = {
        "block_size": MoPropertyMeta("block_size", "blockSize", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cache_size": MoPropertyMeta("cache_size", "cacheSize", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "force_update_version": MoPropertyMeta("force_update_version", "forceUpdateVersion", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "me4308_supported": MoPropertyMeta("me4308_supported", "me4308Supported", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "rotational_speed": MoPropertyMeta("rotational_speed", "rotationalSpeed", "float", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "seek_average_read_write": MoPropertyMeta("seek_average_read_write", "seekAverageReadWrite", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "seek_track_to_track_read_write": MoPropertyMeta("seek_track_to_track_read_write", "seekTrackToTrackReadWrite", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "self_encrypting_drive": MoPropertyMeta("self_encrypting_drive", "selfEncryptingDrive", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "technology": MoPropertyMeta("technology", "technology", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["HDD", "SSD", "unspecified"], []),
    }

    prop_map = {
        "blockSize": "block_size", 
        "cacheSize": "cache_size", 
        "capacity": "capacity", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "forceUpdateVersion": "force_update_version", 
        "intId": "int_id", 
        "linkSpeed": "link_speed", 
        "me4308Supported": "me4308_supported", 
        "name": "name", 
        "numberOfBlocks": "number_of_blocks", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "rotationalSpeed": "rotational_speed", 
        "sacl": "sacl", 
        "seekAverageReadWrite": "seek_average_read_write", 
        "seekTrackToTrackReadWrite": "seek_track_to_track_read_write", 
        "selfEncryptingDrive": "self_encrypting_drive", 
        "status": "status", 
        "technology": "technology", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.block_size = None
        self.cache_size = None
        self.capacity = None
        self.child_action = None
        self.descr = None
        self.force_update_version = None
        self.int_id = None
        self.link_speed = None
        self.me4308_supported = None
        self.name = None
        self.number_of_blocks = None
        self.policy_level = None
        self.policy_owner = None
        self.rotational_speed = None
        self.sacl = None
        self.seek_average_read_write = None
        self.seek_track_to_track_read_write = None
        self.self_encrypting_drive = None
        self.status = None
        self.technology = None

        ManagedObject.__init__(self, "EquipmentLocalDiskDef", parent_mo_or_dn, **kwargs)
