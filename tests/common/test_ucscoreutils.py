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

import ucsmsdk.ucscoreutils as cutil

def setup_func():
    pass

def teardown_func():
    pass

@with_setup(setup_func, teardown_func)
def test_001_get_naming_props():
    rn_pattern = "fault-[code]-[name]-[type]-xyz-[state]"
    rn_str = "fault-F35275-fault-c2-xyz-on"
    np = cutil.get_naming_props(rn_str, rn_pattern)
    assert_equal(np['code'], 'F35275')
    assert_equal(np['name'], 'fault')
    assert_equal(np['type'], 'c2')
    assert_equal(np['state'], 'on')

@with_setup(setup_func, teardown_func)
def test_002_get_naming_props():
    rn_pattern = "[suport_type][card_param_type]"
    rn_str = "11"
    np = cutil.get_naming_props(rn_str, rn_pattern)
    assert_equal(np['suport_type'], '1')
    assert_equal(np['card_param_type'], '1')

@with_setup(setup_func, teardown_func)
def test_003_get_naming_props():
    rn_pattern = "[suport_type][card_param_type]"
    rn_str = "1122"
    np = cutil.get_naming_props(rn_str, rn_pattern)
    #assert_equal(np['suport_type'], '11')
    #assert_equal(np['card_param_type'], '22')



