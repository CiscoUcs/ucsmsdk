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

"""
This is an auto-generated module.
It contains supporting classes for Filter.

"""

from .ucscore import BaseObject
from . import ucsgenutils


class Method(BaseObject):
    """This is Method class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "Method", "method")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class MethodSet(BaseObject):
    """This is MethodSet class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "MethodSet", "methodSet")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class ClassId(BaseObject):
    """This is ClassId class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "ClassId", "classId")
        self.value = None
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class ClassIdSet(BaseObject):
    """This is ClassIdSet class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "ClassIdSet", "classIdSet")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class ConfigConfig(BaseObject):
    """This is ConfigConfig class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "ConfigConfig", "configConfig")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class ConfigMap(BaseObject):
    """This is ConfigMap class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "ConfigMap", "configMap")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class ConfigSet(BaseObject):
    """This is ConfigSet class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "ConfigSet", "configSet")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class Dn(BaseObject):
    """This is Dn class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "Dn", "dn")
        self.value = None
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class DnSet(BaseObject):
    """This is DnSet class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "DnSet", "dnSet")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class FilterFilter(BaseObject):
    """This is FilterFilter class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "FilterFilter", "filter")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class Id(BaseObject):
    """This is Id class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "Id", "id")
        self.value = None
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class IdSet(BaseObject):
    """This is IdSet class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "IdSet", "idSet")
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)


class Pair(BaseObject):
    """This is Pair class."""
    def __init__(self, **kwargs):
        BaseObject.__init__(self, "Pair", "pair")
        self.key = None
        if kwargs:
            for n, v in ucsgenutils.iteritems(kwargs):
                self.attr_set(n, v)
