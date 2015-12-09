"""This module contains the general information for AaaLdapProvider ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AaaLdapProviderConsts():
    ENABLE_SSL_FALSE = "false"
    ENABLE_SSL_NO = "no"
    ENABLE_SSL_TRUE = "true"
    ENABLE_SSL_YES = "yes"
    KEY_SET_FALSE = "false"
    KEY_SET_NO = "no"
    KEY_SET_TRUE = "true"
    KEY_SET_YES = "yes"
    ORDER_LOWEST_AVAILABLE = "lowest-available"
    VENDOR_MS_AD = "MS-AD"
    VENDOR_OPEN_LDAP = "OpenLdap"


class AaaLdapProvider(ManagedObject):
    """This is AaaLdapProvider class."""

    consts = AaaLdapProviderConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AaaLdapProvider", "aaaLdapProvider", "provider-[name]", VersionMeta.Version101e, "InputOutput", 0x7ffffL, [], ["aaa", "admin"], [u'aaaLdapEp'], [u'aaaLdapGroupRule'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "attribute": MoPropertyMeta("attribute", "attribute", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2L, 0, 63, None, [], []), 
        "basedn": MoPropertyMeta("basedn", "basedn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x8L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "enable_ssl": MoPropertyMeta("enable_ssl", "enableSSL", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["false", "no", "true", "yes"], []), 
        "enc_key": MoPropertyMeta("enc_key", "encKey", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, 1, 127, None, [], []), 
        "filter": MoPropertyMeta("filter", "filter", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100L, 0, 127, None, [], []), 
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""[!""#$%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,127}""", [], []), 
        "key_set": MoPropertyMeta("key_set", "keySet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x400L, None, None, r"""^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["lowest-available"], ["0-16"]), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, [], ["1-65535"]), 
        "retries": MoPropertyMeta("retries", "retries", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, [], ["0-5"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4000L, 0, 256, None, [], []), 
        "rootdn": MoPropertyMeta("rootdn", "rootdn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, 0, 255, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, None, [], ["0-60"]), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, None, ["MS-AD", "OpenLdap"], []), 
    }

    prop_map = {
        "attribute": "attribute", 
        "basedn": "basedn", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "enableSSL": "enable_ssl", 
        "encKey": "enc_key", 
        "filter": "filter", 
        "key": "key", 
        "keySet": "key_set", 
        "name": "name", 
        "order": "order", 
        "port": "port", 
        "retries": "retries", 
        "rn": "rn", 
        "rootdn": "rootdn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeout": "timeout", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.attribute = None
        self.basedn = None
        self.child_action = None
        self.descr = None
        self.enable_ssl = None
        self.enc_key = None
        self.filter = None
        self.key = None
        self.key_set = None
        self.order = None
        self.port = None
        self.retries = None
        self.rootdn = None
        self.sacl = None
        self.status = None
        self.timeout = None
        self.vendor = None

        ManagedObject.__init__(self, "AaaLdapProvider", parent_mo_or_dn, **kwargs)
