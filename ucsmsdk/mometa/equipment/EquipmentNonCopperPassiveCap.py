"""This module contains the general information for EquipmentNonCopperPassiveCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentNonCopperPassiveCapConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentNonCopperPassiveCap(ManagedObject):
    """This is EquipmentNonCopperPassiveCap class."""

    consts = EquipmentNonCopperPassiveCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentNonCopperPassiveCap", "equipmentNonCopperPassiveCap", "non-copper-passive-cap", VersionMeta.Version311e, "InputOutput", 0xff, [], [""], ['equipmentSwitchCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version311e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "phy_port_bitmask": MoPropertyMeta("phy_port_bitmask", "phyPortBitmask", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|p53|p49|p45|p41|p37|p33|p29|p25|p21|p17|p13|p9|p5|p1|p54|p50|p46|p42|p38|p34|p30|p26|p22|p18|p14|p10|p6|p2|p51|p47|p43|p39|p35|p31|p27|p23|p19|p15|p11|p7|p3|p52|p48|p44|p40|p36|p32|p28|p24|p20|p16|p12|p8|p4|all|defaultValue),){0,56}(none|p53|p49|p45|p41|p37|p33|p29|p25|p21|p17|p13|p9|p5|p1|p54|p50|p46|p42|p38|p34|p30|p26|p22|p18|p14|p10|p6|p2|p51|p47|p43|p39|p35|p31|p27|p23|p19|p15|p11|p7|p3|p52|p48|p44|p40|p36|p32|p28|p24|p20|p16|p12|p8|p4|all|defaultValue){0,1}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "phyPortBitmask": "phy_port_bitmask", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.phy_port_bitmask = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentNonCopperPassiveCap", parent_mo_or_dn, **kwargs)
