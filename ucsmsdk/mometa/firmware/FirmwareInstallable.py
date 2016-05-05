"""This module contains the general information for FirmwareInstallable ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareInstallableConsts:
    TYPE_ADAPTOR = "adaptor"
    TYPE_BLADE_BIOS = "blade-bios"
    TYPE_BLADE_CONTROLLER = "blade-controller"
    TYPE_BOARD_CONTROLLER = "board-controller"
    TYPE_CATALOG = "catalog"
    TYPE_CMC = "cmc"
    TYPE_DEBUG_PLUG_IN = "debug-plug-in"
    TYPE_DIAG = "diag"
    TYPE_FEX = "fex"
    TYPE_FLEXFLASH_CONTROLLER = "flexflash-controller"
    TYPE_GRAPHICS_CARD = "graphics-card"
    TYPE_HOST_HBA = "host-hba"
    TYPE_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    TYPE_HOST_NIC = "host-nic"
    TYPE_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    TYPE_IOCARD = "iocard"
    TYPE_LOCAL_DISK = "local-disk"
    TYPE_MGMT_EXT = "mgmt-ext"
    TYPE_PSU = "psu"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_STORAGE_CONTROLLER = "storage-controller"
    TYPE_STORAGE_NODE_CONTROLLER = "storage-node-controller"
    TYPE_SWITCH = "switch"
    TYPE_SWITCH_KERNEL = "switch-kernel"
    TYPE_SWITCH_SOFTWARE = "switch-software"
    TYPE_SYSTEM = "system"
    TYPE_UNSPECIFIED = "unspecified"


class FirmwareInstallable(ManagedObject):
    """This is FirmwareInstallable class."""

    consts = FirmwareInstallableConsts()
    naming_props = set([u'vendor', u'model', u'type', u'version'])

    mo_meta = MoMeta("FirmwareInstallable", "firmwareInstallable", "installable-[vendor]|[model]|[type]|[version]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin"], [u'firmwareBootUnit', u'firmwareImage', u'firmwareUpdatable'], [u'firmwareUcscInfo'], ["Get"])

    prop_meta = {
        "checksum": MoPropertyMeta("checksum", "checksum", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "in_progress": MoPropertyMeta("in_progress", "inProgress", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "isoname": MoPropertyMeta("isoname", "isoname", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "catalog", "cmc", "debug-plug-in", "diag", "fex", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "iocard", "local-disk", "mgmt-ext", "psu", "sas-expander", "storage-controller", "storage-node-controller", "switch", "switch-kernel", "switch-software", "system", "unspecified"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []), 
    }

    prop_map = {
        "checksum": "checksum", 
        "childAction": "child_action", 
        "dn": "dn", 
        "inProgress": "in_progress", 
        "isoname": "isoname", 
        "location": "location", 
        "model": "model", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, type, version, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.type = type
        self.version = version
        self.checksum = None
        self.child_action = None
        self.in_progress = None
        self.isoname = None
        self.location = None
        self.name = None
        self.sacl = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareInstallable", parent_mo_or_dn, **kwargs)
