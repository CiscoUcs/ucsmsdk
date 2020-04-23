"""This module contains the general information for AdaptorHostScsiLunRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorHostScsiLunRefConsts:
    BOOT_DEV_DISABLED = "disabled"
    BOOT_DEV_ENABLED = "enabled"
    LUN_ORDER_NOT_APPLICABLE = "not-applicable"
    OPER_LUN_ORDER_NOT_APPLICABLE = "not-applicable"


class AdaptorHostScsiLunRef(ManagedObject):
    """This is AdaptorHostScsiLunRef class."""

    consts = AdaptorHostScsiLunRefConsts()
    naming_props = set(['lunOrder'])

    mo_meta = MoMeta("AdaptorHostScsiLunRef", "adaptorHostScsiLunRef", "host-scsi-lun-[lun_order]", VersionMeta.Version251a, "InputOutput", 0x3f, [], ["admin"], ['adaptorHostScsiIf'], [], ["Get"])

    prop_meta = {
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "lun_dn": MoPropertyMeta("lun_dn", "lunDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "lun_id": MoPropertyMeta("lun_id", "lunId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "lun_name": MoPropertyMeta("lun_name", "lunName", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "lun_order": MoPropertyMeta("lun_order", "lunOrder", "string", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["not-applicable"], ["0-64"]),
        "oper_lun_id": MoPropertyMeta("oper_lun_id", "operLunId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oper_lun_order": MoPropertyMeta("oper_lun_order", "operLunOrder", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-64"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "bootDev": "boot_dev", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "lunDn": "lun_dn", 
        "lunId": "lun_id", 
        "lunName": "lun_name", 
        "lunOrder": "lun_order", 
        "operLunId": "oper_lun_id", 
        "operLunOrder": "oper_lun_order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, lun_order, **kwargs):
        self._dirty_mask = 0
        self.lun_order = lun_order
        self.boot_dev = None
        self.child_action = None
        self.flt_aggr = None
        self.lun_dn = None
        self.lun_id = None
        self.lun_name = None
        self.oper_lun_id = None
        self.oper_lun_order = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorHostScsiLunRef", parent_mo_or_dn, **kwargs)
