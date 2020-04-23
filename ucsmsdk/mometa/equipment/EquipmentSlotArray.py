"""This module contains the general information for EquipmentSlotArray ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentSlotArrayConsts:
    DEVICE_SLOT_OFFSET_UNDEFINED = "undefined"
    HEIGHT_NOT_APPLICABLE = "not-applicable"
    HORIZONTAL_START_OFFSET_NOT_APPLICABLE = "not-applicable"
    INLINE_GROUP_SEPARATION_NOT_APPLICABLE = "not-applicable"
    INLINE_OFFSET_NOT_APPLICABLE = "not-applicable"
    INT_ID_NONE = "none"
    LOCATION_BACK = "back"
    LOCATION_BOTTOM = "bottom"
    LOCATION_FRONT = "front"
    LOCATION_LEFT = "left"
    LOCATION_RIGHT = "right"
    LOCATION_TOP = "top"
    LOCATION_UNKNOWN = "unknown"
    ORIENTATION_HORIZONTAL = "horizontal"
    ORIENTATION_UNKNOWN = "unknown"
    ORIENTATION_VERTICAL = "vertical"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SELECTOR_BLADE = "blade"
    SELECTOR_COM_PORT = "com_port"
    SELECTOR_DISK_SLOT = "disk_slot"
    SELECTOR_DRIVE_SLOT = "drive_slot"
    SELECTOR_DVI_PORT = "dvi_port"
    SELECTOR_ETHERNET_PORT = "ethernet_port"
    SELECTOR_FAN = "fan"
    SELECTOR_GEM = "gem"
    SELECTOR_IOCARD = "iocard"
    SELECTOR_KEYBOARD_PORT = "keyboard_port"
    SELECTOR_MOUSE_PORT = "mouse_port"
    SELECTOR_PAR_PORT = "par_port"
    SELECTOR_PSU = "psu"
    SELECTOR_UNKNOWN = "unknown"
    SELECTOR_USB_PORT = "usb_port"
    SELECTOR_VGA_PORT = "vga_port"
    SUB_OEM_ID_UNDEFINED = "undefined"
    TRANSVERSE_GROUP_SEPARATION_NOT_APPLICABLE = "not-applicable"
    TRANSVERSE_OFFSET_NOT_APPLICABLE = "not-applicable"
    VERTICAL_START_OFFSET_NOT_APPLICABLE = "not-applicable"
    WIDTH_NOT_APPLICABLE = "not-applicable"


class EquipmentSlotArray(ManagedObject):
    """This is EquipmentSlotArray class."""

    consts = EquipmentSlotArrayConsts()
    naming_props = set(['selector'])

    mo_meta = MoMeta("EquipmentSlotArray", "equipmentSlotArray", "[selector]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], [""], ['diagSrvCapProvider', 'equipmentBladeCapProvider', 'equipmentCatalogCapProvider', 'equipmentChassisCapProvider', 'equipmentDbgPluginCapProvider', 'equipmentIOExpanderCapProvider', 'equipmentMgmtCapProvider', 'equipmentMgmtExtCapProvider', 'equipmentRackEnclosureCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSiocCapProvider', 'equipmentStorageEncCapProvider', 'equipmentSwitchCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "device_slot_offset": MoPropertyMeta("device_slot_offset", "deviceSlotOffset", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["undefined"], ["0-65535"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "first_index": MoPropertyMeta("first_index", "firstIndex", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "height": MoPropertyMeta("height", "height", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "horizontal_start_offset": MoPropertyMeta("horizontal_start_offset", "horizontalStartOffset", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "inline_group_separation": MoPropertyMeta("inline_group_separation", "inlineGroupSeparation", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "inline_group_size": MoPropertyMeta("inline_group_size", "inlineGroupSize", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "inline_offset": MoPropertyMeta("inline_offset", "inlineOffset", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["back", "bottom", "front", "left", "right", "top", "unknown"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "number_of_onboard_disks": MoPropertyMeta("number_of_onboard_disks", "numberOfOnboardDisks", "ushort", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "number_of_slots": MoPropertyMeta("number_of_slots", "numberOfSlots", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "onboard_disk_base_port_no": MoPropertyMeta("onboard_disk_base_port_no", "onboardDiskBasePortNo", "ushort", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "onboard_disk_first_index": MoPropertyMeta("onboard_disk_first_index", "onboardDiskFirstIndex", "ushort", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "orientation": MoPropertyMeta("orientation", "orientation", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["horizontal", "unknown", "vertical"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "selector": MoPropertyMeta("selector", "selector", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, None, ["blade", "com_port", "disk_slot", "drive_slot", "dvi_port", "ethernet_port", "fan", "gem", "iocard", "keyboard_port", "mouse_port", "par_port", "psu", "unknown", "usb_port", "vga_port"], []),
        "slots_per_line": MoPropertyMeta("slots_per_line", "slotsPerLine", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "storage_bios_mode": MoPropertyMeta("storage_bios_mode", "storageBiosMode", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "sub_oem_id": MoPropertyMeta("sub_oem_id", "subOemId", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["undefined"], ["0-65535"]),
        "transverse_group_separation": MoPropertyMeta("transverse_group_separation", "transverseGroupSeparation", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "transverse_group_size": MoPropertyMeta("transverse_group_size", "transverseGroupSize", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "transverse_offset": MoPropertyMeta("transverse_offset", "transverseOffset", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "vertical_start_offset": MoPropertyMeta("vertical_start_offset", "verticalStartOffset", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "width": MoPropertyMeta("width", "width", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "deviceSlotOffset": "device_slot_offset", 
        "dn": "dn", 
        "firstIndex": "first_index", 
        "height": "height", 
        "horizontalStartOffset": "horizontal_start_offset", 
        "inlineGroupSeparation": "inline_group_separation", 
        "inlineGroupSize": "inline_group_size", 
        "inlineOffset": "inline_offset", 
        "intId": "int_id", 
        "location": "location", 
        "name": "name", 
        "numberOfOnboardDisks": "number_of_onboard_disks", 
        "numberOfSlots": "number_of_slots", 
        "onboardDiskBasePortNo": "onboard_disk_base_port_no", 
        "onboardDiskFirstIndex": "onboard_disk_first_index", 
        "orientation": "orientation", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "selector": "selector", 
        "slotsPerLine": "slots_per_line", 
        "status": "status", 
        "storageBiosMode": "storage_bios_mode", 
        "subOemId": "sub_oem_id", 
        "transverseGroupSeparation": "transverse_group_separation", 
        "transverseGroupSize": "transverse_group_size", 
        "transverseOffset": "transverse_offset", 
        "verticalStartOffset": "vertical_start_offset", 
        "width": "width", 
    }

    def __init__(self, parent_mo_or_dn, selector, **kwargs):
        self._dirty_mask = 0
        self.selector = selector
        self.child_action = None
        self.descr = None
        self.device_slot_offset = None
        self.first_index = None
        self.height = None
        self.horizontal_start_offset = None
        self.inline_group_separation = None
        self.inline_group_size = None
        self.inline_offset = None
        self.int_id = None
        self.location = None
        self.name = None
        self.number_of_onboard_disks = None
        self.number_of_slots = None
        self.onboard_disk_base_port_no = None
        self.onboard_disk_first_index = None
        self.orientation = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.slots_per_line = None
        self.status = None
        self.storage_bios_mode = None
        self.sub_oem_id = None
        self.transverse_group_separation = None
        self.transverse_group_size = None
        self.transverse_offset = None
        self.vertical_start_offset = None
        self.width = None

        ManagedObject.__init__(self, "EquipmentSlotArray", parent_mo_or_dn, **kwargs)
