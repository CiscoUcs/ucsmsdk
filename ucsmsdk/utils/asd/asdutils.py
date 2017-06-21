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

from collections import defaultdict

import os
import logging
import urllib
import json

from ...ucscoremeta import UcsVersion
from ...ucsdriver import UcsDriver
from ... import ucsxmlcodec
from . import asddatatypes as adt

log = logging.getLogger('ucs')


def get_image_meta_list():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(cur_dir, "imagemeta.xml")
    if not os.path.exists(fpath):
        raise UcsOperationError("get_image_meta_list",
                                "File <%s> does not exist" % fpath)

    with open(fpath, 'r') as fh:
        data = fh.read()
        root = ucsxmlcodec.extract_root_elem(data)

    return root.findall('CcoImageMeta')


def filter_image_meta_category(meta_list, mode, category):
    for meta in meta_list:
        meta_mode = meta.attrib['Mode']
        meta_category = meta.attrib['Category']
        if meta_mode == mode and meta_category == category:
            return meta


def filter_image_meta_mdf(meta_list, mdf_id):
    for meta in meta_list:
        meta_mdf_id = meta.attrib['MdfId']
        if meta_mdf_id == mdf_id:
            return meta


def get_access_token(username, password=None, proxy=None):
    import getpass

    if password is None:
        password = getpass.getpass()

    driver = UcsDriver(proxy)

    values = {
        'client_id': adt.AsdConsts.CLIENT_ID,
        'client_secret': adt.AsdConsts.CLIENT_SECRET,
        'grant_type': adt.AsdConsts.GRANT_TYPE,
        'username': username,
        'password': password
    }

    data = urllib.urlencode(values)
    data = data.encode('utf-8')

    resp = driver.post(uri=adt.AsdConsts.TOKEN_URL,
                       data=data,
                       dump_xml=False,
                       read=True)
    resp_dict = json.loads(resp)
    return resp_dict['access_token']



def _get_url_json_response(url, access_token, proxy=None, data=None):
    log.debug(url)
    driver = UcsDriver(proxy)
    driver.add_header("Authorization", "Bearer %s" % access_token)
    resp = driver.post(uri=url, data=data)
    resp_dict = json.loads(resp)
    return resp_dict


def _get_image_store_url(platform):
    url = adt.AsdConsts.IMAGE_URL
    image_store_url = url.format(platform.udi,
                           platform.mdf_context_id,
                           platform.software_type_id,
                           platform.min_release,
                           platform.page_index)

    if platform.operating_platform:
        image_store_url += "&operating_platform=%s" % platform.operating_platform

    if platform.output_release:
        image_store_url += "&output_release=%s" % platform.output_release

    return image_store_url


def _get_images_by_udi(platform, access_token, proxy=None):
    asd_image_list = None
    url = _get_image_store_url(platform)
    resp_dict = _get_url_json_response(url, access_token, proxy)

    metadata_response = resp_dict['metadata_response']
    metadata_id_list = metadata_response['metadata_id_list']
    asd_metadata_exception = metadata_id_list['asd_metadata_exception']
    if asd_metadata_exception:
        raise Exception

    software_list = metadata_id_list['software_list']
    platform_list = software_list['platform_list']

    for pltform in platform_list:
        release_list = pltform['release_list']
        for release in release_list:
            images = release['image_details']
            for img in images:
                image = adt.UcsAsdImage(img)
                asd_image_exception = image.asd_image_exception
                if asd_image_exception and len(asd_image_exception) >= 1:
                    if asd_image_exception[0]['exception_code'] == "is_Deleted":
                        continue
                image.is_suggested_release = release['is_suggested_rel']
                image.image_version = release['release_version']
                image.access_token = access_token
                image.platform = platform
                image.metadata_transaction_id = metadata_response['metadata_trans_id']
                image.operating_platform = pltform['operating_platform']
                image.proxy = proxy

                if asd_image_list is None:
                    asd_image_list = []
                asd_image_list.append(image)

    pagination_response_record = resp_dict['pagination_response_record']
    log.debug("page_index is <%s>" % str(pagination_response_record['page_index']))
    log.debug("last_index is <%s>" % str(pagination_response_record['last_index']))

    if pagination_response_record['page_index'] != pagination_response_record['last_index']:
        page_index = int(pagination_response_record['page_index'])
        page_index += 1
        platform.page_index = str(page_index)
        images = _get_images_by_udi(platform, access_token, proxy)
        if images and len(images) > 0:
            asd_image_list.extend(images)

    return asd_image_list

def _remove_duplicate_image(images):
    imagedict = defaultdict(list)
    for image in images:
        imagedict[image.image_name].append(image)

    imagelist = []
    for imglist in imagedict.values():
        imagelist.append(max(imglist, key=attrgetter('image_version')))

    return sorted(imagelist, key=attrgetter('image_version'))


def get_asd_images(platform, access_token, proxy=None):
    asdimages = _get_images_by_udi(platform, access_token, proxy)
    if asdimages and len(asdimages) > 1:
        return _remove_duplicate_image(asdimages)


def filter_asd_images(images):
    if not images or  len(images) < 1:
        return None

    # grouping image by version
    image_groups_by_version = defaultdict(list)
    for image in images:
        image_groups_by_version[image.image_version].append(image)

    # find max version under each "major.minor" combination
    version_groups = defaultdict(list)
    for version in image_groups_by_version:
        ver = UcsVersion(version)
        version_groups["%s.%s" %(ver.major, ver.minor)].append(version)

    # hvg - highest version in each group
    hvg = [max(i, key=lambda version: UcsVersion(version)) for i in version_groups.values()]

    return [image for ver in hvg for image in image_groups_by_version[ver]]


def _get_image_download_url(image):
    url = adt.AsdConsts.DOWNLOAD_URL
    image_download_url = url.format(image.platform.udi,
                                    image.platform.mdf_context_id,
                                    image.metadata_transaction_id,
                                    image.image_guid)
    return image_download_url


def get_image_download_info(image):
    url = _get_image_download_url(image)
    resp_dict = _get_url_json_response(url, image.access_token, image.proxy)
    download_info_list = resp_dict['download_info_list']
    asd_download_url_exception = download_info_list[0]['asd_download_url_exception']
    if asd_download_url_exception and len(asd_download_url_exception) > 1:
        exception_code = asd_download_url_exception[0]['exception_code']
        if exception_code != "SW_ADV_IMAGE":
            raise Exception(asd_download_url_exception[0]['exception_message'])
    else:
        download_list = download_info_list[0]
    log.debug(download_list)
    return download_list


def accept_eula_agreement(user_action, access_token, proxy):
    url = adt.AsdConsts.EULA_URL
    data = urllib.urlencode({"user_action": user_action})
    data = data.encode('utf-8')
    resp_dict = _get_url_json_response(url, access_token, proxy, data)
    log.debug(resp_dict)
    return  resp_dict and resp_dict['status_number'] == "0"


def is_correct_image(full_image_path, image):
    from ... import ucsgenutils

    file_md5 = ucsgenutils.get_md5_sum(full_image_path)
    image_md5 = image.image_checksums['md5_checksum']

    if not file_md5 or file_md5 != image_md5:
        UcsWarning("Unable to generate md5sum for file <%s>" % full_image_path)
        UcsWarning("Deleting file <%s> ....." % full_image_path)
        os.remove(full_image_path)
        return False
    return True


def is_eula_accepted(access_token, proxy):
    return accept_eula_agreement(user_action.declined, access_token, proxy)



