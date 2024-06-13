"""This module contains the general information for ComputeFwSyncAck ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeFwSyncAckConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
    ADMIN_STATE_TRIGGERED = "triggered"
    ADMIN_STATE_UNTRIGGERED = "untriggered"
    ADMIN_STATE_USER_ACK = "user-ack"
    ADMIN_STATE_USER_DISCARD = "user-discard"
    AUTO_DELETE_FALSE = "false"
    AUTO_DELETE_NO = "no"
    AUTO_DELETE_TRUE = "true"
    AUTO_DELETE_YES = "yes"
    IGNORE_CAP_FALSE = "false"
    IGNORE_CAP_NO = "no"
    IGNORE_CAP_TRUE = "true"
    IGNORE_CAP_YES = "yes"
    INT_ID_NONE = "none"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_APPLIED = "applied"
    OPER_STATE_APPLY_PENDING = "apply-pending"
    OPER_STATE_EVALUATED = "evaluated"
    OPER_STATE_EVALUATION_PENDING = "evaluation-pending"
    OPER_STATE_EXPIRED = "expired"
    OPER_STATE_NONE = "none"
    OPER_STATE_PENDING = "pending"
    OPER_STATE_UNTRIGGERED = "untriggered"
    OPER_STATE_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
    OPER_STATE_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
    OPER_STATE_WAITING_FOR_USER = "waiting-for-user"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PREV_OPER_STATE_ACTIVE = "active"
    PREV_OPER_STATE_APPLIED = "applied"
    PREV_OPER_STATE_APPLY_PENDING = "apply-pending"
    PREV_OPER_STATE_EVALUATED = "evaluated"
    PREV_OPER_STATE_EVALUATION_PENDING = "evaluation-pending"
    PREV_OPER_STATE_EXPIRED = "expired"
    PREV_OPER_STATE_NONE = "none"
    PREV_OPER_STATE_PENDING = "pending"
    PREV_OPER_STATE_UNTRIGGERED = "untriggered"
    PREV_OPER_STATE_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
    PREV_OPER_STATE_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
    PREV_OPER_STATE_WAITING_FOR_USER = "waiting-for-user"
    TRIGGER_CONFIG_STATE_NONE = "none"
    TRIGGER_CONFIG_STATE_WAITING_FOR_NEXT_BOOT = "waiting-for-next-boot"


class ComputeFwSyncAck(ManagedObject):
    """This is ComputeFwSyncAck class."""

    consts = ComputeFwSyncAckConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeFwSyncAck", "computeFwSyncAck", "fwsyncack", VersionMeta.Version221b, "InputOutput", 0x3ff, [], ["admin"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['faultInst', 'trigLocalSched'], ["Get", "Set"])

    prop_meta = {
        "acked": MoPropertyMeta("acked", "acked", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "acked_by": MoPropertyMeta("acked_by", "ackedBy", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 32, None, [], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack", "user-discard"], []),
        "auto_delete": MoPropertyMeta("auto_delete", "autoDelete", "string", VersionMeta.Version221b, MoPropertyMeta.CREATE_ONLY, 0x4, None, None, None, ["false", "no", "true", "yes"], []),
        "change_by": MoPropertyMeta("change_by", "changeBy", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 32, None, [], []),
        "change_details": MoPropertyMeta("change_details", "changeDetails", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|graphics-card-mode|pci-switch-fw|storage-snic-config|oob-local-storage-config|bootmode-config|bmc-update-bios-fw|host-eth-if-qos-host-control|checkpoint|pin|adaptor-host-fw|blade-identity|boot-local-storage|ip|host-fcoe-if|host-virt-fc-if-pers-bind|host-eth-if-qos|binding|local-disk-data-loss|fan-speed-config|remote-storage-config|secureboot-config|host-if-pcie|local-disk-fw|implicit-reboot|sol|adaptor-nw-fw|agent-policy|boot-virt-pxe|boot-order|vif|host-nonvirt-fc-if-pers-bind|host-eth-if-nw-ctrl|host-virt-eth-if|local-storage-security|sas-exp-reg-fw|vmedia-config|flexflash-config|implicit-host-eth-if-profile-redeploy|implicit-host-fc-if-profile-redeploy|ep-auth|mgmt-controller-fw|bios-fw|boot-nonvirt-pxe|boot-virt-vnic|vlan|host-fc-if-profile|host-virt-fc-if|host-nonvirt-eth-if|nvme-mswitch-fw|asset-tag-config|powercap-config|storage-path|board-controller-fw|bios-profile|local-disk-policy|storage-controller-fw|boot-nonvirt-vnic|vsan|host-fc-if-qos|host-nonvirt-fc-if|host-eth-if-profile|graphics-card-fw|storage-sas-expander-fw),){0,63}(defaultValue|graphics-card-mode|pci-switch-fw|storage-snic-config|oob-local-storage-config|bootmode-config|bmc-update-bios-fw|host-eth-if-qos-host-control|checkpoint|pin|adaptor-host-fw|blade-identity|boot-local-storage|ip|host-fcoe-if|host-virt-fc-if-pers-bind|host-eth-if-qos|binding|local-disk-data-loss|fan-speed-config|remote-storage-config|secureboot-config|host-if-pcie|local-disk-fw|implicit-reboot|sol|adaptor-nw-fw|agent-policy|boot-virt-pxe|boot-order|vif|host-nonvirt-fc-if-pers-bind|host-eth-if-nw-ctrl|host-virt-eth-if|local-storage-security|sas-exp-reg-fw|vmedia-config|flexflash-config|implicit-host-eth-if-profile-redeploy|implicit-host-fc-if-profile-redeploy|ep-auth|mgmt-controller-fw|bios-fw|boot-nonvirt-pxe|boot-virt-vnic|vlan|host-fc-if-profile|host-virt-fc-if|host-nonvirt-eth-if|nvme-mswitch-fw|asset-tag-config|powercap-config|storage-path|board-controller-fw|bios-profile|local-disk-policy|storage-controller-fw|boot-nonvirt-vnic|vsan|host-fc-if-qos|host-nonvirt-fc-if|host-eth-if-profile|graphics-card-fw|storage-sas-expander-fw){0,1}""", [], []),
        "changes": MoPropertyMeta("changes", "changes", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|boot-order|server-assignment|operational-policies|local-storage|server-identity|storage|networking|vnic-vhba-placement),){0,8}(defaultValue|boot-order|server-assignment|operational-policies|local-storage|server-identity|storage|networking|vnic-vhba-placement){0,1}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "disr": MoPropertyMeta("disr", "disr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|ac-power-cycle|local-storage-config-deployment-userack|local-storage-config-deployment-immediate|up-time),){0,4}(defaultValue|ac-power-cycle|local-storage-config-deployment-userack|local-storage-config-deployment-immediate|up-time){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "extd_change_details": MoPropertyMeta("extd_change_details", "extdChangeDetails", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|intel-amc-fw|ubm-fw|persistent-memory-policy|cpld-fw|persistent-memory-dimm-fw|retimer-fw|host-pack-have-backup-set|hybrid-local-slot-config|adaptor-swm-reset),){0,9}(defaultValue|intel-amc-fw|ubm-fw|persistent-memory-policy|cpld-fw|persistent-memory-dimm-fw|retimer-fw|host-pack-have-backup-set|hybrid-local-slot-config|adaptor-swm-reset){0,1}""", [], []),
        "ignore_cap": MoPropertyMeta("ignore_cap", "ignoreCap", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "modified": MoPropertyMeta("modified", "modified", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_scheduler": MoPropertyMeta("oper_scheduler", "operScheduler", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "prev_oper_state": MoPropertyMeta("prev_oper_state", "prevOperState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "scheduler": MoPropertyMeta("scheduler", "scheduler", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "trigger_config_state": MoPropertyMeta("trigger_config_state", "triggerConfigState", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "waiting-for-next-boot"], []),
    }

    prop_map = {
        "acked": "acked", 
        "ackedBy": "acked_by", 
        "adminState": "admin_state", 
        "autoDelete": "auto_delete", 
        "changeBy": "change_by", 
        "changeDetails": "change_details", 
        "changes": "changes", 
        "childAction": "child_action", 
        "descr": "descr", 
        "disr": "disr", 
        "dn": "dn", 
        "extdChangeDetails": "extd_change_details", 
        "ignoreCap": "ignore_cap", 
        "intId": "int_id", 
        "modified": "modified", 
        "name": "name", 
        "operScheduler": "oper_scheduler", 
        "operState": "oper_state", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "prevOperState": "prev_oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "scheduler": "scheduler", 
        "status": "status", 
        "triggerConfigState": "trigger_config_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.acked = None
        self.acked_by = None
        self.admin_state = None
        self.auto_delete = None
        self.change_by = None
        self.change_details = None
        self.changes = None
        self.child_action = None
        self.descr = None
        self.disr = None
        self.extd_change_details = None
        self.ignore_cap = None
        self.int_id = None
        self.modified = None
        self.name = None
        self.oper_scheduler = None
        self.oper_state = None
        self.policy_level = None
        self.policy_owner = None
        self.prev_oper_state = None
        self.sacl = None
        self.scheduler = None
        self.status = None
        self.trigger_config_state = None

        ManagedObject.__init__(self, "ComputeFwSyncAck", parent_mo_or_dn, **kwargs)
