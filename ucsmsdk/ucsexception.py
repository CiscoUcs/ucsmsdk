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
This module contains the SDK defined exceptions.
"""

import logging

log = logging.getLogger('ucs')


def UcsWarning(warn_str):
    """
    Method to throw warnings.
    """

    # import warnings
    #
    # warnings.warn(string)
    log.debug(warn_str)


class UcsWrapperException(Exception):
    """
    Parent class for all ucswrapper exceptions.
    """

    pass


class UcsLoginError(UcsWrapperException):
    """
    LoginFailure Error
    """

    # message = 'Authentication failed'

    def __init__(self, message, error_code=None):
        super(UcsLoginError, self).__init__(message)


class UcsConnectionError(UcsWrapperException):
    """
    Cannot connect to UCS Manager.
    """

    def __init__(self, message):
        super(UcsConnectionError, self).__init__(message)


class UcsOperationError(UcsWrapperException):
    """
    Configuration Error.
    """

    def __init__(self, operation, error):
        message = "%s failed, error: %s" % (operation, error)
        super(UcsOperationError, self).__init__(message)


class UcsError(Exception):
    """
    Base class for exceptions in Ucs module.
    """

    pass


class UcsException(UcsError):
    """
    Class to catch exception thrown from UCSM.
    """

    def __init__(self, error_code, error_descr):
        self.__error_code = error_code
        self.__error_descr = error_descr

    @property
    def error_code(self):
        """Getter Method of UcsException Class"""
        return self.__error_code

    @property
    def error_descr(self):
        """Getter Method of UcsException Class"""
        return self.__error_descr

    def __str__(self):
        return "[ErrorCode]: %s[ErrorDescription]: %s" % (
            self.__error_code, self.__error_descr)


class UcsValidationException(UcsError):
    """
    Class to handle required attributes validation.
    """

    def __init__(self, error_msg):
        self.__error_msg = error_msg

    @property
    def error_msg(self):
        """Getter Method of UcsValidationException Class"""
        return self.__error_msg

    def __str__(self):
        return "[ErrorMessage]: %s" % (self.__error_msg)
