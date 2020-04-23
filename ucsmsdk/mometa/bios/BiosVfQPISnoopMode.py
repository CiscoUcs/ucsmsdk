"""This module contains the general information for BiosVfQPISnoopMode ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfQPISnoopModeConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_QPISNOOP_MODE_AUTO = "auto"
    VP_QPISNOOP_MODE_CLUSTER_ON_DIE = "cluster-on-die"
    VP_QPISNOOP_MODE_EARLY_SNOOP = "early-snoop"
    VP_QPISNOOP_MODE_HOME_DIRECTORY_SNOOP_WITH_OSB = "home-directory-snoop-with-osb"
    VP_QPISNOOP_MODE_HOME_SNOOP = "home-snoop"
    VP_QPISNOOP_MODE_PLATFORM_DEFAULT = "platform-default"
    VP_QPISNOOP_MODE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfQPISnoopMode(ManagedObject):
    """This is BiosVfQPISnoopMode class."""

    consts = BiosVfQPISnoopModeConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfQPISnoopMode", "biosVfQPISnoopMode", "QPI-Snoop-Mode", VersionMeta.Version224b, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_qpi_snoop_mode": MoPropertyMeta("vp_qpi_snoop_mode", "vpQPISnoopMode", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["auto", "cluster-on-die", "early-snoop", "home-directory-snoop-with-osb", "home-snoop", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpQPISnoopMode": "vp_qpi_snoop_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_qpi_snoop_mode = None

        ManagedObject.__init__(self, "BiosVfQPISnoopMode", parent_mo_or_dn, **kwargs)
