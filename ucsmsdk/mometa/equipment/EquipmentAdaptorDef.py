"""This module contains the general information for EquipmentAdaptorDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentAdaptorDefConsts:
    FORCE_UPDATE_VERSION_FALSE = "false"
    FORCE_UPDATE_VERSION_NO = "no"
    FORCE_UPDATE_VERSION_TRUE = "true"
    FORCE_UPDATE_VERSION_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentAdaptorDef(ManagedObject):
    """This is EquipmentAdaptorDef class."""

    consts = EquipmentAdaptorDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentAdaptorDef", "equipmentAdaptorDef", "adaptor", VersionMeta.Version101e, "InputOutput", 0xff, [], [""], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "adaptor_port_speed": MoPropertyMeta("adaptor_port_speed", "adaptorPortSpeed", "string", VersionMeta.Version423b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ethernet_port_speed": MoPropertyMeta("ethernet_port_speed", "ethernetPortSpeed", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-18446744073709551615"]),
        "fibre_channel_port_speed": MoPropertyMeta("fibre_channel_port_speed", "fibreChannelPortSpeed", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-18446744073709551615"]),
        "force_update_version": MoPropertyMeta("force_update_version", "forceUpdateVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adaptorPortSpeed": "adaptor_port_speed", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "ethernetPortSpeed": "ethernet_port_speed", 
        "fibreChannelPortSpeed": "fibre_channel_port_speed", 
        "forceUpdateVersion": "force_update_version", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_port_speed = None
        self.child_action = None
        self.descr = None
        self.ethernet_port_speed = None
        self.fibre_channel_port_speed = None
        self.force_update_version = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentAdaptorDef", parent_mo_or_dn, **kwargs)
