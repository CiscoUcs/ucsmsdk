"""This module contains the general information for BiosBootDev ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosBootDevConsts:
    ERR_VALUE_FAILURE = "FAILURE"
    ERR_VALUE_SUCCESS = "SUCCESS"
    ORDER_1 = "1"
    ORDER_2 = "2"
    ORDER_3 = "3"
    ORDER_4 = "4"
    ORDER_5 = "5"
    ORDER_6 = "6"
    ORDER_7 = "7"


class BiosBootDev(ManagedObject):
    """This is BiosBootDev class."""

    consts = BiosBootDevConsts()
    naming_props = set(['order'])

    mo_meta = MoMeta("BiosBootDev", "biosBootDev", "[order]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["read-only"], ['biosBootDevGrp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "device_name": MoPropertyMeta("device_name", "deviceName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "err_value": MoPropertyMeta("err_value", "errValue", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FAILURE", "SUCCESS"], []),
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, ["1", "2", "3", "4", "5", "6", "7"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "deviceName": "device_name", 
        "dn": "dn", 
        "errValue": "err_value", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.descr = None
        self.device_name = None
        self.err_value = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "BiosBootDev", parent_mo_or_dn, **kwargs)
