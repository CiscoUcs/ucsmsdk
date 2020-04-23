"""This module contains the general information for FirmwareSpec ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareSpecConsts:
    pass


class FirmwareSpec(ManagedObject):
    """This is FirmwareSpec class."""

    consts = FirmwareSpecConsts()
    naming_props = set(['bundleVersion'])

    mo_meta = MoMeta("FirmwareSpec", "firmwareSpec", "fw-spec-bundle-version-[bundle_version]", VersionMeta.Version141i, "InputOutput", 0x3f, [], [""], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "bundle_version": MoPropertyMeta("bundle_version", "bundleVersion", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "eth_efi_version": MoPropertyMeta("eth_efi_version", "ethEFIVersion", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "eth_option_rom_version": MoPropertyMeta("eth_option_rom_version", "ethOptionRomVersion", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fc_fw_version": MoPropertyMeta("fc_fw_version", "fcFWVersion", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fc_option_rom_version": MoPropertyMeta("fc_option_rom_version", "fcOptionRomVersion", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "bundleVersion": "bundle_version", 
        "childAction": "child_action", 
        "dn": "dn", 
        "ethEFIVersion": "eth_efi_version", 
        "ethOptionRomVersion": "eth_option_rom_version", 
        "fcFWVersion": "fc_fw_version", 
        "fcOptionRomVersion": "fc_option_rom_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, bundle_version, **kwargs):
        self._dirty_mask = 0
        self.bundle_version = bundle_version
        self.child_action = None
        self.eth_efi_version = None
        self.eth_option_rom_version = None
        self.fc_fw_version = None
        self.fc_option_rom_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareSpec", parent_mo_or_dn, **kwargs)
