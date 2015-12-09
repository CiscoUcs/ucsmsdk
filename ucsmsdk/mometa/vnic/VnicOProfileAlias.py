"""This module contains the general information for VnicOProfileAlias ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicOProfileAliasConsts():
    MGMT_PLANE_RHEV_M = "rhev-m"
    MGMT_PLANE_SCVMM = "scvmm"
    MGMT_PLANE_UNMANAGED = "unmanaged"
    MGMT_PLANE_VCENTER = "vcenter"


class VnicOProfileAlias(ManagedObject):
    """This is VnicOProfileAlias class."""

    consts = VnicOProfileAliasConsts()
    naming_props = set([u'vSwitchName', u'alias'])

    mo_meta = MoMeta("VnicOProfileAlias", "vnicOProfileAlias", "swid-[v_switch_name]alias-[alias]", VersionMeta.Version201m, "InputOutput", 0x7fL, [], ["read-only"], [u'vmVnicProfInst', u'vnicProfile'], [], ["Get"])

    prop_meta = {
        "alias": MoPropertyMeta("alias", "alias", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x2L, 1, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "mgmt_plane": MoPropertyMeta("mgmt_plane", "mgmtPlane", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["rhev-m", "scvmm", "unmanaged", "vcenter"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "v_switch_id": MoPropertyMeta("v_switch_id", "vSwitchId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{1,40}""", [], []), 
        "v_switch_name": MoPropertyMeta("v_switch_name", "vSwitchName", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x40L, None, None, r"""[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{1,16}""", [], []), 
    }

    prop_map = {
        "alias": "alias", 
        "childAction": "child_action", 
        "dn": "dn", 
        "mgmtPlane": "mgmt_plane", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vSwitchId": "v_switch_id", 
        "vSwitchName": "v_switch_name", 
    }

    def __init__(self, parent_mo_or_dn, v_switch_name, alias, **kwargs):
        self._dirty_mask = 0
        self.v_switch_name = v_switch_name
        self.alias = alias
        self.child_action = None
        self.mgmt_plane = None
        self.sacl = None
        self.status = None
        self.v_switch_id = None

        ManagedObject.__init__(self, "VnicOProfileAlias", parent_mo_or_dn, **kwargs)

