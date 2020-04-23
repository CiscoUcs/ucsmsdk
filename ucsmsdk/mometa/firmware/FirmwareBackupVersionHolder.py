"""This module contains the general information for FirmwareBackupVersionHolder ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareBackupVersionHolderConsts:
    BUNDLE_TYPE_BLADE = "blade"
    BUNDLE_TYPE_CHASSIS = "chassis"
    BUNDLE_TYPE_INFRA = "infra"
    BUNDLE_TYPE_NONE = "none"
    BUNDLE_TYPE_RACK = "rack"


class FirmwareBackupVersionHolder(ManagedObject):
    """This is FirmwareBackupVersionHolder class."""

    consts = FirmwareBackupVersionHolderConsts()
    naming_props = set(['bundleType'])

    mo_meta = MoMeta("FirmwareBackupVersionHolder", "firmwareBackupVersionHolder", "update-backup-version-holder-[bundle_type]", VersionMeta.Version323a, "InputOutput", 0x7f, [], ["admin"], ['firmwareCatalogPack', 'firmwareChassisPack', 'firmwareComputeHostPack', 'firmwareComputeMgmtPack', 'firmwareInfraPack'], ['firmwarePackItem'], ["Get", "Set"])

    prop_meta = {
        "bundle_name": MoPropertyMeta("bundle_name", "bundleName", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "bundle_type": MoPropertyMeta("bundle_type", "bundleType", "string", VersionMeta.Version323a, MoPropertyMeta.NAMING, 0x2, None, None, None, ["blade", "chassis", "infra", "none", "rack"], []),
        "bundle_version": MoPropertyMeta("bundle_version", "bundleVersion", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "bundleName": "bundle_name", 
        "bundleType": "bundle_type", 
        "bundleVersion": "bundle_version", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, bundle_type, **kwargs):
        self._dirty_mask = 0
        self.bundle_type = bundle_type
        self.bundle_name = None
        self.bundle_version = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareBackupVersionHolder", parent_mo_or_dn, **kwargs)
