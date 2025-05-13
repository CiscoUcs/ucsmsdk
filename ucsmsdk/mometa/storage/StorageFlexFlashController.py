"""This module contains the general information for StorageFlexFlashController ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageFlexFlashControllerConsts:
    ADMIN_SLOT_NUMBER_1 = "1"
    ADMIN_SLOT_NUMBER_2 = "2"
    ADMIN_SLOT_NUMBER_NA = "NA"
    CONFIGURED_MODE_INDEPENDENT_DRIVES = "independent-drives"
    CONFIGURED_MODE_MIRROR = "mirror"
    CONFIGURED_MODE_UNKNOWN = "unknown"
    CONTROLLER_HEALTH_FFCH_ERROR_CARDS_ACCESS_ERROR = "FFCH_ERROR_CARDS_ACCESS_ERROR"
    CONTROLLER_HEALTH_FFCH_ERROR_CARD_SIZE_MISMATCH = "FFCH_ERROR_CARD_SIZE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_ERROR_INCONSISTANT_METADATA_IGNORED = "FFCH_ERROR_INCONSISTANT_METADATA_IGNORED"
    CONTROLLER_HEALTH_FFCH_ERROR_INVALID_SIZE = "FFCH_ERROR_INVALID_SIZE"
    CONTROLLER_HEALTH_FFCH_ERROR_MEDIA_WRITE_PROTECTED = "FFCH_ERROR_MEDIA_WRITE_PROTECTED"
    CONTROLLER_HEALTH_FFCH_ERROR_OLD_FIRMWARE_RUNNING = "FFCH_ERROR_OLD_FIRMWARE_RUNNING"
    CONTROLLER_HEALTH_FFCH_ERROR_REBOOTED_DURING_REBUILD = "FFCH_ERROR_REBOOTED_DURING_REBUILD"
    CONTROLLER_HEALTH_FFCH_ERROR_SD247_CARD_DETECTED = "FFCH_ERROR_SD247_CARD_DETECTED"
    CONTROLLER_HEALTH_FFCH_ERROR_SD253_WITH_UN_OR_SD247 = "FFCH_ERROR_SD253_WITH_UN_OR_SD247"
    CONTROLLER_HEALTH_FFCH_ERROR_SD_CARD_NOT_CONFIGURED = "FFCH_ERROR_SD_CARD_NOT_CONFIGURED"
    CONTROLLER_HEALTH_FFCH_ERROR_SECONDARY_UNHEALTHY_CARD = "FFCH_ERROR_SECONDARY_UNHEALTHY_CARD"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD0_IGNORED_SD1 = "FFCH_FLEXD_ERROR_IM_SD0_IGNORED_SD1"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD0_SD1_IGNORED = "FFCH_FLEXD_ERROR_IM_SD0_SD1_IGNORED"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD_CARDS_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_IM_SD_CARDS_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD_HEALTHY_SD_UN_IGNORED = "FFCH_FLEXD_ERROR_IM_SD_HEALTHY_SD_UN_IGNORED"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD_UNHEALTHY_SD_UN_IGNORED = "FFCH_FLEXD_ERROR_IM_SD_UNHEALTHY_SD_UN_IGNORED"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD0_HEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD0_HEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD0_UNHEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD0_UNHEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD1_HEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD1_HEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD1_UNHEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD1_UNHEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_OP_MODE_MISMATCH_WITH_UN = "FFCH_FLEXD_ERROR_SD_OP_MODE_MISMATCH_WITH_UN"
    CONTROLLER_HEALTH_FFCH_INCONSISTENT_METADATA = "FFCH_INCONSISTENT_METADATA"
    CONTROLLER_HEALTH_FFCH_METADATA_FAILURE = "FFCH_METADATA_FAILURE"
    CONTROLLER_HEALTH_FFCH_OK = "FFCH_OK"
    CONTROLLER_STATE_FFC_CONFIG = "FFC_CONFIG"
    CONTROLLER_STATE_FFC_FAILED = "FFC_FAILED"
    CONTROLLER_STATE_FFC_INIT = "FFC_INIT"
    CONTROLLER_STATE_FFC_REBUILDING = "FFC_REBUILDING"
    CONTROLLER_STATE_FFC_SOFTWARE_ERR = "FFC_SOFTWARE_ERR"
    CONTROLLER_STATE_FFC_UNINITALIZED = "FFC_UNINITALIZED"
    CONTROLLER_STATE_FFC_USB_CONNECTED = "FFC_USB_CONNECTED"
    CONTROLLER_STATE_FFC_USB_CONNECTING = "FFC_USB_CONNECTING"
    CONTROLLER_STATE_FFC_USB_DISCONNECTED = "FFC_USB_DISCONNECTED"
    CONTROLLER_STATE_FFC_USB_DISCONNECTING = "FFC_USB_DISCONNECTING"
    CONTROLLER_STATE_FFC_WAIT_USER = "FFC_WAIT_USER"
    FLEX_FLASH_TYPE_ASTORIA = "Astoria"
    FLEX_FLASH_TYPE_FX3_S = "FX3S"
    FLEX_FLASH_TYPE_UNKNOWN = "Unknown"
    FSM_PREV_MOPS_FORMAT_BEGIN = "MOpsFormatBegin"
    FSM_PREV_MOPS_FORMAT_FAIL = "MOpsFormatFail"
    FSM_PREV_MOPS_FORMAT_FORMAT = "MOpsFormatFormat"
    FSM_PREV_MOPS_FORMAT_SUCCESS = "MOpsFormatSuccess"
    FSM_PREV_MOPS_PAIR_BEGIN = "MOpsPairBegin"
    FSM_PREV_MOPS_PAIR_FAIL = "MOpsPairFail"
    FSM_PREV_MOPS_PAIR_PAIR = "MOpsPairPair"
    FSM_PREV_MOPS_PAIR_SUCCESS = "MOpsPairSuccess"
    FSM_PREV_MOPS_RESET_BEGIN = "MOpsResetBegin"
    FSM_PREV_MOPS_RESET_FAIL = "MOpsResetFail"
    FSM_PREV_MOPS_RESET_RESET = "MOpsResetReset"
    FSM_PREV_MOPS_RESET_SUCCESS = "MOpsResetSuccess"
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
    FSM_STATUS_MOPS_FORMAT_BEGIN = "MOpsFormatBegin"
    FSM_STATUS_MOPS_FORMAT_FAIL = "MOpsFormatFail"
    FSM_STATUS_MOPS_FORMAT_FORMAT = "MOpsFormatFormat"
    FSM_STATUS_MOPS_FORMAT_SUCCESS = "MOpsFormatSuccess"
    FSM_STATUS_MOPS_PAIR_BEGIN = "MOpsPairBegin"
    FSM_STATUS_MOPS_PAIR_FAIL = "MOpsPairFail"
    FSM_STATUS_MOPS_PAIR_PAIR = "MOpsPairPair"
    FSM_STATUS_MOPS_PAIR_SUCCESS = "MOpsPairSuccess"
    FSM_STATUS_MOPS_RESET_BEGIN = "MOpsResetBegin"
    FSM_STATUS_MOPS_RESET_FAIL = "MOpsResetFail"
    FSM_STATUS_MOPS_RESET_RESET = "MOpsResetReset"
    FSM_STATUS_MOPS_RESET_SUCCESS = "MOpsResetSuccess"
    FSM_STATUS_NOP = "nop"
    HAS_ERROR_ERROR = "error"
    HAS_ERROR_NO_ERROR = "no_error"
    HOTSWAP_THERMAL_LOWER_CRITICAL = "lower-critical"
    HOTSWAP_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    HOTSWAP_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    HOTSWAP_THERMAL_NOT_SUPPORTED = "not-supported"
    HOTSWAP_THERMAL_OK = "ok"
    HOTSWAP_THERMAL_UNKNOWN = "unknown"
    HOTSWAP_THERMAL_UPPER_CRITICAL = "upper-critical"
    HOTSWAP_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    HOTSWAP_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    INLET2_THERMAL_LOWER_CRITICAL = "lower-critical"
    INLET2_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    INLET2_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    INLET2_THERMAL_NOT_SUPPORTED = "not-supported"
    INLET2_THERMAL_OK = "ok"
    INLET2_THERMAL_UNKNOWN = "unknown"
    INLET2_THERMAL_UPPER_CRITICAL = "upper-critical"
    INLET2_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    INLET2_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    IS_CARD_MISMATCH_MATCH = "MATCH"
    IS_CARD_MISMATCH_MISMATCH = "MISMATCH"
    IS_CARD_MISMATCH_NA = "NA"
    IS_FORMAT_FSMRUNNING_NA = "NA"
    IS_FORMAT_FSMRUNNING_NO = "NO"
    IS_FORMAT_FSMRUNNING_YES = "YES"
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
    OPERATING_MODE_INDEPENDENT_DRIVES = "independent-drives"
    OPERATING_MODE_MIRROR = "mirror"
    OPERATING_MODE_UNKNOWN = "unknown"
    OPERATION_REQUEST_FORMAT = "format"
    OPERATION_REQUEST_PAIR = "pair"
    OPERATION_REQUEST_RESET = "reset"
    OPERATION_REQUEST_UNKNOWN = "unknown"
    OPERATION_REQUEST_UNPAIR = "unpair"
    OUTLET_THERMAL_LOWER_CRITICAL = "lower-critical"
    OUTLET_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    OUTLET_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    OUTLET_THERMAL_NOT_SUPPORTED = "not-supported"
    OUTLET_THERMAL_OK = "ok"
    OUTLET_THERMAL_UNKNOWN = "unknown"
    OUTLET_THERMAL_UPPER_CRITICAL = "upper-critical"
    OUTLET_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    OUTLET_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
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
    RAID_SYNC_SUPPORT_NO = "no"
    RAID_SYNC_SUPPORT_YES = "yes"
    SUB_TYPE_NA = "NA"
    SUB_TYPE_NVME_FRONT = "NVME-FRONT"
    SUB_TYPE_NVME_HHHL = "NVME-HHHL"
    SUB_TYPE_NVME_M2 = "NVME-M2"
    SUB_TYPE_NVME_MEZZ = "NVME-MEZZ"
    SUB_TYPE_NVME_REAR = "NVME-REAR"
    SUB_TYPE_RDE = "RDE"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    TYPE_FCH = "FCH"
    TYPE_FLASH = "FLASH"
    TYPE_HBA = "HBA"
    TYPE_M2 = "M2"
    TYPE_NVME = "NVME"
    TYPE_PCH = "PCH"
    TYPE_PT = "PT"
    TYPE_SAS = "SAS"
    TYPE_SATA = "SATA"
    TYPE_SD = "SD"
    TYPE_EXTERNAL = "external"
    TYPE_UNKNOWN = "unknown"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class StorageFlexFlashController(ManagedObject):
    """This is StorageFlexFlashController class."""

    consts = StorageFlexFlashControllerConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageFlexFlashController", "storageFlexFlashController", "storage-flexflash-[id]", VersionMeta.Version221b, "InputOutput", 0xff, [], ["admin"], ['computeBoard'], ['eventInst', 'faultInst', 'firmwareRunning', 'storageFlexFlashCard', 'storageFlexFlashControllerFsm', 'storageFlexFlashControllerFsmTask', 'storageFlexFlashVirtualDrive', 'storageLocalDiskConfigDef'], ["Get"])

    prop_meta = {
        "admin_slot_number": MoPropertyMeta("admin_slot_number", "adminSlotNumber", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["1", "2", "NA"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "configured_mode": MoPropertyMeta("configured_mode", "configuredMode", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["independent-drives", "mirror", "unknown"], []),
        "controller_health": MoPropertyMeta("controller_health", "controllerHealth", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FFCH_ERROR_CARDS_ACCESS_ERROR", "FFCH_ERROR_CARD_SIZE_MISMATCH", "FFCH_ERROR_INCONSISTANT_METADATA_IGNORED", "FFCH_ERROR_INVALID_SIZE", "FFCH_ERROR_MEDIA_WRITE_PROTECTED", "FFCH_ERROR_OLD_FIRMWARE_RUNNING", "FFCH_ERROR_REBOOTED_DURING_REBUILD", "FFCH_ERROR_SD247_CARD_DETECTED", "FFCH_ERROR_SD253_WITH_UN_OR_SD247", "FFCH_ERROR_SD_CARD_NOT_CONFIGURED", "FFCH_ERROR_SECONDARY_UNHEALTHY_CARD", "FFCH_FLEXD_ERROR_IM_SD0_IGNORED_SD1", "FFCH_FLEXD_ERROR_IM_SD0_SD1_IGNORED", "FFCH_FLEXD_ERROR_IM_SD_CARDS_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_IM_SD_HEALTHY_SD_UN_IGNORED", "FFCH_FLEXD_ERROR_IM_SD_UNHEALTHY_SD_UN_IGNORED", "FFCH_FLEXD_ERROR_SD_CARD0_HEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD0_UNHEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD1_HEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD1_UNHEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_OP_MODE_MISMATCH_WITH_UN", "FFCH_INCONSISTENT_METADATA", "FFCH_METADATA_FAILURE", "FFCH_OK"], []),
        "controller_state": MoPropertyMeta("controller_state", "controllerState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FFC_CONFIG", "FFC_FAILED", "FFC_INIT", "FFC_REBUILDING", "FFC_SOFTWARE_ERR", "FFC_UNINITALIZED", "FFC_USB_CONNECTED", "FFC_USB_CONNECTING", "FFC_USB_DISCONNECTED", "FFC_USB_DISCONNECTING", "FFC_WAIT_USER"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "flex_flash_type": MoPropertyMeta("flex_flash_type", "flexFlashType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Astoria", "FX3S", "Unknown"], []),
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, None, ["MOpsFormatBegin", "MOpsFormatFail", "MOpsFormatFormat", "MOpsFormatSuccess", "MOpsPairBegin", "MOpsPairFail", "MOpsPairPair", "MOpsPairSuccess", "MOpsResetBegin", "MOpsResetFail", "MOpsResetReset", "MOpsResetSuccess", "nop"], []),
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]),
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNLD-usb-unmounted", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-POWER-PROFILE-IN-PROGRESS", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-tp", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-downgrade-fail", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-pwdenc-config-master-key-error", "ERR-pwdenc-delete-master-key-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-key-cert", "ERR-set-login-profile", "ERR-set-min-passphrase-length", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-set-user", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-passwd-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]),
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []),
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []),
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, None, ["MOpsFormatBegin", "MOpsFormatFail", "MOpsFormatFormat", "MOpsFormatSuccess", "MOpsPairBegin", "MOpsPairFail", "MOpsPairPair", "MOpsPairSuccess", "MOpsResetBegin", "MOpsResetFail", "MOpsResetReset", "MOpsResetSuccess", "nop"], []),
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "has_error": MoPropertyMeta("has_error", "hasError", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error", "no_error"], []),
        "hotswap_thermal": MoPropertyMeta("hotswap_thermal", "hotswapThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-64"]),
        "inlet2_thermal": MoPropertyMeta("inlet2_thermal", "inlet2Thermal", "string", VersionMeta.Version423b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "is_card_mismatch": MoPropertyMeta("is_card_mismatch", "isCardMismatch", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["MATCH", "MISMATCH", "NA"], []),
        "is_format_fsm_running": MoPropertyMeta("is_format_fsm_running", "isFormatFSMRunning", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "NO", "YES"], []),
        "location_dn": MoPropertyMeta("location_dn", "locationDn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operating_mode": MoPropertyMeta("operating_mode", "operatingMode", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["independent-drives", "mirror", "unknown"], []),
        "operation_request": MoPropertyMeta("operation_request", "operationRequest", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["format", "pair", "reset", "unknown", "unpair"], []),
        "outlet_thermal": MoPropertyMeta("outlet_thermal", "outletThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "physical_drive_count": MoPropertyMeta("physical_drive_count", "physicalDriveCount", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "primary_slot_number": MoPropertyMeta("primary_slot_number", "primarySlotNumber", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "raid_sync_support": MoPropertyMeta("raid_sync_support", "raidSyncSupport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "read_error_threshold": MoPropertyMeta("read_error_threshold", "readErrorThreshold", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sub_type": MoPropertyMeta("sub_type", "subType", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "NVME-FRONT", "NVME-HHHL", "NVME-M2", "NVME-MEZZ", "NVME-REAR", "RDE"], []),
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FCH", "FLASH", "HBA", "M2", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "virtual_drive_count": MoPropertyMeta("virtual_drive_count", "virtualDriveCount", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "write_error_threshold": MoPropertyMeta("write_error_threshold", "writeErrorThreshold", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
    }

    prop_map = {
        "adminSlotNumber": "admin_slot_number", 
        "childAction": "child_action", 
        "configuredMode": "configured_mode", 
        "controllerHealth": "controller_health", 
        "controllerState": "controller_state", 
        "dn": "dn", 
        "firmwareVersion": "firmware_version", 
        "flexFlashType": "flex_flash_type", 
        "fsmDescr": "fsm_descr", 
        "fsmPrev": "fsm_prev", 
        "fsmProgr": "fsm_progr", 
        "fsmRmtInvErrCode": "fsm_rmt_inv_err_code", 
        "fsmRmtInvErrDescr": "fsm_rmt_inv_err_descr", 
        "fsmRmtInvRslt": "fsm_rmt_inv_rslt", 
        "fsmStageDescr": "fsm_stage_descr", 
        "fsmStamp": "fsm_stamp", 
        "fsmStatus": "fsm_status", 
        "fsmTry": "fsm_try", 
        "hasError": "has_error", 
        "hotswapThermal": "hotswap_thermal", 
        "id": "id", 
        "inlet2Thermal": "inlet2_thermal", 
        "isCardMismatch": "is_card_mismatch", 
        "isFormatFSMRunning": "is_format_fsm_running", 
        "locationDn": "location_dn", 
        "model": "model", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "operatingMode": "operating_mode", 
        "operationRequest": "operation_request", 
        "outletThermal": "outlet_thermal", 
        "pciAddr": "pci_addr", 
        "pciSlot": "pci_slot", 
        "perf": "perf", 
        "physicalDriveCount": "physical_drive_count", 
        "power": "power", 
        "presence": "presence", 
        "primarySlotNumber": "primary_slot_number", 
        "raidSyncSupport": "raid_sync_support", 
        "readErrorThreshold": "read_error_threshold", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "subType": "sub_type", 
        "thermal": "thermal", 
        "type": "type", 
        "vendor": "vendor", 
        "virtualDriveCount": "virtual_drive_count", 
        "voltage": "voltage", 
        "writeErrorThreshold": "write_error_threshold", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_slot_number = None
        self.child_action = None
        self.configured_mode = None
        self.controller_health = None
        self.controller_state = None
        self.firmware_version = None
        self.flex_flash_type = None
        self.fsm_descr = None
        self.fsm_prev = None
        self.fsm_progr = None
        self.fsm_rmt_inv_err_code = None
        self.fsm_rmt_inv_err_descr = None
        self.fsm_rmt_inv_rslt = None
        self.fsm_stage_descr = None
        self.fsm_stamp = None
        self.fsm_status = None
        self.fsm_try = None
        self.has_error = None
        self.hotswap_thermal = None
        self.inlet2_thermal = None
        self.is_card_mismatch = None
        self.is_format_fsm_running = None
        self.location_dn = None
        self.model = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.operating_mode = None
        self.operation_request = None
        self.outlet_thermal = None
        self.pci_addr = None
        self.pci_slot = None
        self.perf = None
        self.physical_drive_count = None
        self.power = None
        self.presence = None
        self.primary_slot_number = None
        self.raid_sync_support = None
        self.read_error_threshold = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.sub_type = None
        self.thermal = None
        self.type = None
        self.vendor = None
        self.virtual_drive_count = None
        self.voltage = None
        self.write_error_threshold = None

        ManagedObject.__init__(self, "StorageFlexFlashController", parent_mo_or_dn, **kwargs)
