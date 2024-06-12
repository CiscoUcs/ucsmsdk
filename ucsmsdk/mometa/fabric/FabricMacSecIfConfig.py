"""This module contains the general information for FabricMacSecIfConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricMacSecIfConfigConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class FabricMacSecIfConfig(ManagedObject):
    """This is FabricMacSecIfConfig class."""

    consts = FabricMacSecIfConfigConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricMacSecIfConfig", "fabricMacSecIfConfig", "macsec-intf-conf-[name]", VersionMeta.Version434a, "InputOutput", 0xfff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricMacSec'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mac_sec_eapol_name": MoPropertyMeta("mac_sec_eapol_name", "macSecEapolName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "mac_sec_fallback_key_chain_name": MoPropertyMeta("mac_sec_fallback_key_chain_name", "macSecFallbackKeyChainName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,63}""", [], []),
        "mac_sec_key_chain_name": MoPropertyMeta("mac_sec_key_chain_name", "macSecKeyChainName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,63}""", [], []),
        "mac_sec_policy_name": MoPropertyMeta("mac_sec_policy_name", "macSecPolicyName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_mac_sec_eapol_name": MoPropertyMeta("oper_mac_sec_eapol_name", "operMacSecEapolName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_mac_sec_fallback_key_chain_name": MoPropertyMeta("oper_mac_sec_fallback_key_chain_name", "operMacSecFallbackKeyChainName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_mac_sec_key_chain_name": MoPropertyMeta("oper_mac_sec_key_chain_name", "operMacSecKeyChainName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_mac_sec_policy_name": MoPropertyMeta("oper_mac_sec_policy_name", "operMacSecPolicyName", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "macSecEapolName": "mac_sec_eapol_name", 
        "macSecFallbackKeyChainName": "mac_sec_fallback_key_chain_name", 
        "macSecKeyChainName": "mac_sec_key_chain_name", 
        "macSecPolicyName": "mac_sec_policy_name", 
        "name": "name", 
        "operMacSecEapolName": "oper_mac_sec_eapol_name", 
        "operMacSecFallbackKeyChainName": "oper_mac_sec_fallback_key_chain_name", 
        "operMacSecKeyChainName": "oper_mac_sec_key_chain_name", 
        "operMacSecPolicyName": "oper_mac_sec_policy_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.mac_sec_eapol_name = None
        self.mac_sec_fallback_key_chain_name = None
        self.mac_sec_key_chain_name = None
        self.mac_sec_policy_name = None
        self.oper_mac_sec_eapol_name = None
        self.oper_mac_sec_fallback_key_chain_name = None
        self.oper_mac_sec_key_chain_name = None
        self.oper_mac_sec_policy_name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricMacSecIfConfig", parent_mo_or_dn, **kwargs)
