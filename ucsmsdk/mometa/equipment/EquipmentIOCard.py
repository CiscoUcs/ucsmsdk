"""This module contains the general information for EquipmentIOCard ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentIOCardConsts:
    ADMIN_PEER_POWER_STATE_CYCLE_IMMEDIATE = "cycle-immediate"
    ADMIN_PEER_POWER_STATE_CYCLE_WAIT = "cycle-wait"
    ADMIN_PEER_POWER_STATE_POLICY = "policy"
    ADMIN_POWER_STATE_CYCLE_IMMEDIATE = "cycle-immediate"
    ADMIN_POWER_STATE_CYCLE_WAIT = "cycle-wait"
    ADMIN_POWER_STATE_POLICY = "policy"
    ADMIN_STATE_ACKNOWLEDGED = "acknowledged"
    ADMIN_STATE_AUTO_ACKNOWLEDGE = "auto-acknowledge"
    ADMIN_STATE_DECOMMISSION = "decommission"
    ADMIN_STATE_DISABLE_PORT_CHANNEL = "disable-port-channel"
    ADMIN_STATE_ENABLE_PORT_CHANNEL = "enable-port-channel"
    ADMIN_STATE_RE_ACKNOWLEDGE = "re-acknowledge"
    ADMIN_STATE_REMOVE = "remove"
    CHASSIS_ID_N_A = "N/A"
    CONFIG_STATE_ACK_IN_PROGRESS = "ack-in-progress"
    CONFIG_STATE_ACKNOWLEDGED = "acknowledged"
    CONFIG_STATE_AUTO_ACK = "auto-ack"
    CONFIG_STATE_EVALUATION = "evaluation"
    CONFIG_STATE_OK = "ok"
    CONFIG_STATE_REMOVING = "removing"
    CONFIG_STATE_UN_ACKNOWLEDGED = "un-acknowledged"
    CONFIG_STATE_UN_INITIALIZED = "un-initialized"
    CONFIG_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    DISCOVERY_AUTO_UPGRADING = "auto-upgrading"
    DISCOVERY_DISCOVERED = "discovered"
    DISCOVERY_OFFLINE = "offline"
    DISCOVERY_ONLINE = "online"
    DISCOVERY_PINGLOST = "pinglost"
    DISCOVERY_UNKNOWN = "unknown"
    DISCOVERY_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    FE_OFFLINE_TS_NEVER = "never"
    FE_READY_TS_NEVER = "never"
    FSM_PREV_EVACUATE_BEGIN = "EvacuateBegin"
    FSM_PREV_EVACUATE_EXECUTE = "EvacuateExecute"
    FSM_PREV_EVACUATE_FAIL = "EvacuateFail"
    FSM_PREV_EVACUATE_SUCCESS = "EvacuateSuccess"
    FSM_PREV_FE_CONN_BEGIN = "FeConnBegin"
    FSM_PREV_FE_CONN_CONFIGURE_END_POINT = "FeConnConfigureEndPoint"
    FSM_PREV_FE_CONN_CONFIGURE_SW_MGMT_END_POINT = "FeConnConfigureSwMgmtEndPoint"
    FSM_PREV_FE_CONN_CONFIGURE_VIF_NS = "FeConnConfigureVifNs"
    FSM_PREV_FE_CONN_DISCOVER_CHASSIS = "FeConnDiscoverChassis"
    FSM_PREV_FE_CONN_ENABLE_CHASSIS = "FeConnEnableChassis"
    FSM_PREV_FE_CONN_FAIL = "FeConnFail"
    FSM_PREV_FE_CONN_SUCCESS = "FeConnSuccess"
    FSM_PREV_FE_PRESENCE_BEGIN = "FePresenceBegin"
    FSM_PREV_FE_PRESENCE_CHECK_LICENSE = "FePresenceCheckLicense"
    FSM_PREV_FE_PRESENCE_CONFIG_CHASSIS_ID = "FePresenceConfigChassisId"
    FSM_PREV_FE_PRESENCE_FAIL = "FePresenceFail"
    FSM_PREV_FE_PRESENCE_IDENTIFY = "FePresenceIdentify"
    FSM_PREV_FE_PRESENCE_SUCCESS = "FePresenceSuccess"
    FSM_PREV_RESET_CMC_BEGIN = "ResetCmcBegin"
    FSM_PREV_RESET_CMC_EXECUTE = "ResetCmcExecute"
    FSM_PREV_RESET_CMC_FAIL = "ResetCmcFail"
    FSM_PREV_RESET_CMC_SUCCESS = "ResetCmcSuccess"
    FSM_PREV_RESET_EVACUATE_BEGIN = "ResetEvacuateBegin"
    FSM_PREV_RESET_EVACUATE_EXECUTE = "ResetEvacuateExecute"
    FSM_PREV_RESET_EVACUATE_FAIL = "ResetEvacuateFail"
    FSM_PREV_RESET_EVACUATE_SUCCESS = "ResetEvacuateSuccess"
    FSM_PREV_RESET_IOM_BEGIN = "ResetIomBegin"
    FSM_PREV_RESET_IOM_EXECUTE = "ResetIomExecute"
    FSM_PREV_RESET_IOM_FAIL = "ResetIomFail"
    FSM_PREV_RESET_IOM_SUCCESS = "ResetIomSuccess"
    FSM_PREV_RESET_PEER_CMC_BEGIN = "ResetPeerCmcBegin"
    FSM_PREV_RESET_PEER_CMC_EXECUTE = "ResetPeerCmcExecute"
    FSM_PREV_RESET_PEER_CMC_FAIL = "ResetPeerCmcFail"
    FSM_PREV_RESET_PEER_CMC_SUCCESS = "ResetPeerCmcSuccess"
    FSM_PREV_MUX_OFFLINE_BEGIN = "muxOfflineBegin"
    FSM_PREV_MUX_OFFLINE_CLEANUP_ENTRIES = "muxOfflineCleanupEntries"
    FSM_PREV_MUX_OFFLINE_FAIL = "muxOfflineFail"
    FSM_PREV_MUX_OFFLINE_SUCCESS = "muxOfflineSuccess"
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
    FSM_RMT_INV_ERR_CODE_ERR_SET_MIN_PASSPHRASE_LENGTH = "ERR-set-min-passphrase-length"
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
    FSM_STATUS_EVACUATE_BEGIN = "EvacuateBegin"
    FSM_STATUS_EVACUATE_EXECUTE = "EvacuateExecute"
    FSM_STATUS_EVACUATE_FAIL = "EvacuateFail"
    FSM_STATUS_EVACUATE_SUCCESS = "EvacuateSuccess"
    FSM_STATUS_FE_CONN_BEGIN = "FeConnBegin"
    FSM_STATUS_FE_CONN_CONFIGURE_END_POINT = "FeConnConfigureEndPoint"
    FSM_STATUS_FE_CONN_CONFIGURE_SW_MGMT_END_POINT = "FeConnConfigureSwMgmtEndPoint"
    FSM_STATUS_FE_CONN_CONFIGURE_VIF_NS = "FeConnConfigureVifNs"
    FSM_STATUS_FE_CONN_DISCOVER_CHASSIS = "FeConnDiscoverChassis"
    FSM_STATUS_FE_CONN_ENABLE_CHASSIS = "FeConnEnableChassis"
    FSM_STATUS_FE_CONN_FAIL = "FeConnFail"
    FSM_STATUS_FE_CONN_SUCCESS = "FeConnSuccess"
    FSM_STATUS_FE_PRESENCE_BEGIN = "FePresenceBegin"
    FSM_STATUS_FE_PRESENCE_CHECK_LICENSE = "FePresenceCheckLicense"
    FSM_STATUS_FE_PRESENCE_CONFIG_CHASSIS_ID = "FePresenceConfigChassisId"
    FSM_STATUS_FE_PRESENCE_FAIL = "FePresenceFail"
    FSM_STATUS_FE_PRESENCE_IDENTIFY = "FePresenceIdentify"
    FSM_STATUS_FE_PRESENCE_SUCCESS = "FePresenceSuccess"
    FSM_STATUS_RESET_CMC_BEGIN = "ResetCmcBegin"
    FSM_STATUS_RESET_CMC_EXECUTE = "ResetCmcExecute"
    FSM_STATUS_RESET_CMC_FAIL = "ResetCmcFail"
    FSM_STATUS_RESET_CMC_SUCCESS = "ResetCmcSuccess"
    FSM_STATUS_RESET_EVACUATE_BEGIN = "ResetEvacuateBegin"
    FSM_STATUS_RESET_EVACUATE_EXECUTE = "ResetEvacuateExecute"
    FSM_STATUS_RESET_EVACUATE_FAIL = "ResetEvacuateFail"
    FSM_STATUS_RESET_EVACUATE_SUCCESS = "ResetEvacuateSuccess"
    FSM_STATUS_RESET_IOM_BEGIN = "ResetIomBegin"
    FSM_STATUS_RESET_IOM_EXECUTE = "ResetIomExecute"
    FSM_STATUS_RESET_IOM_FAIL = "ResetIomFail"
    FSM_STATUS_RESET_IOM_SUCCESS = "ResetIomSuccess"
    FSM_STATUS_RESET_PEER_CMC_BEGIN = "ResetPeerCmcBegin"
    FSM_STATUS_RESET_PEER_CMC_EXECUTE = "ResetPeerCmcExecute"
    FSM_STATUS_RESET_PEER_CMC_FAIL = "ResetPeerCmcFail"
    FSM_STATUS_RESET_PEER_CMC_SUCCESS = "ResetPeerCmcSuccess"
    FSM_STATUS_MUX_OFFLINE_BEGIN = "muxOfflineBegin"
    FSM_STATUS_MUX_OFFLINE_CLEANUP_ENTRIES = "muxOfflineCleanupEntries"
    FSM_STATUS_MUX_OFFLINE_FAIL = "muxOfflineFail"
    FSM_STATUS_MUX_OFFLINE_SUCCESS = "muxOfflineSuccess"
    FSM_STATUS_NOP = "nop"
    MFG_TIME_NOT_APPLICABLE = "not-applicable"
    OPER_EVAC_STATE_DRAIN = "drain"
    OPER_EVAC_STATE_FILL = "fill"
    OPER_EVAC_STATE_UNKNOWN = "unknown"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    OPER_STATE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPER_STATE_CHASSIS_INTRUSION = "chassis-intrusion"
    OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
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
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
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
    OPERABILITY_UNSUPPORTED_CONFIG = "unsupported-config"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    PEER_COMM_STATUS_CONNECTED = "connected"
    PEER_COMM_STATUS_DISCONNECTED = "disconnected"
    PEER_COMM_STATUS_UNKNOWN = "unknown"
    PERF_LOWER_CRITICAL = "lower-critical"
    PERF_LOWER_NON_CRITICAL = "lower-non-critical"
    PERF_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    PERF_NOT_SUPPORTED = "not-supported"
    PERF_OK = "ok"
    PERF_UNKNOWN = "unknown"
    PERF_UPPER_CRITICAL = "upper-critical"
    PERF_UPPER_NON_CRITICAL = "upper-non-critical"
    PERF_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    POWER_DEGRADED = "degraded"
    POWER_ERROR = "error"
    POWER_FAILED = "failed"
    POWER_NOT_SUPPORTED = "not-supported"
    POWER_OFF = "off"
    POWER_OFFDUTY = "offduty"
    POWER_OFFLINE = "offline"
    POWER_OK = "ok"
    POWER_ON = "on"
    POWER_ONLINE = "online"
    POWER_POWER_SAVE = "power-save"
    POWER_TEST = "test"
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
    PROCESSOR_THERMAL_STATE_LOWER_CRITICAL = "lower-critical"
    PROCESSOR_THERMAL_STATE_LOWER_NON_CRITICAL = "lower-non-critical"
    PROCESSOR_THERMAL_STATE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    PROCESSOR_THERMAL_STATE_NOT_SUPPORTED = "not-supported"
    PROCESSOR_THERMAL_STATE_OK = "ok"
    PROCESSOR_THERMAL_STATE_UNKNOWN = "unknown"
    PROCESSOR_THERMAL_STATE_UPPER_CRITICAL = "upper-critical"
    PROCESSOR_THERMAL_STATE_UPPER_NON_CRITICAL = "upper-non-critical"
    PROCESSOR_THERMAL_STATE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    SIDE_LEFT = "left"
    SIDE_RIGHT = "right"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class EquipmentIOCard(ManagedObject):
    """This is EquipmentIOCard class."""

    consts = EquipmentIOCardConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("EquipmentIOCard", "equipmentIOCard", "slot-[id]", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["admin", "ls-network", "ls-network-policy", "pn-equipment", "pn-maintenance", "pn-policy"], [u'equipmentChassis', u'equipmentFex'], [u'equipmentBeaconLed', u'equipmentHealthLed', u'equipmentIOCardBaseFsm', u'equipmentIOCardBaseFsmTask', u'equipmentIOCardFsm', u'equipmentIOCardFsmTask', u'equipmentIOCardStats', u'equipmentIndicatorLed', u'equipmentLocatorLed', u'equipmentPOST', u'eventInst', u'faultInst', u'faultSuppressTask', u'firmwareStatus', u'mgmtController', u'portGroup'], ["Get", "Set"])

    prop_meta = {
        "admin_peer_power_state": MoPropertyMeta("admin_peer_power_state", "adminPeerPowerState", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cycle-immediate", "cycle-wait", "policy"], []), 
        "admin_power_state": MoPropertyMeta("admin_power_state", "adminPowerState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["cycle-immediate", "cycle-wait", "policy"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["acknowledged", "auto-acknowledge", "decommission", "disable-port-channel", "enable-port-channel", "re-acknowledge", "remove"], []), 
        "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "base_addr": MoPropertyMeta("base_addr", "baseAddr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto-upgrading", "discovered", "offline", "online", "pinglost", "unknown", "unsupported-connectivity"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "fe_offline_ts": MoPropertyMeta("fe_offline_ts", "feOfflineTs", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["never"], ["0-18446744073709551615"]), 
        "fe_ready_ts": MoPropertyMeta("fe_ready_ts", "feReadyTs", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["never"], ["0-18446744073709551615"]), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_flags": MoPropertyMeta("fsm_flags", "fsmFlags", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["EvacuateBegin", "EvacuateExecute", "EvacuateFail", "EvacuateSuccess", "FeConnBegin", "FeConnConfigureEndPoint", "FeConnConfigureSwMgmtEndPoint", "FeConnConfigureVifNs", "FeConnDiscoverChassis", "FeConnEnableChassis", "FeConnFail", "FeConnSuccess", "FePresenceBegin", "FePresenceCheckLicense", "FePresenceConfigChassisId", "FePresenceFail", "FePresenceIdentify", "FePresenceSuccess", "ResetCmcBegin", "ResetCmcExecute", "ResetCmcFail", "ResetCmcSuccess", "ResetEvacuateBegin", "ResetEvacuateExecute", "ResetEvacuateFail", "ResetEvacuateSuccess", "ResetIomBegin", "ResetIomExecute", "ResetIomFail", "ResetIomSuccess", "ResetPeerCmcBegin", "ResetPeerCmcExecute", "ResetPeerCmcFail", "ResetPeerCmcSuccess", "muxOfflineBegin", "muxOfflineCleanupEntries", "muxOfflineFail", "muxOfflineSuccess", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNLD-usb-unmounted", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-POWER-PROFILE-IN-PROGRESS", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-tp", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-downgrade-fail", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-key-cert", "ERR-set-min-passphrase-length", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["EvacuateBegin", "EvacuateExecute", "EvacuateFail", "EvacuateSuccess", "FeConnBegin", "FeConnConfigureEndPoint", "FeConnConfigureSwMgmtEndPoint", "FeConnConfigureVifNs", "FeConnDiscoverChassis", "FeConnEnableChassis", "FeConnFail", "FeConnSuccess", "FePresenceBegin", "FePresenceCheckLicense", "FePresenceConfigChassisId", "FePresenceFail", "FePresenceIdentify", "FePresenceSuccess", "ResetCmcBegin", "ResetCmcExecute", "ResetCmcFail", "ResetCmcSuccess", "ResetEvacuateBegin", "ResetEvacuateExecute", "ResetEvacuateFail", "ResetEvacuateSuccess", "ResetIomBegin", "ResetIomExecute", "ResetIomFail", "ResetIomSuccess", "ResetPeerCmcBegin", "ResetPeerCmcExecute", "ResetPeerCmcFail", "ResetPeerCmcSuccess", "muxOfflineBegin", "muxOfflineCleanupEntries", "muxOfflineFail", "muxOfflineSuccess", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-2"]), 
        "lc_name": MoPropertyMeta("lc_name", "lcName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "lc_ts": MoPropertyMeta("lc_ts", "lcTs", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "mfg_time": MoPropertyMeta("mfg_time", "mfgTime", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["not-applicable"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_evac_state": MoPropertyMeta("oper_evac_state", "operEvacState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["drain", "fill", "unknown"], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|thermal|inoperable|voltage|perf|power|removed|fabric-port-problem|post-failure|server-port-problem|fabricpc-link-auto-ack-blocked|backplane-port-problem),){0,12}(defaultValue|not-applicable|thermal|inoperable|voltage|perf|power|removed|fabric-port-problem|post-failure|server-port-problem|fabricpc-link-auto-ack-blocked|backplane-port-problem){0,1}""", [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []), 
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "peer_comm_status": MoPropertyMeta("peer_comm_status", "peerCommStatus", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "disconnected", "unknown"], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "processor_thermal_state": MoPropertyMeta("processor_thermal_state", "processorThermalState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "side": MoPropertyMeta("side", "side", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["left", "right"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "upgrade_status": MoPropertyMeta("upgrade_status", "upgradeStatus", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unasserted|hw-change-detected|fw-change-detected|hw-incompatible|fw-incompatible|unsupported-hw-version|unsupported-fw-version|hw-change-success|fw-change-success),){0,9}(defaultValue|unasserted|hw-change-detected|fw-change-detected|hw-incompatible|fw-incompatible|unsupported-hw-version|unsupported-fw-version|hw-change-success|fw-change-success){0,1}""", [], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
    }

    prop_map = {
        "adminPeerPowerState": "admin_peer_power_state", 
        "adminPowerState": "admin_power_state", 
        "adminState": "admin_state", 
        "assetTag": "asset_tag", 
        "baseAddr": "base_addr", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "discovery": "discovery", 
        "dn": "dn", 
        "feOfflineTs": "fe_offline_ts", 
        "feReadyTs": "fe_ready_ts", 
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
        "lcName": "lc_name", 
        "lcTs": "lc_ts", 
        "mfgTime": "mfg_time", 
        "model": "model", 
        "operEvacState": "oper_evac_state", 
        "operQualifier": "oper_qualifier", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "partNumber": "part_number", 
        "peerCommStatus": "peer_comm_status", 
        "peerDn": "peer_dn", 
        "perf": "perf", 
        "power": "power", 
        "presence": "presence", 
        "processorThermalState": "processor_thermal_state", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "side": "side", 
        "status": "status", 
        "switchId": "switch_id", 
        "thermal": "thermal", 
        "upgradeStatus": "upgrade_status", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
        "vid": "vid", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_peer_power_state = None
        self.admin_power_state = None
        self.admin_state = None
        self.asset_tag = None
        self.base_addr = None
        self.chassis_id = None
        self.child_action = None
        self.config_state = None
        self.discovery = None
        self.fe_offline_ts = None
        self.fe_ready_ts = None
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
        self.lc_name = None
        self.lc_ts = None
        self.mfg_time = None
        self.model = None
        self.oper_evac_state = None
        self.oper_qualifier = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.part_number = None
        self.peer_comm_status = None
        self.peer_dn = None
        self.perf = None
        self.power = None
        self.presence = None
        self.processor_thermal_state = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.side = None
        self.status = None
        self.switch_id = None
        self.thermal = None
        self.upgrade_status = None
        self.usr_lbl = None
        self.vendor = None
        self.vid = None
        self.voltage = None

        ManagedObject.__init__(self, "EquipmentIOCard", parent_mo_or_dn, **kwargs)
