"""This module contains the general information for OrgOrg ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OrgOrgConsts:
    LEVEL_1 = "1"
    LEVEL_2 = "2"
    LEVEL_3 = "3"
    LEVEL_4 = "4"
    LEVEL_5 = "5"
    LEVEL_ROOT = "root"
    PERM_ACCESS_FALSE = "false"
    PERM_ACCESS_NO = "no"
    PERM_ACCESS_TRUE = "true"
    PERM_ACCESS_YES = "yes"


class OrgOrg(ManagedObject):
    """This is OrgOrg class."""

    consts = OrgOrgConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("OrgOrg", "orgOrg", "org-[name]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "org-management"], ['orgOrg'], ['aaaEpAuthProfile', 'adaptorHostEthIfProfile', 'adaptorHostFcIfProfile', 'adaptorHostIscsiIfProfile', 'biosVProfile', 'cimcvmediaMountConfigPolicy', 'commSvcPolicy', 'computeAutoconfigPolicy', 'computeBladeDiscPolicy', 'computeBladeInheritPolicy', 'computeChassisConnPolicy', 'computeChassisDiscPolicy', 'computeFanPolicy', 'computeGraphicsCardPolicy', 'computeHwChangeDiscPolicy', 'computeKvmMgmtPolicy', 'computeMemoryConfigPolicy', 'computeModularChassisFanPolicy', 'computePool', 'computePoolingPolicy', 'computePortDiscPolicy', 'computePowerExtendedPolicy', 'computePowerSavePolicy', 'computePowerSyncPolicy', 'computePsuPolicy', 'computeQual', 'computeRackConnLinkPolicy', 'computeScrubPolicy', 'computeServerDiscPolicy', 'computeServerMgmtPolicy', 'cpmaintMaintPolicy', 'diagRunPolicy', 'epqosDefinition', 'epqosDefinitionDelTask', 'equipmentAutoconfigPolicy', 'equipmentChassisInheritPolicy', 'equipmentChassisProfile', 'equipmentComputeConnPolicy', 'equipmentPool', 'equipmentPoolingPolicy', 'equipmentQual', 'equipmentTier', 'fabricLacpPolicy', 'fabricLanCloudPolicy', 'fabricMulticastPolicy', 'fabricOrgVlanPolicy', 'fabricUdldPolicy', 'fabricVConProfile', 'fabricVlanGroupPermit', 'fabricVlanGroupReq', 'fabricVlanPermit', 'fabricVlanReq', 'faultSuppressTask', 'fcpoolInitiators', 'firmwareAutoSyncPolicy', 'firmwareCatalogPack', 'firmwareChassisPack', 'firmwareComputeHostPack', 'firmwareComputeMgmtPack', 'firmwareInfraPack', 'hostimgPolicy', 'imgprovPolicy', 'imgsecPolicy', 'ippoolPool', 'iqnpoolPool', 'iscsiAuthProfile', 'lsAgentPolicy', 'lsServer', 'lsTier', 'lsbootPolicy', 'lsmaintMaintPolicy', 'lstorageDiskGroupConfigPolicy', 'lstorageDiskZoningPolicy', 'lstorageProfile', 'lstorageSasExpanderConfigPolicy', 'macpoolPool', 'memoryPersistentMemoryPolicy', 'mgmtBackupExportExtPolicy', 'mgmtBackupPolicy', 'mgmtCfgExportPolicy', 'mgmtSpdmCertificatePolicy', 'moKvCfgHolder', 'nwctrlDefinition', 'orgOrg', 'orgSourceMask', 'powerGroupAdditionPolicy', 'powerMgmtPolicy', 'powerPlacement', 'powerPolicy', 'solPolicy', 'statsThresholdPolicy', 'storageConnectionPolicy', 'storageLocalDiskConfigPolicy', 'sysdebugMEpLogPolicy', 'topInfoSyncPolicy', 'trigTest', 'uuidpoolPool', 'vmLifeCyclePolicy', 'vnicDynamicConPolicy', 'vnicFcGroupTempl', 'vnicIScsiInitAutoConfigPolicy', 'vnicLanConnPolicy', 'vnicLanConnTempl', 'vnicSanConnPolicy', 'vnicSanConnTempl', 'vnicSriovHpnConPolicy', 'vnicUsnicConPolicy', 'vnicVhbaBehPolicy', 'vnicVmqConPolicy', 'vnicVnicBehPolicy'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4", "5", "root"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "perm_access": MoPropertyMeta("perm_access", "permAccess", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "level": "level", 
        "name": "name", 
        "permAccess": "perm_access", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.level = None
        self.perm_access = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "OrgOrg", parent_mo_or_dn, **kwargs)
