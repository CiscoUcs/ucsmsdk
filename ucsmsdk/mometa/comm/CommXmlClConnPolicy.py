"""This module contains the general information for CommXmlClConnPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommXmlClConnPolicyConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CLIENT_TYPE_EXTRENAL_API_CLIENT = "extrenal-api-client"
    CLIENT_TYPE_FLEX_UI = "flex-ui"
    CLIENT_TYPE_JAVA_UI = "java-ui"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommXmlClConnPolicy(ManagedObject):
    """This is CommXmlClConnPolicy class."""

    consts = CommXmlClConnPolicyConsts()
    naming_props = set(['clientType'])

    mo_meta = MoMeta("CommXmlClConnPolicy", "commXmlClConnPolicy", "xmlclconnpolicy-[client_type]", VersionMeta.Version131c, "InputOutput", 0x7ff, [], ["aaa", "admin"], ['commSvcEp'], [], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "client_type": MoPropertyMeta("client_type", "clientType", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x8, None, None, None, ["extrenal-api-client", "flex-ui", "java-ui"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131c, MoPropertyMeta.CREATE_ONLY, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_port": MoPropertyMeta("oper_port", "operPort", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["0-65535"]),
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "clientType": "client_type", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operPort": "oper_port", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "port": "port", 
        "proto": "proto", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, client_type, **kwargs):
        self._dirty_mask = 0
        self.client_type = client_type
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.oper_port = None
        self.policy_level = None
        self.policy_owner = None
        self.port = None
        self.proto = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CommXmlClConnPolicy", parent_mo_or_dn, **kwargs)
