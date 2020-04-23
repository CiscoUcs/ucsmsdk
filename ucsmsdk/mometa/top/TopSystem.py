"""This module contains the general information for TopSystem ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class TopSystemConsts:
    MODE_CLUSTER = "cluster"
    MODE_STAND_ALONE = "stand-alone"
    MODE_UNSPECIFIED = "unspecified"


class TopSystem(ManagedObject):
    """This is TopSystem class."""

    consts = TopSystemConsts()
    naming_props = set([])

    mo_meta = MoMeta("TopSystem", "topSystem", "sys", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "ext-lan-config"], ['topRoot'], ['aaaAuthRealm', 'aaaLdapEp', 'aaaRadiusEp', 'aaaSessionInfoTable', 'aaaTacacsPlusEp', 'aaaUserEp', 'cloudMgmtSvc', 'commSvcEp', 'computeRackUnit', 'controllerHaController', 'controllerMgmtDbCheckPol', 'domainChassisFeatureCont', 'domainEnvironmentFeatureCont', 'domainNetworkFeatureCont', 'domainServerFeatureCont', 'domainStorageFeatureCont', 'equipmentChassis', 'equipmentFex', 'equipmentRackEnclosure', 'extmgmtIfMonPolicy', 'extvmmEp', 'featureContextEp', 'firmwareCatalogue', 'firmwareStatus', 'firmwareSystem', 'firmwareUpgradeInfo', 'fsmStatus', 'initiatorRequestorEp', 'initiatorRequestorGrpEp', 'licenseEp', 'mgmtAccessPolicy', 'mgmtBackup', 'mgmtBackupPolicyConfig', 'mgmtController', 'mgmtEntity', 'mgmtImporter', 'mgmtIntAuthPolicy', 'networkElement', 'pkiEp', 'policyControlEp', 'powerEp', 'swatInjection', 'syntheticDirectory', 'syntheticFsObj', 'sysdebugCoreFileRepository', 'sysdebugDiagnosticLogRepository', 'sysdebugEp', 'sysdebugTechSupFileRepository', 'topInfoPolicy', 'trigLocalSched', 'trigMeta', 'trigSched', 'versionEp'], ["Get", "Set"])

    prop_meta = {
        "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "ipv6_addr": MoPropertyMeta("ipv6_addr", "ipv6Addr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster", "stand-alone", "unspecified"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[a-zA-Z][a-zA-Z0-9-]{0,29}""", [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "system_up_time": MoPropertyMeta("system_up_time", "systemUpTime", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", [], []),
    }

    prop_map = {
        "address": "address", 
        "childAction": "child_action", 
        "currentTime": "current_time", 
        "descr": "descr", 
        "dn": "dn", 
        "ipv6Addr": "ipv6_addr", 
        "mode": "mode", 
        "name": "name", 
        "owner": "owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "site": "site", 
        "status": "status", 
        "systemUpTime": "system_up_time", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.address = None
        self.child_action = None
        self.current_time = None
        self.descr = None
        self.ipv6_addr = None
        self.mode = None
        self.name = None
        self.owner = None
        self.sacl = None
        self.site = None
        self.status = None
        self.system_up_time = None

        ManagedObject.__init__(self, "TopSystem", **kwargs)
