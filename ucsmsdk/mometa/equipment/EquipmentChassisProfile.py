"""This module contains the general information for EquipmentChassisProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentChassisProfileConsts:
    ASSIGN_STATE_ASSIGNED = "assigned"
    ASSIGN_STATE_FAILED = "failed"
    ASSIGN_STATE_UNASSIGNED = "unassigned"
    ASSOC_STATE_ASSOCIATED = "associated"
    ASSOC_STATE_ASSOCIATING = "associating"
    ASSOC_STATE_DISASSOCIATING = "disassociating"
    ASSOC_STATE_FAILED = "failed"
    ASSOC_STATE_UNASSOCIATED = "unassociated"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    FSM_PREV_CONFIGURE_ANALYZE_IMPACT = "ConfigureAnalyzeImpact"
    FSM_PREV_CONFIGURE_APPLY_CONFIG = "ConfigureApplyConfig"
    FSM_PREV_CONFIGURE_APPLY_POLICIES = "ConfigureApplyPolicies"
    FSM_PREV_CONFIGURE_APPLY_TEMPLATE = "ConfigureApplyTemplate"
    FSM_PREV_CONFIGURE_BEGIN = "ConfigureBegin"
    FSM_PREV_CONFIGURE_EVALUATE_ASSOCIATION = "ConfigureEvaluateAssociation"
    FSM_PREV_CONFIGURE_FAIL = "ConfigureFail"
    FSM_PREV_CONFIGURE_RESOLVE_DISTRIBUTABLE = "ConfigureResolveDistributable"
    FSM_PREV_CONFIGURE_RESOLVE_DISTRIBUTABLE_NAMES = "ConfigureResolveDistributableNames"
    FSM_PREV_CONFIGURE_RESOLVE_IMAGES = "ConfigureResolveImages"
    FSM_PREV_CONFIGURE_RESOLVE_POLICIES = "ConfigureResolvePolicies"
    FSM_PREV_CONFIGURE_RESOLVE_SCHEDULE = "ConfigureResolveSchedule"
    FSM_PREV_CONFIGURE_SUCCESS = "ConfigureSuccess"
    FSM_PREV_CONFIGURE_VALIDATE_POLICY_OWNERSHIP = "ConfigureValidatePolicyOwnership"
    FSM_PREV_CONFIGURE_WAIT_FOR_ASSOC_COMPLETION = "ConfigureWaitForAssocCompletion"
    FSM_PREV_CONFIGURE_WAIT_FOR_MAINT_PERMISSION = "ConfigureWaitForMaintPermission"
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
    FSM_STATUS_CONFIGURE_ANALYZE_IMPACT = "ConfigureAnalyzeImpact"
    FSM_STATUS_CONFIGURE_APPLY_CONFIG = "ConfigureApplyConfig"
    FSM_STATUS_CONFIGURE_APPLY_POLICIES = "ConfigureApplyPolicies"
    FSM_STATUS_CONFIGURE_APPLY_TEMPLATE = "ConfigureApplyTemplate"
    FSM_STATUS_CONFIGURE_BEGIN = "ConfigureBegin"
    FSM_STATUS_CONFIGURE_EVALUATE_ASSOCIATION = "ConfigureEvaluateAssociation"
    FSM_STATUS_CONFIGURE_FAIL = "ConfigureFail"
    FSM_STATUS_CONFIGURE_RESOLVE_DISTRIBUTABLE = "ConfigureResolveDistributable"
    FSM_STATUS_CONFIGURE_RESOLVE_DISTRIBUTABLE_NAMES = "ConfigureResolveDistributableNames"
    FSM_STATUS_CONFIGURE_RESOLVE_IMAGES = "ConfigureResolveImages"
    FSM_STATUS_CONFIGURE_RESOLVE_POLICIES = "ConfigureResolvePolicies"
    FSM_STATUS_CONFIGURE_RESOLVE_SCHEDULE = "ConfigureResolveSchedule"
    FSM_STATUS_CONFIGURE_SUCCESS = "ConfigureSuccess"
    FSM_STATUS_CONFIGURE_VALIDATE_POLICY_OWNERSHIP = "ConfigureValidatePolicyOwnership"
    FSM_STATUS_CONFIGURE_WAIT_FOR_ASSOC_COMPLETION = "ConfigureWaitForAssocCompletion"
    FSM_STATUS_CONFIGURE_WAIT_FOR_MAINT_PERMISSION = "ConfigureWaitForMaintPermission"
    FSM_STATUS_NOP = "nop"
    INT_ID_NONE = "none"
    OPER_STATE_CHASSIS_FAILED = "chassis-failed"
    OPER_STATE_CHASSIS_MISMATCH = "chassis-mismatch"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIAGNOSTICS = "diagnostics"
    OPER_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_INACCESSIBLE = "inaccessible"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MAINTENANCE = "maintenance"
    OPER_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    OPER_STATE_OK = "ok"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    OPER_STATE_PENDING_REBOOT = "pending-reboot"
    OPER_STATE_POWER_OFF = "power-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_RESTART = "restart"
    OPER_STATE_TEST = "test"
    OPER_STATE_TEST_FAILED = "test-failed"
    OPER_STATE_UNASSOCIATED = "unassociated"
    OPER_STATE_UNCONFIG = "unconfig"
    OPER_STATE_UNCONFIG_FAILED = "unconfig-failed"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"
    OWNER_TIER = "tier"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    RESOLVE_REMOTE_NO = "no"
    RESOLVE_REMOTE_YES = "yes"
    TYPE_INITIAL_TEMPLATE = "initial-template"
    TYPE_INSTANCE = "instance"
    TYPE_UPDATING_TEMPLATE = "updating-template"


class EquipmentChassisProfile(ManagedObject):
    """This is EquipmentChassisProfile class."""

    consts = EquipmentChassisProfileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentChassisProfile", "equipmentChassisProfile", "cp-[name]", VersionMeta.Version312b, "InputOutput", 0x1ffff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['equipmentTier', 'orgOrg'], ['cpmaintAck', 'equipmentBinding', 'equipmentChassisIssues', 'equipmentChassisProfileAssocCtx', 'equipmentChassisProfileFsm', 'equipmentChassisProfileFsmTask', 'equipmentRequirement', 'eventInst', 'faultInst', 'lstorageDiskZoningConfigDef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assign_state": MoPropertyMeta("assign_state", "assignState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned", "failed", "unassigned"], []),
        "assoc_state": MoPropertyMeta("assoc_state", "assocState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "associating", "disassociating", "failed", "unassociated"], []),
        "chassis_dn": MoPropertyMeta("chassis_dn", "chassisDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "chassis_fw_policy_name": MoPropertyMeta("chassis_fw_policy_name", "chassisFwPolicyName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "compute_conn_policy_name": MoPropertyMeta("compute_conn_policy_name", "computeConnPolicyName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|chassis-profile-not-supported|single-path-not-supported|invalid-cmc-version|migration|single-path-unsupported-cmc-version|single-path-operation-not-supported|firmware-version-mismatch|invalid-sas-exp-config-policy-reference|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|connection-management-unsupported-cmc-version|physical-requirement|single-path-expander-inoperable|connection-management-feature-not-supported|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|unsupported-sas-exp-config-settings|compute-conn-unsupported-cmc-version|connection-management-expander-inoperable|chassis-unavailable|invalid-chassis-pack|single-path-invalid-configuration|connection-management-operation-not-supported|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|single-path-feature-not-supported|compute-second-controller-unsupported-cmc-version|connection-management-not-supported|insufficient-power-budget),){0,32}(defaultValue|not-applicable|chassis-profile-not-supported|single-path-not-supported|invalid-cmc-version|migration|single-path-unsupported-cmc-version|single-path-operation-not-supported|firmware-version-mismatch|invalid-sas-exp-config-policy-reference|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|connection-management-unsupported-cmc-version|physical-requirement|single-path-expander-inoperable|connection-management-feature-not-supported|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|unsupported-sas-exp-config-settings|compute-conn-unsupported-cmc-version|connection-management-expander-inoperable|chassis-unavailable|invalid-chassis-pack|single-path-invalid-configuration|connection-management-operation-not-supported|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|single-path-feature-not-supported|compute-second-controller-unsupported-cmc-version|connection-management-not-supported|insufficient-power-budget){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "disk_zoning_policy_name": MoPropertyMeta("disk_zoning_policy_name", "diskZoningPolicyName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_flags": MoPropertyMeta("fsm_flags", "fsmFlags", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, ["ConfigureAnalyzeImpact", "ConfigureApplyConfig", "ConfigureApplyPolicies", "ConfigureApplyTemplate", "ConfigureBegin", "ConfigureEvaluateAssociation", "ConfigureFail", "ConfigureResolveDistributable", "ConfigureResolveDistributableNames", "ConfigureResolveImages", "ConfigureResolvePolicies", "ConfigureResolveSchedule", "ConfigureSuccess", "ConfigureValidatePolicyOwnership", "ConfigureWaitForAssocCompletion", "ConfigureWaitForMaintPermission", "nop"], []),
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]),
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNLD-usb-unmounted", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-POWER-PROFILE-IN-PROGRESS", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-tp", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-downgrade-fail", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-pwdenc-config-master-key-error", "ERR-pwdenc-delete-master-key-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-key-cert", "ERR-set-login-profile", "ERR-set-min-passphrase-length", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-set-user", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-passwd-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]),
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []),
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []),
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, ["ConfigureAnalyzeImpact", "ConfigureApplyConfig", "ConfigureApplyPolicies", "ConfigureApplyTemplate", "ConfigureBegin", "ConfigureEvaluateAssociation", "ConfigureFail", "ConfigureResolveDistributable", "ConfigureResolveDistributableNames", "ConfigureResolveImages", "ConfigureResolvePolicies", "ConfigureResolveSchedule", "ConfigureSuccess", "ConfigureValidatePolicyOwnership", "ConfigureWaitForAssocCompletion", "ConfigureWaitForMaintPermission", "nop"], []),
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "maint_policy_name": MoPropertyMeta("maint_policy_name", "maintPolicyName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_chassis_fw_policy_name": MoPropertyMeta("oper_chassis_fw_policy_name", "operChassisFwPolicyName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_compute_conn_policy_name": MoPropertyMeta("oper_compute_conn_policy_name", "operComputeConnPolicyName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_disk_zoning_policy_name": MoPropertyMeta("oper_disk_zoning_policy_name", "operDiskZoningPolicyName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_maint_policy_name": MoPropertyMeta("oper_maint_policy_name", "operMaintPolicyName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_sas_expander_config_policy_name": MoPropertyMeta("oper_sas_expander_config_policy_name", "operSasExpanderConfigPolicyName", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_src_templ_name": MoPropertyMeta("oper_src_templ_name", "operSrcTemplName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis-failed", "chassis-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "operable", "pending-reassociation", "pending-reboot", "power-off", "removed", "restart", "test", "test-failed", "unassociated", "unconfig", "unconfig-failed"], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy", "tier"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "resolve_remote": MoPropertyMeta("resolve_remote", "resolveRemote", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["no", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sas_expander_config_policy_name": MoPropertyMeta("sas_expander_config_policy_name", "sasExpanderConfigPolicyName", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "src_templ_name": MoPropertyMeta("src_templ_name", "srcTemplName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version312b, MoPropertyMeta.CREATE_ONLY, 0x8000, None, None, None, ["initial-template", "instance", "updating-template"], []),
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
    }

    prop_map = {
        "assignState": "assign_state", 
        "assocState": "assoc_state", 
        "chassisDn": "chassis_dn", 
        "chassisFwPolicyName": "chassis_fw_policy_name", 
        "childAction": "child_action", 
        "computeConnPolicyName": "compute_conn_policy_name", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "descr": "descr", 
        "diskZoningPolicyName": "disk_zoning_policy_name", 
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
        "intId": "int_id", 
        "maintPolicyName": "maint_policy_name", 
        "name": "name", 
        "operChassisFwPolicyName": "oper_chassis_fw_policy_name", 
        "operComputeConnPolicyName": "oper_compute_conn_policy_name", 
        "operDiskZoningPolicyName": "oper_disk_zoning_policy_name", 
        "operMaintPolicyName": "oper_maint_policy_name", 
        "operSasExpanderConfigPolicyName": "oper_sas_expander_config_policy_name", 
        "operSrcTemplName": "oper_src_templ_name", 
        "operState": "oper_state", 
        "owner": "owner", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "propAcl": "prop_acl", 
        "resolveRemote": "resolve_remote", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sasExpanderConfigPolicyName": "sas_expander_config_policy_name", 
        "srcTemplName": "src_templ_name", 
        "status": "status", 
        "type": "type", 
        "usrLbl": "usr_lbl", 
        "uuid": "uuid", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assign_state = None
        self.assoc_state = None
        self.chassis_dn = None
        self.chassis_fw_policy_name = None
        self.child_action = None
        self.compute_conn_policy_name = None
        self.config_qualifier = None
        self.config_state = None
        self.descr = None
        self.disk_zoning_policy_name = None
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
        self.int_id = None
        self.maint_policy_name = None
        self.oper_chassis_fw_policy_name = None
        self.oper_compute_conn_policy_name = None
        self.oper_disk_zoning_policy_name = None
        self.oper_maint_policy_name = None
        self.oper_sas_expander_config_policy_name = None
        self.oper_src_templ_name = None
        self.oper_state = None
        self.owner = None
        self.policy_level = None
        self.policy_owner = None
        self.prop_acl = None
        self.resolve_remote = None
        self.sacl = None
        self.sas_expander_config_policy_name = None
        self.src_templ_name = None
        self.status = None
        self.type = None
        self.usr_lbl = None
        self.uuid = None

        ManagedObject.__init__(self, "EquipmentChassisProfile", parent_mo_or_dn, **kwargs)
