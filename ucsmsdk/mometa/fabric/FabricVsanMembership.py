"""This module contains the general information for FabricVsanMembership ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricVsanMembershipConsts:
    MEMBER_STATUS_DOWN = "down"
    MEMBER_STATUS_UP = "up"
    PARENT_ADMIN_STATE_DISABLED = "disabled"
    PARENT_ADMIN_STATE_ENABLED = "enabled"


class FabricVsanMembership(ManagedObject):
    """This is FabricVsanMembership class."""

    consts = FabricVsanMembershipConsts()
    naming_props = set(['vsanId'])

    mo_meta = MoMeta("FabricVsanMembership", "fabricVsanMembership", "vsanmember-[vsan_id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["read-only"], ['fabricFcSanEp', 'fabricFcSanPc', 'fabricFcoeEstcEp', 'fabricFcoeSanEp', 'fabricFcoeSanPc'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "member_status": MoPropertyMeta("member_status", "memberStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "up"], []),
        "parent_admin_state": MoPropertyMeta("parent_admin_state", "parentAdminState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vsan_id": MoPropertyMeta("vsan_id", "vsanId", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-4093"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "memberStatus": "member_status", 
        "parentAdminState": "parent_admin_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stateQual": "state_qual", 
        "status": "status", 
        "vsanId": "vsan_id", 
    }

    def __init__(self, parent_mo_or_dn, vsan_id, **kwargs):
        self._dirty_mask = 0
        self.vsan_id = vsan_id
        self.child_action = None
        self.member_status = None
        self.parent_admin_state = None
        self.sacl = None
        self.state_qual = None
        self.status = None

        ManagedObject.__init__(self, "FabricVsanMembership", parent_mo_or_dn, **kwargs)
