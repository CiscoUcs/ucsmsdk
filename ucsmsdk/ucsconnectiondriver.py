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

try:
    import requests

    requests.packages.urllib3.disable_warnings()
except Exception as e:
    print e.message

import urllib2
import logging

log = logging.getLogger('ucs')


class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    """This class is to handle redirection error."""

    def http_error_301(self, req, fp, code, msg, headers):
        """This is to handle redirection error code 301"""
        resp_status = [code, headers.dict["location"]]
        return resp_status

    def http_error_302(self, req, fp, code, msg, headers):
        """This is to handle redirection error code 302"""
        resp_status = [code, headers.dict["location"]]
        return resp_status


class UrllibDriver(object):
    """
    To Add docstring
    """

    def __init__(self, secure=True, proxy=None):
        self.__secure = secure
        self.__proxy = proxy
        self.__handlers = self.__get_handlers()

    def __get_handlers(self):
        handlers = []
        if not self.__secure:
            handlers.append(SmartRedirectHandler)
        if self.__proxy:
            proxy_handler = urllib2.ProxyHandler(
                {'http': self.__proxy, 'https': self.__proxy})
            handlers.append(proxy_handler)
        return handlers

    def __post_http_request(self, uri, data):
        req = urllib2.Request(url=uri, data=data)
        opener = urllib2.build_opener(*self.__handlers)
        resp = opener.open(req)
        if type(resp) is list:
            if len(resp) == 2 and (resp[0] == 302 or resp[0] == 301):
                uri = resp[1]
                req = urllib2.Request(url=uri, data=data)
                resp = urllib2.urlopen(req)
        return resp

    def __post_https_request(self, uri, data):
        req = urllib2.Request(url=uri, data=data)
        opener = urllib2.build_opener(*self.__handlers)
        resp = opener.open(req)
        return resp

    def get(self, uri):
        pass

    def post(self, uri, data):
        if self.__secure:
            resp = self.__post_https_request(uri, data)
        else:
            resp = self.__post_http_request(uri, data)

        rsp = resp.read()
        return rsp


class RequestDriver(object):
    """
    To Add docstring
    """

    def __init__(self):
        self.__validate_certificate = False
        self.__timeout = None

    def validate_certificate(self):
        self.__validate_certificate = True

    def ignore_certificate(self):
        self.__validate_certificate = False

    def set_timeout(self, timeout):
        self.__timeout = timeout

    def __getr(self, url, verify, timeout):
        """
        To Add docstring
        """
        rsp = requests.get(url=url, verify=verify, timeout=timeout)
        return rsp

    def __postr(self, data, url, verify, timeout):
        """
        To Add docstring
        """
        rsp = requests.post(url=url, data=data, verify=verify, timeout=timeout,
                            allow_redirects=False)
        if rsp.status_code in [301, 302]:
            url = rsp.headers['location']
            return self.__postr(data, url, verify, timeout)
        return rsp

    def get(self, uri):
        """
        To Add docstring
        uri:
        """
        return self.__getr(url=uri,
                           verify=self.__validate_certificate,
                           timeout=self.__timeout)

    def post(self, uri, data):
        """
        To Add docstring
        data:
        """
        rsp = self.__postr(data=data,
                           url=uri,
                           verify=self.__validate_certificate,
                           timeout=self.__timeout)
        return rsp.text


class UcsConnectionDriver(object):
    """
    To Add docstring
    """

    def __init__(self, ucs_session, use_requests=False):
        self.__use_requests = use_requests
        self.__session = ucs_session
        self.__uri = self.__session.uri
        self.__secure = self.__session.secure
        self.__proxy = self.__session.proxy

        if use_requests:
            self.__driver = RequestDriver()
        else:
            self.__driver = UrllibDriver(secure=self.__secure,
                                         proxy=self.__proxy)

    def get(self):
        """
        To Add docstring
        :return:
        """
        return self.__driver.get()

    def post_xml(self, in_xml_str):
        """
        To Add docstring
        :param in_xml_str:
        :param dump_xml:
        :return:
        """

        response_str = self.__driver.post(self.__uri, in_xml_str)
        return response_str

    def post(self, element, dump_xml=None):
        import ucsgenutils
        import ucsxmlcodec as xc

        if dump_xml is None:
            dump_xml = self.__session.dump_xml

        if dump_xml:
            if element.tag == "aaaLogin":
                element.attrib['inName'] = ucsgenutils.encrypt_password(
                    self.__session.username, "cisco")
                element.attrib['inPassword'] = ucsgenutils.encrypt_password(
                    self.__session.password, "cisco")
                xml_str = xc.to_xml_str(element)
                log.debug('%s ====> %s' % (self.__session.ucs, xml_str))
                element.attrib['inName'] = self.__session.username
                element.attrib['inPassword'] = self.__session.password
                xml_str = xc.to_xml_str(element)
            else:
                xml_str = xc.to_xml_str(element)
                log.debug('%s ====> %s' % (self.__session.ucs, xml_str))
        else:
            xml_str = xc.to_xml_str(element)

        response_str = self.post_xml(xml_str)
        if dump_xml:
            log.debug('%s <==== %s' % (self.__session.ucs, response_str))

        response = xc.from_xml_str(response_str)
        if response:
            return response
        return None
