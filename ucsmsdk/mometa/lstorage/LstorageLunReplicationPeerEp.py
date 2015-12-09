"""This module contains the general information for LstorageLunReplicationPeerEp ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageLunReplicationPeerEpConsts():
    PEER_DEVICE_TYPE_LUN = "LUN"
    PEER_DEVICE_TYPE_NFS = "NFS"
    PEER_TYPE_CISCO = "Cisco"
    PEER_TYPE_LINUX_LVM = "Linux-LVM"
    PEER_TYPE_LINUX_RAW = "Linux-RAW"
    PEER_TYPE_WINDOWS = "Windows"


class LstorageLunReplicationPeerEp(ManagedObject):
    """This is LstorageLunReplicationPeerEp class."""

    consts = LstorageLunReplicationPeerEpConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LstorageLunReplicationPeerEp", "lstorageLunReplicationPeerEp", "repl-target[name]", VersionMeta.Version302c, "InputOutput", 0x7ffL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "peer_addr": MoPropertyMeta("peer_addr", "peerAddr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""^[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?$|^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*(\.[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$""", [], []), 
        "peer_device_type": MoPropertyMeta("peer_device_type", "peerDeviceType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["LUN", "NFS"], []), 
        "peer_dir": MoPropertyMeta("peer_dir", "peerDir", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], []), 
        "peer_type": MoPropertyMeta("peer_type", "peerType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["Cisco", "Linux-LVM", "Linux-RAW", "Windows"], []), 
        "peer_volume": MoPropertyMeta("peer_volume", "peerVolume", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x200L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "peerAddr": "peer_addr", 
        "peerDeviceType": "peer_device_type", 
        "peerDir": "peer_dir", 
        "peerType": "peer_type", 
        "peerVolume": "peer_volume", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.peer_addr = None
        self.peer_device_type = None
        self.peer_dir = None
        self.peer_type = None
        self.peer_volume = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLunReplicationPeerEp", parent_mo_or_dn, **kwargs)

