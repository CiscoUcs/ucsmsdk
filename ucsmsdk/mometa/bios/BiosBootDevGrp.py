"""This module contains the general information for BiosBootDevGrp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosBootDevGrpConsts:
    ERR_VAL_FAILURE = "FAILURE"
    ERR_VAL_SUCCESS = "SUCCESS"
    ORDER_1 = "1"
    ORDER_2 = "2"
    ORDER_3 = "3"
    ORDER_4 = "4"
    ORDER_5 = "5"
    ORDER_6 = "6"
    ORDER_7 = "7"
    TYPE_BEV_ORDER = "bev-order"
    TYPE_CD_ORDER = "cd-order"
    TYPE_CIMC_VMEDIA_CDD_DEVICE_ORDER = "cimc-vmedia-cdd-device-order"
    TYPE_CIMC_VMEDIA_FDD_DEVICE_ORDER = "cimc-vmedia-fdd-device-order"
    TYPE_CIMC_VMEDIA_HDD_DEVICE_ORDER = "cimc-vmedia-hdd-device-order"
    TYPE_EXTERNAL_USB_DEVICE_ORDER = "external-usb-device-order"
    TYPE_FDD_ORDER = "fdd-order"
    TYPE_HDD_ORDER = "hdd-order"
    TYPE_INTERNAL_EFI_SHELL = "internal-efi-shell"
    TYPE_INTERNAL_USB_DEVICE_ORDER = "internal-usb-device-order"
    TYPE_ISCSI_ANY_DEVICE_ORDER = "iscsi-any-device-order"
    TYPE_ISCSI_DEVICE_ORDER = "iscsi-device-order"
    TYPE_KVM_VMEDIA_CDD_DEVICE_ORDER = "kvm-vmedia-cdd-device-order"
    TYPE_KVM_VMEDIA_FDD_DEVICE_ORDER = "kvm-vmedia-fdd-device-order"
    TYPE_KVM_VMEDIA_HDD_DEVICE_ORDER = "kvm-vmedia-hdd-device-order"
    TYPE_LAN_ANY_DEVICE_ORDER = "lan-any-device-order"
    TYPE_LOCAL_STORAGE_ANY_DEVICE_ORDER = "local-storage-any-device-order"
    TYPE_NETWORK_DEVICE_ORDER = "network-device-order"
    TYPE_NVME_DEVICE_ORDER = "nvme-device-order"
    TYPE_NVME_DISK_SSD_DEVICE_ORDER = "nvme-disk-ssd-device-order"
    TYPE_NVME_PCI_SSD_DEVICE_ORDER = "nvme-pci-ssd-device-order"
    TYPE_SAN_ANY_DEVICE_ORDER = "san-any-device-order"
    TYPE_SAN_DEVICE_ORDER = "san-device-order"
    TYPE_SDCARD_DEVICE_ORDER = "sdcard-device-order"
    TYPE_SYSTEM_BOOT_ORDER = "system-boot-order"
    TYPE_UEFI_SHELL_DEVICE_ORDER = "uefi-shell-device-order"
    TYPE_UEFI_TARGET_DEVICE_ORDER = "uefi-target-device-order"
    TYPE_UNKNOWN_DEVICE_ORDER = "unknown-device-order"


class BiosBootDevGrp(ManagedObject):
    """This is BiosBootDevGrp class."""

    consts = BiosBootDevGrpConsts()
    naming_props = set(['order'])

    mo_meta = MoMeta("BiosBootDevGrp", "biosBootDevGrp", "bdg-[order]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["read-only"], ['biosBOT'], ['biosBootDev'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "device_name": MoPropertyMeta("device_name", "deviceName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "err_val": MoPropertyMeta("err_val", "errVal", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FAILURE", "SUCCESS"], []),
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, ["1", "2", "3", "4", "5", "6", "7"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bev-order", "cd-order", "cimc-vmedia-cdd-device-order", "cimc-vmedia-fdd-device-order", "cimc-vmedia-hdd-device-order", "external-usb-device-order", "fdd-order", "hdd-order", "internal-efi-shell", "internal-usb-device-order", "iscsi-any-device-order", "iscsi-device-order", "kvm-vmedia-cdd-device-order", "kvm-vmedia-fdd-device-order", "kvm-vmedia-hdd-device-order", "lan-any-device-order", "local-storage-any-device-order", "network-device-order", "nvme-device-order", "nvme-disk-ssd-device-order", "nvme-pci-ssd-device-order", "san-any-device-order", "san-device-order", "sdcard-device-order", "system-boot-order", "uefi-shell-device-order", "uefi-target-device-order", "unknown-device-order"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "deviceName": "device_name", 
        "dn": "dn", 
        "errVal": "err_val", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.descr = None
        self.device_name = None
        self.err_val = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "BiosBootDevGrp", parent_mo_or_dn, **kwargs)
