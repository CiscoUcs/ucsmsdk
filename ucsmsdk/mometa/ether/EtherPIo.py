"""This module contains the general information for EtherPIo ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherPIoConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CHASSIS_ID_N_A = "N/A"
    ENCAP_DOT1Q = "dot1q"
    ENCAP_ISL = "isl"
    ENCAP_NEGOTIATE = "negotiate"
    ENCAP_PROPRIETARY = "proprietary"
    ENCAP_UNKNOWN = "unknown"
    FSM_PREV_IN_COMPAT_SFP_PRESENCE_BEGIN = "InCompatSfpPresenceBegin"
    FSM_PREV_IN_COMPAT_SFP_PRESENCE_FAIL = "InCompatSfpPresenceFail"
    FSM_PREV_IN_COMPAT_SFP_PRESENCE_SHUTDOWN = "InCompatSfpPresenceShutdown"
    FSM_PREV_IN_COMPAT_SFP_PRESENCE_SUCCESS = "InCompatSfpPresenceSuccess"
    FSM_PREV_IN_COMPAT_SFP_REPLACED_BEGIN = "InCompatSfpReplacedBegin"
    FSM_PREV_IN_COMPAT_SFP_REPLACED_ENABLE_PORT = "InCompatSfpReplacedEnablePort"
    FSM_PREV_IN_COMPAT_SFP_REPLACED_FAIL = "InCompatSfpReplacedFail"
    FSM_PREV_IN_COMPAT_SFP_REPLACED_SUCCESS = "InCompatSfpReplacedSuccess"
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
    FSM_STATUS_IN_COMPAT_SFP_PRESENCE_BEGIN = "InCompatSfpPresenceBegin"
    FSM_STATUS_IN_COMPAT_SFP_PRESENCE_FAIL = "InCompatSfpPresenceFail"
    FSM_STATUS_IN_COMPAT_SFP_PRESENCE_SHUTDOWN = "InCompatSfpPresenceShutdown"
    FSM_STATUS_IN_COMPAT_SFP_PRESENCE_SUCCESS = "InCompatSfpPresenceSuccess"
    FSM_STATUS_IN_COMPAT_SFP_REPLACED_BEGIN = "InCompatSfpReplacedBegin"
    FSM_STATUS_IN_COMPAT_SFP_REPLACED_ENABLE_PORT = "InCompatSfpReplacedEnablePort"
    FSM_STATUS_IN_COMPAT_SFP_REPLACED_FAIL = "InCompatSfpReplacedFail"
    FSM_STATUS_IN_COMPAT_SFP_REPLACED_SUCCESS = "InCompatSfpReplacedSuccess"
    FSM_STATUS_NOP = "nop"
    IF_ROLE_DIAG = "diag"
    IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    IF_ROLE_FCOE_STORAGE = "fcoe-storage"
    IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
    IF_ROLE_MGMT = "mgmt"
    IF_ROLE_MONITOR = "monitor"
    IF_ROLE_NAS_STORAGE = "nas-storage"
    IF_ROLE_NETWORK = "network"
    IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    IF_ROLE_SERVER = "server"
    IF_ROLE_SERVICE = "service"
    IF_ROLE_STORAGE = "storage"
    IF_ROLE_UNKNOWN = "unknown"
    IF_TYPE_AGGREGATION = "aggregation"
    IF_TYPE_PHYSICAL = "physical"
    IF_TYPE_UNKNOWN = "unknown"
    IF_TYPE_VIRTUAL = "virtual"
    IS_BREAKOUT_XCVR_FALSE = "false"
    IS_BREAKOUT_XCVR_NO = "no"
    IS_BREAKOUT_XCVR_TRUE = "true"
    IS_BREAKOUT_XCVR_YES = "yes"
    IS_PORT_CHANNEL_MEMBER_FALSE = "false"
    IS_PORT_CHANNEL_MEMBER_NO = "no"
    IS_PORT_CHANNEL_MEMBER_TRUE = "true"
    IS_PORT_CHANNEL_MEMBER_YES = "yes"
    IS_UPLINK_PEER_PORT_STP_FALSE = "false"
    IS_UPLINK_PEER_PORT_STP_NO = "no"
    IS_UPLINK_PEER_PORT_STP_TRUE = "true"
    IS_UPLINK_PEER_PORT_STP_YES = "yes"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    MODE_E = "E"
    MODE_F = "F"
    MODE_SD = "SD"
    MODE_ACCESS = "access"
    MODE_FABRIC = "fabric"
    MODE_N_PROXY = "n_proxy"
    MODE_PROMISCUOUS_ACCESS = "promiscuousAccess"
    MODE_PROMISCUOUS_TRUNK = "promiscuousTrunk"
    MODE_TRUNK = "trunk"
    MODE_UNKNOWN = "unknown"
    MODE_VNTAG = "vntag"
    NON_CR4_FALSE = "false"
    NON_CR4_NO = "no"
    NON_CR4_TRUE = "true"
    NON_CR4_YES = "yes"
    OPER_SPEED_100GBPS = "100gbps"
    OPER_SPEED_10GBPS = "10gbps"
    OPER_SPEED_1GBPS = "1gbps"
    OPER_SPEED_20GBPS = "20gbps"
    OPER_SPEED_25GBPS = "25gbps"
    OPER_SPEED_40GBPS = "40gbps"
    OPER_SPEED_AUTO = "auto"
    OPER_SPEED_INDETERMINATE = "indeterminate"
    OPER_STATE_ADMIN_DOWN = "admin-down"
    OPER_STATE_DOWN = "down"
    OPER_STATE_ERROR_DISABLED = "error-disabled"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_HARDWARE_FAILURE = "hardware-failure"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_LINK_DOWN = "link-down"
    OPER_STATE_LINK_UP = "link-up"
    OPER_STATE_NO_LICENSE = "no-license"
    OPER_STATE_SFP_NOT_PRESENT = "sfp-not-present"
    OPER_STATE_SOFTWARE_FAILURE = "software-failure"
    OPER_STATE_UDLD_AGGR_DOWN = "udld-aggr-down"
    OPER_STATE_UP = "up"
    PEER_CHASSIS_ID_N_A = "N/A"
    PORT_CAPABILITY_ETH_APPLIANT_PORT = "ethAppliantPort"
    PORT_CAPABILITY_ETH_FEX_SERVER_PORT = "ethFexServerPort"
    PORT_CAPABILITY_ETH_RACK_SERVER_PORT = "ethRackServerPort"
    PORT_CAPABILITY_ETH_UPLINK_PORT = "ethUplinkPort"
    PORT_CAPABILITY_NOT_APPLICABLE = "notApplicable"
    PORT_CAPABILITY_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    UNIFIED_PORT_FALSE = "false"
    UNIFIED_PORT_NO = "no"
    UNIFIED_PORT_TRUE = "true"
    UNIFIED_PORT_YES = "yes"
    XCVR_TYPE_10_25_GBASE = "10/25Gbase"
    XCVR_TYPE_10_25_GBASELRS = "10/25Gbaselrs"
    XCVR_TYPE_1000BASECX = "1000basecx"
    XCVR_TYPE_1000BASELH = "1000baselh"
    XCVR_TYPE_1000BASELX = "1000baselx"
    XCVR_TYPE_1000BASESX = "1000basesx"
    XCVR_TYPE_1000BASET = "1000baset"
    XCVR_TYPE_1000BASEUNKNOWN = "1000baseunknown"
    XCVR_TYPE_1000BASEVX = "1000basevx"
    XCVR_TYPE_1000BASEX = "1000basex"
    XCVR_TYPE_1000BASEZX = "1000basezx"
    XCVR_TYPE_10GBASEER = "10gbaseer"
    XCVR_TYPE_10GBASELR = "10gbaselr"
    XCVR_TYPE_10GBASELRM = "10gbaselrm"
    XCVR_TYPE_10GBASELRS = "10gbaselrs"
    XCVR_TYPE_10GBASESR = "10gbasesr"
    XCVR_TYPE_10GBASESRS = "10gbasesrs"
    XCVR_TYPE_10GBASEZR = "10gbasezr"
    XCVR_TYPE_10GBASEZRS = "10gbasezrs"
    XCVR_TYPE_10GBX40DI = "10gbx40di"
    XCVR_TYPE_10GBX40UI = "10gbx40ui"
    XCVR_TYPE_10GBXDI = "10gbxdi"
    XCVR_TYPE_10GBXUI = "10gbxui"
    XCVR_TYPE_4X32GSW = "4x32gsw"
    XCVR_TYPE_CWDM1471 = "cwdm1471"
    XCVR_TYPE_CWDM1531 = "cwdm1531"
    XCVR_TYPE_CWDM1551 = "cwdm1551"
    XCVR_TYPE_DWDMSFP = "dwdmsfp"
    XCVR_TYPE_FET = "fet"
    XCVR_TYPE_H10GACU10M = "h10gacu10m"
    XCVR_TYPE_H10GACU15M = "h10gacu15m"
    XCVR_TYPE_H10GACU1M = "h10gacu1m"
    XCVR_TYPE_H10GACU3M = "h10gacu3m"
    XCVR_TYPE_H10GACU5M = "h10gacu5m"
    XCVR_TYPE_H10GACU7M = "h10gacu7m"
    XCVR_TYPE_H10GACUAOC10M = "h10gacuaoc10m"
    XCVR_TYPE_H10GACUAOC15M = "h10gacuaoc15m"
    XCVR_TYPE_H10GACUAOC1M = "h10gacuaoc1m"
    XCVR_TYPE_H10GACUAOC2M = "h10gacuaoc2m"
    XCVR_TYPE_H10GACUAOC3M = "h10gacuaoc3m"
    XCVR_TYPE_H10GACUAOC5M = "h10gacuaoc5m"
    XCVR_TYPE_H10GACUAOC7M = "h10gacuaoc7m"
    XCVR_TYPE_H10GAOC10M = "h10gaoc10m"
    XCVR_TYPE_H10GAOC15M = "h10gaoc15m"
    XCVR_TYPE_H10GAOC1M = "h10gaoc1m"
    XCVR_TYPE_H10GAOC2M = "h10gaoc2m"
    XCVR_TYPE_H10GAOC3M = "h10gaoc3m"
    XCVR_TYPE_H10GAOC5M = "h10gaoc5m"
    XCVR_TYPE_H10GAOC7M = "h10gaoc7m"
    XCVR_TYPE_H10GCU1_5M = "h10gcu1-5m"
    XCVR_TYPE_H10GCU10M = "h10gcu10m"
    XCVR_TYPE_H10GCU1M = "h10gcu1m"
    XCVR_TYPE_H10GCU2_5M = "h10gcu2-5m"
    XCVR_TYPE_H10GCU2M = "h10gcu2m"
    XCVR_TYPE_H10GCU3M = "h10gcu3m"
    XCVR_TYPE_H10GCU5M = "h10gcu5m"
    XCVR_TYPE_H10GCU7M = "h10gcu7m"
    XCVR_TYPE_H10GLRMSM = "h10glrmsm"
    XCVR_TYPE_H10GTX = "h10gtx"
    XCVR_TYPE_H10GUSR = "h10gusr"
    XCVR_TYPE_H25GAOC10M = "h25gaoc10m"
    XCVR_TYPE_H25GAOC1M = "h25gaoc1m"
    XCVR_TYPE_H25GAOC2M = "h25gaoc2m"
    XCVR_TYPE_H25GAOC3M = "h25gaoc3m"
    XCVR_TYPE_H25GAOC4M = "h25gaoc4m"
    XCVR_TYPE_H25GAOC5M = "h25gaoc5m"
    XCVR_TYPE_H25GAOC7M = "h25gaoc7m"
    XCVR_TYPE_H25GCU1M = "h25gcu1m"
    XCVR_TYPE_H25GCU2M = "h25gcu2m"
    XCVR_TYPE_H25GCU3M = "h25gcu3m"
    XCVR_TYPE_H25GCU4M = "h25gcu4m"
    XCVR_TYPE_H25GCU5M = "h25gcu5m"
    XCVR_TYPE_H25GLRS = "h25glrs"
    XCVR_TYPE_H25GSRS = "h25gsrs"
    XCVR_TYPE_QSFP100G40GBIDI = "qsfp100g40gbidi"
    XCVR_TYPE_QSFP100GAOC10M = "qsfp100gaoc10m"
    XCVR_TYPE_QSFP100GAOC15M = "qsfp100gaoc15m"
    XCVR_TYPE_QSFP100GAOC1M = "qsfp100gaoc1m"
    XCVR_TYPE_QSFP100GAOC20M = "qsfp100gaoc20m"
    XCVR_TYPE_QSFP100GAOC25M = "qsfp100gaoc25m"
    XCVR_TYPE_QSFP100GAOC2M = "qsfp100gaoc2m"
    XCVR_TYPE_QSFP100GAOC30M = "qsfp100gaoc30m"
    XCVR_TYPE_QSFP100GAOC3M = "qsfp100gaoc3m"
    XCVR_TYPE_QSFP100GAOC5M = "qsfp100gaoc5m"
    XCVR_TYPE_QSFP100GAOC7M = "qsfp100gaoc7m"
    XCVR_TYPE_QSFP100GCR4 = "qsfp100gcr4"
    XCVR_TYPE_QSFP100GCU1M = "qsfp100gcu1m"
    XCVR_TYPE_QSFP100GCU2M = "qsfp100gcu2m"
    XCVR_TYPE_QSFP100GCU3M = "qsfp100gcu3m"
    XCVR_TYPE_QSFP100GDR = "qsfp100gdr"
    XCVR_TYPE_QSFP100GFR = "qsfp100gfr"
    XCVR_TYPE_QSFP100GLR4S = "qsfp100glr4s"
    XCVR_TYPE_QSFP100GPSM4S = "qsfp100gpsm4s"
    XCVR_TYPE_QSFP100GSL4 = "qsfp100gsl4"
    XCVR_TYPE_QSFP100GSMSR = "qsfp100gsmsr"
    XCVR_TYPE_QSFP100GSR1_2 = "qsfp100gsr1.2"
    XCVR_TYPE_QSFP100GSR4 = "qsfp100gsr4"
    XCVR_TYPE_QSFP100GSR4S = "qsfp100gsr4s"
    XCVR_TYPE_QSFP40GCR4 = "qsfp40gcr4"
    XCVR_TYPE_QSFP40GCSR = "qsfp40gcsr"
    XCVR_TYPE_QSFP40GCSR4 = "qsfp40gcsr4"
    XCVR_TYPE_QSFP40GER4 = "qsfp40ger4"
    XCVR_TYPE_QSFP40GFET = "qsfp40gfet"
    XCVR_TYPE_QSFP40GLR4 = "qsfp40glr4"
    XCVR_TYPE_QSFP40GSR4 = "qsfp40gsr4"
    XCVR_TYPE_QSFP40GSRBD = "qsfp40gsrbd"
    XCVR_TYPE_QSFP4SFP10GCU1M = "qsfp4sfp10gcu1m"
    XCVR_TYPE_QSFP4SFP10GCU2M = "qsfp4sfp10gcu2m"
    XCVR_TYPE_QSFP4SFP10GCU3M = "qsfp4sfp10gcu3m"
    XCVR_TYPE_QSFP4SFP10GCU4M = "qsfp4sfp10gcu4m"
    XCVR_TYPE_QSFP4SFP10GCU5M = "qsfp4sfp10gcu5m"
    XCVR_TYPE_QSFP4SFP25GCU1M = "qsfp4sfp25gcu1m"
    XCVR_TYPE_QSFP4SFP25GCU2M = "qsfp4sfp25gcu2m"
    XCVR_TYPE_QSFP4SFP25GCU3M = "qsfp4sfp25gcu3m"
    XCVR_TYPE_QSFP4SFP25GCU5M = "qsfp4sfp25gcu5m"
    XCVR_TYPE_QSFP4SFP25GUNKNOWN = "qsfp4sfp25gunknown"
    XCVR_TYPE_QSFP4X10GA0C10M = "qsfp4x10ga0c10m"
    XCVR_TYPE_QSFP4X10GA0C1M = "qsfp4x10ga0c1m"
    XCVR_TYPE_QSFP4X10GA0C2M = "qsfp4x10ga0c2m"
    XCVR_TYPE_QSFP4X10GA0C3M = "qsfp4x10ga0c3m"
    XCVR_TYPE_QSFP4X10GA0C5M = "qsfp4x10ga0c5m"
    XCVR_TYPE_QSFP4X10GA0C7M = "qsfp4x10ga0c7m"
    XCVR_TYPE_QSFP4X10GA0CUNKNOWN = "qsfp4x10ga0cunknown"
    XCVR_TYPE_QSFP4X10GAC10M = "qsfp4x10gac10m"
    XCVR_TYPE_QSFP4X10GAC1M = "qsfp4x10gac1m"
    XCVR_TYPE_QSFP4X10GAC3M = "qsfp4x10gac3m"
    XCVR_TYPE_QSFP4X10GAC5M = "qsfp4x10gac5m"
    XCVR_TYPE_QSFP4X10GAC7M = "qsfp4x10gac7m"
    XCVR_TYPE_QSFP4X10GLR = "qsfp4x10glr"
    XCVR_TYPE_QSFP4X10GLRS = "qsfp4x10glrs"
    XCVR_TYPE_QSFPH40GACU10M = "qsfph40gacu10m"
    XCVR_TYPE_QSFPH40GACU1M = "qsfph40gacu1m"
    XCVR_TYPE_QSFPH40GACU3M = "qsfph40gacu3m"
    XCVR_TYPE_QSFPH40GACU5M = "qsfph40gacu5m"
    XCVR_TYPE_QSFPH40GACU7M = "qsfph40gacu7m"
    XCVR_TYPE_QSFPH40GAOC10M = "qsfph40gaoc10m"
    XCVR_TYPE_QSFPH40GAOC15M = "qsfph40gaoc15m"
    XCVR_TYPE_QSFPH40GAOC1M = "qsfph40gaoc1m"
    XCVR_TYPE_QSFPH40GAOC20M = "qsfph40gaoc20m"
    XCVR_TYPE_QSFPH40GAOC2M = "qsfph40gaoc2m"
    XCVR_TYPE_QSFPH40GAOC30M = "qsfph40gaoc30m"
    XCVR_TYPE_QSFPH40GAOC3M = "qsfph40gaoc3m"
    XCVR_TYPE_QSFPH40GAOC5M = "qsfph40gaoc5m"
    XCVR_TYPE_QSFPH40GAOC7M = "qsfph40gaoc7m"
    XCVR_TYPE_QSFPH40GAOCUNKNOWN = "qsfph40gaocunknown"
    XCVR_TYPE_QSFPH40GCU1M = "qsfph40gcu1m"
    XCVR_TYPE_QSFPH40GCU2M = "qsfph40gcu2m"
    XCVR_TYPE_QSFPH40GCU3M = "qsfph40gcu3m"
    XCVR_TYPE_QSFPH40GCU5M = "qsfph40gcu5m"
    XCVR_TYPE_QSFPLOOP = "qsfploop"
    XCVR_TYPE_QSFPQSA = "qsfpqsa"
    XCVR_TYPE_QSFPUNKNOWN = "qsfpunknown"
    XCVR_TYPE_SFP = "sfp"
    XCVR_TYPE_SFP25GSL = "sfp25gsl"
    XCVR_TYPE_UNKNOWN = "unknown"
    XCVR_TYPE_X2 = "x2"


class EtherPIo(ManagedObject):
    """This is EtherPIo class."""

    consts = EtherPIoConsts()
    naming_props = set(['portId'])

    mo_meta = MoMeta("EtherPIo", "etherPIo", "port-[port_id]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["read-only"], ['portGroup', 'portSubGroup'], ['equipmentXcvr', 'etherErrStats', 'etherLossStats', 'etherMacSecRxStats', 'etherMacSecSession', 'etherMacSecTxStats', 'etherNiErrStats', 'etherPIoEndPoint', 'etherPIoFsm', 'etherPauseStats', 'etherRxStats', 'etherTxStats', 'eventInst', 'faultInst', 'lldpAcquired', 'networkIfStats', 'portDomainEp', 'portPIoFsm', 'portPIoFsmTask'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "admin_transport": MoPropertyMeta("admin_transport", "adminTransport", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "encap": MoPropertyMeta("encap", "encap", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["dot1q", "isl", "negotiate", "proprietary", "unknown"], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["InCompatSfpPresenceBegin", "InCompatSfpPresenceFail", "InCompatSfpPresenceShutdown", "InCompatSfpPresenceSuccess", "InCompatSfpReplacedBegin", "InCompatSfpReplacedEnablePort", "InCompatSfpReplacedFail", "InCompatSfpReplacedSuccess", "nop"], []),
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]),
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNLD-usb-unmounted", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-POWER-PROFILE-IN-PROGRESS", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-tp", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-downgrade-fail", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-pwdenc-config-master-key-error", "ERR-pwdenc-delete-master-key-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-key-cert", "ERR-set-login-profile", "ERR-set-min-passphrase-length", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-set-user", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-passwd-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]),
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []),
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []),
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["InCompatSfpPresenceBegin", "InCompatSfpPresenceFail", "InCompatSfpPresenceShutdown", "InCompatSfpPresenceSuccess", "InCompatSfpReplacedBegin", "InCompatSfpReplacedEnablePort", "InCompatSfpReplacedFail", "InCompatSfpReplacedSuccess", "nop"], []),
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "is_breakout_xcvr": MoPropertyMeta("is_breakout_xcvr", "isBreakoutXcvr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "is_port_channel_member": MoPropertyMeta("is_port_channel_member", "isPortChannelMember", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "is_uplink_peer_port_stp": MoPropertyMeta("is_uplink_peer_port_stp", "isUplinkPeerPortStp", "string", VersionMeta.Version422d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []),
        "licensing_msg": MoPropertyMeta("licensing_msg", "licensingMsg", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["E", "F", "SD", "access", "fabric", "n_proxy", "promiscuousAccess", "promiscuousTrunk", "trunk", "unknown", "vntag"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "non_c_r4": MoPropertyMeta("non_c_r4", "nonCR4", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error-disabled", "failed", "hardware-failure", "indeterminate", "link-down", "link-up", "no-license", "sfp-not-present", "software-failure", "udld-aggr-down", "up"], []),
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "port_capability": MoPropertyMeta("port_capability", "portCapability", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ethAppliantPort", "ethFexServerPort", "ethRackServerPort", "ethUplinkPort", "notApplicable", "unknown"], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "ts": MoPropertyMeta("ts", "ts", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "unified_port": MoPropertyMeta("unified_port", "unifiedPort", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "xcvr_type": MoPropertyMeta("xcvr_type", "xcvrType", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10/25Gbase", "10/25Gbaselrs", "1000basecx", "1000baselh", "1000baselx", "1000basesx", "1000baset", "1000baseunknown", "1000basevx", "1000basex", "1000basezx", "10gbaseer", "10gbaselr", "10gbaselrm", "10gbaselrs", "10gbasesr", "10gbasesrs", "10gbasezr", "10gbasezrs", "10gbx40di", "10gbx40ui", "10gbxdi", "10gbxui", "4x32gsw", "cwdm1471", "cwdm1531", "cwdm1551", "dwdmsfp", "fet", "h10gacu10m", "h10gacu15m", "h10gacu1m", "h10gacu3m", "h10gacu5m", "h10gacu7m", "h10gacuaoc10m", "h10gacuaoc15m", "h10gacuaoc1m", "h10gacuaoc2m", "h10gacuaoc3m", "h10gacuaoc5m", "h10gacuaoc7m", "h10gaoc10m", "h10gaoc15m", "h10gaoc1m", "h10gaoc2m", "h10gaoc3m", "h10gaoc5m", "h10gaoc7m", "h10gcu1-5m", "h10gcu10m", "h10gcu1m", "h10gcu2-5m", "h10gcu2m", "h10gcu3m", "h10gcu5m", "h10gcu7m", "h10glrmsm", "h10gtx", "h10gusr", "h25gaoc10m", "h25gaoc1m", "h25gaoc2m", "h25gaoc3m", "h25gaoc4m", "h25gaoc5m", "h25gaoc7m", "h25gcu1m", "h25gcu2m", "h25gcu3m", "h25gcu4m", "h25gcu5m", "h25glrs", "h25gsrs", "qsfp100g40gbidi", "qsfp100gaoc10m", "qsfp100gaoc15m", "qsfp100gaoc1m", "qsfp100gaoc20m", "qsfp100gaoc25m", "qsfp100gaoc2m", "qsfp100gaoc30m", "qsfp100gaoc3m", "qsfp100gaoc5m", "qsfp100gaoc7m", "qsfp100gcr4", "qsfp100gcu1m", "qsfp100gcu2m", "qsfp100gcu3m", "qsfp100gdr", "qsfp100gfr", "qsfp100glr4s", "qsfp100gpsm4s", "qsfp100gsl4", "qsfp100gsmsr", "qsfp100gsr1.2", "qsfp100gsr4", "qsfp100gsr4s", "qsfp40gcr4", "qsfp40gcsr", "qsfp40gcsr4", "qsfp40ger4", "qsfp40gfet", "qsfp40glr4", "qsfp40gsr4", "qsfp40gsrbd", "qsfp4sfp10gcu1m", "qsfp4sfp10gcu2m", "qsfp4sfp10gcu3m", "qsfp4sfp10gcu4m", "qsfp4sfp10gcu5m", "qsfp4sfp25gcu1m", "qsfp4sfp25gcu2m", "qsfp4sfp25gcu3m", "qsfp4sfp25gcu5m", "qsfp4sfp25gunknown", "qsfp4x10ga0c10m", "qsfp4x10ga0c1m", "qsfp4x10ga0c2m", "qsfp4x10ga0c3m", "qsfp4x10ga0c5m", "qsfp4x10ga0c7m", "qsfp4x10ga0cunknown", "qsfp4x10gac10m", "qsfp4x10gac1m", "qsfp4x10gac3m", "qsfp4x10gac5m", "qsfp4x10gac7m", "qsfp4x10glr", "qsfp4x10glrs", "qsfph40gacu10m", "qsfph40gacu1m", "qsfph40gacu3m", "qsfph40gacu5m", "qsfph40gacu7m", "qsfph40gaoc10m", "qsfph40gaoc15m", "qsfph40gaoc1m", "qsfph40gaoc20m", "qsfph40gaoc2m", "qsfph40gaoc30m", "qsfph40gaoc3m", "qsfph40gaoc5m", "qsfph40gaoc7m", "qsfph40gaocunknown", "qsfph40gcu1m", "qsfph40gcu2m", "qsfph40gcu3m", "qsfph40gcu5m", "qsfploop", "qsfpqsa", "qsfpunknown", "sfp", "sfp25gsl", "unknown", "x2"], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "adminTransport": "admin_transport", 
        "aggrPortId": "aggr_port_id", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "encap": "encap", 
        "epDn": "ep_dn", 
        "fltAggr": "flt_aggr", 
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
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "isBreakoutXcvr": "is_breakout_xcvr", 
        "isPortChannelMember": "is_port_channel_member", 
        "isUplinkPeerPortStp": "is_uplink_peer_port_stp", 
        "lc": "lc", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "licensingMsg": "licensing_msg", 
        "locale": "locale", 
        "mac": "mac", 
        "mode": "mode", 
        "model": "model", 
        "name": "name", 
        "nonCR4": "non_c_r4", 
        "operSpeed": "oper_speed", 
        "operState": "oper_state", 
        "peerAggrPortId": "peer_aggr_port_id", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "portCapability": "port_capability", 
        "portId": "port_id", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "slotId": "slot_id", 
        "stateQual": "state_qual", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "ts": "ts", 
        "type": "type", 
        "unifiedPort": "unified_port", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
        "xcvrType": "xcvr_type", 
    }

    def __init__(self, parent_mo_or_dn, port_id, **kwargs):
        self._dirty_mask = 0
        self.port_id = port_id
        self.admin_state = None
        self.admin_transport = None
        self.aggr_port_id = None
        self.chassis_id = None
        self.child_action = None
        self.encap = None
        self.ep_dn = None
        self.flt_aggr = None
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
        self.if_role = None
        self.if_type = None
        self.is_breakout_xcvr = None
        self.is_port_channel_member = None
        self.is_uplink_peer_port_stp = None
        self.lc = None
        self.lic_gp = None
        self.lic_state = None
        self.licensing_msg = None
        self.locale = None
        self.mac = None
        self.mode = None
        self.model = None
        self.name = None
        self.non_c_r4 = None
        self.oper_speed = None
        self.oper_state = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.port_capability = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.slot_id = None
        self.state_qual = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.ts = None
        self.type = None
        self.unified_port = None
        self.usr_lbl = None
        self.vendor = None
        self.xcvr_type = None

        ManagedObject.__init__(self, "EtherPIo", parent_mo_or_dn, **kwargs)
