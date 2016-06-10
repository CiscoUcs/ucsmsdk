"""This module contains the general information for EquipmentXcvr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentXcvrConsts:
    TYPE_1000BASECX = "1000basecx"
    TYPE_1000BASELH = "1000baselh"
    TYPE_1000BASELX = "1000baselx"
    TYPE_1000BASESX = "1000basesx"
    TYPE_1000BASET = "1000baset"
    TYPE_1000BASEUNKNOWN = "1000baseunknown"
    TYPE_1000BASEVX = "1000basevx"
    TYPE_1000BASEX = "1000basex"
    TYPE_1000BASEZX = "1000basezx"
    TYPE_10GBASEER = "10gbaseer"
    TYPE_10GBASELR = "10gbaselr"
    TYPE_10GBASELRM = "10gbaselrm"
    TYPE_10GBASESR = "10gbasesr"
    TYPE_10GBASEZR = "10gbasezr"
    TYPE_CWDM1471 = "cwdm1471"
    TYPE_CWDM1531 = "cwdm1531"
    TYPE_CWDM1551 = "cwdm1551"
    TYPE_DWDMSFP = "dwdmsfp"
    TYPE_FET = "fet"
    TYPE_H10GACU10M = "h10gacu10m"
    TYPE_H10GACU15M = "h10gacu15m"
    TYPE_H10GACU1M = "h10gacu1m"
    TYPE_H10GACU3M = "h10gacu3m"
    TYPE_H10GACU5M = "h10gacu5m"
    TYPE_H10GACU7M = "h10gacu7m"
    TYPE_H10GACUAOC10M = "h10gacuaoc10m"
    TYPE_H10GACUAOC15M = "h10gacuaoc15m"
    TYPE_H10GACUAOC1M = "h10gacuaoc1m"
    TYPE_H10GACUAOC2M = "h10gacuaoc2m"
    TYPE_H10GACUAOC3M = "h10gacuaoc3m"
    TYPE_H10GACUAOC5M = "h10gacuaoc5m"
    TYPE_H10GACUAOC7M = "h10gacuaoc7m"
    TYPE_H10GAOC10M = "h10gaoc10m"
    TYPE_H10GAOC1M = "h10gaoc1m"
    TYPE_H10GAOC2M = "h10gaoc2m"
    TYPE_H10GAOC3M = "h10gaoc3m"
    TYPE_H10GAOC5M = "h10gaoc5m"
    TYPE_H10GAOC7M = "h10gaoc7m"
    TYPE_H10GCU10M = "h10gcu10m"
    TYPE_H10GCU1M = "h10gcu1m"
    TYPE_H10GCU2M = "h10gcu2m"
    TYPE_H10GCU3M = "h10gcu3m"
    TYPE_H10GCU5M = "h10gcu5m"
    TYPE_H10GCU7M = "h10gcu7m"
    TYPE_H10GLRMSM = "h10glrmsm"
    TYPE_H10GUSR = "h10gusr"
    TYPE_QSFP40GCR4 = "qsfp40gcr4"
    TYPE_QSFP40GCSR4 = "qsfp40gcsr4"
    TYPE_QSFP40GFET = "qsfp40gfet"
    TYPE_QSFP40GLR4 = "qsfp40glr4"
    TYPE_QSFP40GSR4 = "qsfp40gsr4"
    TYPE_QSFP40GSRBD = "qsfp40gsrbd"
    TYPE_QSFP4SFP10GCU1M = "qsfp4sfp10gcu1m"
    TYPE_QSFP4SFP10GCU2M = "qsfp4sfp10gcu2m"
    TYPE_QSFP4SFP10GCU3M = "qsfp4sfp10gcu3m"
    TYPE_QSFP4SFP10GCU5M = "qsfp4sfp10gcu5m"
    TYPE_QSFP4X10GA0C10M = "qsfp4x10ga0c10m"
    TYPE_QSFP4X10GA0C1M = "qsfp4x10ga0c1m"
    TYPE_QSFP4X10GA0C2M = "qsfp4x10ga0c2m"
    TYPE_QSFP4X10GA0C3M = "qsfp4x10ga0c3m"
    TYPE_QSFP4X10GA0C5M = "qsfp4x10ga0c5m"
    TYPE_QSFP4X10GA0C7M = "qsfp4x10ga0c7m"
    TYPE_QSFP4X10GA0CUNKNOWN = "qsfp4x10ga0cunknown"
    TYPE_QSFP4X10GAC10M = "qsfp4x10gac10m"
    TYPE_QSFP4X10GAC1M = "qsfp4x10gac1m"
    TYPE_QSFP4X10GAC3M = "qsfp4x10gac3m"
    TYPE_QSFP4X10GAC5M = "qsfp4x10gac5m"
    TYPE_QSFP4X10GAC7M = "qsfp4x10gac7m"
    TYPE_QSFP4X10GLR = "qsfp4x10glr"
    TYPE_QSFPH40GACU10M = "qsfph40gacu10m"
    TYPE_QSFPH40GACU1M = "qsfph40gacu1m"
    TYPE_QSFPH40GACU3M = "qsfph40gacu3m"
    TYPE_QSFPH40GACU5M = "qsfph40gacu5m"
    TYPE_QSFPH40GACU7M = "qsfph40gacu7m"
    TYPE_QSFPH40GAOC10M = "qsfph40gaoc10m"
    TYPE_QSFPH40GAOC15M = "qsfph40gaoc15m"
    TYPE_QSFPH40GAOC1M = "qsfph40gaoc1m"
    TYPE_QSFPH40GAOC2M = "qsfph40gaoc2m"
    TYPE_QSFPH40GAOC3M = "qsfph40gaoc3m"
    TYPE_QSFPH40GAOC5M = "qsfph40gaoc5m"
    TYPE_QSFPH40GAOC7M = "qsfph40gaoc7m"
    TYPE_QSFPH40GAOCUNKNOWN = "qsfph40gaocunknown"
    TYPE_QSFPH40GCU1M = "qsfph40gcu1m"
    TYPE_QSFPH40GCU2M = "qsfph40gcu2m"
    TYPE_QSFPH40GCU3M = "qsfph40gcu3m"
    TYPE_QSFPH40GCU5M = "qsfph40gcu5m"
    TYPE_QSFPLOOP = "qsfploop"
    TYPE_QSFPQSA = "qsfpqsa"
    TYPE_QSFPUNKNOWN = "qsfpunknown"
    TYPE_SFP = "sfp"
    TYPE_UNKNOWN = "unknown"
    TYPE_X2 = "x2"


class EquipmentXcvr(ManagedObject):
    """This is EquipmentXcvr class."""

    consts = EquipmentXcvrConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentXcvr", "equipmentXcvr", "transceiver", VersionMeta.Version141i, "InputOutput", 0x1f, [], ["read-only"], [u'etherPIo', u'etherServerIntFIo', u'etherSwitchIntFIo', u'fcPIo'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-128"]), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "ts": MoPropertyMeta("ts", "ts", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1000basecx", "1000baselh", "1000baselx", "1000basesx", "1000baset", "1000baseunknown", "1000basevx", "1000basex", "1000basezx", "10gbaseer", "10gbaselr", "10gbaselrm", "10gbasesr", "10gbasezr", "cwdm1471", "cwdm1531", "cwdm1551", "dwdmsfp", "fet", "h10gacu10m", "h10gacu15m", "h10gacu1m", "h10gacu3m", "h10gacu5m", "h10gacu7m", "h10gacuaoc10m", "h10gacuaoc15m", "h10gacuaoc1m", "h10gacuaoc2m", "h10gacuaoc3m", "h10gacuaoc5m", "h10gacuaoc7m", "h10gaoc10m", "h10gaoc1m", "h10gaoc2m", "h10gaoc3m", "h10gaoc5m", "h10gaoc7m", "h10gcu10m", "h10gcu1m", "h10gcu2m", "h10gcu3m", "h10gcu5m", "h10gcu7m", "h10glrmsm", "h10gusr", "qsfp40gcr4", "qsfp40gcsr4", "qsfp40gfet", "qsfp40glr4", "qsfp40gsr4", "qsfp40gsrbd", "qsfp4sfp10gcu1m", "qsfp4sfp10gcu2m", "qsfp4sfp10gcu3m", "qsfp4sfp10gcu5m", "qsfp4x10ga0c10m", "qsfp4x10ga0c1m", "qsfp4x10ga0c2m", "qsfp4x10ga0c3m", "qsfp4x10ga0c5m", "qsfp4x10ga0c7m", "qsfp4x10ga0cunknown", "qsfp4x10gac10m", "qsfp4x10gac1m", "qsfp4x10gac3m", "qsfp4x10gac5m", "qsfp4x10gac7m", "qsfp4x10glr", "qsfph40gacu10m", "qsfph40gacu1m", "qsfph40gacu3m", "qsfph40gacu5m", "qsfph40gacu7m", "qsfph40gaoc10m", "qsfph40gaoc15m", "qsfph40gaoc1m", "qsfph40gaoc2m", "qsfph40gaoc3m", "qsfph40gaoc5m", "qsfph40gaoc7m", "qsfph40gaocunknown", "qsfph40gcu1m", "qsfph40gcu2m", "qsfph40gcu3m", "qsfph40gcu5m", "qsfploop", "qsfpqsa", "qsfpunknown", "sfp", "unknown", "x2"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "ts": "ts", 
        "type": "type", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.id = None
        self.model = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.ts = None
        self.type = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentXcvr", parent_mo_or_dn, **kwargs)
