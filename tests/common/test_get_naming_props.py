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

import unittest

import ucsmsdk.ucscoreutils


class TestNamingPattern(unittest.TestCase):
    def test_001_rn_pattern(self):
        rn_pattern = "compute-ep-ven-[vendor]-mod-[model]-ser-[serial]"
        rn_str = "compute-ep-ven-Cisco Systems Inc-mod-UCSB-B200-M4-ser-3403"
        ucsmsdk.ucscoreutils.get_naming_props(rn_str, rn_pattern)
