"""This module contains the general information for AdaptorVmmqConnDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorVmmqConnDefConsts:
    pass


class AdaptorVmmqConnDef(ManagedObject):
    """This is AdaptorVmmqConnDef class."""

    consts = AdaptorVmmqConnDefConsts()
    naming_props = set([u'conPolicyName'])

    mo_meta = MoMeta("AdaptorVmmqConnDef", "adaptorVmmqConnDef", "vmmq-conn-def-[con_policy_name]", None, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "read-only"], [u'adaptorHostEthIf'], [u'adaptorEthCompQueueProfile', u'adaptorEthInterruptProfile', u'adaptorEthRecvQueueProfile', u'adaptorEthRoCEProfile', u'adaptorEthWorkQueueProfile', u'adaptorRssProfile'], [None])

    prop_meta = {
        "vmmq_sub_vnic_count": MoPropertyMeta("vmmq_sub_vnic_count", "VmmqSubVnicCount", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", None, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "VmmqSubVnicCount": "vmmq_sub_vnic_count", 
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, con_policy_name, **kwargs):
        self._dirty_mask = 0
        self.con_policy_name = con_policy_name
        self.vmmq_sub_vnic_count = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorVmmqConnDef", parent_mo_or_dn, **kwargs)
