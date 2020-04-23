"""This module contains the general information for ClitestTypeTest ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ClitestTypeTestConsts:
    ANENUM_DOWN = "down"
    ANENUM_KIND_OF_UP = "kindOfUp"
    ANENUM_SORT_OF_DOWN = "sortOfDown"
    ANENUM_UP = "up"


class ClitestTypeTest(ManagedObject):
    """This is ClitestTypeTest class."""

    consts = ClitestTypeTestConsts()
    naming_props = set([])

    mo_meta = MoMeta("ClitestTypeTest", "clitestTypeTest", "tt-", VersionMeta.Version101e, "InputOutput", 0xfffffff, [], ["admin"], ['topRoot'], [], ["Get"])

    prop_meta = {
        "achar": MoPropertyMeta("achar", "achar", "byte", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "adate": MoPropertyMeta("adate", "adate", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "adatetime": MoPropertyMeta("adatetime", "adatetime", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "afloat": MoPropertyMeta("afloat", "afloat", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "amac": MoPropertyMeta("amac", "amac", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "anenum": MoPropertyMeta("anenum", "anenum", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["down", "kindOfUp", "sortOfDown", "up"], []),
        "anipv4": MoPropertyMeta("anipv4", "anipv4", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "anipv6": MoPropertyMeta("anipv6", "anipv6", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, None, [], []),
        "ansbyte": MoPropertyMeta("ansbyte", "ansbyte", "sbyte", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []),
        "ansint16": MoPropertyMeta("ansint16", "ansint16", "short", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []),
        "ansint32": MoPropertyMeta("ansint32", "ansint32", "int", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], []),
        "ansint64": MoPropertyMeta("ansint64", "ansint64", "long", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], []),
        "apassword": MoPropertyMeta("apassword", "apassword", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []),
        "arange": MoPropertyMeta("arange", "arange", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], ["7-55", "99-255"]),
        "arcstring": MoPropertyMeta("arcstring", "arcstring", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""[abcdefghijklmnoprstuvwyA-Z0-9]{0,15}""", [], []),
        "arxstring": MoPropertyMeta("arxstring", "arxstring", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""(red|blue|green)+(yellow|purple)+""", [], []),
        "astring": MoPropertyMeta("astring", "astring", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000, 0, 510, None, [], []),
        "atime": MoPropertyMeta("atime", "atime", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], []),
        "aubyte": MoPropertyMeta("aubyte", "aubyte", "byte", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, [], []),
        "auint16": MoPropertyMeta("auint16", "auint16", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, [], []),
        "auint32": MoPropertyMeta("auint32", "auint32", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200000, None, None, None, [], []),
        "auint64": MoPropertyMeta("auint64", "auint64", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400000, None, None, None, [], []),
        "awwn": MoPropertyMeta("awwn", "awwn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800000, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1000000, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2000000, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4000000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "achar": "achar", 
        "adate": "adate", 
        "adatetime": "adatetime", 
        "afloat": "afloat", 
        "amac": "amac", 
        "anenum": "anenum", 
        "anipv4": "anipv4", 
        "anipv6": "anipv6", 
        "ansbyte": "ansbyte", 
        "ansint16": "ansint16", 
        "ansint32": "ansint32", 
        "ansint64": "ansint64", 
        "apassword": "apassword", 
        "arange": "arange", 
        "arcstring": "arcstring", 
        "arxstring": "arxstring", 
        "astring": "astring", 
        "atime": "atime", 
        "aubyte": "aubyte", 
        "auint16": "auint16", 
        "auint32": "auint32", 
        "auint64": "auint64", 
        "awwn": "awwn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.achar = None
        self.adate = None
        self.adatetime = None
        self.afloat = None
        self.amac = None
        self.anenum = None
        self.anipv4 = None
        self.anipv6 = None
        self.ansbyte = None
        self.ansint16 = None
        self.ansint32 = None
        self.ansint64 = None
        self.apassword = None
        self.arange = None
        self.arcstring = None
        self.arxstring = None
        self.astring = None
        self.atime = None
        self.aubyte = None
        self.auint16 = None
        self.auint32 = None
        self.auint64 = None
        self.awwn = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ClitestTypeTest", **kwargs)
