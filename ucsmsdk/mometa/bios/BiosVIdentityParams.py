"""This module contains the general information for BiosVIdentityParams ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVIdentityParamsConsts:
    pass


class BiosVIdentityParams(ManagedObject):
    """This is BiosVIdentityParams class."""

    consts = BiosVIdentityParamsConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVIdentityParams", "biosVIdentityParams", "bios-videntity-params", VersionMeta.Version201m, "InputOutput", 0x1f, [], [""], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ls_server_name": MoPropertyMeta("ls_server_name", "lsServerName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "ls_server_tmpl_name": MoPropertyMeta("ls_server_tmpl_name", "lsServerTmplName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sys_name": MoPropertyMeta("sys_name", "sysName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lsServerName": "ls_server_name", 
        "lsServerTmplName": "ls_server_tmpl_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "sysName": "sys_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.ls_server_name = None
        self.ls_server_tmpl_name = None
        self.sacl = None
        self.status = None
        self.sys_name = None

        ManagedObject.__init__(self, "BiosVIdentityParams", parent_mo_or_dn, **kwargs)
