"""This module contains the general information for AdaptorUsnicConnDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorUsnicConnDefConsts():
    pass


class AdaptorUsnicConnDef(ManagedObject):
    """This is AdaptorUsnicConnDef class."""

    consts = AdaptorUsnicConnDefConsts()
    naming_props = set([u'conPolicyName'])

    mo_meta = MoMeta("AdaptorUsnicConnDef", "adaptorUsnicConnDef", "usnic-conn-def-[con_policy_name]", VersionMeta.Version221b, "InputOutput", 0x3fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "read-only"], [u'adaptorHostEthIf'], [u'adaptorEthCompQueueProfile', u'adaptorEthFailoverProfile', u'adaptorEthInterruptProfile', u'adaptorEthOffloadProfile', u'adaptorEthRecvQueueProfile', u'adaptorEthWorkQueueProfile', u'adaptorExtIpV6RssHashProfile', u'adaptorIpV4RssHashProfile', u'adaptorIpV6RssHashProfile', u'adaptorRssProfile'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x4L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "usnic_count": MoPropertyMeta("usnic_count", "usnicCount", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "usnicCount": "usnic_count", 
    }

    def __init__(self, parent_mo_or_dn, con_policy_name, **kwargs):
        self._dirty_mask = 0
        self.con_policy_name = con_policy_name
        self.child_action = None
        self.sacl = None
        self.status = None
        self.usnic_count = None

        ManagedObject.__init__(self, "AdaptorUsnicConnDef", parent_mo_or_dn, **kwargs)

