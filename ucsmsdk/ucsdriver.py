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

from __future__ import print_function
from __future__ import unicode_literals

import sys
import socket
import ssl

try:
    import urllib2
    import httplib
    from urllib2 import HTTPError
except:
    import urllib.request as urllib2
    import http.client as httplib
    from urllib.error import HTTPError


import logging

log = logging.getLogger('ucs')


class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    """This class is to handle redirection error."""

    def http_error_301(self, req, fp, code, msg, headers):
        """This is to handle redirection error code 301"""
        resp_status = [code, headers.get('Location')]
        return resp_status

    def http_error_302(self, req, fp, code, msg, headers):
        """This is to handle redirection error code 302"""
        resp_status = [code, headers.get('Location')]
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


class UcsDriver(object):
    """
    This class is responsible to create http and https connection using urllib
    library.

    Args:
        proxy (str): The proxy object to be used to connect

    Example:
        driver = UcsDriver(proxy="192.168.1.1:80")
    """

    def __init__(self, proxy=None):
        self.__redirect_uri = None
        self.__proxy = proxy
        self.__headers = {}
        self.__handlers = self.__get_handlers()

    def __get_handlers(self):
        """
        Internal method to handle redirection and use TLS protocol.
        """

        handlers = [SmartRedirectHandler, TLS1Handler]
        if self.__proxy:
            proxy_handler = urllib2.ProxyHandler(
                {'http': self.__proxy, 'https': self.__proxy})
            handlers.append(proxy_handler)
        return handlers

    def add_header(self, header_prop, header_value):
        """
        Adds header to http/ https web request

        Args:
            header_prop (str): header name
            header (str): header value

        Returns:
            None

        Example:
            driver=UcsDriver()\n
            driver.add_header('Cookie', 'xxxxxxxxxxxxxx')\n
        """

        self.__headers[header_prop] = header_value

    def remove_header(self, header_prop):
        """
        Removes header from http/ https web request

        Args:
            header_prop (str): header name

        Returns:
            None

        Example:
            driver=UcsDriver()\n
            driver.remove_header('Cookie')\n
        """

        del self.__headers[header_prop]

    @property
    def redirect_uri(self):
        """
        Getter method of UcsDriver class
        """

        return self.__redirect_uri

    def __create_request(self, uri, data=None):
        """
        Internal method to create http/https web request

        Args:
            uri (str): protocol://web_address:port
            data (str): data to send over web request

        Returns:
            web request object
        """

        request_ = urllib2.Request(url=uri, data=data)
        headers = self.__headers
        for header in headers:
            request_.add_header(header, headers[header])
        return request_

    def get(self, uri):
        pass

    def post(self, uri, data=None, dump_xml=False, read=True):
        """
        sends the web request and receives the response from ucsm server

        Args:
            uri (str): URI of the  the UCS Server
            data (str): request data to send via post request
            dump_xml (bool): if True, displays request and response
            read (bool): if True, returns response.read() else returns object.

        Returns:
            response xml string or response object

        Example:
            response = post("http://192.168.1.1:80", data=xml_str)
        """

        try:
            if self.__redirect_uri:
                uri = self.__redirect_uri
            request = self.__create_request(uri=uri, data=data)
            if dump_xml:
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
                    if dump_xml:
                        log.debug('%s <==== %s' % (uri, data))

                    opener = urllib2.build_opener(*self.__handlers)
                    response = opener.open(request)
                    # response = urllib2.urlopen(request)
            if read:
                response = response.read().decode('utf-8')
                if dump_xml:
                    log.debug('%s <==== %s' % (uri, response))
            return response
        except HTTPError as e:
            log.debug(e.headers)
            raise
