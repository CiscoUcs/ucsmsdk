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

from nose.tools import *
from ucsmsdk.mometa.ls.LsServer import LsServer

obj = None


def setup_func():
    global obj
    obj = LsServer("org-root", "test")


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
@raises(Exception)
def test_001_set_ro_property():
    # This is a read only property
    # Should fail with an exception
    obj.oper_state = "up"


@with_setup(setup_func, teardown_func)
def test_002_set_rw_property():
    # This is a read write property.
    # Should happen without any issues
    obj.descr = "test_description"


@with_setup(setup_func(), teardown_func())
@raises(Exception)
def test_003_set_naming_property():
    # This is a naming property. so, it is create only
    # Should fail with an exception
    obj.name = "test1"

