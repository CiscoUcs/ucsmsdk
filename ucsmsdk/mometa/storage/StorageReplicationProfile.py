"""This module contains the general information for StorageReplicationProfile ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageReplicationProfileConsts():
    ACTION_TYPE_MANUAL = "manual"
    ACTION_TYPE_POLICY = "policy"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    DEPLOY_ACTION_ABORT_REPLICATION = "abort-replication"
    DEPLOY_ACTION_CREATE = "create"
    DEPLOY_ACTION_DELETE = "delete"
    DEPLOY_ACTION_MODIFY = "modify"
    DEPLOY_ACTION_NO_ACTION = "no-action"
    DEPLOY_ACTION_REPLACE = "replace"
    DEPLOY_ACTION_RESTORE = "restore"
    DEPLOY_ACTION_SET_OFFLINE = "set-offline"
    DEPLOY_ACTION_SET_ONLINE = "set-online"
    LAST_ERROR_CODE_CANCELED_BY_USER = "canceled-by user"
    LAST_ERROR_CODE_FAILED_TO_CREATE_TARGET = "failed-to-create-target"
    LAST_ERROR_CODE_FAILED_TO_INCREASE_SIZE = "failed-to-increase-size"
    LAST_ERROR_CODE_FAILED_TO_REPLICATE_METADATA = "failed-to-replicate-metadata"
    LAST_ERROR_CODE_INCORRECT_SHARED_SECRET_KEY = "incorrect-shared-secret-key"
    LAST_ERROR_CODE_INTERNAL_ERROR = "internal-error"
    LAST_ERROR_CODE_LOST_CONNECTION = "lost connection"
    LAST_ERROR_CODE_NONE = "none"
    LAST_ERROR_CODE_NOT_ON_ALLOW_LIST = "not-on-allow-list"
    LAST_ERROR_CODE_SUCCESS = "success"
    LAST_ERROR_CODE_TCP_CONNECTION_FAILED = "tcp-connection-failed"
    LAST_ERROR_CODE_UNSUPPORTED_ASYNCREP_PROTOCOL_VER = "unsupported-asyncrep-protocol-ver"
    PEER_DEVICE_TYPE_LUN = "LUN"
    PEER_DEVICE_TYPE_NFS = "NFS"
    PEER_TYPE_CISCO = "Cisco"
    PEER_TYPE_LINUX_LVM = "Linux-LVM"
    PEER_TYPE_LINUX_RAW = "Linux-RAW"
    PEER_TYPE_WINDOWS = "Windows"
    REPLICATION_STATE_OFFLINE = "offline"
    REPLICATION_STATE_ONLINE = "online"
    REPLICATION_STATUS_IDLE = "idle"
    REPLICATION_STATUS_REPLICATION_IN_PROGRESS = "replication-in-progress"
    REPLICATION_STATUS_RESTORE_IN_PROGRESS = "restore-in-progress"


class StorageReplicationProfile(ManagedObject):
    """This is StorageReplicationProfile class."""

    consts = StorageReplicationProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageReplicationProfile", "storageReplicationProfile", "repl-profile", VersionMeta.Version302c, "InputOutput", 0x1fL, [], ["read-only"], [u'storageScsiLun'], [u'lstorageInvictaReplicationExt', u'trigSched'], [None])

    prop_meta = {
        "action_type": MoPropertyMeta("action_type", "actionType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["manual", "policy"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier_reason": MoPropertyMeta("config_qualifier_reason", "configQualifierReason", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned"], []), 
        "deploy_action": MoPropertyMeta("deploy_action", "deployAction", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["abort-replication", "create", "delete", "modify", "no-action", "replace", "restore", "set-offline", "set-online"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "last_error": MoPropertyMeta("last_error", "lastError", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "last_error_code": MoPropertyMeta("last_error_code", "lastErrorCode", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["canceled-by user", "failed-to-create-target", "failed-to-increase-size", "failed-to-replicate-metadata", "incorrect-shared-secret-key", "internal-error", "lost connection", "none", "not-on-allow-list", "success", "tcp-connection-failed", "unsupported-asyncrep-protocol-ver"], []), 
        "last_replication": MoPropertyMeta("last_replication", "lastReplication", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "last_restore": MoPropertyMeta("last_restore", "lastRestore", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "peer_addr": MoPropertyMeta("peer_addr", "peerAddr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?$|^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*(\.[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$""", [], []), 
        "peer_device_type": MoPropertyMeta("peer_device_type", "peerDeviceType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["LUN", "NFS"], []), 
        "peer_dir": MoPropertyMeta("peer_dir", "peerDir", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "peer_type": MoPropertyMeta("peer_type", "peerType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Cisco", "Linux-LVM", "Linux-RAW", "Windows"], []), 
        "peer_volume": MoPropertyMeta("peer_volume", "peerVolume", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "replication_peer_ep_name": MoPropertyMeta("replication_peer_ep_name", "replicationPeerEpName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "replication_peer_name": MoPropertyMeta("replication_peer_name", "replicationPeerName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "replication_state": MoPropertyMeta("replication_state", "replicationState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["offline", "online"], []), 
        "replication_status": MoPropertyMeta("replication_status", "replicationStatus", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["idle", "replication-in-progress", "restore-in-progress"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "actionType": "action_type", 
        "childAction": "child_action", 
        "configQualifierReason": "config_qualifier_reason", 
        "configState": "config_state", 
        "deployAction": "deploy_action", 
        "dn": "dn", 
        "lastError": "last_error", 
        "lastErrorCode": "last_error_code", 
        "lastReplication": "last_replication", 
        "lastRestore": "last_restore", 
        "peerAddr": "peer_addr", 
        "peerDeviceType": "peer_device_type", 
        "peerDir": "peer_dir", 
        "peerType": "peer_type", 
        "peerVolume": "peer_volume", 
        "replicationPeerEpName": "replication_peer_ep_name", 
        "replicationPeerName": "replication_peer_name", 
        "replicationState": "replication_state", 
        "replicationStatus": "replication_status", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.action_type = None
        self.child_action = None
        self.config_qualifier_reason = None
        self.config_state = None
        self.deploy_action = None
        self.last_error = None
        self.last_error_code = None
        self.last_replication = None
        self.last_restore = None
        self.peer_addr = None
        self.peer_device_type = None
        self.peer_dir = None
        self.peer_type = None
        self.peer_volume = None
        self.replication_peer_ep_name = None
        self.replication_peer_name = None
        self.replication_state = None
        self.replication_status = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageReplicationProfile", parent_mo_or_dn, **kwargs)

