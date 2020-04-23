"""This module contains the general information for FirmwareActivity ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareActivityConsts:
    SERVERS_POWER_STATE_NONE = "none"
    SERVERS_POWER_STATE_OFF = "off"
    SERVERS_POWER_STATE_OFF_NOWAIT = "off-nowait"
    SERVERS_POWER_STATE_ON = "on"


class FirmwareActivity(ManagedObject):
    """This is FirmwareActivity class."""

    consts = FirmwareActivityConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareActivity", "firmwareActivity", "fw-activity", VersionMeta.Version251a, "InputOutput", 0x1f, [], ["admin"], ['equipmentChassis'], [], [None])

    prop_meta = {
        "activity_trigger_time": MoPropertyMeta("activity_trigger_time", "activityTriggerTime", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "chassis_comp_in_activation_dn": MoPropertyMeta("chassis_comp_in_activation_dn", "chassisCompInActivationDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "server_comp_in_activation_dn": MoPropertyMeta("server_comp_in_activation_dn", "serverCompInActivationDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "servers_power_state": MoPropertyMeta("servers_power_state", "serversPowerState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "off", "off-nowait", "on"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "upgrade_priority_info": MoPropertyMeta("upgrade_priority_info", "upgradePriorityInfo", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|cmc-update|cmc-activate|board-controller|storage-controller|chassis-adaptor-update|chassis-adaptor-activate|cmc-right-update|cmc-right-activate|chassis-adaptor-right-update|chassis-adaptor-right-activate|sas-expander-update|sas-expander-activate|sas-expander-right-update|sas-expander-right-activate|board-controller-right),){0,15}(none|cmc-update|cmc-activate|board-controller|storage-controller|chassis-adaptor-update|chassis-adaptor-activate|cmc-right-update|cmc-right-activate|chassis-adaptor-right-update|chassis-adaptor-right-activate|sas-expander-update|sas-expander-activate|sas-expander-right-update|sas-expander-right-activate|board-controller-right){0,1}""", [], []),
    }

    prop_map = {
        "activityTriggerTime": "activity_trigger_time", 
        "chassisCompInActivationDn": "chassis_comp_in_activation_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverCompInActivationDn": "server_comp_in_activation_dn", 
        "serversPowerState": "servers_power_state", 
        "status": "status", 
        "upgradePriorityInfo": "upgrade_priority_info", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.activity_trigger_time = None
        self.chassis_comp_in_activation_dn = None
        self.child_action = None
        self.sacl = None
        self.server_comp_in_activation_dn = None
        self.servers_power_state = None
        self.status = None
        self.upgrade_priority_info = None

        ManagedObject.__init__(self, "FirmwareActivity", parent_mo_or_dn, **kwargs)
