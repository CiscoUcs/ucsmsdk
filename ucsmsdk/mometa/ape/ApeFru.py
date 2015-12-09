"""This module contains the general information for ApeFru ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeFruConsts():
    ENTITY_TYPE_ADD_IN_CARD = "ADD_IN_CARD"
    ENTITY_TYPE_BACK_PANEL_BOARD = "BACK_PANEL_BOARD"
    ENTITY_TYPE_BATTERY = "BATTERY"
    ENTITY_TYPE_BIOS = "BIOS"
    ENTITY_TYPE_CABLE_INTERCONNECT = "CABLE_INTERCONNECT"
    ENTITY_TYPE_CHASSIS_BACK_PANEL_BOARD = "CHASSIS_BACK_PANEL_BOARD"
    ENTITY_TYPE_CMC = "CMC"
    ENTITY_TYPE_CONNECTIVITY_SWITCH = "CONNECTIVITY_SWITCH"
    ENTITY_TYPE_COOLING_UNIT = "COOLING_UNIT"
    ENTITY_TYPE_DEVICE_BAY = "DEVICE_BAY"
    ENTITY_TYPE_DISK = "DISK"
    ENTITY_TYPE_DISK_DRIVE_BAY = "DISK_DRIVE_BAY"
    ENTITY_TYPE_DRIVE_BACKPLANE = "DRIVE_BACKPLANE"
    ENTITY_TYPE_EXTERNAL_ENVIRONMENT = "EXTERNAL_ENVIRONMENT"
    ENTITY_TYPE_FAN_COOLING = "FAN_COOLING"
    ENTITY_TYPE_FRONT_PANEL_BOARD = "FRONT_PANEL_BOARD"
    ENTITY_TYPE_GROUP = "GROUP"
    ENTITY_TYPE_IBMC = "IBMC"
    ENTITY_TYPE_IO_MODULE = "IO_MODULE"
    ENTITY_TYPE_IPMI_CHANNEL = "IPMI_CHANNEL"
    ENTITY_TYPE_MEMORY_DEVICE = "MEMORY_DEVICE"
    ENTITY_TYPE_MEMORY_MODULE = "MEMORY_MODULE"
    ENTITY_TYPE_MGMT_CONTROLLER_FIRMWARE = "MGMT_CONTROLLER_FIRMWARE"
    ENTITY_TYPE_OPERATING_SYSTEM = "OPERATING_SYSTEM"
    ENTITY_TYPE_OTHER = "OTHER"
    ENTITY_TYPE_OTHER_CHASSIS_BOARD = "OTHER_CHASSIS_BOARD"
    ENTITY_TYPE_OTHER_SYSTEM_BOARD = "OTHER_SYSTEM_BOARD"
    ENTITY_TYPE_PCI_BUS = "PCI_BUS"
    ENTITY_TYPE_PCI_EXPRESS_BUS = "PCI_EXPRESS_BUS"
    ENTITY_TYPE_PERIPHERAL = "PERIPHERAL"
    ENTITY_TYPE_PERIPHERAL_BAY = "PERIPHERAL_BAY"
    ENTITY_TYPE_POWER_MANAGEMENT_BOARD = "POWER_MANAGEMENT_BOARD"
    ENTITY_TYPE_POWER_MODULE = "POWER_MODULE"
    ENTITY_TYPE_POWER_SUPPLY = "POWER_SUPPLY"
    ENTITY_TYPE_POWER_SYSTEM_BOARD = "POWER_SYSTEM_BOARD"
    ENTITY_TYPE_POWER_UNIT = "POWER_UNIT"
    ENTITY_TYPE_PROCESSING_BLADE = "PROCESSING_BLADE"
    ENTITY_TYPE_PROCESSOR = "PROCESSOR"
    ENTITY_TYPE_PROCESSOR_BOARD = "PROCESSOR_BOARD"
    ENTITY_TYPE_PROCESSOR_FRONT_SIDE_BUS = "PROCESSOR_FRONT_SIDE_BUS"
    ENTITY_TYPE_PROCESSOR_IO_MODULE = "PROCESSOR_IO_MODULE"
    ENTITY_TYPE_PROCESSOR_MEMORY_MODULE = "PROCESSOR_MEMORY_MODULE"
    ENTITY_TYPE_PROCESSOR_MODULE = "PROCESSOR_MODULE"
    ENTITY_TYPE_REMOTE_MGMT_COMM_DEVICE = "REMOTE_MGMT_COMM_DEVICE"
    ENTITY_TYPE_SATA_SAS_BUS = "SATA_SAS_BUS"
    ENTITY_TYPE_SCSI_BUS = "SCSI_BUS"
    ENTITY_TYPE_SUB_CHASSIS = "SUB_CHASSIS"
    ENTITY_TYPE_SYSTEM_BOARD = "SYSTEM_BOARD"
    ENTITY_TYPE_SYSTEM_BUS = "SYSTEM_BUS"
    ENTITY_TYPE_SYSTEM_CHASSIS = "SYSTEM_CHASSIS"
    ENTITY_TYPE_SYSTEM_INTERNAL_EXPANSION_BOARD = "SYSTEM_INTERNAL_EXPANSION_BOARD"
    ENTITY_TYPE_SYSTEM_MANAGEMENT_MODULE = "SYSTEM_MANAGEMENT_MODULE"
    ENTITY_TYPE_SYSTEM_MANAGEMENT_SOFTWARE = "SYSTEM_MANAGEMENT_SOFTWARE"
    ENTITY_TYPE_UNKNOWN = "UNKNOWN"
    ENTITY_TYPE_UNSPECIFIED = "UNSPECIFIED"


class ApeFru(ManagedObject):
    """This is ApeFru class."""

    consts = ApeFruConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ApeFru", "apeFru", "fru-[id]", VersionMeta.Version101e, "InputOutput", 0x7fffffffL, [], ["read-only"], [u'apeMcTable'], [], [None])

    prop_meta = {
        "board_fru": MoPropertyMeta("board_fru", "boardFru", "string", None, MoPropertyMeta.READ_WRITE, 0x2L, 0, 510, None, [], []), 
        "board_manufacturer": MoPropertyMeta("board_manufacturer", "boardManufacturer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, 0, 510, None, [], []), 
        "board_mfg_time": MoPropertyMeta("board_mfg_time", "boardMfgTime", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "board_part_no": MoPropertyMeta("board_part_no", "boardPartNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, 0, 510, None, [], []), 
        "board_product_name": MoPropertyMeta("board_product_name", "boardProductName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], []), 
        "board_serial_no": MoPropertyMeta("board_serial_no", "boardSerialNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], []), 
        "board_vid": MoPropertyMeta("board_vid", "boardVid", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x80L, 0, 510, None, [], []), 
        "chassis_part_no": MoPropertyMeta("chassis_part_no", "chassisPartNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, 0, 510, None, [], []), 
        "chassis_serial_no": MoPropertyMeta("chassis_serial_no", "chassisSerialNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x400L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "control_plane_mac1": MoPropertyMeta("control_plane_mac1", "controlPlaneMac1", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "control_plane_mac2": MoPropertyMeta("control_plane_mac2", "controlPlaneMac2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "data_plane_mac1": MoPropertyMeta("data_plane_mac1", "dataPlaneMac1", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "data_plane_mac2": MoPropertyMeta("data_plane_mac2", "dataPlaneMac2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "data_plane_wwn1": MoPropertyMeta("data_plane_wwn1", "dataPlaneWwn1", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
        "data_plane_wwn2": MoPropertyMeta("data_plane_wwn2", "dataPlaneWwn2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000L, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20000L, 0, 256, None, [], []), 
        "entity_type": MoPropertyMeta("entity_type", "entityType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, None, ["ADD_IN_CARD", "BACK_PANEL_BOARD", "BATTERY", "BIOS", "CABLE_INTERCONNECT", "CHASSIS_BACK_PANEL_BOARD", "CMC", "CONNECTIVITY_SWITCH", "COOLING_UNIT", "DEVICE_BAY", "DISK", "DISK_DRIVE_BAY", "DRIVE_BACKPLANE", "EXTERNAL_ENVIRONMENT", "FAN_COOLING", "FRONT_PANEL_BOARD", "GROUP", "IBMC", "IO_MODULE", "IPMI_CHANNEL", "MEMORY_DEVICE", "MEMORY_MODULE", "MGMT_CONTROLLER_FIRMWARE", "OPERATING_SYSTEM", "OTHER", "OTHER_CHASSIS_BOARD", "OTHER_SYSTEM_BOARD", "PCI_BUS", "PCI_EXPRESS_BUS", "PERIPHERAL", "PERIPHERAL_BAY", "POWER_MANAGEMENT_BOARD", "POWER_MODULE", "POWER_SUPPLY", "POWER_SYSTEM_BOARD", "POWER_UNIT", "PROCESSING_BLADE", "PROCESSOR", "PROCESSOR_BOARD", "PROCESSOR_FRONT_SIDE_BUS", "PROCESSOR_IO_MODULE", "PROCESSOR_MEMORY_MODULE", "PROCESSOR_MODULE", "REMOTE_MGMT_COMM_DEVICE", "SATA_SAS_BUS", "SCSI_BUS", "SUB_CHASSIS", "SYSTEM_BOARD", "SYSTEM_BUS", "SYSTEM_CHASSIS", "SYSTEM_INTERNAL_EXPANSION_BOARD", "SYSTEM_MANAGEMENT_MODULE", "SYSTEM_MANAGEMENT_SOFTWARE", "UNKNOWN", "UNSPECIFIED"], ["0-4294967295"]), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80000L, None, None, None, [], []), 
        "instance": MoPropertyMeta("instance", "instance", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100000L, None, None, None, [], []), 
        "product_asset_tag": MoPropertyMeta("product_asset_tag", "productAssetTag", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200000L, 0, 510, None, [], []), 
        "product_fru": MoPropertyMeta("product_fru", "productFru", "string", None, MoPropertyMeta.READ_WRITE, 0x400000L, 0, 510, None, [], []), 
        "product_manufacturer": MoPropertyMeta("product_manufacturer", "productManufacturer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800000L, 0, 510, None, [], []), 
        "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000000L, 0, 510, None, [], []), 
        "product_part_no": MoPropertyMeta("product_part_no", "productPartNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000000L, 0, 510, None, [], []), 
        "product_serial_no": MoPropertyMeta("product_serial_no", "productSerialNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000000L, 0, 510, None, [], []), 
        "product_version_no": MoPropertyMeta("product_version_no", "productVersionNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000000L, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10000000L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000000L, None, None, None, [], []), 
    }

    prop_map = {
        "boardFru": "board_fru", 
        "boardManufacturer": "board_manufacturer", 
        "boardMfgTime": "board_mfg_time", 
        "boardPartNo": "board_part_no", 
        "boardProductName": "board_product_name", 
        "boardSerialNo": "board_serial_no", 
        "boardVid": "board_vid", 
        "chassisPartNo": "chassis_part_no", 
        "chassisSerialNo": "chassis_serial_no", 
        "childAction": "child_action", 
        "controlPlaneMac1": "control_plane_mac1", 
        "controlPlaneMac2": "control_plane_mac2", 
        "dataPlaneMac1": "data_plane_mac1", 
        "dataPlaneMac2": "data_plane_mac2", 
        "dataPlaneWwn1": "data_plane_wwn1", 
        "dataPlaneWwn2": "data_plane_wwn2", 
        "dn": "dn", 
        "entityType": "entity_type", 
        "id": "id", 
        "instance": "instance", 
        "productAssetTag": "product_asset_tag", 
        "productFru": "product_fru", 
        "productManufacturer": "product_manufacturer", 
        "productName": "product_name", 
        "productPartNo": "product_part_no", 
        "productSerialNo": "product_serial_no", 
        "productVersionNo": "product_version_no", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.board_fru = None
        self.board_manufacturer = None
        self.board_mfg_time = None
        self.board_part_no = None
        self.board_product_name = None
        self.board_serial_no = None
        self.board_vid = None
        self.chassis_part_no = None
        self.chassis_serial_no = None
        self.child_action = None
        self.control_plane_mac1 = None
        self.control_plane_mac2 = None
        self.data_plane_mac1 = None
        self.data_plane_mac2 = None
        self.data_plane_wwn1 = None
        self.data_plane_wwn2 = None
        self.entity_type = None
        self.instance = None
        self.product_asset_tag = None
        self.product_fru = None
        self.product_manufacturer = None
        self.product_name = None
        self.product_part_no = None
        self.product_serial_no = None
        self.product_version_no = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "ApeFru", parent_mo_or_dn, **kwargs)

