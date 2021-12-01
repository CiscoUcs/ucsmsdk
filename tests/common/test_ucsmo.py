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

from ucsmsdk.ucsmo import ManagedObject


class TestUCSMo(unittest.TestCase):
    def test_001_create_mo_directly(self):
        # Create a Managed Object by specifying the classId and parent dn
        # this should raise an exception as the associated Meta's will not
        # be initialised.
        with self.assertRaises(Exception):
            ManagedObject("LsServer", "org-root")

    def test_002_create_specific_obj(self):
        # Create an object of type LsServer with parent dn specified
        # check if the object has the right values populated
        from ucsmsdk.mometa.ls.LsServer import LsServer
        obj = LsServer("org-root", "temp_sp")
        self.assertEqual(obj.name, "temp_sp")
        self.assertEqual(obj.rn, "ls-temp_sp")
        self.assertEqual(obj.dn, "org-root/ls-temp_sp")
