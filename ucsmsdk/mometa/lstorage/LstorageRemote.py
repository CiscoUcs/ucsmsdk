"""This module contains the general information for LstorageRemote ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageRemoteConsts:
    pass


class LstorageRemote(ManagedObject):
    """This is LstorageRemote class."""

    consts = LstorageRemoteConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageRemote", "lstorageRemote", "remote", VersionMeta.Version321d, "InputOutput", 0x7ff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['computeBoard', 'lstorageDriveSecurity'], ['lstorageLogin'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deployed_security_key": MoPropertyMeta("deployed_security_key", "deployedSecurityKey", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x4, 0, 32, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "port": MoPropertyMeta("port", "port", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1024-65535"]),
        "primary_server": MoPropertyMeta("primary_server", "primaryServer", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "secondary_server": MoPropertyMeta("secondary_server", "secondaryServer", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []),
        "server_cert": MoPropertyMeta("server_cert", "serverCert", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "timeout": MoPropertyMeta("timeout", "timeout", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["5-20"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "deployedSecurityKey": "deployed_security_key", 
        "dn": "dn", 
        "port": "port", 
        "primaryServer": "primary_server", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secondaryServer": "secondary_server", 
        "serverCert": "server_cert", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.deployed_security_key = None
        self.port = None
        self.primary_server = None
        self.sacl = None
        self.secondary_server = None
        self.server_cert = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "LstorageRemote", parent_mo_or_dn, **kwargs)
