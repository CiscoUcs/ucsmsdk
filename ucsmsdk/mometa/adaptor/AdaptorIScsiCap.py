"""This module contains the general information for AdaptorIScsiCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorIScsiCapConsts:
    BOOT_ORDER_TYPE_BEV_ORDER = "bev-order"
    BOOT_ORDER_TYPE_CD_ORDER = "cd-order"
    BOOT_ORDER_TYPE_CIMC_VMEDIA_CDD_DEVICE_ORDER = "cimc-vmedia-cdd-device-order"
    BOOT_ORDER_TYPE_CIMC_VMEDIA_FDD_DEVICE_ORDER = "cimc-vmedia-fdd-device-order"
    BOOT_ORDER_TYPE_CIMC_VMEDIA_HDD_DEVICE_ORDER = "cimc-vmedia-hdd-device-order"
    BOOT_ORDER_TYPE_EXTERNAL_USB_DEVICE_ORDER = "external-usb-device-order"
    BOOT_ORDER_TYPE_FDD_ORDER = "fdd-order"
    BOOT_ORDER_TYPE_HDD_ORDER = "hdd-order"
    BOOT_ORDER_TYPE_INTERNAL_EFI_SHELL = "internal-efi-shell"
    BOOT_ORDER_TYPE_INTERNAL_USB_DEVICE_ORDER = "internal-usb-device-order"
    BOOT_ORDER_TYPE_ISCSI_ANY_DEVICE_ORDER = "iscsi-any-device-order"
    BOOT_ORDER_TYPE_ISCSI_DEVICE_ORDER = "iscsi-device-order"
    BOOT_ORDER_TYPE_KVM_VMEDIA_CDD_DEVICE_ORDER = "kvm-vmedia-cdd-device-order"
    BOOT_ORDER_TYPE_KVM_VMEDIA_FDD_DEVICE_ORDER = "kvm-vmedia-fdd-device-order"
    BOOT_ORDER_TYPE_KVM_VMEDIA_HDD_DEVICE_ORDER = "kvm-vmedia-hdd-device-order"
    BOOT_ORDER_TYPE_LAN_ANY_DEVICE_ORDER = "lan-any-device-order"
    BOOT_ORDER_TYPE_LOCAL_STORAGE_ANY_DEVICE_ORDER = "local-storage-any-device-order"
    BOOT_ORDER_TYPE_NETWORK_DEVICE_ORDER = "network-device-order"
    BOOT_ORDER_TYPE_NVME_DEVICE_ORDER = "nvme-device-order"
    BOOT_ORDER_TYPE_NVME_DISK_SSD_DEVICE_ORDER = "nvme-disk-ssd-device-order"
    BOOT_ORDER_TYPE_NVME_PCI_SSD_DEVICE_ORDER = "nvme-pci-ssd-device-order"
    BOOT_ORDER_TYPE_SAN_ANY_DEVICE_ORDER = "san-any-device-order"
    BOOT_ORDER_TYPE_SAN_DEVICE_ORDER = "san-device-order"
    BOOT_ORDER_TYPE_SDCARD_DEVICE_ORDER = "sdcard-device-order"
    BOOT_ORDER_TYPE_SYSTEM_BOOT_ORDER = "system-boot-order"
    BOOT_ORDER_TYPE_UEFI_SHELL_DEVICE_ORDER = "uefi-shell-device-order"
    BOOT_ORDER_TYPE_UEFI_TARGET_DEVICE_ORDER = "uefi-target-device-order"
    BOOT_ORDER_TYPE_UNKNOWN_DEVICE_ORDER = "unknown-device-order"
    OFFLOAD_SUPPORT_FALSE = "false"
    OFFLOAD_SUPPORT_NO = "no"
    OFFLOAD_SUPPORT_TRUE = "true"
    OFFLOAD_SUPPORT_YES = "yes"
    OFFLOAD_TYPE_NONE = "none"
    OFFLOAD_TYPE_PHYSICAL = "physical"
    OFFLOAD_TYPE_VIRTUAL = "virtual"
    VLAN_FOR_BOOT_FALSE = "false"
    VLAN_FOR_BOOT_NO = "no"
    VLAN_FOR_BOOT_TRUE = "true"
    VLAN_FOR_BOOT_YES = "yes"


class AdaptorIScsiCap(ManagedObject):
    """This is AdaptorIScsiCap class."""

    consts = AdaptorIScsiCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorIScsiCap", "adaptorIScsiCap", "iscsi", VersionMeta.Version201m, "InputOutput", 0x7ff, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "boot_order_type": MoPropertyMeta("boot_order_type", "bootOrderType", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["bev-order", "cd-order", "cimc-vmedia-cdd-device-order", "cimc-vmedia-fdd-device-order", "cimc-vmedia-hdd-device-order", "external-usb-device-order", "fdd-order", "hdd-order", "internal-efi-shell", "internal-usb-device-order", "iscsi-any-device-order", "iscsi-device-order", "kvm-vmedia-cdd-device-order", "kvm-vmedia-fdd-device-order", "kvm-vmedia-hdd-device-order", "lan-any-device-order", "local-storage-any-device-order", "network-device-order", "nvme-device-order", "nvme-disk-ssd-device-order", "nvme-pci-ssd-device-order", "san-any-device-order", "san-device-order", "sdcard-device-order", "system-boot-order", "uefi-shell-device-order", "uefi-target-device-order", "unknown-device-order"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "mac_offset1": MoPropertyMeta("mac_offset1", "macOffset1", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "mac_offset2": MoPropertyMeta("mac_offset2", "macOffset2", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "offload_support": MoPropertyMeta("offload_support", "offloadSupport", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "offload_type": MoPropertyMeta("offload_type", "offloadType", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["none", "physical", "virtual"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vlan_for_boot": MoPropertyMeta("vlan_for_boot", "vlanForBoot", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "bootOrderType": "boot_order_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "macOffset1": "mac_offset1", 
        "macOffset2": "mac_offset2", 
        "offloadSupport": "offload_support", 
        "offloadType": "offload_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vlanForBoot": "vlan_for_boot", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.boot_order_type = None
        self.child_action = None
        self.mac_offset1 = None
        self.mac_offset2 = None
        self.offload_support = None
        self.offload_type = None
        self.sacl = None
        self.status = None
        self.vlan_for_boot = None

        ManagedObject.__init__(self, "AdaptorIScsiCap", parent_mo_or_dn, **kwargs)
