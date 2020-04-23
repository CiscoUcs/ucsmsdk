"""This module contains the general information for EquipmentPhysDevicesPerBoard ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPhysDevicesPerBoardConsts:
    pass


class EquipmentPhysDevicesPerBoard(ManagedObject):
    """This is EquipmentPhysDevicesPerBoard class."""

    consts = EquipmentPhysDevicesPerBoardConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentPhysDevicesPerBoard", "equipmentPhysDevicesPerBoard", "phys-dev-per-board", VersionMeta.Version222c, "InputOutput", 0x3ff, [], [""], ['equipmentBladeAggregationCapRef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "num_of_cpu": MoPropertyMeta("num_of_cpu", "numOfCpu", "byte", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "num_of_dimm": MoPropertyMeta("num_of_dimm", "numOfDimm", "ushort", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "num_of_local_disk": MoPropertyMeta("num_of_local_disk", "numOfLocalDisk", "byte", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "num_of_storage_controller": MoPropertyMeta("num_of_storage_controller", "numOfStorageController", "byte", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
        "num_ofadaptor": MoPropertyMeta("num_ofadaptor", "numOfadaptor", "byte", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "numOfCpu": "num_of_cpu", 
        "numOfDimm": "num_of_dimm", 
        "numOfLocalDisk": "num_of_local_disk", 
        "numOfStorageController": "num_of_storage_controller", 
        "numOfadaptor": "num_ofadaptor", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.num_of_cpu = None
        self.num_of_dimm = None
        self.num_of_local_disk = None
        self.num_of_storage_controller = None
        self.num_ofadaptor = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPhysDevicesPerBoard", parent_mo_or_dn, **kwargs)
