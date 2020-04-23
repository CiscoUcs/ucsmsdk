"""This module contains the general information for ApeVirtualMediaBoot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeVirtualMediaBootConsts:
    CHASSIS_ID_N_A = "N/A"
    IS_HOST_AGENT_PRESENT_FALSE = "false"
    IS_HOST_AGENT_PRESENT_NO = "no"
    IS_HOST_AGENT_PRESENT_TRUE = "true"
    IS_HOST_AGENT_PRESENT_YES = "yes"
    TYPE_LINUX = "Linux"
    TYPE_PNU_OS = "PnuOS"
    TYPE_SOLARIS = "Solaris"
    TYPE_VMWARE_ESX = "VMWareESX"
    TYPE_WINDOWS = "Windows"
    TYPE_UNSPECIFIED = "unspecified"


class ApeVirtualMediaBoot(ManagedObject):
    """This is ApeVirtualMediaBoot class."""

    consts = ApeVirtualMediaBootConsts()
    naming_props = set(['chassisId', 'slotId'])

    mo_meta = MoMeta("ApeVirtualMediaBoot", "apeVirtualMediaBoot", "virtualmediaboot-[chassis_id]-[slot_id]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin"], ['apeManager'], [], [None])

    prop_meta = {
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x2, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "is_host_agent_present": MoPropertyMeta("is_host_agent_present", "isHostAgentPresent", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "kernel_name": MoPropertyMeta("kernel_name", "kernelName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "kernel_release": MoPropertyMeta("kernel_release", "kernelRelease", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "kernel_version": MoPropertyMeta("kernel_version", "kernelVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Linux", "PnuOS", "Solaris", "VMWareESX", "Windows", "unspecified"], []),
    }

    prop_map = {
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "hostname": "hostname", 
        "isHostAgentPresent": "is_host_agent_present", 
        "kernelName": "kernel_name", 
        "kernelRelease": "kernel_release", 
        "kernelVersion": "kernel_version", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, chassis_id, slot_id, **kwargs):
        self._dirty_mask = 0
        self.chassis_id = chassis_id
        self.slot_id = slot_id
        self.child_action = None
        self.hostname = None
        self.is_host_agent_present = None
        self.kernel_name = None
        self.kernel_release = None
        self.kernel_version = None
        self.name = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "ApeVirtualMediaBoot", parent_mo_or_dn, **kwargs)
