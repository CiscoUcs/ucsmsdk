"""This module contains the general information for CimcvmediaActualMountEntry ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CimcvmediaActualMountEntryConsts:
    AUTH_OPTION_DEFAULT = "default"
    AUTH_OPTION_NONE = "none"
    AUTH_OPTION_NTLM = "ntlm"
    AUTH_OPTION_NTLMI = "ntlmi"
    AUTH_OPTION_NTLMSSP = "ntlmssp"
    AUTH_OPTION_NTLMSSPI = "ntlmsspi"
    AUTH_OPTION_NTLMV2 = "ntlmv2"
    AUTH_OPTION_NTLMV2I = "ntlmv2i"
    DEVICE_TYPE_CDD = "cdd"
    DEVICE_TYPE_HDD = "hdd"
    DEVICE_TYPE_UNKNOWN = "unknown"
    ERROR_TYPE_ALREADY_MAPPED = "already-mapped"
    ERROR_TYPE_AUTHENTICATION_FAILED = "authentication-failed"
    ERROR_TYPE_BAD_PARAM = "bad-param"
    ERROR_TYPE_BAD_PATH = "bad-path"
    ERROR_TYPE_CONNECTION_REJECTED = "connection-rejected"
    ERROR_TYPE_CONNECTION_TIMEOUT = "connection-timeout"
    ERROR_TYPE_DISK_EJECTED = "disk-ejected"
    ERROR_TYPE_DISK_IO_FAILURE = "disk-io-failure"
    ERROR_TYPE_FILE_NOT_FOUND = "file-not-found"
    ERROR_TYPE_GENERIC_FAILURE = "generic-failure"
    ERROR_TYPE_HTTP_SERVER_NO_CONTENT_LENGTH = "http-server-no-content-length"
    ERROR_TYPE_HTTP_SERVER_NO_RANGE_SUPPORT = "http-server-no-range-support"
    ERROR_TYPE_IMAGE_STORE_FULL = "image-store-full"
    ERROR_TYPE_IMGAGE_DELETED = "imgage-deleted"
    ERROR_TYPE_INVALID_ARGUMENT = "invalid-argument"
    ERROR_TYPE_INVALID_VDISK_TYPE = "invalid-vdisk-type"
    ERROR_TYPE_INVALID_VDISK_USAGE = "invalid-vdisk-usage"
    ERROR_TYPE_MOUNT_IN_USE = "mount-in-use"
    ERROR_TYPE_NONE = "none"
    ERROR_TYPE_OPEN_RO_FAILED = "open-ro-failed"
    ERROR_TYPE_OPEN_RW_FAILED = "open-rw-failed"
    ERROR_TYPE_POSTMAP_ERROR = "postmap-error"
    ERROR_TYPE_UNKNOWN = "unknown"
    ERROR_TYPE_WRITE_TO_READONLY_FILE = "write-to-readonly-file"
    IMAGE_NAME_VARIABLE_NONE = "none"
    IMAGE_NAME_VARIABLE_SERVICE_PROFILE_NAME = "service-profile-name"
    MOUNT_PROTOCOL_CIFS = "cifs"
    MOUNT_PROTOCOL_HTTP = "http"
    MOUNT_PROTOCOL_HTTPS = "https"
    MOUNT_PROTOCOL_NFS = "nfs"
    MOUNT_PROTOCOL_UNKNOWN = "unknown"
    OPER_MOUNT_STATUS_MOUNT_EJECTED_BY_OS = "mount-ejected-by-os"
    OPER_MOUNT_STATUS_MOUNT_FAILED = "mount-failed"
    OPER_MOUNT_STATUS_MOUNTED = "mounted"
    OPER_MOUNT_STATUS_MOUNTING = "mounting"
    OPER_MOUNT_STATUS_NOT_MOUNTED = "not-mounted"
    OPER_MOUNT_STATUS_UNKNOWN = "unknown"
    OPER_MOUNT_STATUS_UNMOUNT_FAILED = "unmount-failed"
    OPER_MOUNT_STATUS_UNMOUNTING = "unmounting"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"
    REMAP_ON_EJECT_FALSE = "false"
    REMAP_ON_EJECT_NO = "no"
    REMAP_ON_EJECT_TRUE = "true"
    REMAP_ON_EJECT_YES = "yes"
    WRITABLE_FALSE = "false"
    WRITABLE_NO = "no"
    WRITABLE_TRUE = "true"
    WRITABLE_YES = "yes"


class CimcvmediaActualMountEntry(ManagedObject):
    """This is CimcvmediaActualMountEntry class."""

    consts = CimcvmediaActualMountEntryConsts()
    naming_props = set(['virtualDiskId'])

    mo_meta = MoMeta("CimcvmediaActualMountEntry", "cimcvmediaActualMountEntry", "actual-mount-entry-[virtual_disk_id]", VersionMeta.Version222c, "InputOutput", 0xfffff, [], ["read-only"], ['cimcvmediaActualMountList'], ['faultInst'], ["Get"])

    prop_meta = {
        "auth_option": MoPropertyMeta("auth_option", "authOption", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["default", "none", "ntlm", "ntlmi", "ntlmssp", "ntlmsspi", "ntlmv2", "ntlmv2i"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "device_type": MoPropertyMeta("device_type", "deviceType", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["cdd", "hdd", "unknown"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "enc_pwd": MoPropertyMeta("enc_pwd", "encPwd", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "error_type": MoPropertyMeta("error_type", "errorType", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["already-mapped", "authentication-failed", "bad-param", "bad-path", "connection-rejected", "connection-timeout", "disk-ejected", "disk-io-failure", "file-not-found", "generic-failure", "http-server-no-content-length", "http-server-no-range-support", "image-store-full", "imgage-deleted", "invalid-argument", "invalid-vdisk-type", "invalid-vdisk-usage", "mount-in-use", "none", "open-ro-failed", "open-rw-failed", "postmap-error", "unknown", "write-to-readonly-file"], []),
        "image_file_name": MoPropertyMeta("image_file_name", "imageFileName", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "image_name_variable": MoPropertyMeta("image_name_variable", "imageNameVariable", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["none", "service-profile-name"], []),
        "image_path": MoPropertyMeta("image_path", "imagePath", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "mapping_name": MoPropertyMeta("mapping_name", "mappingName", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "mount_protocol": MoPropertyMeta("mount_protocol", "mountProtocol", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["cifs", "http", "https", "nfs", "unknown"], []),
        "oper_mount_status": MoPropertyMeta("oper_mount_status", "operMountStatus", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["mount-ejected-by-os", "mount-failed", "mounted", "mounting", "not-mounted", "unknown", "unmount-failed", "unmounting"], []),
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,128}""", [], []),
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "remap_on_eject": MoPropertyMeta("remap_on_eject", "remapOnEject", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["false", "no", "true", "yes"], []),
        "remote_host": MoPropertyMeta("remote_host", "remoteHost", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []),
        "remote_ip_address": MoPropertyMeta("remote_ip_address", "remoteIpAddress", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []),
        "remote_port": MoPropertyMeta("remote_port", "remotePort", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "user_id": MoPropertyMeta("user_id", "userId", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20000, 0, 63, None, [], []),
        "virtual_disk_id": MoPropertyMeta("virtual_disk_id", "virtualDiskId", "byte", VersionMeta.Version222c, MoPropertyMeta.NAMING, 0x40000, None, None, None, [], ["0-8"]),
        "writable": MoPropertyMeta("writable", "writable", "string", VersionMeta.Version411a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "authOption": "auth_option", 
        "childAction": "child_action", 
        "deviceType": "device_type", 
        "dn": "dn", 
        "encPwd": "enc_pwd", 
        "errorType": "error_type", 
        "imageFileName": "image_file_name", 
        "imageNameVariable": "image_name_variable", 
        "imagePath": "image_path", 
        "mappingName": "mapping_name", 
        "mountProtocol": "mount_protocol", 
        "operMountStatus": "oper_mount_status", 
        "password": "password", 
        "pwdSet": "pwd_set", 
        "remapOnEject": "remap_on_eject", 
        "remoteHost": "remote_host", 
        "remoteIpAddress": "remote_ip_address", 
        "remotePort": "remote_port", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "userId": "user_id", 
        "virtualDiskId": "virtual_disk_id", 
        "writable": "writable", 
    }

    def __init__(self, parent_mo_or_dn, virtual_disk_id, **kwargs):
        self._dirty_mask = 0
        self.virtual_disk_id = virtual_disk_id
        self.auth_option = None
        self.child_action = None
        self.device_type = None
        self.enc_pwd = None
        self.error_type = None
        self.image_file_name = None
        self.image_name_variable = None
        self.image_path = None
        self.mapping_name = None
        self.mount_protocol = None
        self.oper_mount_status = None
        self.password = None
        self.pwd_set = None
        self.remap_on_eject = None
        self.remote_host = None
        self.remote_ip_address = None
        self.remote_port = None
        self.sacl = None
        self.status = None
        self.user_id = None
        self.writable = None

        ManagedObject.__init__(self, "CimcvmediaActualMountEntry", parent_mo_or_dn, **kwargs)
