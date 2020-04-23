"""This module contains the general information for ExtvmmFabricNetwork ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtvmmFabricNetworkConsts:
    INT_ID_NONE = "none"
    NETWORK_TYPE_CONNECTED = "connected"
    NETWORK_TYPE_NOT_CONNECTED = "not-connected"
    NETWORK_TYPE_NOT_CONNECTED_PVLANS = "not-connected-pvlans"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REF_OPER_STATE_INVALID_REFERENCE = "invalid-reference"
    REF_OPER_STATE_UP = "up"


class ExtvmmFabricNetwork(ManagedObject):
    """This is ExtvmmFabricNetwork class."""

    consts = ExtvmmFabricNetworkConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ExtvmmFabricNetwork", "extvmmFabricNetwork", "fabric-network-[name]", VersionMeta.Version221b, "InputOutput", 0x3ff, [], ["admin", "ls-network", "ls-network-policy"], ['extvmmNetworkSets'], ['extvmmFabricNetworkDefinition'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "network_type": MoPropertyMeta("network_type", "networkType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["connected", "not-connected", "not-connected-pvlans"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "ref_oper_state": MoPropertyMeta("ref_oper_state", "refOperState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["invalid-reference", "up"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "guid": "guid", 
        "intId": "int_id", 
        "name": "name", 
        "networkType": "network_type", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "refOperState": "ref_oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.guid = None
        self.int_id = None
        self.network_type = None
        self.policy_level = None
        self.policy_owner = None
        self.ref_oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtvmmFabricNetwork", parent_mo_or_dn, **kwargs)
