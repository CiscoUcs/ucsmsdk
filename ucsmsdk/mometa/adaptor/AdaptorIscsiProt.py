"""This module contains the general information for AdaptorIscsiProt ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorIscsiProtConsts():
    TCP_TIME_STAMP_FALSE = "false"
    TCP_TIME_STAMP_NO = "no"
    TCP_TIME_STAMP_TRUE = "true"
    TCP_TIME_STAMP_YES = "yes"


class AdaptorIscsiProt(ManagedObject):
    """This is AdaptorIscsiProt class."""

    consts = AdaptorIscsiProtConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorIscsiProt", "adaptorIscsiProt", "iscsi-prot", VersionMeta.Version201m, "InputOutput", 0x1fL, [], ["read-only"], [u'adaptorHostIscsiIf'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_time_out": MoPropertyMeta("connection_time_out", "connectionTimeOut", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-255"]), 
        "dhcp_time_out": MoPropertyMeta("dhcp_time_out", "dhcpTimeOut", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["60-300"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "initiator_name": MoPropertyMeta("initiator_name", "initiatorName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "lun_busy_retry_count": MoPropertyMeta("lun_busy_retry_count", "lunBusyRetryCount", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-60"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tcp_time_stamp": MoPropertyMeta("tcp_time_stamp", "tcpTimeStamp", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "connectionTimeOut": "connection_time_out", 
        "dhcpTimeOut": "dhcp_time_out", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "initiatorName": "initiator_name", 
        "lunBusyRetryCount": "lun_busy_retry_count", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tcpTimeStamp": "tcp_time_stamp", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.connection_time_out = None
        self.dhcp_time_out = None
        self.flt_aggr = None
        self.initiator_name = None
        self.lun_busy_retry_count = None
        self.sacl = None
        self.status = None
        self.tcp_time_stamp = None

        ManagedObject.__init__(self, "AdaptorIscsiProt", parent_mo_or_dn, **kwargs)
