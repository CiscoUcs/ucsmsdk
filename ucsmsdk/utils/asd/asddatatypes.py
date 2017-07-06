# Copyright 2017 Cisco Systems, Inc.
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

"""
This module has helper methods to facilitate image download from ASD
"""

from __future__ import print_function
from __future__ import unicode_literals

import urllib
import logging
import json

from ...ucsdriver import UcsDriver

log = logging.getLogger('ucs')


class AsdConsts:
    CLIENT_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    CLIENT_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    GRANT_TYPE = "password"
    DEFAULT = "Default"
    B_SERIES = "B-Series"
    INFRASTRUCTURE = "Infrastructure"
    DRIVERS = "Drivers"
    FIRMWARE = "Firmware"
    E_SERIES = "E-Series"
    UCS_CENTRAL = "UcsCentral"
    UCS_Handle = "UcsHandle"
    IMC_HANDLE = "ImcHandle"
    UCS_CENTRAL_HANDLE = "UcsCentralHandle"
    TOKEN_URL = "https://cloudsso.cisco.com/as/token.oauth2"
    IMAGE_URL = "https://api.cisco.com/software/v2.0/metadata/udi/{0}/mdf_id/{1}/software_type_id/{2}/current_release/{3}?page_index={4}"
    DOWNLOAD_URL = "https://api.cisco.com/software/v2.0/downloads/urls/udi/{0}/mdf_id/{1}/metadata_trans_id/{2}/image_guids/{3}"
    EULA_URL = "https://api.cisco.com/software/v2.0/compliance/forms/eula"


class Platform(object):
    def __init__(self, software_id, mdf_id, version, udi, page_index="1"):
        self.__software_type_id = software_id
        self.__mdf_context_id = mdf_id
        self.__min_release = version
        self.__udi = udi
        self.__operating_platform = None
        self.__output_release = None
        self.page_index = page_index

    @property
    def software_type_id(self):
        return self.__software_type_id

    @property
    def mdf_context_id(self):
        return self.__mdf_context_id

    @property
    def min_release(self):
        return self.__min_release

    @property
    def udi(self):
        return self.__udi

    @property
    def operating_platform(self):
        return self.__operating_platform

    @property
    def output_release(self):
        return self.__output_release


class UcsAsdImage(object):
    def __init__(self, d):
        for key in d:
            setattr(self, key, d[key])

    def __str__(self):
        """
        Overridden str
        """
        tab_size = 8
        out_str = "\n"
        out_str += str("name").ljust(tab_size * 4) + ':' + str(
            self.image_name) + "\n"
        out_str += str("version").ljust(tab_size * 4) + ':' + str(
            self.image_version) + "\n"
        out_str += str("size").ljust(tab_size * 4) + ':' + str(
            self.image_size) + "\n"
        out_str += str("description").ljust(tab_size * 4) + ':' + str(
            self.image_description) + "\n"
        out_str += str("checksum_md5").ljust(tab_size * 4) + ':' + str(
            self.image_checksums['md5_checksum']) + "\n"
        out_str += str("access_token").ljust(tab_size * 4) + ':' + str(
            self.access_token) + "\n"
        out_str += str("proxy").ljust(tab_size * 4) + ':' + str(
            self.proxy) + "\n"
        out_str += "\n"
        return out_str
