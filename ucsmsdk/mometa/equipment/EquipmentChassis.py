"""This module contains the general information for EquipmentChassis ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentChassisConsts:
    ACK_PROGRESS_INDICATOR_ACK_IN_PROGRESS = "ack-in-progress"
    ACK_PROGRESS_INDICATOR_ACK_NOT_IN_PROGRESS = "ack-not-in-progress"
    ADMIN_STATE_ACKNOWLEDGED = "acknowledged"
    ADMIN_STATE_AUTO_ACKNOWLEDGE = "auto-acknowledge"
    ADMIN_STATE_DECOMMISSION = "decommission"
    ADMIN_STATE_DISABLE_PORT_CHANNEL = "disable-port-channel"
    ADMIN_STATE_ENABLE_PORT_CHANNEL = "enable-port-channel"
    ADMIN_STATE_RE_ACKNOWLEDGE = "re-acknowledge"
    ADMIN_STATE_REMOVE = "remove"
    ASSOCIATION_ASSOCIATED = "associated"
    ASSOCIATION_ESTABLISHING = "establishing"
    ASSOCIATION_FAILED = "failed"
    ASSOCIATION_NONE = "none"
    ASSOCIATION_REMOVING = "removing"
    ASSOCIATION_THROTTLED = "throttled"
    AVAILABILITY_AVAILABLE = "available"
    AVAILABILITY_UNAVAILABLE = "unavailable"
    CONFIG_STATE_ACK_IN_PROGRESS = "ack-in-progress"
    CONFIG_STATE_ACKNOWLEDGED = "acknowledged"
    CONFIG_STATE_AUTO_ACK = "auto-ack"
    CONFIG_STATE_EVALUATION = "evaluation"
    CONFIG_STATE_OK = "ok"
    CONFIG_STATE_REMOVING = "removing"
    CONFIG_STATE_UN_ACKNOWLEDGED = "un-acknowledged"
    CONFIG_STATE_UN_INITIALIZED = "un-initialized"
    CONFIG_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    DISCOVERY_COMPLETE = "complete"
    DISCOVERY_FAILED = "failed"
    DISCOVERY_FRU_IDENTITY_INDETERMINATE = "fru-identity-indeterminate"
    DISCOVERY_FRU_NOT_READY = "fru-not-ready"
    DISCOVERY_FRU_STATE_INDETERMINATE = "fru-state-indeterminate"
    DISCOVERY_ILLEGAL_FRU = "illegal-fru"
    DISCOVERY_IN_PROGRESS = "in-progress"
    DISCOVERY_INSUFFICIENTLY_EQUIPPED = "insufficiently-equipped"
    DISCOVERY_INVALID_ADAPTOR_IOCARD = "invalid-adaptor-iocard"
    DISCOVERY_MALFORMED_FRU_INFO = "malformed-fru-info"
    DISCOVERY_RETRY = "retry"
    DISCOVERY_THROTTLED = "throttled"
    DISCOVERY_UNDISCOVERED = "undiscovered"
    FAN_SPEED_CONFIG_STATE_ACOUSTIC = "Acoustic"
    FAN_SPEED_CONFIG_STATE_BALANCED = "Balanced"
    FAN_SPEED_CONFIG_STATE_HIGH_POWER = "High Power"
    FAN_SPEED_CONFIG_STATE_LOW_POWER = "Low Power"
    FAN_SPEED_CONFIG_STATE_MAX_POWER = "Max Power"
    FAN_SPEED_CONFIG_STATE_PERFORMANCE = "Performance"
    FSM_PREV_ASSOCIATE_ACTIVATE_ADAPTOR = "AssociateActivateAdaptor"
    FSM_PREV_ASSOCIATE_ACTIVATE_BRD_CTLR = "AssociateActivateBrdCtlr"
    FSM_PREV_ASSOCIATE_ACTIVATE_CMC = "AssociateActivateCmc"
    FSM_PREV_ASSOCIATE_ACTIVATE_LOCAL_DISK = "AssociateActivateLocalDisk"
    FSM_PREV_ASSOCIATE_ACTIVATE_SAS_EXPANDER = "AssociateActivateSasExpander"
    FSM_PREV_ASSOCIATE_ACTIVATE_STORAGE_CTLR = "AssociateActivateStorageCtlr"
    FSM_PREV_ASSOCIATE_BEGIN = "AssociateBegin"
    FSM_PREV_ASSOCIATE_CHASSIS_PEER_ADAPTER_REBOOT = "AssociateChassisPeerAdapterReboot"
    FSM_PREV_ASSOCIATE_CONFIG_CHASSIS_ADAPTER_CONNECTIVITY = "AssociateConfigChassisAdapterConnectivity"
    FSM_PREV_ASSOCIATE_COPY_REMOTE = "AssociateCopyRemote"
    FSM_PREV_ASSOCIATE_DELETE_CURL_DOWNLOADED_IMAGES = "AssociateDeleteCurlDownloadedImages"
    FSM_PREV_ASSOCIATE_DELETE_IMAGES_REMOTE = "AssociateDeleteImagesRemote"
    FSM_PREV_ASSOCIATE_DISK_ZONING_CONFIG = "AssociateDiskZoningConfig"
    FSM_PREV_ASSOCIATE_DOWNLOAD_IMAGES = "AssociateDownloadImages"
    FSM_PREV_ASSOCIATE_FAIL = "AssociateFail"
    FSM_PREV_ASSOCIATE_POLL_ADAPTOR_ACTIVATION = "AssociatePollAdaptorActivation"
    FSM_PREV_ASSOCIATE_POLL_BRD_CTLR_ACTIVATION = "AssociatePollBrdCtlrActivation"
    FSM_PREV_ASSOCIATE_POLL_CMC_ACTIVATION = "AssociatePollCmcActivation"
    FSM_PREV_ASSOCIATE_POLL_POST_DISK_ZONE_STORAGE_INV_CIMC = "AssociatePollPostDiskZoneStorageInvCIMC"
    FSM_PREV_ASSOCIATE_POLL_SAS_EXPANDER_ACTIVATE = "AssociatePollSasExpanderActivate"
    FSM_PREV_ASSOCIATE_POLL_SAS_EXPANDER_CONFIG = "AssociatePollSasExpanderConfig"
    FSM_PREV_ASSOCIATE_POLL_STORAGE_CTLR_ACTIVATION = "AssociatePollStorageCtlrActivation"
    FSM_PREV_ASSOCIATE_POLL_UPDATE_ADAPTOR = "AssociatePollUpdateAdaptor"
    FSM_PREV_ASSOCIATE_POLL_UPDATE_CMC = "AssociatePollUpdateCmc"
    FSM_PREV_ASSOCIATE_POLL_UPDATE_SAS_EXPANDER = "AssociatePollUpdateSasExpander"
    FSM_PREV_ASSOCIATE_POST_DISK_ZONE_STORAGE_INV_CIMC = "AssociatePostDiskZoneStorageInvCIMC"
    FSM_PREV_ASSOCIATE_POST_DISK_ZONE_STORAGE_INV_CMC = "AssociatePostDiskZoneStorageInvCMC"
    FSM_PREV_ASSOCIATE_POWER_OFF_SERVERS = "AssociatePowerOffServers"
    FSM_PREV_ASSOCIATE_POWER_ON_SERVERS = "AssociatePowerOnServers"
    FSM_PREV_ASSOCIATE_SAS_EXPANDER_CONFIG = "AssociateSasExpanderConfig"
    FSM_PREV_ASSOCIATE_SUCCESS = "AssociateSuccess"
    FSM_PREV_ASSOCIATE_UNLOCK_FIRMWARE_IMAGE = "AssociateUnlockFirmwareImage"
    FSM_PREV_ASSOCIATE_UPDATE_ADAPTOR = "AssociateUpdateAdaptor"
    FSM_PREV_ASSOCIATE_UPDATE_CMC = "AssociateUpdateCmc"
    FSM_PREV_ASSOCIATE_UPDATE_SAS_EXPANDER = "AssociateUpdateSasExpander"
    FSM_PREV_ASSOCIATE_WAIT_BEFORE_INSTALLATION = "AssociateWaitBeforeInstallation"
    FSM_PREV_ASSOCIATE_WAIT_FOR_POWER_OFF = "AssociateWaitForPowerOff"
    FSM_PREV_CHASSIS_UPGRADE_ACTIVATE_ADAPTOR = "ChassisUpgradeActivateAdaptor"
    FSM_PREV_CHASSIS_UPGRADE_ACTIVATE_BRD_CTLR = "ChassisUpgradeActivateBrdCtlr"
    FSM_PREV_CHASSIS_UPGRADE_ACTIVATE_CMC = "ChassisUpgradeActivateCmc"
    FSM_PREV_CHASSIS_UPGRADE_ACTIVATE_LOCAL_DISK = "ChassisUpgradeActivateLocalDisk"
    FSM_PREV_CHASSIS_UPGRADE_ACTIVATE_SAS_EXPANDER = "ChassisUpgradeActivateSasExpander"
    FSM_PREV_CHASSIS_UPGRADE_ACTIVATE_STORAGE_CTLR = "ChassisUpgradeActivateStorageCtlr"
    FSM_PREV_CHASSIS_UPGRADE_BEGIN = "ChassisUpgradeBegin"
    FSM_PREV_CHASSIS_UPGRADE_FAIL = "ChassisUpgradeFail"
    FSM_PREV_CHASSIS_UPGRADE_POLL_ADAPTOR_ACTIVATION = "ChassisUpgradePollAdaptorActivation"
    FSM_PREV_CHASSIS_UPGRADE_POLL_BRD_CTLR_ACTIVATION = "ChassisUpgradePollBrdCtlrActivation"
    FSM_PREV_CHASSIS_UPGRADE_POLL_CMC_ACTIVATION = "ChassisUpgradePollCmcActivation"
    FSM_PREV_CHASSIS_UPGRADE_POLL_LOCAL_DISK_ACTIVATE = "ChassisUpgradePollLocalDiskActivate"
    FSM_PREV_CHASSIS_UPGRADE_POLL_SAS_EXPANDER_ACTIVATE = "ChassisUpgradePollSasExpanderActivate"
    FSM_PREV_CHASSIS_UPGRADE_POLL_STORAGE_CTLR_ACTIVATION = "ChassisUpgradePollStorageCtlrActivation"
    FSM_PREV_CHASSIS_UPGRADE_POLL_UPDATE_STATUS = "ChassisUpgradePollUpdateStatus"
    FSM_PREV_CHASSIS_UPGRADE_POWER_OFF_SERVERS = "ChassisUpgradePowerOffServers"
    FSM_PREV_CHASSIS_UPGRADE_POWER_ON_SERVERS = "ChassisUpgradePowerOnServers"
    FSM_PREV_CHASSIS_UPGRADE_RESET_SAS_EXPANDER = "ChassisUpgradeResetSasExpander"
    FSM_PREV_CHASSIS_UPGRADE_SUCCESS = "ChassisUpgradeSuccess"
    FSM_PREV_CHASSIS_UPGRADE_UPDATE_REQUEST = "ChassisUpgradeUpdateRequest"
    FSM_PREV_CHASSIS_UPGRADE_WAIT_FOR_POWER_OFF = "ChassisUpgradeWaitForPowerOff"
    FSM_PREV_DISASSOCIATE_BEGIN = "DisassociateBegin"
    FSM_PREV_DISASSOCIATE_COMPLETE = "DisassociateComplete"
    FSM_PREV_DISASSOCIATE_FAIL = "DisassociateFail"
    FSM_PREV_DISASSOCIATE_SUCCESS = "DisassociateSuccess"
    FSM_PREV_DYNAMIC_REALLOCATION_BEGIN = "DynamicReallocationBegin"
    FSM_PREV_DYNAMIC_REALLOCATION_CONFIG = "DynamicReallocationConfig"
    FSM_PREV_DYNAMIC_REALLOCATION_FAIL = "DynamicReallocationFail"
    FSM_PREV_DYNAMIC_REALLOCATION_SUCCESS = "DynamicReallocationSuccess"
    FSM_PREV_FAN_POLICY_CONFIG_BEGIN = "FanPolicyConfigBegin"
    FSM_PREV_FAN_POLICY_CONFIG_EXECUTE = "FanPolicyConfigExecute"
    FSM_PREV_FAN_POLICY_CONFIG_FAIL = "FanPolicyConfigFail"
    FSM_PREV_FAN_POLICY_CONFIG_SUCCESS = "FanPolicyConfigSuccess"
    FSM_PREV_FW_UPGRADE_BEGIN = "FwUpgradeBegin"
    FSM_PREV_FW_UPGRADE_COPY_REMOTE = "FwUpgradeCopyRemote"
    FSM_PREV_FW_UPGRADE_DELETE_CURL_DOWNLOADED_IMAGES = "FwUpgradeDeleteCurlDownloadedImages"
    FSM_PREV_FW_UPGRADE_DELETE_IMAGES_REMOTE = "FwUpgradeDeleteImagesRemote"
    FSM_PREV_FW_UPGRADE_DOWNLOAD_IMAGES = "FwUpgradeDownloadImages"
    FSM_PREV_FW_UPGRADE_FAIL = "FwUpgradeFail"
    FSM_PREV_FW_UPGRADE_POLL_UPDATE_ADAPTOR = "FwUpgradePollUpdateAdaptor"
    FSM_PREV_FW_UPGRADE_POLL_UPDATE_CMC = "FwUpgradePollUpdateCmc"
    FSM_PREV_FW_UPGRADE_POLL_UPDATE_SAS_EXPANDER = "FwUpgradePollUpdateSasExpander"
    FSM_PREV_FW_UPGRADE_SUCCESS = "FwUpgradeSuccess"
    FSM_PREV_FW_UPGRADE_UNLOCK_FIRMWARE_IMAGE = "FwUpgradeUnlockFirmwareImage"
    FSM_PREV_FW_UPGRADE_UPDATE_ADAPTOR = "FwUpgradeUpdateAdaptor"
    FSM_PREV_FW_UPGRADE_UPDATE_CMC = "FwUpgradeUpdateCmc"
    FSM_PREV_FW_UPGRADE_UPDATE_SAS_EXPANDER = "FwUpgradeUpdateSasExpander"
    FSM_PREV_FW_UPGRADE_WAIT_BEFORE_INSTALLATION = "FwUpgradeWaitBeforeInstallation"
    FSM_PREV_OOB_STORAGE_ADMIN_CFG_BEGIN = "OobStorageAdminCfgBegin"
    FSM_PREV_OOB_STORAGE_ADMIN_CFG_FAIL = "OobStorageAdminCfgFail"
    FSM_PREV_OOB_STORAGE_ADMIN_CFG_OOB_STORAGE_CONFIG = "OobStorageAdminCfgOobStorageConfig"
    FSM_PREV_OOB_STORAGE_ADMIN_CFG_OOB_STORAGE_INVENTORY = "OobStorageAdminCfgOobStorageInventory"
    FSM_PREV_OOB_STORAGE_ADMIN_CFG_SUCCESS = "OobStorageAdminCfgSuccess"
    FSM_PREV_POWER_CAP_BEGIN = "PowerCapBegin"
    FSM_PREV_POWER_CAP_CONFIG = "PowerCapConfig"
    FSM_PREV_POWER_CAP_FAIL = "PowerCapFail"
    FSM_PREV_POWER_CAP_SUCCESS = "PowerCapSuccess"
    FSM_PREV_POWER_CAP_WAIT = "PowerCapWait"
    FSM_PREV_POWER_EXTENDED_POLICY_CONFIG_BEGIN = "PowerExtendedPolicyConfigBegin"
    FSM_PREV_POWER_EXTENDED_POLICY_CONFIG_EXECUTE = "PowerExtendedPolicyConfigExecute"
    FSM_PREV_POWER_EXTENDED_POLICY_CONFIG_FAIL = "PowerExtendedPolicyConfigFail"
    FSM_PREV_POWER_EXTENDED_POLICY_CONFIG_SUCCESS = "PowerExtendedPolicyConfigSuccess"
    FSM_PREV_POWER_SAVE_POLICY_CONFIG_BEGIN = "PowerSavePolicyConfigBegin"
    FSM_PREV_POWER_SAVE_POLICY_CONFIG_EXECUTE = "PowerSavePolicyConfigExecute"
    FSM_PREV_POWER_SAVE_POLICY_CONFIG_FAIL = "PowerSavePolicyConfigFail"
    FSM_PREV_POWER_SAVE_POLICY_CONFIG_SUCCESS = "PowerSavePolicyConfigSuccess"
    FSM_PREV_PSU_POLICY_CONFIG_BEGIN = "PsuPolicyConfigBegin"
    FSM_PREV_PSU_POLICY_CONFIG_EXECUTE = "PsuPolicyConfigExecute"
    FSM_PREV_PSU_POLICY_CONFIG_FAIL = "PsuPolicyConfigFail"
    FSM_PREV_PSU_POLICY_CONFIG_SUCCESS = "PsuPolicyConfigSuccess"
    FSM_PREV_REMOVE_CHASSIS_BEGIN = "RemoveChassisBegin"
    FSM_PREV_REMOVE_CHASSIS_CLEANUP_VNICS_LOCAL = "RemoveChassisCleanupVnicsLocal"
    FSM_PREV_REMOVE_CHASSIS_CLEANUP_VNICS_PEER = "RemoveChassisCleanupVnicsPeer"
    FSM_PREV_REMOVE_CHASSIS_DECOMISSION = "RemoveChassisDecomission"
    FSM_PREV_REMOVE_CHASSIS_DISABLE_END_POINT = "RemoveChassisDisableEndPoint"
    FSM_PREV_REMOVE_CHASSIS_FAIL = "RemoveChassisFail"
    FSM_PREV_REMOVE_CHASSIS_SUCCESS = "RemoveChassisSuccess"
    FSM_PREV_REMOVE_CHASSIS_UN_IDENTIFY_LOCAL = "RemoveChassisUnIdentifyLocal"
    FSM_PREV_REMOVE_CHASSIS_UN_IDENTIFY_PEER = "RemoveChassisUnIdentifyPeer"
    FSM_PREV_REMOVE_CHASSIS_WAIT = "RemoveChassisWait"
    FSM_PREV_NOP = "nop"
    FSM_RMT_INV_ERR_CODE_ERR_2FA_AUTH_RETRY = "ERR-2fa-auth-retry"
    FSM_RMT_INV_ERR_CODE_ERR_ACTIVATE_FAILED = "ERR-ACTIVATE-failed"
    FSM_RMT_INV_ERR_CODE_ERR_ACTIVATE_IN_PROGRESS = "ERR-ACTIVATE-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_ACTIVATE_RETRY = "ERR-ACTIVATE-retry"
    FSM_RMT_INV_ERR_CODE_ERR_BIOS_TOKENS_OLD_BIOS = "ERR-BIOS-TOKENS-OLD-BIOS"
    FSM_RMT_INV_ERR_CODE_ERR_BIOS_TOKENS_OLD_CIMC = "ERR-BIOS-TOKENS-OLD-CIMC"
    FSM_RMT_INV_ERR_CODE_ERR_BIOS_NETWORK_BOOT_ORDER_NOT_FOUND = "ERR-BIOS-network-boot-order-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_BOARDCTRLUPDATE_IGNORE = "ERR-BOARDCTRLUPDATE-ignore"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_CANCELLED = "ERR-DIAG-cancelled"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_FSM_RESTARTED = "ERR-DIAG-fsm-restarted"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_TEST_FAILED = "ERR-DIAG-test-failed"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_AUTHENTICATION_FAILURE = "ERR-DNLD-authentication-failure"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_HOSTKEY_MISMATCH = "ERR-DNLD-hostkey-mismatch"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_INVALID_IMAGE = "ERR-DNLD-invalid-image"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_FILE = "ERR-DNLD-no-file"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_SPACE = "ERR-DNLD-no-space"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_USB_UNMOUNTED = "ERR-DNLD-usb-unmounted"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_DELETE_ERROR = "ERR-DNS-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_GET_ERROR = "ERR-DNS-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_SET_ERROR = "ERR-DNS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_DIAGNOSTICS_IN_PROGRESS = "ERR-Diagnostics-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_DIAGNOSTICS_MEMTEST_IN_PROGRESS = "ERR-Diagnostics-memtest-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_DIAGNOSTICS_NETWORK_IN_PROGRESS = "ERR-Diagnostics-network-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_FILTER_ILLEGAL_FORMAT = "ERR-FILTER-illegal-format"
    FSM_RMT_INV_ERR_CODE_ERR_FSM_NO_SUCH_STATE = "ERR-FSM-no-such-state"
    FSM_RMT_INV_ERR_CODE_ERR_HOST_FRU_IDENTITY_MISMATCH = "ERR-HOST-fru-identity-mismatch"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_SET_ERROR = "ERR-HTTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTPS_SET_ERROR = "ERR-HTTPS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_ANALYZE_RESULTS = "ERR-IBMC-analyze-results"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_CONNECT_ERROR = "ERR-IBMC-connect-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_CONNECTOR_INFO_RETRIEVAL_ERROR = "ERR-IBMC-connector-info-retrieval-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_FRU_RETRIEVAL_ERROR = "ERR-IBMC-fru-retrieval-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_INVALID_END_POINT_CONFIG = "ERR-IBMC-invalid-end-point-config"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_RESULTS_NOT_READY = "ERR-IBMC-results-not-ready"
    FSM_RMT_INV_ERR_CODE_ERR_MAX_SUBSCRIPTIONS_ALLOWED_ERROR = "ERR-MAX-subscriptions-allowed-error"
    FSM_RMT_INV_ERR_CODE_ERR_MO_CONFIG_CHILD_OBJECT_CANT_BE_CONFIGURED = "ERR-MO-CONFIG-child-object-cant-be-configured"
    FSM_RMT_INV_ERR_CODE_ERR_MO_META_NO_SUCH_OBJECT_CLASS = "ERR-MO-META-no-such-object-class"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_NO_SUCH_PROPERTY = "ERR-MO-PROPERTY-no-such-property"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_VALUE_OUT_OF_RANGE = "ERR-MO-PROPERTY-value-out-of-range"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ACCESS_DENIED = "ERR-MO-access-denied"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DELETION_RULE_VIOLATION = "ERR-MO-deletion-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DUPLICATE_OBJECT = "ERR-MO-duplicate-object"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CONTAINMENT = "ERR-MO-illegal-containment"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CREATION = "ERR-MO-illegal-creation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_ITERATOR_STATE = "ERR-MO-illegal-iterator-state"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_OBJECT_LIFECYCLE_TRANSITION = "ERR-MO-illegal-object-lifecycle-transition"
    FSM_RMT_INV_ERR_CODE_ERR_MO_NAMING_RULE_VIOLATION = "ERR-MO-naming-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_OBJECT_NOT_FOUND = "ERR-MO-object-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_MO_RESOURCE_ALLOCATION = "ERR-MO-resource-allocation"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_DELETE_ERROR = "ERR-NTP-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_GET_ERROR = "ERR-NTP-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_SET_ERROR = "ERR-NTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_POWER_CAP_UNSUPPORTED = "ERR-POWER-CAP-UNSUPPORTED"
    FSM_RMT_INV_ERR_CODE_ERR_POWER_PROFILE_IN_PROGRESS = "ERR-POWER-PROFILE-IN-PROGRESS"
    FSM_RMT_INV_ERR_CODE_ERR_SERVER_MIS_CONNECT = "ERR-SERVER-mis-connect"
    FSM_RMT_INV_ERR_CODE_ERR_SWITCH_INVALID_IF_CONFIG = "ERR-SWITCH-invalid-if-config"
    FSM_RMT_INV_ERR_CODE_ERR_TOKEN_REQUEST_DENIED = "ERR-TOKEN-request-denied"
    FSM_RMT_INV_ERR_CODE_ERR_UNABLE_TO_FETCH_BIOS_SETTINGS = "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_FAILED = "ERR-UPDATE-failed"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_IN_PROGRESS = "ERR-UPDATE-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_RETRY = "ERR-UPDATE-retry"
    FSM_RMT_INV_ERR_CODE_ERR_AAA_CONFIG_MODIFY_ERROR = "ERR-aaa-config-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_ACCT_REALM_SET_ERROR = "ERR-acct-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_ADMIN_PASSWD_SET = "ERR-admin-passwd-set"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_ISSUE = "ERR-auth-issue"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_REALM_GET_ERROR = "ERR-auth-realm-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_REALM_SET_ERROR = "ERR-auth-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHENTICATION = "ERR-authentication"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHORIZATION_REQUIRED = "ERR-authorization-required"
    FSM_RMT_INV_ERR_CODE_ERR_CLI_SESSION_LIMIT_REACHED = "ERR-cli-session-limit-reached"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_KEYRING = "ERR-create-keyring"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_LOCALE = "ERR-create-locale"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_ROLE = "ERR-create-role"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_TP = "ERR-create-tp"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_USER = "ERR-create-user"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_LOCALE = "ERR-delete-locale"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_ROLE = "ERR-delete-role"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_SESSION = "ERR-delete-session"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_USER = "ERR-delete-user"
    FSM_RMT_INV_ERR_CODE_ERR_DOWNGRADE_FAIL = "ERR-downgrade-fail"
    FSM_RMT_INV_ERR_CODE_ERR_EFI_DIAGNOSTICS_IN_PROGRESS = "ERR-efi-Diagnostics--in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_ENABLE_MGMT_CONN = "ERR-enable-mgmt-conn"
    FSM_RMT_INV_ERR_CODE_ERR_EP_SET_ERROR = "ERR-ep-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_GET_MAX_HTTP_USER_SESSIONS = "ERR-get-max-http-user-sessions"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_INITIALIZING = "ERR-http-initializing"
    FSM_RMT_INV_ERR_CODE_ERR_INSUFFICIENTLY_EQUIPPED = "ERR-insufficiently-equipped"
    FSM_RMT_INV_ERR_CODE_ERR_INTERNAL_ERROR = "ERR-internal-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_DELETE_ERROR = "ERR-ldap-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GET_ERROR = "ERR-ldap-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_MODIFY_ERROR = "ERR-ldap-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_SET_ERROR = "ERR-ldap-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_SET_ERROR = "ERR-ldap-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LOCALE_SET_ERROR = "ERR-locale-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_MAX_USERID_SESSIONS_REACHED = "ERR-max-userid-sessions-reached"
    FSM_RMT_INV_ERR_CODE_ERR_MISSING_METHOD = "ERR-missing-method"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_LOCALE = "ERR-modify-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_ROLE = "ERR-modify-role"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER = "ERR-modify-user"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_LOCALE = "ERR-modify-user-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_ROLE = "ERR-modify-user-role"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_MODIFY_ERROR = "ERR-provider-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_SET_ERROR = "ERR-provider-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_PWDENC_CONFIG_MASTER_KEY_ERROR = "ERR-pwdenc-config-master-key-error"
    FSM_RMT_INV_ERR_CODE_ERR_PWDENC_DELETE_MASTER_KEY_ERROR = "ERR-pwdenc-delete-master-key-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GET_ERROR = "ERR-radius-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GLOBAL_SET_ERROR = "ERR-radius-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GROUP_SET_ERROR = "ERR-radius-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_SET_ERROR = "ERR-radius-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_REQUEST_TIMEOUT = "ERR-request-timeout"
    FSM_RMT_INV_ERR_CODE_ERR_RESET_ADAPTER = "ERR-reset-adapter"
    FSM_RMT_INV_ERR_CODE_ERR_ROLE_SET_ERROR = "ERR-role-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_SECONDARY_NODE = "ERR-secondary-node"
    FSM_RMT_INV_ERR_CODE_ERR_SERVICE_NOT_READY = "ERR-service-not-ready"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_CACHE_FULL = "ERR-session-cache-full"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_NOT_FOUND = "ERR-session-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_SET_KEY_CERT = "ERR-set-key-cert"
    FSM_RMT_INV_ERR_CODE_ERR_SET_LOGIN_PROFILE = "ERR-set-login-profile"
    FSM_RMT_INV_ERR_CODE_ERR_SET_MIN_PASSPHRASE_LENGTH = "ERR-set-min-passphrase-length"
    FSM_RMT_INV_ERR_CODE_ERR_SET_NETWORK = "ERR-set-network"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PASSWORD_STRENGTH_CHECK = "ERR-set-password-strength-check"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PORT_CHANNEL = "ERR-set-port-channel"
    FSM_RMT_INV_ERR_CODE_ERR_SET_USER = "ERR-set-user"
    FSM_RMT_INV_ERR_CODE_ERR_STORE_PRE_LOGIN_BANNER_MSG = "ERR-store-pre-login-banner-msg"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_ENABLE_ERROR = "ERR-tacacs-enable-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GLOBAL_SET_ERROR = "ERR-tacacs-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GROUP_SET_ERROR = "ERR-tacacs-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_PLUS_GET_ERROR = "ERR-tacacs-plus-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_SET_ERROR = "ERR-tacacs-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TEST_ERROR_1 = "ERR-test-error-1"
    FSM_RMT_INV_ERR_CODE_ERR_TEST_ERROR_2 = "ERR-test-error-2"
    FSM_RMT_INV_ERR_CODE_ERR_TIMEZONE_SET_ERROR = "ERR-timezone-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_USER_ACCOUNT_EXPIRED = "ERR-user-account-expired"
    FSM_RMT_INV_ERR_CODE_ERR_USER_PASSWD_EXPIRED = "ERR-user-passwd-expired"
    FSM_RMT_INV_ERR_CODE_ERR_USER_SET_ERROR = "ERR-user-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_XML_PARSE_ERROR = "ERR-xml-parse-error"
    FSM_RMT_INV_ERR_CODE_NONE = "none"
    FSM_STAMP_NEVER = "never"
    FSM_STATUS_ASSOCIATE_ACTIVATE_ADAPTOR = "AssociateActivateAdaptor"
    FSM_STATUS_ASSOCIATE_ACTIVATE_BRD_CTLR = "AssociateActivateBrdCtlr"
    FSM_STATUS_ASSOCIATE_ACTIVATE_CMC = "AssociateActivateCmc"
    FSM_STATUS_ASSOCIATE_ACTIVATE_LOCAL_DISK = "AssociateActivateLocalDisk"
    FSM_STATUS_ASSOCIATE_ACTIVATE_SAS_EXPANDER = "AssociateActivateSasExpander"
    FSM_STATUS_ASSOCIATE_ACTIVATE_STORAGE_CTLR = "AssociateActivateStorageCtlr"
    FSM_STATUS_ASSOCIATE_BEGIN = "AssociateBegin"
    FSM_STATUS_ASSOCIATE_CHASSIS_PEER_ADAPTER_REBOOT = "AssociateChassisPeerAdapterReboot"
    FSM_STATUS_ASSOCIATE_CONFIG_CHASSIS_ADAPTER_CONNECTIVITY = "AssociateConfigChassisAdapterConnectivity"
    FSM_STATUS_ASSOCIATE_COPY_REMOTE = "AssociateCopyRemote"
    FSM_STATUS_ASSOCIATE_DELETE_CURL_DOWNLOADED_IMAGES = "AssociateDeleteCurlDownloadedImages"
    FSM_STATUS_ASSOCIATE_DELETE_IMAGES_REMOTE = "AssociateDeleteImagesRemote"
    FSM_STATUS_ASSOCIATE_DISK_ZONING_CONFIG = "AssociateDiskZoningConfig"
    FSM_STATUS_ASSOCIATE_DOWNLOAD_IMAGES = "AssociateDownloadImages"
    FSM_STATUS_ASSOCIATE_FAIL = "AssociateFail"
    FSM_STATUS_ASSOCIATE_POLL_ADAPTOR_ACTIVATION = "AssociatePollAdaptorActivation"
    FSM_STATUS_ASSOCIATE_POLL_BRD_CTLR_ACTIVATION = "AssociatePollBrdCtlrActivation"
    FSM_STATUS_ASSOCIATE_POLL_CMC_ACTIVATION = "AssociatePollCmcActivation"
    FSM_STATUS_ASSOCIATE_POLL_POST_DISK_ZONE_STORAGE_INV_CIMC = "AssociatePollPostDiskZoneStorageInvCIMC"
    FSM_STATUS_ASSOCIATE_POLL_SAS_EXPANDER_ACTIVATE = "AssociatePollSasExpanderActivate"
    FSM_STATUS_ASSOCIATE_POLL_SAS_EXPANDER_CONFIG = "AssociatePollSasExpanderConfig"
    FSM_STATUS_ASSOCIATE_POLL_STORAGE_CTLR_ACTIVATION = "AssociatePollStorageCtlrActivation"
    FSM_STATUS_ASSOCIATE_POLL_UPDATE_ADAPTOR = "AssociatePollUpdateAdaptor"
    FSM_STATUS_ASSOCIATE_POLL_UPDATE_CMC = "AssociatePollUpdateCmc"
    FSM_STATUS_ASSOCIATE_POLL_UPDATE_SAS_EXPANDER = "AssociatePollUpdateSasExpander"
    FSM_STATUS_ASSOCIATE_POST_DISK_ZONE_STORAGE_INV_CIMC = "AssociatePostDiskZoneStorageInvCIMC"
    FSM_STATUS_ASSOCIATE_POST_DISK_ZONE_STORAGE_INV_CMC = "AssociatePostDiskZoneStorageInvCMC"
    FSM_STATUS_ASSOCIATE_POWER_OFF_SERVERS = "AssociatePowerOffServers"
    FSM_STATUS_ASSOCIATE_POWER_ON_SERVERS = "AssociatePowerOnServers"
    FSM_STATUS_ASSOCIATE_SAS_EXPANDER_CONFIG = "AssociateSasExpanderConfig"
    FSM_STATUS_ASSOCIATE_SUCCESS = "AssociateSuccess"
    FSM_STATUS_ASSOCIATE_UNLOCK_FIRMWARE_IMAGE = "AssociateUnlockFirmwareImage"
    FSM_STATUS_ASSOCIATE_UPDATE_ADAPTOR = "AssociateUpdateAdaptor"
    FSM_STATUS_ASSOCIATE_UPDATE_CMC = "AssociateUpdateCmc"
    FSM_STATUS_ASSOCIATE_UPDATE_SAS_EXPANDER = "AssociateUpdateSasExpander"
    FSM_STATUS_ASSOCIATE_WAIT_BEFORE_INSTALLATION = "AssociateWaitBeforeInstallation"
    FSM_STATUS_ASSOCIATE_WAIT_FOR_POWER_OFF = "AssociateWaitForPowerOff"
    FSM_STATUS_CHASSIS_UPGRADE_ACTIVATE_ADAPTOR = "ChassisUpgradeActivateAdaptor"
    FSM_STATUS_CHASSIS_UPGRADE_ACTIVATE_BRD_CTLR = "ChassisUpgradeActivateBrdCtlr"
    FSM_STATUS_CHASSIS_UPGRADE_ACTIVATE_CMC = "ChassisUpgradeActivateCmc"
    FSM_STATUS_CHASSIS_UPGRADE_ACTIVATE_LOCAL_DISK = "ChassisUpgradeActivateLocalDisk"
    FSM_STATUS_CHASSIS_UPGRADE_ACTIVATE_SAS_EXPANDER = "ChassisUpgradeActivateSasExpander"
    FSM_STATUS_CHASSIS_UPGRADE_ACTIVATE_STORAGE_CTLR = "ChassisUpgradeActivateStorageCtlr"
    FSM_STATUS_CHASSIS_UPGRADE_BEGIN = "ChassisUpgradeBegin"
    FSM_STATUS_CHASSIS_UPGRADE_FAIL = "ChassisUpgradeFail"
    FSM_STATUS_CHASSIS_UPGRADE_POLL_ADAPTOR_ACTIVATION = "ChassisUpgradePollAdaptorActivation"
    FSM_STATUS_CHASSIS_UPGRADE_POLL_BRD_CTLR_ACTIVATION = "ChassisUpgradePollBrdCtlrActivation"
    FSM_STATUS_CHASSIS_UPGRADE_POLL_CMC_ACTIVATION = "ChassisUpgradePollCmcActivation"
    FSM_STATUS_CHASSIS_UPGRADE_POLL_LOCAL_DISK_ACTIVATE = "ChassisUpgradePollLocalDiskActivate"
    FSM_STATUS_CHASSIS_UPGRADE_POLL_SAS_EXPANDER_ACTIVATE = "ChassisUpgradePollSasExpanderActivate"
    FSM_STATUS_CHASSIS_UPGRADE_POLL_STORAGE_CTLR_ACTIVATION = "ChassisUpgradePollStorageCtlrActivation"
    FSM_STATUS_CHASSIS_UPGRADE_POLL_UPDATE_STATUS = "ChassisUpgradePollUpdateStatus"
    FSM_STATUS_CHASSIS_UPGRADE_POWER_OFF_SERVERS = "ChassisUpgradePowerOffServers"
    FSM_STATUS_CHASSIS_UPGRADE_POWER_ON_SERVERS = "ChassisUpgradePowerOnServers"
    FSM_STATUS_CHASSIS_UPGRADE_RESET_SAS_EXPANDER = "ChassisUpgradeResetSasExpander"
    FSM_STATUS_CHASSIS_UPGRADE_SUCCESS = "ChassisUpgradeSuccess"
    FSM_STATUS_CHASSIS_UPGRADE_UPDATE_REQUEST = "ChassisUpgradeUpdateRequest"
    FSM_STATUS_CHASSIS_UPGRADE_WAIT_FOR_POWER_OFF = "ChassisUpgradeWaitForPowerOff"
    FSM_STATUS_DISASSOCIATE_BEGIN = "DisassociateBegin"
    FSM_STATUS_DISASSOCIATE_COMPLETE = "DisassociateComplete"
    FSM_STATUS_DISASSOCIATE_FAIL = "DisassociateFail"
    FSM_STATUS_DISASSOCIATE_SUCCESS = "DisassociateSuccess"
    FSM_STATUS_DYNAMIC_REALLOCATION_BEGIN = "DynamicReallocationBegin"
    FSM_STATUS_DYNAMIC_REALLOCATION_CONFIG = "DynamicReallocationConfig"
    FSM_STATUS_DYNAMIC_REALLOCATION_FAIL = "DynamicReallocationFail"
    FSM_STATUS_DYNAMIC_REALLOCATION_SUCCESS = "DynamicReallocationSuccess"
    FSM_STATUS_FAN_POLICY_CONFIG_BEGIN = "FanPolicyConfigBegin"
    FSM_STATUS_FAN_POLICY_CONFIG_EXECUTE = "FanPolicyConfigExecute"
    FSM_STATUS_FAN_POLICY_CONFIG_FAIL = "FanPolicyConfigFail"
    FSM_STATUS_FAN_POLICY_CONFIG_SUCCESS = "FanPolicyConfigSuccess"
    FSM_STATUS_FW_UPGRADE_BEGIN = "FwUpgradeBegin"
    FSM_STATUS_FW_UPGRADE_COPY_REMOTE = "FwUpgradeCopyRemote"
    FSM_STATUS_FW_UPGRADE_DELETE_CURL_DOWNLOADED_IMAGES = "FwUpgradeDeleteCurlDownloadedImages"
    FSM_STATUS_FW_UPGRADE_DELETE_IMAGES_REMOTE = "FwUpgradeDeleteImagesRemote"
    FSM_STATUS_FW_UPGRADE_DOWNLOAD_IMAGES = "FwUpgradeDownloadImages"
    FSM_STATUS_FW_UPGRADE_FAIL = "FwUpgradeFail"
    FSM_STATUS_FW_UPGRADE_POLL_UPDATE_ADAPTOR = "FwUpgradePollUpdateAdaptor"
    FSM_STATUS_FW_UPGRADE_POLL_UPDATE_CMC = "FwUpgradePollUpdateCmc"
    FSM_STATUS_FW_UPGRADE_POLL_UPDATE_SAS_EXPANDER = "FwUpgradePollUpdateSasExpander"
    FSM_STATUS_FW_UPGRADE_SUCCESS = "FwUpgradeSuccess"
    FSM_STATUS_FW_UPGRADE_UNLOCK_FIRMWARE_IMAGE = "FwUpgradeUnlockFirmwareImage"
    FSM_STATUS_FW_UPGRADE_UPDATE_ADAPTOR = "FwUpgradeUpdateAdaptor"
    FSM_STATUS_FW_UPGRADE_UPDATE_CMC = "FwUpgradeUpdateCmc"
    FSM_STATUS_FW_UPGRADE_UPDATE_SAS_EXPANDER = "FwUpgradeUpdateSasExpander"
    FSM_STATUS_FW_UPGRADE_WAIT_BEFORE_INSTALLATION = "FwUpgradeWaitBeforeInstallation"
    FSM_STATUS_OOB_STORAGE_ADMIN_CFG_BEGIN = "OobStorageAdminCfgBegin"
    FSM_STATUS_OOB_STORAGE_ADMIN_CFG_FAIL = "OobStorageAdminCfgFail"
    FSM_STATUS_OOB_STORAGE_ADMIN_CFG_OOB_STORAGE_CONFIG = "OobStorageAdminCfgOobStorageConfig"
    FSM_STATUS_OOB_STORAGE_ADMIN_CFG_OOB_STORAGE_INVENTORY = "OobStorageAdminCfgOobStorageInventory"
    FSM_STATUS_OOB_STORAGE_ADMIN_CFG_SUCCESS = "OobStorageAdminCfgSuccess"
    FSM_STATUS_POWER_CAP_BEGIN = "PowerCapBegin"
    FSM_STATUS_POWER_CAP_CONFIG = "PowerCapConfig"
    FSM_STATUS_POWER_CAP_FAIL = "PowerCapFail"
    FSM_STATUS_POWER_CAP_SUCCESS = "PowerCapSuccess"
    FSM_STATUS_POWER_CAP_WAIT = "PowerCapWait"
    FSM_STATUS_POWER_EXTENDED_POLICY_CONFIG_BEGIN = "PowerExtendedPolicyConfigBegin"
    FSM_STATUS_POWER_EXTENDED_POLICY_CONFIG_EXECUTE = "PowerExtendedPolicyConfigExecute"
    FSM_STATUS_POWER_EXTENDED_POLICY_CONFIG_FAIL = "PowerExtendedPolicyConfigFail"
    FSM_STATUS_POWER_EXTENDED_POLICY_CONFIG_SUCCESS = "PowerExtendedPolicyConfigSuccess"
    FSM_STATUS_POWER_SAVE_POLICY_CONFIG_BEGIN = "PowerSavePolicyConfigBegin"
    FSM_STATUS_POWER_SAVE_POLICY_CONFIG_EXECUTE = "PowerSavePolicyConfigExecute"
    FSM_STATUS_POWER_SAVE_POLICY_CONFIG_FAIL = "PowerSavePolicyConfigFail"
    FSM_STATUS_POWER_SAVE_POLICY_CONFIG_SUCCESS = "PowerSavePolicyConfigSuccess"
    FSM_STATUS_PSU_POLICY_CONFIG_BEGIN = "PsuPolicyConfigBegin"
    FSM_STATUS_PSU_POLICY_CONFIG_EXECUTE = "PsuPolicyConfigExecute"
    FSM_STATUS_PSU_POLICY_CONFIG_FAIL = "PsuPolicyConfigFail"
    FSM_STATUS_PSU_POLICY_CONFIG_SUCCESS = "PsuPolicyConfigSuccess"
    FSM_STATUS_REMOVE_CHASSIS_BEGIN = "RemoveChassisBegin"
    FSM_STATUS_REMOVE_CHASSIS_CLEANUP_VNICS_LOCAL = "RemoveChassisCleanupVnicsLocal"
    FSM_STATUS_REMOVE_CHASSIS_CLEANUP_VNICS_PEER = "RemoveChassisCleanupVnicsPeer"
    FSM_STATUS_REMOVE_CHASSIS_DECOMISSION = "RemoveChassisDecomission"
    FSM_STATUS_REMOVE_CHASSIS_DISABLE_END_POINT = "RemoveChassisDisableEndPoint"
    FSM_STATUS_REMOVE_CHASSIS_FAIL = "RemoveChassisFail"
    FSM_STATUS_REMOVE_CHASSIS_SUCCESS = "RemoveChassisSuccess"
    FSM_STATUS_REMOVE_CHASSIS_UN_IDENTIFY_LOCAL = "RemoveChassisUnIdentifyLocal"
    FSM_STATUS_REMOVE_CHASSIS_UN_IDENTIFY_PEER = "RemoveChassisUnIdentifyPeer"
    FSM_STATUS_REMOVE_CHASSIS_WAIT = "RemoveChassisWait"
    FSM_STATUS_NOP = "nop"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    MFG_TIME_NOT_APPLICABLE = "not-applicable"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    OPER_STATE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPER_STATE_CHASSIS_INTRUSION = "chassis-intrusion"
    OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIMM_DISABLED = "dimm-disabled"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPER_STATE_IDENTIFY = "identify"
    OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
    OPER_STATE_MALFORMED_FRU = "malformed-fru"
    OPER_STATE_NON_OPTIMAL = "non-optimal"
    OPER_STATE_NON_OPTIMAL_SEVERE = "non-optimal-severe"
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPER_STATE_PEER_DIMM_DISABLED = "peer-dimm-disabled"
    OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    OPER_STATE_POST_FAILURE = "post-failure"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_POWERED_OFF = "powered-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UNSUPPORTED_CONFIG = "unsupported-config"
    OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_INTRUSION = "chassis-intrusion"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
    OPERABILITY_DIMM_DISABLED = "dimm-disabled"
    OPERABILITY_DISABLED = "disabled"
    OPERABILITY_DISCOVERY = "discovery"
    OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPERABILITY_IDENTIFY = "identify"
    OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
    OPERABILITY_MALFORMED_FRU = "malformed-fru"
    OPERABILITY_NON_OPTIMAL = "non-optimal"
    OPERABILITY_NON_OPTIMAL_SEVERE = "non-optimal-severe"
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PEER_DIMM_DISABLED = "peer-dimm-disabled"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UNSUPPORTED_CONFIG = "unsupported-config"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    POWER_FAILED = "failed"
    POWER_INPUT_DEGRADED = "input-degraded"
    POWER_INPUT_FAILED = "input-failed"
    POWER_OK = "ok"
    POWER_OUTPUT_DEGRADED = "output-degraded"
    POWER_OUTPUT_FAILED = "output-failed"
    POWER_REDUNDANCY_DEGRADED = "redundancy-degraded"
    POWER_REDUNDANCY_FAILED = "redundancy-failed"
    POWER_UNKNOWN = "unknown"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_DEPRECATED = "equipped-deprecated"
    PRESENCE_EQUIPPED_DISC_ERROR = "equipped-disc-error"
    PRESENCE_EQUIPPED_DISC_IN_PROGRESS = "equipped-disc-in-progress"
    PRESENCE_EQUIPPED_DISC_NOT_STARTED = "equipped-disc-not-started"
    PRESENCE_EQUIPPED_DISC_UNKNOWN = "equipped-disc-unknown"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    SEEPROM_OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    SEEPROM_OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    SEEPROM_OPER_STATE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    SEEPROM_OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    SEEPROM_OPER_STATE_CHASSIS_INTRUSION = "chassis-intrusion"
    SEEPROM_OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    SEEPROM_OPER_STATE_CONFIG = "config"
    SEEPROM_OPER_STATE_DECOMISSIONING = "decomissioning"
    SEEPROM_OPER_STATE_DEGRADED = "degraded"
    SEEPROM_OPER_STATE_DIMM_DISABLED = "dimm-disabled"
    SEEPROM_OPER_STATE_DISABLED = "disabled"
    SEEPROM_OPER_STATE_DISCOVERY = "discovery"
    SEEPROM_OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    SEEPROM_OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    SEEPROM_OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    SEEPROM_OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    SEEPROM_OPER_STATE_IDENTIFY = "identify"
    SEEPROM_OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    SEEPROM_OPER_STATE_INOPERABLE = "inoperable"
    SEEPROM_OPER_STATE_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
    SEEPROM_OPER_STATE_MALFORMED_FRU = "malformed-fru"
    SEEPROM_OPER_STATE_NON_OPTIMAL = "non-optimal"
    SEEPROM_OPER_STATE_NON_OPTIMAL_SEVERE = "non-optimal-severe"
    SEEPROM_OPER_STATE_NOT_SUPPORTED = "not-supported"
    SEEPROM_OPER_STATE_OPERABLE = "operable"
    SEEPROM_OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    SEEPROM_OPER_STATE_PEER_DIMM_DISABLED = "peer-dimm-disabled"
    SEEPROM_OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    SEEPROM_OPER_STATE_POST_FAILURE = "post-failure"
    SEEPROM_OPER_STATE_POWER_PROBLEM = "power-problem"
    SEEPROM_OPER_STATE_POWERED_OFF = "powered-off"
    SEEPROM_OPER_STATE_REMOVED = "removed"
    SEEPROM_OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    SEEPROM_OPER_STATE_UNKNOWN = "unknown"
    SEEPROM_OPER_STATE_UNSUPPORTED_CONFIG = "unsupported-config"
    SEEPROM_OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    SEEPROM_OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    SERVICE_STATE_IN_MAINTENANCE = "in-maintenance"
    SERVICE_STATE_IN_SERVICE = "in-service"
    SERVICE_STATE_OUT_OF_SERVICE = "out-of-service"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    VERSION_HOLDER_FALSE = "false"
    VERSION_HOLDER_NO = "no"
    VERSION_HOLDER_TRUE = "true"
    VERSION_HOLDER_YES = "yes"


class EquipmentChassis(ManagedObject):
    """This is EquipmentChassis class."""

    consts = EquipmentChassisConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentChassis", "equipmentChassis", "chassis-[id]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['topSystem'], ['computeBlade', 'computeBoardController', 'computeCartridge', 'computePsuControl', 'equipmentBeaconLed', 'equipmentChassisFsm', 'equipmentChassisFsmTask', 'equipmentChassisStats', 'equipmentComputeConn', 'equipmentCrossFabricModule', 'equipmentFanModule', 'equipmentHealthLed', 'equipmentIOCard', 'equipmentIndicatorLed', 'equipmentLocatorLed', 'equipmentPcieNode', 'equipmentPoolable', 'equipmentPsu', 'equipmentSharedIOModule', 'equipmentSwitchIOCard', 'equipmentSystemIOController', 'eventInst', 'fabricLocale', 'faultInst', 'faultSuppressTask', 'firmwareActivity', 'firmwareActivityTrigger', 'firmwareImageLock', 'firmwareStatus', 'mgmtController', 'powerBudget', 'sesEnclosure', 'storageController', 'storageEnclosure', 'storageSasExpander', 'storageVirtualDriveContainer', 'vnicRackServerDiscoveryProfile'], ["Get", "Set"])

    prop_meta = {
        "ack_progress_indicator": MoPropertyMeta("ack_progress_indicator", "ackProgressIndicator", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "ack-not-in-progress"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["acknowledged", "auto-acknowledge", "decommission", "disable-port-channel", "enable-port-channel", "re-acknowledge", "remove"], []),
        "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "association": MoPropertyMeta("association", "association", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "establishing", "failed", "none", "removing", "throttled"], []),
        "availability": MoPropertyMeta("availability", "availability", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "unavailable"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], []),
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []),
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []),
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["complete", "failed", "fru-identity-indeterminate", "fru-not-ready", "fru-state-indeterminate", "illegal-fru", "in-progress", "insufficiently-equipped", "invalid-adaptor-iocard", "malformed-fru-info", "retry", "throttled", "undiscovered"], []),
        "discovery_status": MoPropertyMeta("discovery_status", "discoveryStatus", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "fabric_ep_dn": MoPropertyMeta("fabric_ep_dn", "fabricEpDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "fan_speed_config_state": MoPropertyMeta("fan_speed_config_state", "fanSpeedConfigState", "string", VersionMeta.Version411a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Acoustic", "Balanced", "High Power", "Low Power", "Max Power", "Performance"], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_flags": MoPropertyMeta("fsm_flags", "fsmFlags", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["AssociateActivateAdaptor", "AssociateActivateBrdCtlr", "AssociateActivateCmc", "AssociateActivateLocalDisk", "AssociateActivateSasExpander", "AssociateActivateStorageCtlr", "AssociateBegin", "AssociateChassisPeerAdapterReboot", "AssociateConfigChassisAdapterConnectivity", "AssociateCopyRemote", "AssociateDeleteCurlDownloadedImages", "AssociateDeleteImagesRemote", "AssociateDiskZoningConfig", "AssociateDownloadImages", "AssociateFail", "AssociatePollAdaptorActivation", "AssociatePollBrdCtlrActivation", "AssociatePollCmcActivation", "AssociatePollPostDiskZoneStorageInvCIMC", "AssociatePollSasExpanderActivate", "AssociatePollSasExpanderConfig", "AssociatePollStorageCtlrActivation", "AssociatePollUpdateAdaptor", "AssociatePollUpdateCmc", "AssociatePollUpdateSasExpander", "AssociatePostDiskZoneStorageInvCIMC", "AssociatePostDiskZoneStorageInvCMC", "AssociatePowerOffServers", "AssociatePowerOnServers", "AssociateSasExpanderConfig", "AssociateSuccess", "AssociateUnlockFirmwareImage", "AssociateUpdateAdaptor", "AssociateUpdateCmc", "AssociateUpdateSasExpander", "AssociateWaitBeforeInstallation", "AssociateWaitForPowerOff", "ChassisUpgradeActivateAdaptor", "ChassisUpgradeActivateBrdCtlr", "ChassisUpgradeActivateCmc", "ChassisUpgradeActivateLocalDisk", "ChassisUpgradeActivateSasExpander", "ChassisUpgradeActivateStorageCtlr", "ChassisUpgradeBegin", "ChassisUpgradeFail", "ChassisUpgradePollAdaptorActivation", "ChassisUpgradePollBrdCtlrActivation", "ChassisUpgradePollCmcActivation", "ChassisUpgradePollLocalDiskActivate", "ChassisUpgradePollSasExpanderActivate", "ChassisUpgradePollStorageCtlrActivation", "ChassisUpgradePollUpdateStatus", "ChassisUpgradePowerOffServers", "ChassisUpgradePowerOnServers", "ChassisUpgradeResetSasExpander", "ChassisUpgradeSuccess", "ChassisUpgradeUpdateRequest", "ChassisUpgradeWaitForPowerOff", "DisassociateBegin", "DisassociateComplete", "DisassociateFail", "DisassociateSuccess", "DynamicReallocationBegin", "DynamicReallocationConfig", "DynamicReallocationFail", "DynamicReallocationSuccess", "FanPolicyConfigBegin", "FanPolicyConfigExecute", "FanPolicyConfigFail", "FanPolicyConfigSuccess", "FwUpgradeBegin", "FwUpgradeCopyRemote", "FwUpgradeDeleteCurlDownloadedImages", "FwUpgradeDeleteImagesRemote", "FwUpgradeDownloadImages", "FwUpgradeFail", "FwUpgradePollUpdateAdaptor", "FwUpgradePollUpdateCmc", "FwUpgradePollUpdateSasExpander", "FwUpgradeSuccess", "FwUpgradeUnlockFirmwareImage", "FwUpgradeUpdateAdaptor", "FwUpgradeUpdateCmc", "FwUpgradeUpdateSasExpander", "FwUpgradeWaitBeforeInstallation", "OobStorageAdminCfgBegin", "OobStorageAdminCfgFail", "OobStorageAdminCfgOobStorageConfig", "OobStorageAdminCfgOobStorageInventory", "OobStorageAdminCfgSuccess", "PowerCapBegin", "PowerCapConfig", "PowerCapFail", "PowerCapSuccess", "PowerCapWait", "PowerExtendedPolicyConfigBegin", "PowerExtendedPolicyConfigExecute", "PowerExtendedPolicyConfigFail", "PowerExtendedPolicyConfigSuccess", "PowerSavePolicyConfigBegin", "PowerSavePolicyConfigExecute", "PowerSavePolicyConfigFail", "PowerSavePolicyConfigSuccess", "PsuPolicyConfigBegin", "PsuPolicyConfigExecute", "PsuPolicyConfigFail", "PsuPolicyConfigSuccess", "RemoveChassisBegin", "RemoveChassisCleanupVnicsLocal", "RemoveChassisCleanupVnicsPeer", "RemoveChassisDecomission", "RemoveChassisDisableEndPoint", "RemoveChassisFail", "RemoveChassisSuccess", "RemoveChassisUnIdentifyLocal", "RemoveChassisUnIdentifyPeer", "RemoveChassisWait", "nop"], []),
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]),
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNLD-usb-unmounted", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-POWER-PROFILE-IN-PROGRESS", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-tp", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-downgrade-fail", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-pwdenc-config-master-key-error", "ERR-pwdenc-delete-master-key-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-key-cert", "ERR-set-login-profile", "ERR-set-min-passphrase-length", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-set-user", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-passwd-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]),
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []),
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []),
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["AssociateActivateAdaptor", "AssociateActivateBrdCtlr", "AssociateActivateCmc", "AssociateActivateLocalDisk", "AssociateActivateSasExpander", "AssociateActivateStorageCtlr", "AssociateBegin", "AssociateChassisPeerAdapterReboot", "AssociateConfigChassisAdapterConnectivity", "AssociateCopyRemote", "AssociateDeleteCurlDownloadedImages", "AssociateDeleteImagesRemote", "AssociateDiskZoningConfig", "AssociateDownloadImages", "AssociateFail", "AssociatePollAdaptorActivation", "AssociatePollBrdCtlrActivation", "AssociatePollCmcActivation", "AssociatePollPostDiskZoneStorageInvCIMC", "AssociatePollSasExpanderActivate", "AssociatePollSasExpanderConfig", "AssociatePollStorageCtlrActivation", "AssociatePollUpdateAdaptor", "AssociatePollUpdateCmc", "AssociatePollUpdateSasExpander", "AssociatePostDiskZoneStorageInvCIMC", "AssociatePostDiskZoneStorageInvCMC", "AssociatePowerOffServers", "AssociatePowerOnServers", "AssociateSasExpanderConfig", "AssociateSuccess", "AssociateUnlockFirmwareImage", "AssociateUpdateAdaptor", "AssociateUpdateCmc", "AssociateUpdateSasExpander", "AssociateWaitBeforeInstallation", "AssociateWaitForPowerOff", "ChassisUpgradeActivateAdaptor", "ChassisUpgradeActivateBrdCtlr", "ChassisUpgradeActivateCmc", "ChassisUpgradeActivateLocalDisk", "ChassisUpgradeActivateSasExpander", "ChassisUpgradeActivateStorageCtlr", "ChassisUpgradeBegin", "ChassisUpgradeFail", "ChassisUpgradePollAdaptorActivation", "ChassisUpgradePollBrdCtlrActivation", "ChassisUpgradePollCmcActivation", "ChassisUpgradePollLocalDiskActivate", "ChassisUpgradePollSasExpanderActivate", "ChassisUpgradePollStorageCtlrActivation", "ChassisUpgradePollUpdateStatus", "ChassisUpgradePowerOffServers", "ChassisUpgradePowerOnServers", "ChassisUpgradeResetSasExpander", "ChassisUpgradeSuccess", "ChassisUpgradeUpdateRequest", "ChassisUpgradeWaitForPowerOff", "DisassociateBegin", "DisassociateComplete", "DisassociateFail", "DisassociateSuccess", "DynamicReallocationBegin", "DynamicReallocationConfig", "DynamicReallocationFail", "DynamicReallocationSuccess", "FanPolicyConfigBegin", "FanPolicyConfigExecute", "FanPolicyConfigFail", "FanPolicyConfigSuccess", "FwUpgradeBegin", "FwUpgradeCopyRemote", "FwUpgradeDeleteCurlDownloadedImages", "FwUpgradeDeleteImagesRemote", "FwUpgradeDownloadImages", "FwUpgradeFail", "FwUpgradePollUpdateAdaptor", "FwUpgradePollUpdateCmc", "FwUpgradePollUpdateSasExpander", "FwUpgradeSuccess", "FwUpgradeUnlockFirmwareImage", "FwUpgradeUpdateAdaptor", "FwUpgradeUpdateCmc", "FwUpgradeUpdateSasExpander", "FwUpgradeWaitBeforeInstallation", "OobStorageAdminCfgBegin", "OobStorageAdminCfgFail", "OobStorageAdminCfgOobStorageConfig", "OobStorageAdminCfgOobStorageInventory", "OobStorageAdminCfgSuccess", "PowerCapBegin", "PowerCapConfig", "PowerCapFail", "PowerCapSuccess", "PowerCapWait", "PowerExtendedPolicyConfigBegin", "PowerExtendedPolicyConfigExecute", "PowerExtendedPolicyConfigFail", "PowerExtendedPolicyConfigSuccess", "PowerSavePolicyConfigBegin", "PowerSavePolicyConfigExecute", "PowerSavePolicyConfigFail", "PowerSavePolicyConfigSuccess", "PsuPolicyConfigBegin", "PsuPolicyConfigExecute", "PsuPolicyConfigFail", "PsuPolicyConfigSuccess", "RemoveChassisBegin", "RemoveChassisCleanupVnicsLocal", "RemoveChassisCleanupVnicsPeer", "RemoveChassisDecomission", "RemoveChassisDisableEndPoint", "RemoveChassisFail", "RemoveChassisSuccess", "RemoveChassisUnIdentifyLocal", "RemoveChassisUnIdentifyPeer", "RemoveChassisWait", "nop"], []),
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-254"]),
        "lc_ts": MoPropertyMeta("lc_ts", "lcTs", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []),
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "mfg_time": MoPropertyMeta("mfg_time", "mfgTime", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["not-applicable"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|psu-voltage|iocard-voltage|fabric-unsupported-conn|chassis-post-failure|fan-power|compute-power|fan-inoperable|compute-inoperable|chassis-power|chassis-unsupported|chassis-thermal|psu-perf|iocard-perf|chassis-limit-exceeded|psu-thermal|iocard-thermal|iocard-inaccessible|chassis-inoperable|fan-voltage|removed|compute-voltage|backplane-port-problem|psu-power|iocard-power|chassis-vif-capacity-reduced|chassis-voltage|psu-inoperable|iocard-inoperable|fabric-conn-problem|config|fan-perf|compute-perf|chassis-discovery-policy-unsupported|fan-thermal|compute-thermal|chassis-port-channel-enabled|chassis-perf),){0,38}(defaultValue|not-applicable|psu-voltage|iocard-voltage|fabric-unsupported-conn|chassis-post-failure|fan-power|compute-power|fan-inoperable|compute-inoperable|chassis-power|chassis-unsupported|chassis-thermal|psu-perf|iocard-perf|chassis-limit-exceeded|psu-thermal|iocard-thermal|iocard-inaccessible|chassis-inoperable|fan-voltage|removed|compute-voltage|backplane-port-problem|psu-power|iocard-power|chassis-vif-capacity-reduced|chassis-voltage|psu-inoperable|iocard-inoperable|fabric-conn-problem|config|fan-perf|compute-perf|chassis-discovery-policy-unsupported|fan-thermal|compute-thermal|chassis-port-channel-enabled|chassis-perf){0,1}""", [], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "input-degraded", "input-failed", "ok", "output-degraded", "output-failed", "redundancy-degraded", "redundancy-failed", "unknown"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "seeprom_oper_state": MoPropertyMeta("seeprom_oper_state", "seepromOperState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "service_state": MoPropertyMeta("service_state", "serviceState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-maintenance", "in-service", "out-of-service"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "thermal_state_qualifier": MoPropertyMeta("thermal_state_qualifier", "thermalStateQualifier", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "version_holder": MoPropertyMeta("version_holder", "versionHolder", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "ackProgressIndicator": "ack_progress_indicator", 
        "adminState": "admin_state", 
        "assetTag": "asset_tag", 
        "assignedToDn": "assigned_to_dn", 
        "association": "association", 
        "availability": "availability", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "discovery": "discovery", 
        "discoveryStatus": "discovery_status", 
        "dn": "dn", 
        "fabricEpDn": "fabric_ep_dn", 
        "fanSpeedConfigState": "fan_speed_config_state", 
        "fltAggr": "flt_aggr", 
        "fsmDescr": "fsm_descr", 
        "fsmFlags": "fsm_flags", 
        "fsmPrev": "fsm_prev", 
        "fsmProgr": "fsm_progr", 
        "fsmRmtInvErrCode": "fsm_rmt_inv_err_code", 
        "fsmRmtInvErrDescr": "fsm_rmt_inv_err_descr", 
        "fsmRmtInvRslt": "fsm_rmt_inv_rslt", 
        "fsmStageDescr": "fsm_stage_descr", 
        "fsmStamp": "fsm_stamp", 
        "fsmStatus": "fsm_status", 
        "fsmTry": "fsm_try", 
        "id": "id", 
        "lcTs": "lc_ts", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "managingInst": "managing_inst", 
        "mfgTime": "mfg_time", 
        "model": "model", 
        "operQualifier": "oper_qualifier", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "partNumber": "part_number", 
        "power": "power", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "seepromOperState": "seeprom_oper_state", 
        "serial": "serial", 
        "serviceState": "service_state", 
        "status": "status", 
        "thermal": "thermal", 
        "thermalStateQualifier": "thermal_state_qualifier", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
        "versionHolder": "version_holder", 
        "vid": "vid", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.ack_progress_indicator = None
        self.admin_state = None
        self.asset_tag = None
        self.assigned_to_dn = None
        self.association = None
        self.availability = None
        self.child_action = None
        self.config_state = None
        self.conn_path = None
        self.conn_status = None
        self.discovery = None
        self.discovery_status = None
        self.fabric_ep_dn = None
        self.fan_speed_config_state = None
        self.flt_aggr = None
        self.fsm_descr = None
        self.fsm_flags = None
        self.fsm_prev = None
        self.fsm_progr = None
        self.fsm_rmt_inv_err_code = None
        self.fsm_rmt_inv_err_descr = None
        self.fsm_rmt_inv_rslt = None
        self.fsm_stage_descr = None
        self.fsm_stamp = None
        self.fsm_status = None
        self.fsm_try = None
        self.lc_ts = None
        self.lic_gp = None
        self.lic_state = None
        self.managing_inst = None
        self.mfg_time = None
        self.model = None
        self.oper_qualifier = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.part_number = None
        self.power = None
        self.presence = None
        self.revision = None
        self.sacl = None
        self.seeprom_oper_state = None
        self.serial = None
        self.service_state = None
        self.status = None
        self.thermal = None
        self.thermal_state_qualifier = None
        self.usr_lbl = None
        self.vendor = None
        self.version_holder = None
        self.vid = None

        ManagedObject.__init__(self, "EquipmentChassis", parent_mo_or_dn, **kwargs)
