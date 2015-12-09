"""This module contains the general information for ApeReading ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeReadingConsts():
    pass


class ApeReading(ManagedObject):
    """This is ApeReading class."""

    consts = ApeReadingConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ApeReading", "apeReading", "reading-[id]", VersionMeta.Version101e, "InputOutput", 0xffffL, [], ["read-only"], [u'apeMcTable'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], []), 
        "is_analog": MoPropertyMeta("is_analog", "is_analog", "ushort", None, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sensor_type": MoPropertyMeta("sensor_type", "sensorType", "ushort", None, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "state": MoPropertyMeta("state", "state", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "threshold_lc": MoPropertyMeta("threshold_lc", "thresholdLc", "float", None, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, [], []), 
        "threshold_lnc": MoPropertyMeta("threshold_lnc", "thresholdLnc", "float", None, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], []), 
        "threshold_lnr": MoPropertyMeta("threshold_lnr", "thresholdLnr", "float", None, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], []), 
        "threshold_uc": MoPropertyMeta("threshold_uc", "thresholdUc", "float", None, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, [], []), 
        "threshold_unc": MoPropertyMeta("threshold_unc", "thresholdUnc", "float", None, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, [], []), 
        "threshold_unr": MoPropertyMeta("threshold_unr", "thresholdUnr", "float", None, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, [], []), 
        "value": MoPropertyMeta("value", "value", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "is_analog": "is_analog", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sensorType": "sensor_type", 
        "state": "state", 
        "status": "status", 
        "thresholdLc": "threshold_lc", 
        "thresholdLnc": "threshold_lnc", 
        "thresholdLnr": "threshold_lnr", 
        "thresholdUc": "threshold_uc", 
        "thresholdUnc": "threshold_unc", 
        "thresholdUnr": "threshold_unr", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.is_analog = None
        self.sacl = None
        self.sensor_type = None
        self.state = None
        self.status = None
        self.threshold_lc = None
        self.threshold_lnc = None
        self.threshold_lnr = None
        self.threshold_uc = None
        self.threshold_unc = None
        self.threshold_unr = None
        self.value = None

        ManagedObject.__init__(self, "ApeReading", parent_mo_or_dn, **kwargs)

