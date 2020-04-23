"""This module contains the general information for MoKvCfgHolder ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MoKvCfgHolderConsts:
    FILE_TX_ADMIN_STATE_DISABLED = "disabled"
    FILE_TX_ADMIN_STATE_ENABLED = "enabled"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OK = "ok"


class MoKvCfgHolder(ManagedObject):
    """This is MoKvCfgHolder class."""

    consts = MoKvCfgHolderConsts()
    naming_props = set([])

    mo_meta = MoMeta("MoKvCfgHolder", "moKvCfgHolder", "cfg-kv", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["admin"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'lsServer', 'orgOrg'], ['moIpV4AddrKv', 'moIpV6AddrKv', 'moKv', 'moVnicKv'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "file_tx_admin_state": MoPropertyMeta("file_tx_admin_state", "fileTxAdminState", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["config-failure", "not-supported", "ok"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fileTxAdminState": "file_tx_admin_state", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.file_tx_admin_state = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MoKvCfgHolder", parent_mo_or_dn, **kwargs)
