"""This module contains the general information for VnicSriovHpnConPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicSriovHpnConPolicyConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class VnicSriovHpnConPolicy(ManagedObject):
    """This is VnicSriovHpnConPolicy class."""

    consts = VnicSriovHpnConPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicSriovHpnConPolicy", "vnicSriovHpnConPolicy", "sriov-hpn-con-[name]", VersionMeta.Version432b, "InputOutput", 0x1fff, [], ["admin", "ls-network", "ls-network-policy", "ls-server"], ['orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "completion_queue_count": MoPropertyMeta("completion_queue_count", "completionQueueCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-16"]),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version432b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "interrupt_count": MoPropertyMeta("interrupt_count", "interruptCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-16"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version432b, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "receive_queue_count": MoPropertyMeta("receive_queue_count", "receiveQueueCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-8"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sriovhpn_count": MoPropertyMeta("sriovhpn_count", "sriovhpnCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["1-64"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transmit_queue_count": MoPropertyMeta("transmit_queue_count", "transmitQueueCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["1-8"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "completionQueueCount": "completion_queue_count", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "interruptCount": "interrupt_count", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "receiveQueueCount": "receive_queue_count", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sriovhpnCount": "sriovhpn_count", 
        "status": "status", 
        "transmitQueueCount": "transmit_queue_count", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.completion_queue_count = None
        self.descr = None
        self.int_id = None
        self.interrupt_count = None
        self.policy_level = None
        self.policy_owner = None
        self.receive_queue_count = None
        self.sacl = None
        self.sriovhpn_count = None
        self.status = None
        self.transmit_queue_count = None

        ManagedObject.__init__(self, "VnicSriovHpnConPolicy", parent_mo_or_dn, **kwargs)
