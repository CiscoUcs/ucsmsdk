"""This module contains the general information for FirmwareTPMConstraint ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareTPMConstraintConsts:
    CHECK_RUNNING_VER_FALSE = "false"
    CHECK_RUNNING_VER_NO = "no"
    CHECK_RUNNING_VER_TRUE = "true"
    CHECK_RUNNING_VER_YES = "yes"


class FirmwareTPMConstraint(ManagedObject):
    """This is FirmwareTPMConstraint class."""

    consts = FirmwareTPMConstraintConsts()
    naming_props = set(['tpmRevision'])

    mo_meta = MoMeta("FirmwareTPMConstraint", "firmwareTPMConstraint", "constraint-tpm-revision-[tpm_revision]", VersionMeta.Version227b, "InputOutput", 0x3f, [], [""], ['firmwareConstraints'], [], [None])

    prop_meta = {
        "check_running_ver": MoPropertyMeta("check_running_ver", "checkRunningVer", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "min_bios_version": MoPropertyMeta("min_bios_version", "minBiosVersion", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "tpm_revision": MoPropertyMeta("tpm_revision", "tpmRevision", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
    }

    prop_map = {
        "checkRunningVer": "check_running_ver", 
        "childAction": "child_action", 
        "dn": "dn", 
        "minBiosVersion": "min_bios_version", 
        "minCimcVersion": "min_cimc_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tpmRevision": "tpm_revision", 
    }

    def __init__(self, parent_mo_or_dn, tpm_revision, **kwargs):
        self._dirty_mask = 0
        self.tpm_revision = tpm_revision
        self.check_running_ver = None
        self.child_action = None
        self.min_bios_version = None
        self.min_cimc_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareTPMConstraint", parent_mo_or_dn, **kwargs)
