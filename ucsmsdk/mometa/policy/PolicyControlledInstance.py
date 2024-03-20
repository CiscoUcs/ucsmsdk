"""This module contains the general information for PolicyControlledInstance ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyControlledInstanceConsts:
    RESOLVE_TYPE_NAME = "name"
    RESOLVE_TYPE_RN = "rn"


class PolicyControlledInstance(ManagedObject):
    """This is PolicyControlledInstance class."""

    consts = PolicyControlledInstanceConsts()
    naming_props = set(['type', 'name'])

    mo_meta = MoMeta("PolicyControlledInstance", "policyControlledInstance", "ctrlled-[type]-inst-[name]", VersionMeta.Version211a, "InputOutput", 0x1ff, [], ["admin"], ['policyCommunication', 'policyConfigBackup', 'policyDateTime', 'policyDiscovery', 'policyDns', 'policyEquipment', 'policyFault', 'policyInfraFirmware', 'policyMEp', 'policyModularChassisFan', 'policyMonitoring', 'policyPortConfig', 'policyPowerExtended', 'policyPowerMgmt', 'policyPowerSave', 'policyPsu', 'policySecurity', 'policyStorageAutoConfig'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_dn": MoPropertyMeta("def_dn", "defDn", "string", VersionMeta.Version211a, MoPropertyMeta.CREATE_ONLY, 0x4, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "external_resolve_name": MoPropertyMeta("external_resolve_name", "externalResolveName", "string", VersionMeta.Version211a, MoPropertyMeta.CREATE_ONLY, 0x10, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
        "resolve_type": MoPropertyMeta("resolve_type", "resolveType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["name", "rn"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defDn": "def_dn", 
        "dn": "dn", 
        "externalResolveName": "external_resolve_name", 
        "name": "name", 
        "resolveType": "resolve_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, name, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.name = name
        self.child_action = None
        self.def_dn = None
        self.external_resolve_name = None
        self.resolve_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyControlledInstance", parent_mo_or_dn, **kwargs)
