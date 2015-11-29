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

import sys
import os
import urllib2
import httplib
import socket
import ssl

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


class TLS1Handler(urllib2.HTTPSHandler):
    """Like HTTPSHandler but more specific"""

    def __init__(self):
        urllib2.HTTPSHandler.__init__(self)

    def https_open(self, req):
        return self.do_open(TLS1Connection, req)


class TLS1Connection(httplib.HTTPSConnection):
    """Like HTTPSConnection but more specific"""

    def __init__(self, host, **kwargs):
        httplib.HTTPSConnection.__init__(self, host, **kwargs)

    def connect(self):
        """Overrides HTTPSConnection.connect to specify TLS version"""
        # Standard implementation from HTTPSConnection, which is not
        # designed for extension, unfortunately
        if sys.version_info >= (2, 7):
            sock = socket.create_connection((self.host, self.port),
                                            self.timeout, self.source_address)
        elif sys.version_info >= (2, 6):
            sock = socket.create_connection((self.host, self.port),
                                            self.timeout)
        else:
            sock = socket.create_connection((self.host, self.port))

        if getattr(self, '_tunnel_host', None):
            self.sock = sock
            self._tunnel()

        # This is the only difference; default wrap_socket uses SSLv23
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
                                    ssl_version=ssl.PROTOCOL_TLSv1)


class UrllibDriver(object):
    """
    To Add docstring
    """

    def __init__(self, proxy=None):
        self.__redirect_uri = None
        self.__proxy = proxy
        self.__headers = {}
        self.__handlers = self.__get_handlers()

    def __get_handlers(self):
        handlers = [SmartRedirectHandler, TLS1Handler]
        if self.__proxy:
            proxy_handler = urllib2.ProxyHandler(
                {'http': self.__proxy, 'https': self.__proxy})
            handlers.append(proxy_handler)
        return handlers

    def add_header(self, header_prop, header_value):
        self.__headers[header_prop] = header_value

    def remove_header(self, header_prop):
        del self.__headers[header_prop]

    @property
    def redirect_uri(self):
        return self.__redirect_uri

    def __create_request(self, uri, data=None):
        request_ = urllib2.Request(url=uri, data=data)
        headers = self.__headers
        for header in headers:
            request_.add_header(header, headers[header])
        return request_

    def get(self, uri):
        pass

    def post(self, uri, data=None, show_traffic=False, read=True):
        if self.__redirect_uri:
            uri = self.__redirect_uri
        request = self.__create_request(uri=uri, data=data)
        if show_traffic:
            log.debug('%s ====> %s' % (uri, data))

        opener = urllib2.build_opener(*self.__handlers)
        response = opener.open(request)

        if type(response) is list:
            if len(response) == 2 and \
                    (response[0] == 302 or response[0] == 301):
                uri = response[1]
                self.__redirect = True
                self.__redirect_uri = uri
                request = self.__create_request(uri=uri, data=data)
                if show_traffic:
                    log.debug('%s <==== %s' % (uri, data))

                opener = urllib2.build_opener(*self.__handlers)
                response = opener.open(request)
                # response = urllib2.urlopen(request)
        if read:
            response = response.read()
            if show_traffic:
                log.debug('%s <==== %s' % (uri, response))
        return response


class UcsConnectionDriver(object):
    """
    To Add docstring
    """

    def __init__(self, ucs_session):
        self.__redirect = False
        self.__session = ucs_session
        self.__uri = self.__session.uri
        self.__secure = self.__session.secure
        self.__proxy = self.__session.proxy

        self.__driver = UrllibDriver(proxy=self.__proxy)

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

        response_str = self.__driver.post(self.__uri, in_xml_str,
                                          show_traffic=False)
        if self.__driver.redirect_uri:
            self.__session._AbstractSession__uri = self.__driver.redirect_uri

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
                log.debug('%s ====> %s' % (self.__session.uri, xml_str))
                element.attrib['inName'] = self.__session.username
                element.attrib['inPassword'] = self.__session.password
                xml_str = xc.to_xml_str(element)
            else:
                xml_str = xc.to_xml_str(element)
                log.debug('%s ====> %s' % (self.__session.uri, xml_str))
        else:
            xml_str = xc.to_xml_str(element)

        response_str = self.post_xml(xml_str)
        if dump_xml:
            log.debug('%s <==== %s' % (self.__session.uri, response_str))

        response = xc.from_xml_str(response_str)
        if response:
            return response
        return None

    def download_file(self, url_suffix, file_dir, file_name):
        from ucsgenutils import download_file
        ucsm_uri = self.__session.uri
        ucsm_uri = ucsm_uri.rstrip('/nuova')
        file_url = "%s/%s" % (ucsm_uri, url_suffix)

        self.__driver.add_header('Cookie', 'ucsm-cookie=%s'
                                 % self.__session.cookie)

        download_file(driver=self.__driver,
                      file_url=file_url,
                      file_dir=file_dir,
                      file_name=file_name)

        self.__driver.remove_header('Cookie')

    def upload_file(self, url_suffix, file_dir, file_name):
        from ucsgenutils import upload_file

        ucsm_uri = self.__session.uri
        ucsm_uri = ucsm_uri.rstrip('/nuova')
        file_url = "%s/%s" % (ucsm_uri, url_suffix)

        self.__driver.add_header('Cookie', 'ucsm-cookie=%s'
                                 % self.__session.cookie)

        upload_file(self.__driver,
                    uri=file_url,
                    file_dir=file_dir,
                    file_name=file_name)

        self.__driver.remove_header('Cookie')
