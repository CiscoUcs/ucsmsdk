"""This module contains the general information for BiosVfUSBPortConfiguration ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfUSBPortConfigurationConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PORT6064_EMULATION_DISABLED = "disabled"
    VP_PORT6064_EMULATION_ENABLED = "enabled"
    VP_PORT6064_EMULATION_PLATFORM_DEFAULT = "platform-default"
    VP_PORT6064_EMULATION_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_USBPORT_FRONT_DISABLED = "disabled"
    VP_USBPORT_FRONT_ENABLED = "enabled"
    VP_USBPORT_FRONT_PLATFORM_DEFAULT = "platform-default"
    VP_USBPORT_FRONT_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_USBPORT_INTERNAL_DISABLED = "disabled"
    VP_USBPORT_INTERNAL_ENABLED = "enabled"
    VP_USBPORT_INTERNAL_PLATFORM_DEFAULT = "platform-default"
    VP_USBPORT_INTERNAL_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_USBPORT_KVM_DISABLED = "disabled"
    VP_USBPORT_KVM_ENABLED = "enabled"
    VP_USBPORT_KVM_PLATFORM_DEFAULT = "platform-default"
    VP_USBPORT_KVM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_USBPORT_REAR_DISABLED = "disabled"
    VP_USBPORT_REAR_ENABLED = "enabled"
    VP_USBPORT_REAR_PLATFORM_DEFAULT = "platform-default"
    VP_USBPORT_REAR_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_USBPORT_SDCARD_DISABLED = "disabled"
    VP_USBPORT_SDCARD_ENABLED = "enabled"
    VP_USBPORT_SDCARD_PLATFORM_DEFAULT = "platform-default"
    VP_USBPORT_SDCARD_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_USBPORT_VMEDIA_DISABLED = "disabled"
    VP_USBPORT_VMEDIA_ENABLED = "enabled"
    VP_USBPORT_VMEDIA_PLATFORM_DEFAULT = "platform-default"
    VP_USBPORT_VMEDIA_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfUSBPortConfiguration(ManagedObject):
    """This is BiosVfUSBPortConfiguration class."""

    consts = BiosVfUSBPortConfigurationConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfUSBPortConfiguration", "biosVfUSBPortConfiguration", "USB-port-configuration", VersionMeta.Version222c, "InputOutput", 0xfff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_port6064_emulation": MoPropertyMeta("vp_port6064_emulation", "vpPort6064Emulation", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_usb_port_front": MoPropertyMeta("vp_usb_port_front", "vpUSBPortFront", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_usb_port_internal": MoPropertyMeta("vp_usb_port_internal", "vpUSBPortInternal", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_usb_port_kvm": MoPropertyMeta("vp_usb_port_kvm", "vpUSBPortKVM", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_usb_port_rear": MoPropertyMeta("vp_usb_port_rear", "vpUSBPortRear", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_usb_port_sd_card": MoPropertyMeta("vp_usb_port_sd_card", "vpUSBPortSDCard", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_usb_port_v_media": MoPropertyMeta("vp_usb_port_v_media", "vpUSBPortVMedia", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpPort6064Emulation": "vp_port6064_emulation", 
        "vpUSBPortFront": "vp_usb_port_front", 
        "vpUSBPortInternal": "vp_usb_port_internal", 
        "vpUSBPortKVM": "vp_usb_port_kvm", 
        "vpUSBPortRear": "vp_usb_port_rear", 
        "vpUSBPortSDCard": "vp_usb_port_sd_card", 
        "vpUSBPortVMedia": "vp_usb_port_v_media", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_port6064_emulation = None
        self.vp_usb_port_front = None
        self.vp_usb_port_internal = None
        self.vp_usb_port_kvm = None
        self.vp_usb_port_rear = None
        self.vp_usb_port_sd_card = None
        self.vp_usb_port_v_media = None

        ManagedObject.__init__(self, "BiosVfUSBPortConfiguration", parent_mo_or_dn, **kwargs)
