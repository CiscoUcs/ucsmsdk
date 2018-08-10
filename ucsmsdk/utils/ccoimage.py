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


"""
This module has helper methods to facilitate image download from CCO
"""

from __future__ import print_function
from __future__ import unicode_literals

import os
import logging

from .. import ucsgenutils
from ..ucsexception import UcsValidationException, UcsWarning
from ..ucsdriver import UcsDriver

from six.moves import input


log = logging.getLogger('ucs')


class _UcsCcoImageList:
    """enum for cco image attributes"""
    IDAC_TAG_VERSION = "version"
    IDAC_TAG_IMAGE_NAME = "imageName"
    IDAC_TAG_URL = "url"
    IDAC_TAG_IP_URL = "IPurl"
    IDAC_TAG_SIZE = "size"
    IDAC_TAG_CHECKSUM = "checksum"
    IDAC_TAG_FILE_DESCRIPTION = "fileDescription"


class UcsCcoImage(object):
    """
    Describes the cco image object
    """

    def __init__(self):
        self.image_name = None
        self.version = None
        self.url = None
        self.ip_url = None
        self.size = None
        self.checksum_md5 = None
        self.file_description = None
        self.network_credential = None
        self.proxy = None

    def __str__(self):
        """
        Overridden str
        """
        tab_size = 8
        out_str = "\n"
        out_str += str("image_name").ljust(tab_size * 4) + ':' + str(
            self.image_name) + "\n"
        out_str += str("version").ljust(tab_size * 4) + ':' + str(
            self.version) + "\n"
        out_str += str("url").ljust(tab_size * 4) + ':' + str(self.url) + "\n"
        out_str += str("ip_url").ljust(tab_size * 4) + ':' + str(
            self.ip_url) + "\n"
        out_str += str("size").ljust(tab_size * 4) + ':' + str(
            self.size) + "\n"
        out_str += str("checksum_md5").ljust(tab_size * 4) + ':' + str(
            self.checksum_md5) + "\n"
        out_str += str("file_description").ljust(tab_size * 4) + ':' + str(
            self.file_description) + "\n"
        out_str += str("network_credential").ljust(tab_size * 4) + ':' + str(
            self.network_credential) + "\n"
        out_str += str("proxy").ljust(tab_size * 4) + ':' + str(
            self.proxy) + "\n"
        out_str += "\n"
        return out_str


def get_ucs_cco_image_list(username=None, password=None, mdf_id_list=None,
                           proxy=None):
    """
    Gets the list of images available on CCO

    Args:
        username (str): username to connect to image server
        password (str): password to connect to image server
        mdf_id_list (list): list of mdf id
        proxy (str): proxy used for connection

    Returns:
        List of UcsCcoImage objects

    Example:
        image_list = get_ucs_cco_image_list("username", "password")
    """

    import getpass
    import xml.dom
    import xml.dom.minidom
    import base64

    if username is None:
        username = input("Username: ")
    if password is None:
        password = getpass.getpass()

    ucs_mdf_ids = (283612660, 283853163, 283862063)
    url = "https://www.cisco.com/cgi-bin/front.x/ida/locator/locator.pl"
    ida_xml_query_header = 'input_xml=<?xml version="1.0" encoding="UTF-8"?>' \
                           '<locator>' \
                           '<input>'
    ida_xml_query_mdf_id = '<mdfConcept id="%s" name=""/>'
    ida_xml_query_footer = '</input></locator>'

    # create input_xml string to post as
    # data to the respective url via post method
    input_xml = ""
    input_xml += ida_xml_query_header
    if not mdf_id_list:
        for mdf_id in ucs_mdf_ids:
            input_xml += ida_xml_query_mdf_id % mdf_id
    else:
        for mdf_id in mdf_id_list:
            input_xml += ida_xml_query_mdf_id % mdf_id

    input_xml += ida_xml_query_footer
    log.debug(input_xml)

    # base64encode for Authorization header
    credential = base64.b64encode((username + ":" + password).encode()).decode(
        'utf-8')
    log.debug(credential)

    # send request to server
    driver = UcsDriver(proxy)
    driver.add_header("Authorization", "Basic %s" % credential)
    ida_xml_response = driver.post(uri=url,
                                   data=input_xml.encode(),
                                   dump_xml=True,
                                   read=True)

    if not ida_xml_response:
        raise UcsValidationException("No Response from <%s>" % url)

    doc = xml.dom.minidom.parseString(ida_xml_response)
    image_node_list = doc.getElementsByTagName("image")

    if not image_node_list:
        raise UcsValidationException("No Images Found")

    # Serialize image nodes in objects
    cco_image_list = []
    for image_node in image_node_list:
        image = UcsCcoImage()
        image.network_credential = credential

        property_node_list = [child_node for child_node in
                              image_node.childNodes if
                              child_node.nodeType == child_node.ELEMENT_NODE
                              and child_node.localName == "property"]
        for property_node in property_node_list:
            if not property_node.hasAttribute("name"):
                continue
            if property_node.getAttribute(
                    "name") == _UcsCcoImageList.IDAC_TAG_VERSION:
                image.version = property_node.getAttribute("value")
                continue
            if property_node.getAttribute(
                    "name") == _UcsCcoImageList.IDAC_TAG_IMAGE_NAME:
                image.image_name = property_node.getAttribute("value")
                continue
            if property_node.getAttribute(
                    "name") == _UcsCcoImageList.IDAC_TAG_URL:
                image.url = property_node.getAttribute("value")
                continue
            if property_node.getAttribute(
                    "name") == _UcsCcoImageList.IDAC_TAG_IP_URL:
                image.ip_url = property_node.getAttribute("value")
                continue
            if property_node.getAttribute(
                    "name") == _UcsCcoImageList.IDAC_TAG_SIZE:
                image.size = int(property_node.getAttribute("value"))
                continue
            if property_node.getAttribute(
                    "name") == _UcsCcoImageList.IDAC_TAG_CHECKSUM:
                if property_node.getAttribute("type") == "md5":
                    image.checksum_md5 = property_node.getAttribute("value")
                    continue
            if property_node.getAttribute(
                    "name") == _UcsCcoImageList.IDAC_TAG_FILE_DESCRIPTION:
                image.file_description = property_node.getAttribute("value")
                continue

        cco_image_list.append(image)
    return cco_image_list


def get_ucs_cco_image(image, file_dir, proxy=None):
    """
    Downloads image from CCO

    Args:
        image (UcsCcoImage): object of type UcsCcoImage
        file_dir (str): directory to download image to
        proxy (str): proxy (if any)

    Returns:
        None

    Example:
        image_list = get_ucs_cco_image_list("username", "password")\n
        get_ucs_cco_image(image=image_list[0], file_dir="/home/user/images")\n
    """

    if not image:
        raise UcsValidationException("Provide an image to be downloaded.")
    if not isinstance(image, UcsCcoImage):
        raise UcsValidationException("Object is not of type UcsCcoImage")

    if not file_dir:
        raise UcsValidationException("Provide file_dir to download image to.")
    if not os.path.isdir(file_dir):
        raise UcsValidationException(
            "Not a valid directory <%s>" % file_dir)

    image_url = image.url
    print("Processing Image " + str(image.image_name))

    driver = UcsDriver(proxy)
    driver.add_header("Authorization", "Basic %s" % image.network_credential)
    ucsgenutils.download_file(driver,
                              file_url=image_url,
                              file_dir=file_dir,
                              file_name=str(image.image_name))

    local_file = os.path.join(file_dir, str(image.image_name))

    if not os.path.exists(local_file):
        raise UcsValidationException("URL parameter is not provided.")

    md5_sum = ucsgenutils.get_md5_sum(local_file)
    if not md5_sum:
        UcsWarning("Unable to generate md5sum for file <%s>" % local_file)
        UcsWarning("Deleting file <%s> ....." % local_file)
        os.remove(local_file)
        return
    log.debug(md5_sum)
    log.debug(image.checksum_md5)
    if md5_sum != image.checksum_md5:
        UcsWarning("Incorrect md5sum for file <%s>" % local_file)
        UcsWarning("Deleting file <%s> ....." % local_file)
        os.remove(local_file)
        return
