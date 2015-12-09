"""This module contains the general information for EtherPIoEndPoint ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EtherPIoEndPointConsts():
    EP_CLOUD_TYPE_LAN = "lan"
    EP_CLOUD_TYPE_SAN = "san"
    EP_CLOUD_TYPE_UNCLASSIFIED = "unclassified"


class EtherPIoEndPoint(ManagedObject):
    """This is EtherPIoEndPoint class."""

    consts = EtherPIoEndPointConsts()
    naming_props = set([u'epCloudType'])

    mo_meta = MoMeta("EtherPIoEndPoint", "etherPIoEndPoint", "EndPointDn-cloud-[ep_cloud_type]", VersionMeta.Version211a, "InputOutput", 0x7fL, [], ["read-only"], [u'etherPIo'], [], [None])

    prop_meta = {
        "end_point_dn": MoPropertyMeta("end_point_dn", "EndPointDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "ep_cloud_type": MoPropertyMeta("ep_cloud_type", "epCloudType", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8L, None, None, None, ["lan", "san", "unclassified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
    }

    prop_map = {
        "EndPointDn": "end_point_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epCloudType": "ep_cloud_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "usrLbl": "usr_lbl", 
    }

    def __init__(self, parent_mo_or_dn, ep_cloud_type, **kwargs):
        self._dirty_mask = 0
        self.ep_cloud_type = ep_cloud_type
        self.end_point_dn = None
        self.child_action = None
        self.sacl = None
        self.status = None
        self.usr_lbl = None

        ManagedObject.__init__(self, "EtherPIoEndPoint", parent_mo_or_dn, **kwargs)

