# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import time
import logging
from threading import Timer

import ucsexception as ex
import ucsmethodfactory as mf
from ucsconnectiondriver import UcsConnectionDriver

log = logging.getLogger('ucs')

class AbstractSession(object):
    """
    To add docstring
    """

    def __init__(self, host, port, secure):
        self.__host = host

        if secure is not None and port is not None:
            self.__secure = secure
            self.__port = int(port)
        elif secure is not None and port is None:
            if secure:
                self.__port = 443
                self.__secure = True
            else:
                self.__port = 80
                self.__secure = False
        elif secure is None and port is not None:
            if int(port) == 80:
                self.__secure = False
                self.__port = 80
            elif int(port) == 443:
                self.__secure = True
                self.__port = 443
            else:
                self.__secure = True
                self.__port = int(port)
        else:
            self.__secure = True
            self.__port = 443

        self.__uri = self.__create_uri()

    @property
    def secure(self):
        return self.__secure

    @property
    def uri(self):
        return self.__uri

    def __create_uri(self):
        https_or_http = ("http", "https")[self.__secure]
        host = self.__host
        port = str(self.__port)
        uri = "%s://%s%s%s%s" % (https_or_http, host, ":", port, "/nuova")
        return uri


class UcsSession(AbstractSession):
    def __init__(self, ip, username, password, port=None, secure=None,
                 proxy=None, dump_xml=False):
        self.__ip = ip
        self.__username = username
        self.__password = password
        self.__port = port
        self.__secure = secure
        self.__proxy = proxy
        self.__dump_xml = dump_xml
        AbstractSession.__init__(self, self.__ip, self.__port, self.__secure)

        self.__ucs = ip
        self.__cookie = None
        self.__refresh_period = None
        self.__priv = None
        self.__domains = None
        self.__channel = None
        self.__evt_channel = None
        self.__session_id = None
        self.__version = None
        self.__name = None

        self.__refresh_timer = None
        self.__force = False
        self.__driver = UcsConnectionDriver(self)

    @property
    def driver(self):
        return self.__driver

    def __getattr__(self, item):
        key = "_UcsSession__" + item
        if hasattr(self, key):
            return getattr(self, key)
        else:
            raise AttributeError

    def _set_dump_xml(self):
        self.__dump_xml = True

    def _unset_dump_xml(self):
        self.__dump_xml = False

    def __clear(self):
        self.__cookie = None
        self.__refresh_period = None
        self.__priv = None
        self.__domains = None
        self.__channel = None
        self.__evt_channel = None
        self.__session_id = None
        self.__version = None
        self.__name = None
        self.__last_update_time = str(time.asctime())

    def __update(self, response):
        from ucscoremeta import UcsVersion
        self.__cookie = response.out_cookie
        self.__refresh_period = response.out_refresh_period
        self.__priv = response.out_priv
        self.__domains = response.out_domains
        self.__channel = response.out_channel
        self.__evt_channel = response.out_evt_channel
        self.__session_id = response.out_session_id
        self.__version = UcsVersion(response.out_version)
        self.__name = response.out_name

    def __start_refresh_timer(self):
        """ Internal method to support auto-refresh functionality. """
        if self.__refresh_period > 60:
            interval = int(self.__refresh_period) - 60
        else:
            interval = 60
        self.__refresh_timer = Timer(interval, self.refresh)
        # TODO:handle exit and logout active connections. revert from daemon
        self.__refresh_timer.setDaemon(True)
        self.__refresh_timer.start()

    def __stop_refresh_timer(self):
        """ Internal method to support auto-refresh functionality. """
        if self.__refresh_timer is not None:
            self.__refresh_timer.cancel()
            self.__refresh_timer = None

    def refresh(self, auto_relogin=False):
        """
        Sends the aaaRefresh query to the UCS to refresh the connection
        (to prevent session expiration).
        """
        self.__stop_refresh_timer()

        element = mf.aaa_refresh(self.__cookie, self.__username,
                                 self.__password)
        response = self.__driver.post(element)
        if response.error_code != 0:
            self.__cookie = None
            if auto_relogin:
                return self.login()
            return False

        self.__domains = response.out_domains
        self.__priv = response.out_priv.split(',')
        self.__refresh_period = int(response.out_refresh_period)
        self.__cookie = response.out_cookie

        # re-enable the timer
        self.__start_refresh_timer()
        return True

    def __validate_connection(self):
        from mometa.top.TopSystem import TopSystem

        if self.__cookie is not None and self.__cookie != "":
            if not self.__force:
                top_system = TopSystem()
                element = mf.config_resolve_dn(cookie=self.__cookie,
                                               dn=top_system.dn)
                response = self.__driver.post(element)
                if response.error_code != 0:
                    raise ex.UcsException(response.error_code,
                                          response.error_descr)
                return True
            else:
                self.logout()
        return False

    def _login(self, auto_refresh=False, force=False):
        """
        To Do Add DocString
        """
        from mometa.top.TopSystem import TopSystem
        from mometa.firmware.FirmwareRunning import FirmwareRunning, \
            FirmwareRunningConsts
        from ucscoremeta import UcsVersion

        if self.__validate_connection():
            return True

        element = mf.aaa_login(in_name=self.__username,
                               in_password=self.__password)
        response = self.__driver.post(element)
        if response.error_code != 0:
            self.__clear()
            raise ex.UcsException(response.error_code, response.error_descr)
        self.__update(response)

        # Verify not to connect to IMC
        nw_element = mf.config_resolve_class(cookie=self.__cookie,
                                             in_filter=None,
                                             class_id="networkElement")
        nw_element_response = self.__driver.post(nw_element)
        # To Do - returns error tag
        if nw_element_response.error_code != 0:
            self.__clear()
            return False

        top_system = TopSystem()
        if response.out_version is None or response.out_version == "":
            firmware = FirmwareRunning(top_system,
                                       FirmwareRunningConsts.DEPLOYMENT_SYSTEM)
            element = mf.config_resolve_dn(cookie=self.__cookie,
                                           dn=firmware.dn)
            response = self.__driver.post(element)
            if response.error_code != 0:
                raise ex.UcsException(response.error_code,
                                      response.error_descr)
            firmware = response.out_config.child[0]
            self.__version = UcsVersion(firmware.version)

        top_system = TopSystem()
        element = mf.config_resolve_dn(cookie=self.__cookie, dn=top_system.dn)
        response = self.__driver.post(element)
        if response.error_code != 0:
            raise ex.UcsException(response.error_code, response.error_descr)
        top_system = response.out_config.child[0]
        self.__ucs = top_system.name
        self.__virtual_ipv4_address = top_system.address

        if auto_refresh:
            self.__start_refresh_timer()

        return True

    def _logout(self):
        """
        To Do - Add docstring
        :return:
        """
        if self.__cookie is None:
            return True

        if self.__refresh_timer:
            self.__refresh_timer.cancel()

        if self.__cookie:
            # TO DO NewParam inDelaySec introduced in 224b
            element = mf.aaa_logout(self.__cookie, 301)
            response = self.__driver.post(element)

            if response.error_code == "555":
                return True

            if response.error_code != 0:
                raise ex.UcsException(response.error_code,
                                      response.error_descr)

            self.__clear()

            return True
