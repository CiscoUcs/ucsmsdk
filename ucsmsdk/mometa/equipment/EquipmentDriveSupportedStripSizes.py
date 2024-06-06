"""This module contains the general information for EquipmentDriveSupportedStripSizes ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentDriveSupportedStripSizesConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentDriveSupportedStripSizes(ManagedObject):
    """This is EquipmentDriveSupportedStripSizes class."""

    consts = EquipmentDriveSupportedStripSizesConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentDriveSupportedStripSizes", "equipmentDriveSupportedStripSizes", "drive-supported-strip-sizes", VersionMeta.Version434a, "InputOutput", 0xff, [], [""], ['equipmentLocalDiskControllerCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "hdd_supported_strip_sizes": MoPropertyMeta("hdd_supported_strip_sizes", "hddSupportedStripSizes", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB),){0,19}(defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB){0,1}""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "ssd_supported_strip_sizes": MoPropertyMeta("ssd_supported_strip_sizes", "ssdSupportedStripSizes", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB),){0,19}(defaultValue|unknown|not-applicable|8KB|16KB|32KB|64KB|128KB|256KB|512KB|1MB|2MB|4MB|8MB|16MB|32MB|64MB|128MB|256MB|512MB){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "hddSupportedStripSizes": "hdd_supported_strip_sizes", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "ssdSupportedStripSizes": "ssd_supported_strip_sizes", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.hdd_supported_strip_sizes = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.ssd_supported_strip_sizes = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentDriveSupportedStripSizes", parent_mo_or_dn, **kwargs)
