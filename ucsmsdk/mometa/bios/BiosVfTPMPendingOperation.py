"""This module contains the general information for BiosVfTPMPendingOperation ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfTPMPendingOperationConsts():
    VP_TPMPENDING_OPERATION_NONE = "none"
    VP_TPMPENDING_OPERATION_PLATFORM_DEFAULT = "platform-default"
    VP_TPMPENDING_OPERATION_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_TPMPENDING_OPERATION_TPMCLEAR = "tpmclear"
    VP_TPMPENDING_OPERATION_TPMPPIOOWNEROFF = "tpmppioowneroff"
    VP_TPMPENDING_OPERATION_TPMPPIOOWNERON = "tpmppioowneron"


class BiosVfTPMPendingOperation(ManagedObject):
    """This is BiosVfTPMPendingOperation class."""

    consts = BiosVfTPMPendingOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfTPMPendingOperation", "biosVfTPMPendingOperation", "TPM-Pending-Operation", VersionMeta.Version224a, "InputOutput", 0xfL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vp_tpm_pending_operation": MoPropertyMeta("vp_tpm_pending_operation", "vpTPMPendingOperation", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "platform-default", "platform-recommended", "tpmclear", "tpmppioowneroff", "tpmppioowneron"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpTPMPendingOperation": "vp_tpm_pending_operation", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_tpm_pending_operation = None

        ManagedObject.__init__(self, "BiosVfTPMPendingOperation", parent_mo_or_dn, **kwargs)

