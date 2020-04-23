"""This module contains the general information for BiosVfConsoleRedirection ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfConsoleRedirectionConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_BAUD_RATE_115200 = "115200"
    VP_BAUD_RATE_19200 = "19200"
    VP_BAUD_RATE_38400 = "38400"
    VP_BAUD_RATE_57600 = "57600"
    VP_BAUD_RATE_9600 = "9600"
    VP_BAUD_RATE_PLATFORM_DEFAULT = "platform-default"
    VP_BAUD_RATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_CONSOLE_REDIRECTION_COM_0 = "com-0"
    VP_CONSOLE_REDIRECTION_COM_1 = "com-1"
    VP_CONSOLE_REDIRECTION_DISABLED = "disabled"
    VP_CONSOLE_REDIRECTION_ENABLED = "enabled"
    VP_CONSOLE_REDIRECTION_PLATFORM_DEFAULT = "platform-default"
    VP_CONSOLE_REDIRECTION_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_CONSOLE_REDIRECTION_SERIAL_PORT_A = "serial-port-a"
    VP_CONSOLE_REDIRECTION_SERIAL_PORT_B = "serial-port-b"
    VP_FLOW_CONTROL_NONE = "none"
    VP_FLOW_CONTROL_PLATFORM_DEFAULT = "platform-default"
    VP_FLOW_CONTROL_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_FLOW_CONTROL_RTS_CTS = "rts-cts"
    VP_LEGACY_OSREDIRECTION_80X24 = "80x24"
    VP_LEGACY_OSREDIRECTION_80X25 = "80x25"
    VP_LEGACY_OSREDIRECTION_DISABLED = "disabled"
    VP_LEGACY_OSREDIRECTION_ENABLED = "enabled"
    VP_LEGACY_OSREDIRECTION_PLATFORM_DEFAULT = "platform-default"
    VP_LEGACY_OSREDIRECTION_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PUTTY_KEY_PAD_ESCN = "escn"
    VP_PUTTY_KEY_PAD_LINUX = "linux"
    VP_PUTTY_KEY_PAD_PLATFORM_DEFAULT = "platform-default"
    VP_PUTTY_KEY_PAD_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PUTTY_KEY_PAD_SCO = "sco"
    VP_PUTTY_KEY_PAD_VT100 = "vt100"
    VP_PUTTY_KEY_PAD_VT400 = "vt400"
    VP_PUTTY_KEY_PAD_XTERMR6 = "xtermr6"
    VP_TERMINAL_TYPE_PC_ANSI = "pc-ansi"
    VP_TERMINAL_TYPE_PLATFORM_DEFAULT = "platform-default"
    VP_TERMINAL_TYPE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_TERMINAL_TYPE_VT_UTF8 = "vt-utf8"
    VP_TERMINAL_TYPE_VT100 = "vt100"
    VP_TERMINAL_TYPE_VT100_PLUS = "vt100-plus"


class BiosVfConsoleRedirection(ManagedObject):
    """This is BiosVfConsoleRedirection class."""

    consts = BiosVfConsoleRedirectionConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfConsoleRedirection", "biosVfConsoleRedirection", "Console-redirection", VersionMeta.Version111j, "InputOutput", 0x7ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_baud_rate": MoPropertyMeta("vp_baud_rate", "vpBaudRate", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["115200", "19200", "38400", "57600", "9600", "platform-default", "platform-recommended"], []),
        "vp_console_redirection": MoPropertyMeta("vp_console_redirection", "vpConsoleRedirection", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["com-0", "com-1", "disabled", "enabled", "platform-default", "platform-recommended", "serial-port-a", "serial-port-b"], []),
        "vp_flow_control": MoPropertyMeta("vp_flow_control", "vpFlowControl", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["none", "platform-default", "platform-recommended", "rts-cts"], []),
        "vp_legacy_os_redirection": MoPropertyMeta("vp_legacy_os_redirection", "vpLegacyOSRedirection", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["80x24", "80x25", "disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_putty_key_pad": MoPropertyMeta("vp_putty_key_pad", "vpPuttyKeyPad", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["escn", "linux", "platform-default", "platform-recommended", "sco", "vt100", "vt400", "xtermr6"], []),
        "vp_terminal_type": MoPropertyMeta("vp_terminal_type", "vpTerminalType", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["pc-ansi", "platform-default", "platform-recommended", "vt-utf8", "vt100", "vt100-plus"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpBaudRate": "vp_baud_rate", 
        "vpConsoleRedirection": "vp_console_redirection", 
        "vpFlowControl": "vp_flow_control", 
        "vpLegacyOSRedirection": "vp_legacy_os_redirection", 
        "vpPuttyKeyPad": "vp_putty_key_pad", 
        "vpTerminalType": "vp_terminal_type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_baud_rate = None
        self.vp_console_redirection = None
        self.vp_flow_control = None
        self.vp_legacy_os_redirection = None
        self.vp_putty_key_pad = None
        self.vp_terminal_type = None

        ManagedObject.__init__(self, "BiosVfConsoleRedirection", parent_mo_or_dn, **kwargs)
