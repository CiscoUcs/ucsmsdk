"""This module contains the general information for ApeSANBoot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeSANBootConsts:
    IS_HOST_AGENT_PRESENT_FALSE = "false"
    IS_HOST_AGENT_PRESENT_NO = "no"
    IS_HOST_AGENT_PRESENT_TRUE = "true"
    IS_HOST_AGENT_PRESENT_YES = "yes"
    TARGET_LUN_UNSPECIFIED = "unspecified"
    TYPE_LINUX = "Linux"
    TYPE_PNU_OS = "PnuOS"
    TYPE_SOLARIS = "Solaris"
    TYPE_VMWARE_ESX = "VMWareESX"
    TYPE_WINDOWS = "Windows"
    TYPE_UNSPECIFIED = "unspecified"


class ApeSANBoot(ManagedObject):
    """This is ApeSANBoot class."""

    consts = ApeSANBootConsts()
    naming_props = set(['targetWWN'])

    mo_meta = MoMeta("ApeSANBoot", "apeSANBoot", "sanboot-[target_wwn]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin"], ['apeManager'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "is_host_agent_present": MoPropertyMeta("is_host_agent_present", "isHostAgentPresent", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "kernel_name": MoPropertyMeta("kernel_name", "kernelName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "kernel_release": MoPropertyMeta("kernel_release", "kernelRelease", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "kernel_version": MoPropertyMeta("kernel_version", "kernelVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "target_lun": MoPropertyMeta("target_lun", "targetLun", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["unspecified"], ["0-4294967295"]),
        "target_wwn": MoPropertyMeta("target_wwn", "targetWWN", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Linux", "PnuOS", "Solaris", "VMWareESX", "Windows", "unspecified"], []),
    }

    prop_map = {
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
        "status": "status", 
        "targetLun": "target_lun", 
        "targetWWN": "target_wwn", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, target_wwn, **kwargs):
        self._dirty_mask = 0
        self.target_wwn = target_wwn
        self.child_action = None
        self.hostname = None
        self.is_host_agent_present = None
        self.kernel_name = None
        self.kernel_release = None
        self.kernel_version = None
        self.name = None
        self.sacl = None
        self.status = None
        self.target_lun = None
        self.type = None

        ManagedObject.__init__(self, "ApeSANBoot", parent_mo_or_dn, **kwargs)
