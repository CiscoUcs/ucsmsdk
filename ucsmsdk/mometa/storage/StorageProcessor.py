"""This module contains the general information for StorageProcessor ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageProcessorConsts():
    ADMIN_LEADERSHIP_ACTIVE = "active"
    ADMIN_LEADERSHIP_PASSIVE = "passive"
    ADMIN_LEADERSHIP_UNKNOWN = "unknown"
    ADMIN_STATE_IN_MAINTENANCE = "in-maintenance"
    ADMIN_STATE_IN_SERVICE = "in-service"
    CIMC_BACKUP_TRIGGER_STATUS_DISABLED = "disabled"
    CIMC_BACKUP_TRIGGER_STATUS_ENABLED = "enabled"
    CIMC_BACKUP_TRIGGER_STATUS_UNKNOWN = "unknown"
    CIMC_HEARTBEAT_STATUS_DISABLED = "disabled"
    CIMC_HEARTBEAT_STATUS_RUNNING = "running"
    CIMC_HEARTBEAT_STATUS_TIMED_OUT = "timed-out"
    CIMC_HEARTBEAT_STATUS_UNKNOWN = "unknown"
    CLUSTER_STATE_DEGRADED = "degraded"
    CLUSTER_STATE_OK = "ok"
    CLUSTER_STATE_UNKNOWN = "unknown"
    CONFIG_STATE_DISRUPTIVE = "disruptive"
    CONFIG_STATE_OK = "ok"
    CONFIG_STATE_UNKNOWN = "unknown"
    DEPLOY_ACTION_ABORT_REPLICATION = "abort-replication"
    DEPLOY_ACTION_CREATE = "create"
    DEPLOY_ACTION_DELETE = "delete"
    DEPLOY_ACTION_MODIFY = "modify"
    DEPLOY_ACTION_NO_ACTION = "no-action"
    DEPLOY_ACTION_REPLACE = "replace"
    DEPLOY_ACTION_RESTORE = "restore"
    DEPLOY_ACTION_SET_OFFLINE = "set-offline"
    DEPLOY_ACTION_SET_ONLINE = "set-online"
    FSM_PREV_DEPLOY_SYSTEM_BEGIN = "DeploySystemBegin"
    FSM_PREV_DEPLOY_SYSTEM_CONFIG_HASTATE = "DeploySystemConfigHAState"
    FSM_PREV_DEPLOY_SYSTEM_CONFIG_NETWORK = "DeploySystemConfigNetwork"
    FSM_PREV_DEPLOY_SYSTEM_CONFIG_PLATFORM = "DeploySystemConfigPlatform"
    FSM_PREV_DEPLOY_SYSTEM_CONFIG_STORAGE_REPLICATION_SERVICE = "DeploySystemConfigStorageReplicationService"
    FSM_PREV_DEPLOY_SYSTEM_CONFIG_STORAGE_TARGET_IDENTITY = "DeploySystemConfigStorageTargetIdentity"
    FSM_PREV_DEPLOY_SYSTEM_CONNECT_SMELOCAL = "DeploySystemConnectSMELocal"
    FSM_PREV_DEPLOY_SYSTEM_CONNECT_SMEREMOTE = "DeploySystemConnectSMERemote"
    FSM_PREV_DEPLOY_SYSTEM_FAIL = "DeploySystemFail"
    FSM_PREV_DEPLOY_SYSTEM_POWER_ON = "DeploySystemPowerOn"
    FSM_PREV_DEPLOY_SYSTEM_SUCCESS = "DeploySystemSuccess"
    FSM_PREV_DISCOVER_SYSTEM_BEGIN = "DiscoverSystemBegin"
    FSM_PREV_DISCOVER_SYSTEM_CONNECT_SMELOCAL = "DiscoverSystemConnectSMELocal"
    FSM_PREV_DISCOVER_SYSTEM_CONNECT_SMEREMOTE = "DiscoverSystemConnectSMERemote"
    FSM_PREV_DISCOVER_SYSTEM_FAIL = "DiscoverSystemFail"
    FSM_PREV_DISCOVER_SYSTEM_INITIATE_POLL_BMCLOCAL = "DiscoverSystemInitiatePollBMCLocal"
    FSM_PREV_DISCOVER_SYSTEM_INITIATE_POLL_BMCREMOTE = "DiscoverSystemInitiatePollBMCRemote"
    FSM_PREV_DISCOVER_SYSTEM_SUCCESS = "DiscoverSystemSuccess"
    FSM_PREV_DISCOVER_SYSTEM_WAIT_FOR_INVENTORY = "DiscoverSystemWaitForInventory"
    FSM_PREV_DISCOVER_SYSTEM_WAIT_FOR_OSSTATUS = "DiscoverSystemWaitForOSStatus"
    FSM_PREV_DISCOVER_SYSTEM_WAIT_FOR_SMECONNECTION = "DiscoverSystemWaitForSMEConnection"
    FSM_PREV_ENTER_MAINTENANCE_BEGIN = "EnterMaintenanceBegin"
    FSM_PREV_ENTER_MAINTENANCE_DISABLE_STORAGE_TARGET = "EnterMaintenanceDisableStorageTarget"
    FSM_PREV_ENTER_MAINTENANCE_FAIL = "EnterMaintenanceFail"
    FSM_PREV_ENTER_MAINTENANCE_POWER_OFF = "EnterMaintenancePowerOff"
    FSM_PREV_ENTER_MAINTENANCE_SLOT_POWER_CYCLE = "EnterMaintenanceSlotPowerCycle"
    FSM_PREV_ENTER_MAINTENANCE_SUCCESS = "EnterMaintenanceSuccess"
    FSM_PREV_ENTER_MAINTENANCE_WAIT_FOR_SERVER_SHUTDOWN = "EnterMaintenanceWaitForServerShutdown"
    FSM_PREV_EXIT_MAINTENANCE_BEGIN = "ExitMaintenanceBegin"
    FSM_PREV_EXIT_MAINTENANCE_ENABLE_STORAGE_TARGET = "ExitMaintenanceEnableStorageTarget"
    FSM_PREV_EXIT_MAINTENANCE_FAIL = "ExitMaintenanceFail"
    FSM_PREV_EXIT_MAINTENANCE_SUCCESS = "ExitMaintenanceSuccess"
    FSM_PREV_EXIT_MAINTENANCE_WAIT_FOR_HAQUORUM = "ExitMaintenanceWaitForHAQuorum"
    FSM_PREV_EXIT_MAINTENANCE_WAIT_FOR_SMECONNECTION = "ExitMaintenanceWaitForSMEConnection"
    FSM_PREV_EXIT_MAINTENANCE_WAIT_FOR_SERVER_POWER_UP = "ExitMaintenanceWaitForServerPowerUp"
    FSM_PREV_HA_TAKE_OVER_BEGIN = "HaTakeOverBegin"
    FSM_PREV_HA_TAKE_OVER_FAIL = "HaTakeOverFail"
    FSM_PREV_HA_TAKE_OVER_PERFORM_HA_TAKE_OVER = "HaTakeOverPerformHaTakeOver"
    FSM_PREV_HA_TAKE_OVER_SUCCESS = "HaTakeOverSuccess"
    FSM_PREV_UNDEPLOY_SYSTEM_BEGIN = "UndeploySystemBegin"
    FSM_PREV_UNDEPLOY_SYSTEM_DISABLE_STORAGE_TARGET = "UndeploySystemDisableStorageTarget"
    FSM_PREV_UNDEPLOY_SYSTEM_DISASSOC_STORAGE_CONTROLLER = "UndeploySystemDisassocStorageController"
    FSM_PREV_UNDEPLOY_SYSTEM_FAIL = "UndeploySystemFail"
    FSM_PREV_UNDEPLOY_SYSTEM_POWER_OFF = "UndeploySystemPowerOff"
    FSM_PREV_UNDEPLOY_SYSTEM_SLOT_POWER_CYCLE = "UndeploySystemSlotPowerCycle"
    FSM_PREV_UNDEPLOY_SYSTEM_SUCCESS = "UndeploySystemSuccess"
    FSM_PREV_UNDEPLOY_SYSTEM_UNDEPLOY_NETWORK = "UndeploySystemUndeployNetwork"
    FSM_PREV_UNDEPLOY_SYSTEM_UNDEPLOY_PLATFORM = "UndeploySystemUndeployPlatform"
    FSM_PREV_UNDEPLOY_SYSTEM_UNDEPLOY_STORAGE = "UndeploySystemUndeployStorage"
    FSM_PREV_UNDEPLOY_SYSTEM_UNDEPLOY_TARGET_IDENTITY = "UndeploySystemUndeployTargetIdentity"
    FSM_PREV_UNDEPLOY_SYSTEM_WAIT_FOR_DISASSOC_COMPLETION = "UndeploySystemWaitForDisassocCompletion"
    FSM_PREV_UNDEPLOY_SYSTEM_WAIT_FOR_SERVER_SHUTDOWN = "UndeploySystemWaitForServerShutdown"
    FSM_PREV_UNDEPLOY_SYSTEM_WAIT_FOR_UNDEPLOY_STORAGE = "UndeploySystemWaitForUndeployStorage"
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
    FSM_RMT_INV_ERR_CODE_ERR_SET_NETWORK = "ERR-set-network"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PASSWORD_STRENGTH_CHECK = "ERR-set-password-strength-check"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PORT_CHANNEL = "ERR-set-port-channel"
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
    FSM_RMT_INV_ERR_CODE_ERR_USER_SET_ERROR = "ERR-user-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_XML_PARSE_ERROR = "ERR-xml-parse-error"
    FSM_RMT_INV_ERR_CODE_NONE = "none"
    FSM_STAMP_NEVER = "never"
    FSM_STATUS_DEPLOY_SYSTEM_BEGIN = "DeploySystemBegin"
    FSM_STATUS_DEPLOY_SYSTEM_CONFIG_HASTATE = "DeploySystemConfigHAState"
    FSM_STATUS_DEPLOY_SYSTEM_CONFIG_NETWORK = "DeploySystemConfigNetwork"
    FSM_STATUS_DEPLOY_SYSTEM_CONFIG_PLATFORM = "DeploySystemConfigPlatform"
    FSM_STATUS_DEPLOY_SYSTEM_CONFIG_STORAGE_REPLICATION_SERVICE = "DeploySystemConfigStorageReplicationService"
    FSM_STATUS_DEPLOY_SYSTEM_CONFIG_STORAGE_TARGET_IDENTITY = "DeploySystemConfigStorageTargetIdentity"
    FSM_STATUS_DEPLOY_SYSTEM_CONNECT_SMELOCAL = "DeploySystemConnectSMELocal"
    FSM_STATUS_DEPLOY_SYSTEM_CONNECT_SMEREMOTE = "DeploySystemConnectSMERemote"
    FSM_STATUS_DEPLOY_SYSTEM_FAIL = "DeploySystemFail"
    FSM_STATUS_DEPLOY_SYSTEM_POWER_ON = "DeploySystemPowerOn"
    FSM_STATUS_DEPLOY_SYSTEM_SUCCESS = "DeploySystemSuccess"
    FSM_STATUS_DISCOVER_SYSTEM_BEGIN = "DiscoverSystemBegin"
    FSM_STATUS_DISCOVER_SYSTEM_CONNECT_SMELOCAL = "DiscoverSystemConnectSMELocal"
    FSM_STATUS_DISCOVER_SYSTEM_CONNECT_SMEREMOTE = "DiscoverSystemConnectSMERemote"
    FSM_STATUS_DISCOVER_SYSTEM_FAIL = "DiscoverSystemFail"
    FSM_STATUS_DISCOVER_SYSTEM_INITIATE_POLL_BMCLOCAL = "DiscoverSystemInitiatePollBMCLocal"
    FSM_STATUS_DISCOVER_SYSTEM_INITIATE_POLL_BMCREMOTE = "DiscoverSystemInitiatePollBMCRemote"
    FSM_STATUS_DISCOVER_SYSTEM_SUCCESS = "DiscoverSystemSuccess"
    FSM_STATUS_DISCOVER_SYSTEM_WAIT_FOR_INVENTORY = "DiscoverSystemWaitForInventory"
    FSM_STATUS_DISCOVER_SYSTEM_WAIT_FOR_OSSTATUS = "DiscoverSystemWaitForOSStatus"
    FSM_STATUS_DISCOVER_SYSTEM_WAIT_FOR_SMECONNECTION = "DiscoverSystemWaitForSMEConnection"
    FSM_STATUS_ENTER_MAINTENANCE_BEGIN = "EnterMaintenanceBegin"
    FSM_STATUS_ENTER_MAINTENANCE_DISABLE_STORAGE_TARGET = "EnterMaintenanceDisableStorageTarget"
    FSM_STATUS_ENTER_MAINTENANCE_FAIL = "EnterMaintenanceFail"
    FSM_STATUS_ENTER_MAINTENANCE_POWER_OFF = "EnterMaintenancePowerOff"
    FSM_STATUS_ENTER_MAINTENANCE_SLOT_POWER_CYCLE = "EnterMaintenanceSlotPowerCycle"
    FSM_STATUS_ENTER_MAINTENANCE_SUCCESS = "EnterMaintenanceSuccess"
    FSM_STATUS_ENTER_MAINTENANCE_WAIT_FOR_SERVER_SHUTDOWN = "EnterMaintenanceWaitForServerShutdown"
    FSM_STATUS_EXIT_MAINTENANCE_BEGIN = "ExitMaintenanceBegin"
    FSM_STATUS_EXIT_MAINTENANCE_ENABLE_STORAGE_TARGET = "ExitMaintenanceEnableStorageTarget"
    FSM_STATUS_EXIT_MAINTENANCE_FAIL = "ExitMaintenanceFail"
    FSM_STATUS_EXIT_MAINTENANCE_SUCCESS = "ExitMaintenanceSuccess"
    FSM_STATUS_EXIT_MAINTENANCE_WAIT_FOR_HAQUORUM = "ExitMaintenanceWaitForHAQuorum"
    FSM_STATUS_EXIT_MAINTENANCE_WAIT_FOR_SMECONNECTION = "ExitMaintenanceWaitForSMEConnection"
    FSM_STATUS_EXIT_MAINTENANCE_WAIT_FOR_SERVER_POWER_UP = "ExitMaintenanceWaitForServerPowerUp"
    FSM_STATUS_HA_TAKE_OVER_BEGIN = "HaTakeOverBegin"
    FSM_STATUS_HA_TAKE_OVER_FAIL = "HaTakeOverFail"
    FSM_STATUS_HA_TAKE_OVER_PERFORM_HA_TAKE_OVER = "HaTakeOverPerformHaTakeOver"
    FSM_STATUS_HA_TAKE_OVER_SUCCESS = "HaTakeOverSuccess"
    FSM_STATUS_UNDEPLOY_SYSTEM_BEGIN = "UndeploySystemBegin"
    FSM_STATUS_UNDEPLOY_SYSTEM_DISABLE_STORAGE_TARGET = "UndeploySystemDisableStorageTarget"
    FSM_STATUS_UNDEPLOY_SYSTEM_DISASSOC_STORAGE_CONTROLLER = "UndeploySystemDisassocStorageController"
    FSM_STATUS_UNDEPLOY_SYSTEM_FAIL = "UndeploySystemFail"
    FSM_STATUS_UNDEPLOY_SYSTEM_POWER_OFF = "UndeploySystemPowerOff"
    FSM_STATUS_UNDEPLOY_SYSTEM_SLOT_POWER_CYCLE = "UndeploySystemSlotPowerCycle"
    FSM_STATUS_UNDEPLOY_SYSTEM_SUCCESS = "UndeploySystemSuccess"
    FSM_STATUS_UNDEPLOY_SYSTEM_UNDEPLOY_NETWORK = "UndeploySystemUndeployNetwork"
    FSM_STATUS_UNDEPLOY_SYSTEM_UNDEPLOY_PLATFORM = "UndeploySystemUndeployPlatform"
    FSM_STATUS_UNDEPLOY_SYSTEM_UNDEPLOY_STORAGE = "UndeploySystemUndeployStorage"
    FSM_STATUS_UNDEPLOY_SYSTEM_UNDEPLOY_TARGET_IDENTITY = "UndeploySystemUndeployTargetIdentity"
    FSM_STATUS_UNDEPLOY_SYSTEM_WAIT_FOR_DISASSOC_COMPLETION = "UndeploySystemWaitForDisassocCompletion"
    FSM_STATUS_UNDEPLOY_SYSTEM_WAIT_FOR_SERVER_SHUTDOWN = "UndeploySystemWaitForServerShutdown"
    FSM_STATUS_UNDEPLOY_SYSTEM_WAIT_FOR_UNDEPLOY_STORAGE = "UndeploySystemWaitForUndeployStorage"
    FSM_STATUS_NOP = "nop"
    HA_STATE_DEGRADED = "degraded"
    HA_STATE_ELECTION_FAILED = "election-failed"
    HA_STATE_FAILOVER_IN_PROGRESS = "failover-in-progress"
    HA_STATE_NOT_READY = "not-ready"
    HA_STATE_READY = "ready"
    HA_STATE_UNKNOWN = "unknown"
    LEADERSHIP_ACTIVE = "active"
    LEADERSHIP_PASSIVE = "passive"
    LEADERSHIP_UNKNOWN = "unknown"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    OPER_STATE_CLUSTER_DEGRADED = "cluster-degraded"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_IN_MAINTENANCE = "in-maintenance"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
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
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
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


class StorageProcessor(ManagedObject):
    """This is StorageProcessor class."""

    consts = StorageProcessorConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("StorageProcessor", "storageProcessor", "processor-[name]", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["read-only"], [u'storageArray'], [u'commLocale', u'eventInst', u'faultInst', u'lstorageLunReplicationService', u'osController', u'pkiLocale', u'storageEthLif', u'storageProcessorFsm', u'storageProcessorFsmTask', u'storageProcessorRuntime', u'storageTargetIdentity'], [None])

    prop_meta = {
        "admin_leadership": MoPropertyMeta("admin_leadership", "adminLeadership", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "passive", "unknown"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-maintenance", "in-service"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cimc_backup_trigger_status": MoPropertyMeta("cimc_backup_trigger_status", "cimcBackupTriggerStatus", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], []), 
        "cimc_heartbeat_status": MoPropertyMeta("cimc_heartbeat_status", "cimcHeartbeatStatus", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "running", "timed-out", "unknown"], []), 
        "cluster_state": MoPropertyMeta("cluster_state", "clusterState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "ok", "unknown"], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disruptive", "ok", "unknown"], []), 
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "deploy_action": MoPropertyMeta("deploy_action", "deployAction", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["abort-replication", "create", "delete", "modify", "no-action", "replace", "restore", "set-offline", "set-online"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_flags": MoPropertyMeta("fsm_flags", "fsmFlags", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, ["DeploySystemBegin", "DeploySystemConfigHAState", "DeploySystemConfigNetwork", "DeploySystemConfigPlatform", "DeploySystemConfigStorageReplicationService", "DeploySystemConfigStorageTargetIdentity", "DeploySystemConnectSMELocal", "DeploySystemConnectSMERemote", "DeploySystemFail", "DeploySystemPowerOn", "DeploySystemSuccess", "DiscoverSystemBegin", "DiscoverSystemConnectSMELocal", "DiscoverSystemConnectSMERemote", "DiscoverSystemFail", "DiscoverSystemInitiatePollBMCLocal", "DiscoverSystemInitiatePollBMCRemote", "DiscoverSystemSuccess", "DiscoverSystemWaitForInventory", "DiscoverSystemWaitForOSStatus", "DiscoverSystemWaitForSMEConnection", "EnterMaintenanceBegin", "EnterMaintenanceDisableStorageTarget", "EnterMaintenanceFail", "EnterMaintenancePowerOff", "EnterMaintenanceSlotPowerCycle", "EnterMaintenanceSuccess", "EnterMaintenanceWaitForServerShutdown", "ExitMaintenanceBegin", "ExitMaintenanceEnableStorageTarget", "ExitMaintenanceFail", "ExitMaintenanceSuccess", "ExitMaintenanceWaitForHAQuorum", "ExitMaintenanceWaitForSMEConnection", "ExitMaintenanceWaitForServerPowerUp", "HaTakeOverBegin", "HaTakeOverFail", "HaTakeOverPerformHaTakeOver", "HaTakeOverSuccess", "UndeploySystemBegin", "UndeploySystemDisableStorageTarget", "UndeploySystemDisassocStorageController", "UndeploySystemFail", "UndeploySystemPowerOff", "UndeploySystemSlotPowerCycle", "UndeploySystemSuccess", "UndeploySystemUndeployNetwork", "UndeploySystemUndeployPlatform", "UndeploySystemUndeployStorage", "UndeploySystemUndeployTargetIdentity", "UndeploySystemWaitForDisassocCompletion", "UndeploySystemWaitForServerShutdown", "UndeploySystemWaitForUndeployStorage", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNLD-usb-unmounted", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-POWER-PROFILE-IN-PROGRESS", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-tp", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, ["DeploySystemBegin", "DeploySystemConfigHAState", "DeploySystemConfigNetwork", "DeploySystemConfigPlatform", "DeploySystemConfigStorageReplicationService", "DeploySystemConfigStorageTargetIdentity", "DeploySystemConnectSMELocal", "DeploySystemConnectSMERemote", "DeploySystemFail", "DeploySystemPowerOn", "DeploySystemSuccess", "DiscoverSystemBegin", "DiscoverSystemConnectSMELocal", "DiscoverSystemConnectSMERemote", "DiscoverSystemFail", "DiscoverSystemInitiatePollBMCLocal", "DiscoverSystemInitiatePollBMCRemote", "DiscoverSystemSuccess", "DiscoverSystemWaitForInventory", "DiscoverSystemWaitForOSStatus", "DiscoverSystemWaitForSMEConnection", "EnterMaintenanceBegin", "EnterMaintenanceDisableStorageTarget", "EnterMaintenanceFail", "EnterMaintenancePowerOff", "EnterMaintenanceSlotPowerCycle", "EnterMaintenanceSuccess", "EnterMaintenanceWaitForServerShutdown", "ExitMaintenanceBegin", "ExitMaintenanceEnableStorageTarget", "ExitMaintenanceFail", "ExitMaintenanceSuccess", "ExitMaintenanceWaitForHAQuorum", "ExitMaintenanceWaitForSMEConnection", "ExitMaintenanceWaitForServerPowerUp", "HaTakeOverBegin", "HaTakeOverFail", "HaTakeOverPerformHaTakeOver", "HaTakeOverSuccess", "UndeploySystemBegin", "UndeploySystemDisableStorageTarget", "UndeploySystemDisassocStorageController", "UndeploySystemFail", "UndeploySystemPowerOff", "UndeploySystemSlotPowerCycle", "UndeploySystemSuccess", "UndeploySystemUndeployNetwork", "UndeploySystemUndeployPlatform", "UndeploySystemUndeployStorage", "UndeploySystemUndeployTargetIdentity", "UndeploySystemWaitForDisassocCompletion", "UndeploySystemWaitForServerShutdown", "UndeploySystemWaitForUndeployStorage", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "ha_peer_dn": MoPropertyMeta("ha_peer_dn", "haPeerDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "ha_state": MoPropertyMeta("ha_state", "haState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "election-failed", "failover-in-progress", "not-ready", "ready", "unknown"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "leadership": MoPropertyMeta("leadership", "leadership", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "passive", "unknown"], []), 
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_config_issues": MoPropertyMeta("oper_config_issues", "operConfigIssues", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|invalid-config|invicta-uptime-out-of-sync),){0,3}(defaultValue|not-applicable|invalid-config|invicta-uptime-out-of-sync){0,1}""", [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster-degraded", "compute-degraded", "compute-inoperable", "in-maintenance", "offline", "online", "undefined"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "orig_iqn": MoPropertyMeta("orig_iqn", "origIqn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminLeadership": "admin_leadership", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "cimcBackupTriggerStatus": "cimc_backup_trigger_status", 
        "cimcHeartbeatStatus": "cimc_heartbeat_status", 
        "clusterState": "cluster_state", 
        "configState": "config_state", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "deployAction": "deploy_action", 
        "dn": "dn", 
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
        "haPeerDn": "ha_peer_dn", 
        "haState": "ha_state", 
        "id": "id", 
        "leadership": "leadership", 
        "lsDn": "ls_dn", 
        "managingInst": "managing_inst", 
        "name": "name", 
        "operConfigIssues": "oper_config_issues", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "origIqn": "orig_iqn", 
        "peerDn": "peer_dn", 
        "pnDn": "pn_dn", 
        "presence": "presence", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_leadership = None
        self.admin_state = None
        self.child_action = None
        self.cimc_backup_trigger_status = None
        self.cimc_heartbeat_status = None
        self.cluster_state = None
        self.config_state = None
        self.conn_path = None
        self.conn_status = None
        self.deploy_action = None
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
        self.ha_peer_dn = None
        self.ha_state = None
        self.id = None
        self.leadership = None
        self.ls_dn = None
        self.managing_inst = None
        self.oper_config_issues = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.orig_iqn = None
        self.peer_dn = None
        self.pn_dn = None
        self.presence = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageProcessor", parent_mo_or_dn, **kwargs)

