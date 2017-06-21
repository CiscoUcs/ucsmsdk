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
This module has helper methods to facilitate image download from CCO
"""

from __future__ import print_function
from __future__ import unicode_literals

import os
import logging


from . import asdutils as au
from . import asdimagehandler as aih
from ... import ucsgenutils
from ...ucsexception import UcsOperationError, UcsValidationException, UcsWarning
from ...ucsdriver import UcsDriver

log = logging.getLogger('ucs')


def get_ucs_software_image_list(handle, username, password=None,
                                mdf_id=None, software_id=None,
                                category="default", type="firmware",
                                model=None, all_releases=False, proxy=None):
    import getpass

    if password is None:
        password = getpass.getpass()

    udi = handle.udi # Todo
    pid = handle.pid if model is None else model

    log.debug("Get meta for software images")
    image_meta_list = au.get_image_meta_list()

    if mdf_id and software_id:
        # use mdf_id to fetch image list
        image_meta = au.filter_image_meta_by_mdf(image_meta_list, mdf_id)
        if not image_meta:
            raise UcsOperationError("get_ucs_software_image_list",
                    "Invalid mdf_id <%s>." % mdf_id)

        image_firmware_id = image_meta.attrib['FirmwareId']
        image_firmware_version = image_meta.attrib['FirmwareVersion']

        image_driver_id = image_meta.attrib['DriverId']
        image_driver_version = image_meta.attrib['DriverVersion']

        if software_id == image_firmware_id:
            version = image_firmware_version
        elif software_id == image_driver_id:
            version = image_driver_version
        else:
            raise UcsOperationError("get_ucs_software_image_list",
                    "Invalid Combination of mdf_id <%s> and software_id <%s>" %
                     (mdf_id, software_id))
    else:
        if model:
            UcsWarning("model parameter is ignored.")

        image_meta = au.filter_image_meta(image_meta_list,
                                       mode=AsdConstants.B_SERIES,
                                       category=category)

        image_category = image_meta.attrib['Category']
        image_firmware_id = image_meta.attrib['FirmwareId']
        image_firmware_version = image_meta.attrib['FirmwareVersion']
        image_driver_id = image_meta.attrib['DriverId']
        image_driver_version = image_meta.attrib['DriverVersion']
        image_mdf_id = image_meta.attrib['MdfId']

        mdf_id = image_mdf_id

        if image_category == AsdConstants.INFRASTRUCTURE:
            software_id = image_firmware_id
            version = image_firmware_version

            if type == AsdConstants.DRIVERS:
                UcsWarning("type parameter is ignored.")
        elif type == AsdConstants.DRIVERS:
            software_id = image_driver_id
            version = image_driver_version
        else:
            software_id = image_firmware_id
            version = image_firmware_version


    #host_config = adt.HostConfig(username, password, proxy)
    #access_token = host_config.access_token
    access_token = au.get_access_token(username, password, proxy)
    if not access_token:
        raise UcsOperationError("get_ucs_software_image_list",
                                "Failed to get access token.")

    log.debug("Access Token is <%s>" % access_token)
    host_platform = adt.Platform(software_id=software_id,
                                 mdf_id=mdf_id,
                                 version=version,
                                 udi=udi)

    log.debug("Get Images.....")
    asd_image_list = au.get_asd_images(host_platform, access_token, proxy)

    if not all_releases:
        asd_image_list = au.filter_asd_images(asd_image_list)

    return asd_image_list


def get_ucs_software_image(image, file_dir):
    """
    Downloads ucs firmware image

    Args:
        image (UcsSoftwareImage): object of type UcsSoftwareImage
        file_dir (str): directory to download image to

    Returns:
        None

    Example:
        image_list = get_ucs_cco_image_list("username", "password")\n
        get_ucs_software_image(image=image_list[0],
                               file_dir="/home/user/images")\n
    """

    if not isinstance(image, UcsAsdImage):
        raise UcsValidationException("Invalid Image.")

    if not os.path.isdir(file_dir):
        raise UcsValidationException(
            "Not a valid directory <%s>" % file_dir)

    local_file = os.path.join(file_dir, str(image.image_name))
    if os.path.exists(local_file):
        if au.is_correct_image(local_file):
            UcsWarning("File <%s> already exist. Exiting." % local_file)
            return
        else:
            os.remove(local_file)
            log.info("Invalid Image. Removing it.")

    # accept eula agreement explicitly : TO DO - Need to be removed
    if not au.accept_eula_agreement("Accepted", image.access_token,
                                    image.proxy):
        raise UcsOperationError("get_ucs_software_image",
                                "Unable to accept end user license agreement.")

    download_info = au.get_image_download_info(image)
    download_url = download_info['download_url']
    if not download_url:
        raise UcsOperationError("get_ucs_software_image",
                                "Download URL is not available.")

    log.info("Processing image " + str(image.image_name))
    image_url = download_url + "&access_token=%s" % image.access_token
    log.debug(image_url)
    driver = UcsDriver(image.proxy)
    ucsgenutils.download_file(driver,
                              file_url=image_url,
                              file_dir=file_dir,
                              file_name=str(image.image_name))

    driver = UcsDriver(proxy)
    driver.add_header("Authorization", "Basic %s" % image.network_credential)
    ucsgenutils.download_file(driver,
                              file_url=image_url,
                              file_dir=file_dir,
                              file_name=str(image.image_name))

    local_file = os.path.join(file_dir, str(image.image_name))
    if not os.path.exists(local_file):
        raise UcsOperationError("get_ucs_software_image",
                                "File not downloaded.")

    if not au.is_correct_image(local_file):
        raise UcsOperationError("get_ucs_software_image",
                                "Invalid Image.Deleting it.")

    log.info("Image processing complete.")


