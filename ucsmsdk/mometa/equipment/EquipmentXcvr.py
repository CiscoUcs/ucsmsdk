"""This module contains the general information for EquipmentXcvr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentXcvrConsts:
    TYPE_10_25_GBASE = "10/25Gbase"
    TYPE_10_25_GBASELRS = "10/25Gbaselrs"
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
    TYPE_10GBASELRS = "10gbaselrs"
    TYPE_10GBASESR = "10gbasesr"
    TYPE_10GBASESRS = "10gbasesrs"
    TYPE_10GBASEZR = "10gbasezr"
    TYPE_10GBASEZRS = "10gbasezrs"
    TYPE_10GBX40DI = "10gbx40di"
    TYPE_10GBX40UI = "10gbx40ui"
    TYPE_10GBXDI = "10gbxdi"
    TYPE_10GBXUI = "10gbxui"
    TYPE_4X32GSW = "4x32gsw"
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
    TYPE_H10GAOC15M = "h10gaoc15m"
    TYPE_H10GAOC1M = "h10gaoc1m"
    TYPE_H10GAOC2M = "h10gaoc2m"
    TYPE_H10GAOC3M = "h10gaoc3m"
    TYPE_H10GAOC5M = "h10gaoc5m"
    TYPE_H10GAOC7M = "h10gaoc7m"
    TYPE_H10GCU1_5M = "h10gcu1-5m"
    TYPE_H10GCU10M = "h10gcu10m"
    TYPE_H10GCU1M = "h10gcu1m"
    TYPE_H10GCU2_5M = "h10gcu2-5m"
    TYPE_H10GCU2M = "h10gcu2m"
    TYPE_H10GCU3M = "h10gcu3m"
    TYPE_H10GCU5M = "h10gcu5m"
    TYPE_H10GCU7M = "h10gcu7m"
    TYPE_H10GLRMSM = "h10glrmsm"
    TYPE_H10GTX = "h10gtx"
    TYPE_H10GUSR = "h10gusr"
    TYPE_H25GAOC10M = "h25gaoc10m"
    TYPE_H25GAOC1M = "h25gaoc1m"
    TYPE_H25GAOC2M = "h25gaoc2m"
    TYPE_H25GAOC3M = "h25gaoc3m"
    TYPE_H25GAOC4M = "h25gaoc4m"
    TYPE_H25GAOC5M = "h25gaoc5m"
    TYPE_H25GAOC7M = "h25gaoc7m"
    TYPE_H25GCU1M = "h25gcu1m"
    TYPE_H25GCU2M = "h25gcu2m"
    TYPE_H25GCU3M = "h25gcu3m"
    TYPE_H25GCU4M = "h25gcu4m"
    TYPE_H25GCU5M = "h25gcu5m"
    TYPE_H25GLRS = "h25glrs"
    TYPE_H25GSRS = "h25gsrs"
    TYPE_QSFP100G40GBIDI = "qsfp100g40gbidi"
    TYPE_QSFP100GAOC10M = "qsfp100gaoc10m"
    TYPE_QSFP100GAOC15M = "qsfp100gaoc15m"
    TYPE_QSFP100GAOC1M = "qsfp100gaoc1m"
    TYPE_QSFP100GAOC20M = "qsfp100gaoc20m"
    TYPE_QSFP100GAOC25M = "qsfp100gaoc25m"
    TYPE_QSFP100GAOC2M = "qsfp100gaoc2m"
    TYPE_QSFP100GAOC30M = "qsfp100gaoc30m"
    TYPE_QSFP100GAOC3M = "qsfp100gaoc3m"
    TYPE_QSFP100GAOC5M = "qsfp100gaoc5m"
    TYPE_QSFP100GAOC7M = "qsfp100gaoc7m"
    TYPE_QSFP100GCR4 = "qsfp100gcr4"
    TYPE_QSFP100GCU1M = "qsfp100gcu1m"
    TYPE_QSFP100GCU2M = "qsfp100gcu2m"
    TYPE_QSFP100GCU3M = "qsfp100gcu3m"
    TYPE_QSFP100GDR = "qsfp100gdr"
    TYPE_QSFP100GFR = "qsfp100gfr"
    TYPE_QSFP100GLR4S = "qsfp100glr4s"
    TYPE_QSFP100GPSM4S = "qsfp100gpsm4s"
    TYPE_QSFP100GSL4 = "qsfp100gsl4"
    TYPE_QSFP100GSMSR = "qsfp100gsmsr"
    TYPE_QSFP100GSR1_2 = "qsfp100gsr1.2"
    TYPE_QSFP100GSR4 = "qsfp100gsr4"
    TYPE_QSFP100GSR4S = "qsfp100gsr4s"
    TYPE_QSFP40GCR4 = "qsfp40gcr4"
    TYPE_QSFP40GCSR = "qsfp40gcsr"
    TYPE_QSFP40GCSR4 = "qsfp40gcsr4"
    TYPE_QSFP40GER4 = "qsfp40ger4"
    TYPE_QSFP40GFET = "qsfp40gfet"
    TYPE_QSFP40GLR4 = "qsfp40glr4"
    TYPE_QSFP40GSR4 = "qsfp40gsr4"
    TYPE_QSFP40GSRBD = "qsfp40gsrbd"
    TYPE_QSFP4SFP10GCU1M = "qsfp4sfp10gcu1m"
    TYPE_QSFP4SFP10GCU2M = "qsfp4sfp10gcu2m"
    TYPE_QSFP4SFP10GCU3M = "qsfp4sfp10gcu3m"
    TYPE_QSFP4SFP10GCU4M = "qsfp4sfp10gcu4m"
    TYPE_QSFP4SFP10GCU5M = "qsfp4sfp10gcu5m"
    TYPE_QSFP4SFP25GCU1M = "qsfp4sfp25gcu1m"
    TYPE_QSFP4SFP25GCU2M = "qsfp4sfp25gcu2m"
    TYPE_QSFP4SFP25GCU3M = "qsfp4sfp25gcu3m"
    TYPE_QSFP4SFP25GCU5M = "qsfp4sfp25gcu5m"
    TYPE_QSFP4SFP25GUNKNOWN = "qsfp4sfp25gunknown"
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
    TYPE_QSFP4X10GLRS = "qsfp4x10glrs"
    TYPE_QSFPH40GACU10M = "qsfph40gacu10m"
    TYPE_QSFPH40GACU1M = "qsfph40gacu1m"
    TYPE_QSFPH40GACU3M = "qsfph40gacu3m"
    TYPE_QSFPH40GACU5M = "qsfph40gacu5m"
    TYPE_QSFPH40GACU7M = "qsfph40gacu7m"
    TYPE_QSFPH40GAOC10M = "qsfph40gaoc10m"
    TYPE_QSFPH40GAOC15M = "qsfph40gaoc15m"
    TYPE_QSFPH40GAOC1M = "qsfph40gaoc1m"
    TYPE_QSFPH40GAOC20M = "qsfph40gaoc20m"
    TYPE_QSFPH40GAOC2M = "qsfph40gaoc2m"
    TYPE_QSFPH40GAOC30M = "qsfph40gaoc30m"
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
    TYPE_SFP25GSL = "sfp25gsl"
    TYPE_UNKNOWN = "unknown"
    TYPE_X2 = "x2"


class EquipmentXcvr(ManagedObject):
    """This is EquipmentXcvr class."""

    consts = EquipmentXcvrConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentXcvr", "equipmentXcvr", "transceiver", VersionMeta.Version141i, "InputOutput", 0x1f, [], ["read-only"], ['etherPIo', 'etherServerIntFIo', 'etherSwitchIntFIo', 'fcPIo'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-128"]),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "ts": MoPropertyMeta("ts", "ts", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10/25Gbase", "10/25Gbaselrs", "1000basecx", "1000baselh", "1000baselx", "1000basesx", "1000baset", "1000baseunknown", "1000basevx", "1000basex", "1000basezx", "10gbaseer", "10gbaselr", "10gbaselrm", "10gbaselrs", "10gbasesr", "10gbasesrs", "10gbasezr", "10gbasezrs", "10gbx40di", "10gbx40ui", "10gbxdi", "10gbxui", "4x32gsw", "cwdm1471", "cwdm1531", "cwdm1551", "dwdmsfp", "fet", "h10gacu10m", "h10gacu15m", "h10gacu1m", "h10gacu3m", "h10gacu5m", "h10gacu7m", "h10gacuaoc10m", "h10gacuaoc15m", "h10gacuaoc1m", "h10gacuaoc2m", "h10gacuaoc3m", "h10gacuaoc5m", "h10gacuaoc7m", "h10gaoc10m", "h10gaoc15m", "h10gaoc1m", "h10gaoc2m", "h10gaoc3m", "h10gaoc5m", "h10gaoc7m", "h10gcu1-5m", "h10gcu10m", "h10gcu1m", "h10gcu2-5m", "h10gcu2m", "h10gcu3m", "h10gcu5m", "h10gcu7m", "h10glrmsm", "h10gtx", "h10gusr", "h25gaoc10m", "h25gaoc1m", "h25gaoc2m", "h25gaoc3m", "h25gaoc4m", "h25gaoc5m", "h25gaoc7m", "h25gcu1m", "h25gcu2m", "h25gcu3m", "h25gcu4m", "h25gcu5m", "h25glrs", "h25gsrs", "qsfp100g40gbidi", "qsfp100gaoc10m", "qsfp100gaoc15m", "qsfp100gaoc1m", "qsfp100gaoc20m", "qsfp100gaoc25m", "qsfp100gaoc2m", "qsfp100gaoc30m", "qsfp100gaoc3m", "qsfp100gaoc5m", "qsfp100gaoc7m", "qsfp100gcr4", "qsfp100gcu1m", "qsfp100gcu2m", "qsfp100gcu3m", "qsfp100gdr", "qsfp100gfr", "qsfp100glr4s", "qsfp100gpsm4s", "qsfp100gsl4", "qsfp100gsmsr", "qsfp100gsr1.2", "qsfp100gsr4", "qsfp100gsr4s", "qsfp40gcr4", "qsfp40gcsr", "qsfp40gcsr4", "qsfp40ger4", "qsfp40gfet", "qsfp40glr4", "qsfp40gsr4", "qsfp40gsrbd", "qsfp4sfp10gcu1m", "qsfp4sfp10gcu2m", "qsfp4sfp10gcu3m", "qsfp4sfp10gcu4m", "qsfp4sfp10gcu5m", "qsfp4sfp25gcu1m", "qsfp4sfp25gcu2m", "qsfp4sfp25gcu3m", "qsfp4sfp25gcu5m", "qsfp4sfp25gunknown", "qsfp4x10ga0c10m", "qsfp4x10ga0c1m", "qsfp4x10ga0c2m", "qsfp4x10ga0c3m", "qsfp4x10ga0c5m", "qsfp4x10ga0c7m", "qsfp4x10ga0cunknown", "qsfp4x10gac10m", "qsfp4x10gac1m", "qsfp4x10gac3m", "qsfp4x10gac5m", "qsfp4x10gac7m", "qsfp4x10glr", "qsfp4x10glrs", "qsfph40gacu10m", "qsfph40gacu1m", "qsfph40gacu3m", "qsfph40gacu5m", "qsfph40gacu7m", "qsfph40gaoc10m", "qsfph40gaoc15m", "qsfph40gaoc1m", "qsfph40gaoc20m", "qsfph40gaoc2m", "qsfph40gaoc30m", "qsfph40gaoc3m", "qsfph40gaoc5m", "qsfph40gaoc7m", "qsfph40gaocunknown", "qsfph40gcu1m", "qsfph40gcu2m", "qsfph40gcu3m", "qsfph40gcu5m", "qsfploop", "qsfpqsa", "qsfpunknown", "sfp", "sfp25gsl", "unknown", "x2"], []),
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
