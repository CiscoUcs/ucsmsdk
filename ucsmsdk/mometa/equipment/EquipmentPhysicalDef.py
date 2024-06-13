"""This module contains the general information for EquipmentPhysicalDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPhysicalDefConsts:
    DEPTH_NOT_APPLICABLE = "not-applicable"
    HEIGHT_NOT_APPLICABLE = "not-applicable"
    INT_ID_NONE = "none"
    MAXIMUM_POWER_NOT_APPLICABLE = "not-applicable"
    MAXIMUM_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
    MINIMUM_POWER_NOT_APPLICABLE = "not-applicable"
    MINIMUM_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
    NOMINAL_POWER_NOT_APPLICABLE = "not-applicable"
    NOMINAL_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    WEIGHT_NOT_APPLICABLE = "not-applicable"
    WIDTH_NOT_APPLICABLE = "not-applicable"


class EquipmentPhysicalDef(ManagedObject):
    """This is EquipmentPhysicalDef class."""

    consts = EquipmentPhysicalDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentPhysicalDef", "equipmentPhysicalDef", "physical", VersionMeta.Version101e, "InputOutput", 0xff, [], [""], ['adaptorFruCapProvider', 'diagSrvCapProvider', 'equipmentBaseBoardCapProvider', 'equipmentBladeBiosCapProvider', 'equipmentBladeCapProvider', 'equipmentCatalogCapProvider', 'equipmentChassisCapProvider', 'equipmentCoprocessorUnitCapProvider', 'equipmentCpldCapProvider', 'equipmentCrossFabricModuleCapProvider', 'equipmentDbgPluginCapProvider', 'equipmentFanModuleCapProvider', 'equipmentFexCapProvider', 'equipmentGemCapProvider', 'equipmentGraphicsCardCapProvider', 'equipmentHostIfCapProvider', 'equipmentIOCardCapProvider', 'equipmentIOExpanderCapProvider', 'equipmentIntelAmcCapProvider', 'equipmentLocalDiskCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentMemoryUnitCapProvider', 'equipmentMgmtCapProvider', 'equipmentMgmtExtCapProvider', 'equipmentMiniStorageCapProvider', 'equipmentPciSwitchCapProvider', 'equipmentPcieConnectorCapProvider', 'equipmentPcieNodeCapProvider', 'equipmentPersistentMemoryUnitCapProvider', 'equipmentProcessorUnitCapProvider', 'equipmentPsuCapProvider', 'equipmentRackEnclosureCapProvider', 'equipmentRackUnitCapProvider', 'equipmentRetimerCapProvider', 'equipmentSecurityUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSiocCapProvider', 'equipmentStorageEncCapProvider', 'equipmentStorageNvmeSwitchCapProvider', 'equipmentStorageSasExpanderCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider', 'equipmentTpmCapProvider', 'equipmentUbmCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "depth": MoPropertyMeta("depth", "depth", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "height": MoPropertyMeta("height", "height", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "maximum_power": MoPropertyMeta("maximum_power", "maximumPower", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "maximum_temperature": MoPropertyMeta("maximum_temperature", "maximumTemperature", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "minimum_power": MoPropertyMeta("minimum_power", "minimumPower", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "minimum_temperature": MoPropertyMeta("minimum_temperature", "minimumTemperature", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "nominal_power": MoPropertyMeta("nominal_power", "nominalPower", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "nominal_temperature": MoPropertyMeta("nominal_temperature", "nominalTemperature", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "operating_voltages": MoPropertyMeta("operating_voltages", "operatingVoltages", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "weight": MoPropertyMeta("weight", "weight", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "width": MoPropertyMeta("width", "width", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "depth": "depth", 
        "descr": "descr", 
        "dn": "dn", 
        "height": "height", 
        "intId": "int_id", 
        "maximumPower": "maximum_power", 
        "maximumTemperature": "maximum_temperature", 
        "minimumPower": "minimum_power", 
        "minimumTemperature": "minimum_temperature", 
        "name": "name", 
        "nominalPower": "nominal_power", 
        "nominalTemperature": "nominal_temperature", 
        "operatingVoltages": "operating_voltages", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "weight": "weight", 
        "width": "width", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.depth = None
        self.descr = None
        self.height = None
        self.int_id = None
        self.maximum_power = None
        self.maximum_temperature = None
        self.minimum_power = None
        self.minimum_temperature = None
        self.name = None
        self.nominal_power = None
        self.nominal_temperature = None
        self.operating_voltages = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.weight = None
        self.width = None

        ManagedObject.__init__(self, "EquipmentPhysicalDef", parent_mo_or_dn, **kwargs)
