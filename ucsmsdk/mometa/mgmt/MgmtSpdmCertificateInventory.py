"""This module contains the general information for MgmtSpdmCertificateInventory ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtSpdmCertificateInventoryConsts:
    FAULT_ALERT_SETTING_DISABLED = "disabled"
    FAULT_ALERT_SETTING_FULL = "full"
    FAULT_ALERT_SETTING_PARTIAL = "partial"


class MgmtSpdmCertificateInventory(ManagedObject):
    """This is MgmtSpdmCertificateInventory class."""

    consts = MgmtSpdmCertificateInventoryConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtSpdmCertificateInventory", "mgmtSpdmCertificateInventory", "spdm-cert-inventory", VersionMeta.Version421a, "InputOutput", 0x3f, [], ["admin"], ['mgmtController'], ['mgmtSpdmCertificateData'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fault_alert_setting": MoPropertyMeta("fault_alert_setting", "faultAlertSetting", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "full", "partial"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "faultAlertSetting": "fault_alert_setting", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fault_alert_setting = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtSpdmCertificateInventory", parent_mo_or_dn, **kwargs)
