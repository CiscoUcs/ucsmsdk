"""This module contains the general information for ApePalo ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApePaloConsts:
    TYPE_MENLO = "Menlo"
    TYPE_OPLIN = "Oplin"
    TYPE_PALO = "Palo"
    TYPE_UNKNOWN = "Unknown"


class ApePalo(ManagedObject):
    """This is ApePalo class."""

    consts = ApePaloConsts()
    naming_props = set(['mac1'])

    mo_meta = MoMeta("ApePalo", "apePalo", "Palo-[mac1]", VersionMeta.Version101e, "InputOutput", 0xffff, [], ["read-only"], ['apeNicAgManager'], ['apeMenloVnic', 'apePaloVnic'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "fru_id": MoPropertyMeta("fru_id", "fruId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []),
        "hw_version": MoPropertyMeta("hw_version", "hwVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
        "mac1": MoPropertyMeta("mac1", "mac1", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "mac2": MoPropertyMeta("mac2", "mac2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "start_event": MoPropertyMeta("start_event", "startEvent", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sw_backup_version": MoPropertyMeta("sw_backup_version", "swBackupVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []),
        "sw_startup_version": MoPropertyMeta("sw_startup_version", "swStartupVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], []),
        "sw_version": MoPropertyMeta("sw_version", "swVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000, 0, 510, None, [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["Menlo", "Oplin", "Palo", "Unknown"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "fruId": "fru_id", 
        "hwVersion": "hw_version", 
        "mac1": "mac1", 
        "mac2": "mac2", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "startEvent": "start_event", 
        "status": "status", 
        "swBackupVersion": "sw_backup_version", 
        "swStartupVersion": "sw_startup_version", 
        "swVersion": "sw_version", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, mac1, **kwargs):
        self._dirty_mask = 0
        self.mac1 = mac1
        self.child_action = None
        self.description = None
        self.fru_id = None
        self.hw_version = None
        self.mac2 = None
        self.name = None
        self.sacl = None
        self.serial = None
        self.start_event = None
        self.status = None
        self.sw_backup_version = None
        self.sw_startup_version = None
        self.sw_version = None
        self.type = None

        ManagedObject.__init__(self, "ApePalo", parent_mo_or_dn, **kwargs)
