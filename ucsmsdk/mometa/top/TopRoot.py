"""This module contains the general information for TopRoot ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class TopRootConsts():
    pass


class TopRoot(ManagedObject):
    """This is TopRoot class."""

    consts = TopRootConsts()
    naming_props = set([])

    mo_meta = MoMeta("TopRoot", "topRoot", "", VersionMeta.Version101e, "InputOutput", 0x1fL, [], ["read-only"], [], [u'aaaLog', u'apeManager', u'callhomeEp', u'capabilityCatalogue', u'clitestTypeTest', u'clitestTypeTest2', u'computeDefaults', u'dhcpInst', u'eventHolder', u'eventLog', u'extpolEp', u'fabricEp', u'faultHolder', u'fcpoolUniverse', u'gmetaEp', u'identMetaVerse', u'ippoolUniverse', u'iqnpoolUniverse', u'macpoolUniverse', u'nfsEp', u'observeObservedCont', u'orgOrg', u'policyPolicyEp', u'procManager', u'statsHolder', u'storageCloud', u'storageDomainEp', u'syntheticFileSystem', u'topMetaInf', u'topSysDefaults', u'topSystem', u'uuidpoolUniverse', u'vmEp'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "TopRoot", parent_mo_or_dn, **kwargs)

