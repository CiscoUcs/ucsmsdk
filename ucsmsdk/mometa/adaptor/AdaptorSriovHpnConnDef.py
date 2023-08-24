"""This module contains the general information for AdaptorSriovHpnConnDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorSriovHpnConnDefConsts:
    pass


class AdaptorSriovHpnConnDef(ManagedObject):
    """This is AdaptorSriovHpnConnDef class."""

    consts = AdaptorSriovHpnConnDefConsts()
    naming_props = set(['conPolicyName'])

    mo_meta = MoMeta("AdaptorSriovHpnConnDef", "adaptorSriovHpnConnDef", "sriov-hpn-conn-def-[con_policy_name]", VersionMeta.Version432b, "InputOutput", 0x3ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "read-only"], ['adaptorHostEthIf'], [], [None])

    prop_meta = {
        "sriov_hpn_vf_count": MoPropertyMeta("sriov_hpn_vf_count", "SriovHpnVfCount", "uint", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "completion_queue_count": MoPropertyMeta("completion_queue_count", "completionQueueCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-16"]),
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version432b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "interrupt_count": MoPropertyMeta("interrupt_count", "interruptCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-16"]),
        "receive_queue_count": MoPropertyMeta("receive_queue_count", "receiveQueueCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-8"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transmit_queue_count": MoPropertyMeta("transmit_queue_count", "transmitQueueCount", "ushort", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["1-8"]),
    }

    prop_map = {
        "SriovHpnVfCount": "sriov_hpn_vf_count", 
        "childAction": "child_action", 
        "completionQueueCount": "completion_queue_count", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "interruptCount": "interrupt_count", 
        "receiveQueueCount": "receive_queue_count", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transmitQueueCount": "transmit_queue_count", 
    }

    def __init__(self, parent_mo_or_dn, con_policy_name, **kwargs):
        self._dirty_mask = 0
        self.con_policy_name = con_policy_name
        self.sriov_hpn_vf_count = None
        self.child_action = None
        self.completion_queue_count = None
        self.interrupt_count = None
        self.receive_queue_count = None
        self.sacl = None
        self.status = None
        self.transmit_queue_count = None

        ManagedObject.__init__(self, "AdaptorSriovHpnConnDef", parent_mo_or_dn, **kwargs)
