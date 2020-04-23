"""This module contains the general information for ApeSdr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeSdrConsts:
    EVENT_READING_TYPE_DISCRETE_ACPI_POWER = "DISCRETE_ACPI_POWER"
    EVENT_READING_TYPE_DISCRETE_AVAILABILITY = "DISCRETE_AVAILABILITY"
    EVENT_READING_TYPE_DISCRETE_DEVICE_ENABLE = "DISCRETE_DEVICE_ENABLE"
    EVENT_READING_TYPE_DISCRETE_DEVICE_PRESENCE = "DISCRETE_DEVICE_PRESENCE"
    EVENT_READING_TYPE_DISCRETE_LIMIT_EXCEEDED = "DISCRETE_LIMIT_EXCEEDED"
    EVENT_READING_TYPE_DISCRETE_PERFORMANCE_MET = "DISCRETE_PERFORMANCE_MET"
    EVENT_READING_TYPE_DISCRETE_PREDICTIVE_FAILURE = "DISCRETE_PREDICTIVE_FAILURE"
    EVENT_READING_TYPE_DISCRETE_REDUNDANCY = "DISCRETE_REDUNDANCY"
    EVENT_READING_TYPE_DISCRETE_SEVERITY = "DISCRETE_SEVERITY"
    EVENT_READING_TYPE_DISCRETE_STATE = "DISCRETE_STATE"
    EVENT_READING_TYPE_DISCRETE_USAGE = "DISCRETE_USAGE"
    EVENT_READING_TYPE_OEM1 = "OEM1"
    EVENT_READING_TYPE_SENSOR_SPECIFIC = "SENSOR_SPECIFIC"
    EVENT_READING_TYPE_THRESHOLD = "THRESHOLD"
    EVENT_READING_TYPE_UNKNOWN = "UNKNOWN"
    INSTANCE_ADD_IN_CARD = "ADD_IN_CARD"
    INSTANCE_BATTERY = "BATTERY"
    INSTANCE_BOOT_ERROR = "BOOT_ERROR"
    INSTANCE_BUTTON = "BUTTON"
    INSTANCE_CABLE_INTERCONNECT = "CABLE_INTERCONNECT"
    INSTANCE_CHASSIS = "CHASSIS"
    INSTANCE_CHIP_SET = "CHIP_SET"
    INSTANCE_COOLING_DEVICE = "COOLING_DEVICE"
    INSTANCE_CRITICAL_INTERRUPT = "CRITICAL_INTERRUPT"
    INSTANCE_CURRENT = "CURRENT"
    INSTANCE_DRIVE_SLOT = "DRIVE_SLOT"
    INSTANCE_ENTITY_PRESENCE = "ENTITY_PRESENCE"
    INSTANCE_EVENT_LOGGING_DISABLED = "EVENT_LOGGING_DISABLED"
    INSTANCE_FAN = "FAN"
    INSTANCE_FRU_STATE = "FRU_STATE"
    INSTANCE_LAN = "LAN"
    INSTANCE_MANAGEMENT_SUBSYSTEM_HEALTH = "MANAGEMENT_SUBSYSTEM_HEALTH"
    INSTANCE_MEMORY = "MEMORY"
    INSTANCE_MICROCONTROLLER_COPROCESSOR = "MICROCONTROLLER_COPROCESSOR"
    INSTANCE_MODULE_BOARD = "MODULE_BOARD"
    INSTANCE_MONITOR_ASIC_IC = "MONITOR_ASIC_IC"
    INSTANCE_OEM1 = "OEM1"
    INSTANCE_OEM2 = "OEM2"
    INSTANCE_OEM3 = "OEM3"
    INSTANCE_OEM4 = "OEM4"
    INSTANCE_OEM5 = "OEM5"
    INSTANCE_OEM7 = "OEM7"
    INSTANCE_OS_BOOT = "OS_BOOT"
    INSTANCE_OS_CRITICAL_STOP = "OS_CRITICAL_STOP"
    INSTANCE_OTHER_FRU = "OTHER_FRU"
    INSTANCE_OTHER_UNITS_BASED_SENSOR = "OTHER_UNITS_BASED_SENSOR"
    INSTANCE_PHYSICAL_SECURITY = "PHYSICAL_SECURITY"
    INSTANCE_PLATFORM_ALERT = "PLATFORM_ALERT"
    INSTANCE_PLATFORM_SECURITY = "PLATFORM_SECURITY"
    INSTANCE_POWER_MEMORY_RESIZE = "POWER_MEMORY_RESIZE"
    INSTANCE_POWER_SUPPLY = "POWER_SUPPLY"
    INSTANCE_POWER_UNIT = "POWER_UNIT"
    INSTANCE_PROCESSOR = "PROCESSOR"
    INSTANCE_SESSION_AUDIT = "SESSION_AUDIT"
    INSTANCE_SLOT_CONNECTOR = "SLOT_CONNECTOR"
    INSTANCE_SYSTEM_ACPI_POWER_STATE = "SYSTEM_ACPI_POWER_STATE"
    INSTANCE_SYSTEM_BOOT_INITIATED = "SYSTEM_BOOT_INITIATED"
    INSTANCE_SYSTEM_EVENT = "SYSTEM_EVENT"
    INSTANCE_SYSTEM_FIRMWARE_PROGRESS = "SYSTEM_FIRMWARE_PROGRESS"
    INSTANCE_TEMPERATURE = "TEMPERATURE"
    INSTANCE_TERMINATOR = "TERMINATOR"
    INSTANCE_UNKNOWN = "UNKNOWN"
    INSTANCE_VERSION_CHANGE = "VERSION_CHANGE"
    INSTANCE_VOLTAGE = "VOLTAGE"
    INSTANCE_WATCHDOG_1 = "WATCHDOG_1"
    INSTANCE_WATCHDOG_2 = "WATCHDOG_2"
    SDR_TYPE_COMPACT_SENSOR_RECORD = "COMPACT_SENSOR_RECORD"
    SDR_TYPE_FULL_SENSOR_RECORD = "FULL_SENSOR_RECORD"
    SDR_TYPE_UNKNOWN_RECORD = "UNKNOWN_RECORD"
    UNITS_AMPS = "AMPS"
    UNITS_BECQUERELS = "BECQUERELS"
    UNITS_BITS = "BITS"
    UNITS_BYTES = "BYTES"
    UNITS_CANDELA = "CANDELA"
    UNITS_CENTIMETERS = "CENTIMETERS"
    UNITS_CFM = "CFM"
    UNITS_CHARACTERS = "CHARACTERS"
    UNITS_COLLISIONS = "COLLISIONS"
    UNITS_COLOR_TEMP_DEG_K = "COLOR_TEMP_DEG_K"
    UNITS_CORRECTABLE_ERRORS = "CORRECTABLE_ERRORS"
    UNITS_COULOMBS = "COULOMBS"
    UNITS_CUBIC_CENTIMETERS = "CUBIC_CENTIMETERS"
    UNITS_CUBIC_FEET = "CUBIC_FEET"
    UNITS_CUBIC_INCHS = "CUBIC_INCHS"
    UNITS_CUBIC_METERS = "CUBIC_METERS"
    UNITS_CYCLES = "CYCLES"
    UNITS_DAY = "DAY"
    UNITS_DECIBELS = "DECIBELS"
    UNITS_DEGREES_C = "DEGREES_C"
    UNITS_DEGREES_F = "DEGREES_F"
    UNITS_DEGREES_K = "DEGREES_K"
    UNITS_DWORDS = "DWORDS"
    UNITS_DB_A = "DbA"
    UNITS_DB_C = "DbC"
    UNITS_ERRORS = "ERRORS"
    UNITS_FARADS = "FARADS"
    UNITS_FATAL_ERRORS = "FATAL_ERRORS"
    UNITS_FEET = "FEET"
    UNITS_FL_OZ = "FL_OZ"
    UNITS_FOOT_POUNDS = "FOOT_POUNDS"
    UNITS_GAUSS = "GAUSS"
    UNITS_GBITS = "GBITS"
    UNITS_GBYTES = "GBYTES"
    UNITS_GILBERTS = "GILBERTS"
    UNITS_GRAMS = "GRAMS"
    UNITS_GRAVITIES = "GRAVITIES"
    UNITS_GRAYS = "GRAYS"
    UNITS_HENRIES = "HENRIES"
    UNITS_HITS = "HITS"
    UNITS_HOUR = "HOUR"
    UNITS_HZ = "HZ"
    UNITS_INCHES = "INCHES"
    UNITS_JOULES = "JOULES"
    UNITS_KBITS = "KBITS"
    UNITS_KBYTES = "KBYTES"
    UNITS_KPA = "KPA"
    UNITS_LINES = "LINES"
    UNITS_LITERS = "LITERS"
    UNITS_LUMENS = "LUMENS"
    UNITS_LUX = "LUX"
    UNITS_MBITS = "MBITS"
    UNITS_MBYTES = "MBYTES"
    UNITS_MESSAGES = "MESSAGES"
    UNITS_METERS = "METERS"
    UNITS_MHENRIES = "MHENRIES"
    UNITS_MIL = "MIL"
    UNITS_MILLIMETERS = "MILLIMETERS"
    UNITS_MINUTE = "MINUTE"
    UNITS_MISSES = "MISSES"
    UNITS_MOLES = "MOLES"
    UNITS_MSECONDS = "MSECONDS"
    UNITS_NEWTONS = "NEWTONS"
    UNITS_NITS = "NITS"
    UNITS_OHMS = "OHMS"
    UNITS_OUNCES = "OUNCES"
    UNITS_OUNCE_INCHES = "OUNCE_INCHES"
    UNITS_OVERRUNS = "OVERRUNS"
    UNITS_PACKETS = "PACKETS"
    UNITS_POUNDS = "POUNDS"
    UNITS_PPM = "PPM"
    UNITS_PSI = "PSI"
    UNITS_QWORDS = "QWORDS"
    UNITS_RADIANS = "RADIANS"
    UNITS_RESETS = "RESETS"
    UNITS_RETRIES = "RETRIES"
    UNITS_REVOLUTIONS = "REVOLUTIONS"
    UNITS_RPM = "RPM"
    UNITS_SECONDS = "SECONDS"
    UNITS_SERADIANS = "SERADIANS"
    UNITS_SIEMENS = "SIEMENS"
    UNITS_SIEVERTS = "SIEVERTS"
    UNITS_UFARADS = "UFARADS"
    UNITS_UNCORRECTABLE_ERRORS = "UNCORRECTABLE_ERRORS"
    UNITS_UNDERRUNS = "UNDERRUNS"
    UNITS_UNSPECIFIED = "UNSPECIFIED"
    UNITS_USECONDS = "USECONDS"
    UNITS_VA = "VA"
    UNITS_VOLTS = "VOLTS"
    UNITS_WATTS = "WATTS"
    UNITS_WEEK = "WEEK"
    UNITS_WORDS = "WORDS"
    UNITS_RESERVED1 = "reserved1"


class ApeSdr(ManagedObject):
    """This is ApeSdr class."""

    consts = ApeSdrConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ApeSdr", "apeSdr", "sdr-[id]", VersionMeta.Version101e, "InputOutput", 0x3fff, [], ["read-only"], ['apeMcTable'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "entity_type": MoPropertyMeta("entity_type", "entityType", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "event_reading_type": MoPropertyMeta("event_reading_type", "eventReadingType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["DISCRETE_ACPI_POWER", "DISCRETE_AVAILABILITY", "DISCRETE_DEVICE_ENABLE", "DISCRETE_DEVICE_PRESENCE", "DISCRETE_LIMIT_EXCEEDED", "DISCRETE_PERFORMANCE_MET", "DISCRETE_PREDICTIVE_FAILURE", "DISCRETE_REDUNDANCY", "DISCRETE_SEVERITY", "DISCRETE_STATE", "DISCRETE_USAGE", "OEM1", "SENSOR_SPECIFIC", "THRESHOLD", "UNKNOWN"], ["0-65535"]),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []),
        "instance": MoPropertyMeta("instance", "instance", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["ADD_IN_CARD", "BATTERY", "BOOT_ERROR", "BUTTON", "CABLE_INTERCONNECT", "CHASSIS", "CHIP_SET", "COOLING_DEVICE", "CRITICAL_INTERRUPT", "CURRENT", "DRIVE_SLOT", "ENTITY_PRESENCE", "EVENT_LOGGING_DISABLED", "FAN", "FRU_STATE", "LAN", "MANAGEMENT_SUBSYSTEM_HEALTH", "MEMORY", "MICROCONTROLLER_COPROCESSOR", "MODULE_BOARD", "MONITOR_ASIC_IC", "OEM1", "OEM2", "OEM3", "OEM4", "OEM5", "OEM7", "OS_BOOT", "OS_CRITICAL_STOP", "OTHER_FRU", "OTHER_UNITS_BASED_SENSOR", "PHYSICAL_SECURITY", "PLATFORM_ALERT", "PLATFORM_SECURITY", "POWER_MEMORY_RESIZE", "POWER_SUPPLY", "POWER_UNIT", "PROCESSOR", "SESSION_AUDIT", "SLOT_CONNECTOR", "SYSTEM_ACPI_POWER_STATE", "SYSTEM_BOOT_INITIATED", "SYSTEM_EVENT", "SYSTEM_FIRMWARE_PROGRESS", "TEMPERATURE", "TERMINATOR", "UNKNOWN", "VERSION_CHANGE", "VOLTAGE", "WATCHDOG_1", "WATCHDOG_2"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sdr_type": MoPropertyMeta("sdr_type", "sdr_type", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["COMPACT_SENSOR_RECORD", "FULL_SENSOR_RECORD", "UNKNOWN_RECORD"], []),
        "sensor_id": MoPropertyMeta("sensor_id", "sensorId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []),
        "sensor_type": MoPropertyMeta("sensor_type", "sensor_type", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "units": MoPropertyMeta("units", "units", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["AMPS", "BECQUERELS", "BITS", "BYTES", "CANDELA", "CENTIMETERS", "CFM", "CHARACTERS", "COLLISIONS", "COLOR_TEMP_DEG_K", "CORRECTABLE_ERRORS", "COULOMBS", "CUBIC_CENTIMETERS", "CUBIC_FEET", "CUBIC_INCHS", "CUBIC_METERS", "CYCLES", "DAY", "DECIBELS", "DEGREES_C", "DEGREES_F", "DEGREES_K", "DWORDS", "DbA", "DbC", "ERRORS", "FARADS", "FATAL_ERRORS", "FEET", "FL_OZ", "FOOT_POUNDS", "GAUSS", "GBITS", "GBYTES", "GILBERTS", "GRAMS", "GRAVITIES", "GRAYS", "HENRIES", "HITS", "HOUR", "HZ", "INCHES", "JOULES", "KBITS", "KBYTES", "KPA", "LINES", "LITERS", "LUMENS", "LUX", "MBITS", "MBYTES", "MESSAGES", "METERS", "MHENRIES", "MIL", "MILLIMETERS", "MINUTE", "MISSES", "MOLES", "MSECONDS", "NEWTONS", "NITS", "OHMS", "OUNCES", "OUNCE_INCHES", "OVERRUNS", "PACKETS", "POUNDS", "PPM", "PSI", "QWORDS", "RADIANS", "RESETS", "RETRIES", "REVOLUTIONS", "RPM", "SECONDS", "SERADIANS", "SIEMENS", "SIEVERTS", "UFARADS", "UNCORRECTABLE_ERRORS", "UNDERRUNS", "UNSPECIFIED", "USECONDS", "VA", "VOLTS", "WATTS", "WEEK", "WORDS", "reserved1"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "entityType": "entity_type", 
        "eventReadingType": "event_reading_type", 
        "id": "id", 
        "instance": "instance", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sdr_type": "sdr_type", 
        "sensorId": "sensor_id", 
        "sensor_type": "sensor_type", 
        "status": "status", 
        "units": "units", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.entity_type = None
        self.event_reading_type = None
        self.instance = None
        self.name = None
        self.sacl = None
        self.sdr_type = None
        self.sensor_id = None
        self.sensor_type = None
        self.status = None
        self.units = None

        ManagedObject.__init__(self, "ApeSdr", parent_mo_or_dn, **kwargs)
