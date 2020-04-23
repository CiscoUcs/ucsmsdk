"""This module contains the general information for LicenseFeature ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LicenseFeatureConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    TYPE_BOOLEAN = "boolean"
    TYPE_COUNTED = "counted"


class LicenseFeature(ManagedObject):
    """This is LicenseFeature class."""

    consts = LicenseFeatureConsts()
    naming_props = set(['name', 'vendor', 'version'])

    mo_meta = MoMeta("LicenseFeature", "licenseFeature", "feature-[name]-[vendor]-[version]", VersionMeta.Version141i, "InputOutput", 0x3ff, [], ["admin"], ['licenseEp'], ['licenseInstance'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "grace_period": MoPropertyMeta("grace_period", "gracePeriod", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["boolean", "counted"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x100, None, None, None, [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x200, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "gracePeriod": "grace_period", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, name, vendor, version, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.vendor = vendor
        self.version = version
        self.child_action = None
        self.descr = None
        self.grace_period = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LicenseFeature", parent_mo_or_dn, **kwargs)
