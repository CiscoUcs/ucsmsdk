"""This module contains the general information for LstorageSharedCredential ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageSharedCredentialConsts():
    pass


class LstorageSharedCredential(ManagedObject):
    """This is LstorageSharedCredential class."""

    consts = LstorageSharedCredentialConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageSharedCredential", "lstorageSharedCredential", "shared-credential", VersionMeta.Version302c, "InputOutput", 0xffL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'lstorageLunReplicationService'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "enc_secret": MoPropertyMeta("enc_secret", "encSecret", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, 1, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "secret": MoPropertyMeta("secret", "secret", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,64}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "str_secret": MoPropertyMeta("str_secret", "strSecret", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80L, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "encSecret": "enc_secret", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secret": "secret", 
        "status": "status", 
        "strSecret": "str_secret", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.enc_secret = None
        self.prop_acl = None
        self.sacl = None
        self.secret = None
        self.status = None
        self.str_secret = None

        ManagedObject.__init__(self, "LstorageSharedCredential", parent_mo_or_dn, **kwargs)

