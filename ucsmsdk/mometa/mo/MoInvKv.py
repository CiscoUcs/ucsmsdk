"""This module contains the general information for MoInvKv ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MoInvKvConsts:
    OWNER_INVENTORY = "inventory"
    OWNER_MGMT = "mgmt"
    TYPE_IPV4_ADDR = "ipv4-addr"
    TYPE_IPV6_ADDR = "ipv6-addr"
    TYPE_KEY_VALUE = "key-value"
    TYPE_VLAN = "vlan"
    TYPE_VNIC = "vnic"


class MoInvKv(ManagedObject):
    """This is MoInvKv class."""

    consts = MoInvKvConsts()
    naming_props = set(['key'])

    mo_meta = MoMeta("MoInvKv", "moInvKv", "kv-[key]", VersionMeta.Version321d, "InputOutput", 0x7f, [], ["admin", "read-only"], ['moKvInvHolder'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["inventory", "mgmt"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4-addr", "ipv6-addr", "key-value", "vlan", "vnic"], []),
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "key": "key", 
        "owner": "owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, key, **kwargs):
        self._dirty_mask = 0
        self.key = key
        self.child_action = None
        self.owner = None
        self.sacl = None
        self.status = None
        self.type = None
        self.value = None

        ManagedObject.__init__(self, "MoInvKv", parent_mo_or_dn, **kwargs)
