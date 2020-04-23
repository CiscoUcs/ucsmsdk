"""This module contains the general information for ApeFru ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeFruConsts:
    pass


class ApeFru(ManagedObject):
    """This is ApeFru class."""

    consts = ApeFruConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ApeFru", "apeFru", "fru-[id]", VersionMeta.Version101e, "InputOutput", 0x7fffffff, [], ["read-only"], ['apeMcTable'], [], [None])

    prop_meta = {
        "board_fru": MoPropertyMeta("board_fru", "boardFru", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []),
        "board_manufacturer": MoPropertyMeta("board_manufacturer", "boardManufacturer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []),
        "board_mfg_time": MoPropertyMeta("board_mfg_time", "boardMfgTime", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "board_part_no": MoPropertyMeta("board_part_no", "boardPartNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []),
        "board_product_name": MoPropertyMeta("board_product_name", "boardProductName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
        "board_serial_no": MoPropertyMeta("board_serial_no", "boardSerialNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
        "board_vid": MoPropertyMeta("board_vid", "boardVid", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []),
        "chassis_part_no": MoPropertyMeta("chassis_part_no", "chassisPartNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []),
        "chassis_serial_no": MoPropertyMeta("chassis_serial_no", "chassisSerialNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x400, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "control_plane_mac1": MoPropertyMeta("control_plane_mac1", "controlPlaneMac1", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "control_plane_mac2": MoPropertyMeta("control_plane_mac2", "controlPlaneMac2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "data_plane_mac1": MoPropertyMeta("data_plane_mac1", "dataPlaneMac1", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "data_plane_mac2": MoPropertyMeta("data_plane_mac2", "dataPlaneMac2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "data_plane_wwn1": MoPropertyMeta("data_plane_wwn1", "dataPlaneWwn1", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        "data_plane_wwn2": MoPropertyMeta("data_plane_wwn2", "dataPlaneWwn2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20000, 0, 256, None, [], []),
        "entity_type": MoPropertyMeta("entity_type", "entityType", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80000, None, None, None, [], []),
        "instance": MoPropertyMeta("instance", "instance", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, [], []),
        "product_asset_tag": MoPropertyMeta("product_asset_tag", "productAssetTag", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200000, 0, 510, None, [], []),
        "product_fru": MoPropertyMeta("product_fru", "productFru", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x400000, 0, 510, None, [], []),
        "product_manufacturer": MoPropertyMeta("product_manufacturer", "productManufacturer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800000, 0, 510, None, [], []),
        "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000000, 0, 510, None, [], []),
        "product_part_no": MoPropertyMeta("product_part_no", "productPartNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000000, 0, 510, None, [], []),
        "product_serial_no": MoPropertyMeta("product_serial_no", "productSerialNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000000, 0, 510, None, [], []),
        "product_version_no": MoPropertyMeta("product_version_no", "productVersionNo", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10000000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000000, None, None, None, [], []),
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
