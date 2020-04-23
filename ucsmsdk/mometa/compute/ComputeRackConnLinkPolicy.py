"""This module contains the general information for ComputeRackConnLinkPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeRackConnLinkPolicyConsts:
    INT_ID_NONE = "none"
    LINK_GROUPING_NONE = "none"
    LINK_GROUPING_PORT_CHANNEL = "port-channel"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class ComputeRackConnLinkPolicy(ManagedObject):
    """This is ComputeRackConnLinkPolicy class."""

    consts = ComputeRackConnLinkPolicyConsts()
    naming_props = set(['rackId', 'switchId'])

    mo_meta = MoMeta("ComputeRackConnLinkPolicy", "computeRackConnLinkPolicy", "rack-conn-link-policy-rack-unit-[rack_id]-fabric-[switch_id]", VersionMeta.Version323a, "InputOutput", 0x7ff, [], ["admin", "pn-policy"], ['orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "link_grouping": MoPropertyMeta("link_grouping", "linkGrouping", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["none", "port-channel"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rack_id": MoPropertyMeta("rack_id", "rackId", "uint", VersionMeta.Version323a, MoPropertyMeta.NAMING, 0x80, None, None, None, [], ["1-255"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version323a, MoPropertyMeta.NAMING, 0x400, None, None, None, ["A", "B", "NONE"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "linkGrouping": "link_grouping", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qualifier": "qualifier", 
        "rackId": "rack_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, rack_id, switch_id, **kwargs):
        self._dirty_mask = 0
        self.rack_id = rack_id
        self.switch_id = switch_id
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.link_grouping = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.qualifier = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeRackConnLinkPolicy", parent_mo_or_dn, **kwargs)
