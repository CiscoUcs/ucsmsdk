"""This module contains the general information for VnicIScsiBootVnic ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIScsiBootVnicConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class VnicIScsiBootVnic(ManagedObject):
    """This is VnicIScsiBootVnic class."""

    consts = VnicIScsiBootVnicConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicIScsiBootVnic", "vnicIScsiBootVnic", "boot-vnic-[name]", VersionMeta.Version211a, "InputOutput", 0x7ff, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server", "ls-storage"], ['vnicIScsiBootParams'], ['faultInst', 'vnicIPv4If', 'vnicIScsiAutoTargetIf', 'vnicIScsiStaticTargetIf'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "auth_profile_name": MoPropertyMeta("auth_profile_name", "authProfileName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "initiator_name": MoPropertyMeta("initiator_name", "initiatorName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[0-9a-zA-Z\.:-]{0,223}$""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "iqn_ident_pool_name": MoPropertyMeta("iqn_ident_pool_name", "iqnIdentPoolName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_auth_profile_name": MoPropertyMeta("oper_auth_profile_name", "operAuthProfileName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_iqn_ident_pool_name": MoPropertyMeta("oper_iqn_ident_pool_name", "operIqnIdentPoolName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "authProfileName": "auth_profile_name", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "initiatorName": "initiator_name", 
        "intId": "int_id", 
        "iqnIdentPoolName": "iqn_ident_pool_name", 
        "name": "name", 
        "operAuthProfileName": "oper_auth_profile_name", 
        "operIqnIdentPoolName": "oper_iqn_ident_pool_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.auth_profile_name = None
        self.child_action = None
        self.descr = None
        self.initiator_name = None
        self.int_id = None
        self.iqn_ident_pool_name = None
        self.oper_auth_profile_name = None
        self.oper_iqn_ident_pool_name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicIScsiBootVnic", parent_mo_or_dn, **kwargs)
