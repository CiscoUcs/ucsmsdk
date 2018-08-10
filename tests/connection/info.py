# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from six.moves import configparser

host = "ucs"
skip_msg = "Not connected to a valid UCSM domain."


def custom_setup():
    import os
    from ucsmsdk.ucshandle import UcsHandle

    config = configparser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    try:
        hostname = config.get(host, "hostname")
        username = config.get(host, "username")
        password = config.get(host, "password")
    except:
        return None
    handle = UcsHandle(hostname, username, password)
    handle.login(auto_refresh=True, force=True)
    return handle


def custom_teardown(handle):
    if handle:
        handle.logout()


def get_skip_msg():
    return skip_msg
