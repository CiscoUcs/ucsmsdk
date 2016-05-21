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

from .ucscore import AbstractFilter


class AllbitsFilter(AbstractFilter):
    """This is AllbitsFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "AllbitsFilter", "allbits")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class AndFilter(AbstractFilter):
    """This is AndFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "AndFilter", "and")

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        pass


class AnybitFilter(AbstractFilter):
    """This is AnybitFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "AnybitFilter", "anybit")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class BwFilter(AbstractFilter):
    """This is BwFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "BwFilter", "bw")
        self.class_ = None
        self.first_value = None
        self.property = None
        self.second_value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.first_value = kwargs['first_value']
        self.property = kwargs['property']
        self.second_value = kwargs['second_value']


class EqFilter(AbstractFilter):
    """This is EqFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "EqFilter", "eq")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class GeFilter(AbstractFilter):
    """This is GeFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "GeFilter", "ge")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class GtFilter(AbstractFilter):
    """This is GtFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "GtFilter", "gt")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class LeFilter(AbstractFilter):
    """This is LeFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "LeFilter", "le")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class LtFilter(AbstractFilter):
    """This is LtFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "LtFilter", "lt")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class NeFilter(AbstractFilter):
    """This is NeFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "NeFilter", "ne")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']


class NotFilter(AbstractFilter):
    """This is NotFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "NotFilter", "not")

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        pass


class OrFilter(AbstractFilter):
    """This is OrFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "OrFilter", "or")

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        pass


class WcardFilter(AbstractFilter):
    """This is WcardFilter class."""
    def __init__(self):
        AbstractFilter.__init__(self, "WcardFilter", "wcard")
        self.class_ = None
        self.property = None
        self.value = None

    def create(self, **kwargs):
        """This method populate the attribute of filter object."""
        self.class_ = kwargs['class_']
        self.property = kwargs['property']
        self.value = kwargs['value']
