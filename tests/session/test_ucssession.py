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

from ucsmsdk.ucshandle import UcsHandle


class TestSession(unittest.TestCase):
    def test_001_create_uri(self):
        # Create an object of type LsServer with parent dn specified
        # check if the object has the right values populated
        handle = UcsHandle("192.168.1.1", "admin", "password")

        self.assertEqual(
            handle._UcsSession__create_uri(
                port=None,
                secure=None),
            'https://192.168.1.1:443')

        self.assertEqual(
            handle._UcsSession__create_uri(
                port=8080,
                secure=None),
            'https://192.168.1.1:8080')

        self.assertEqual(
            handle._UcsSession__create_uri(
                port=None,
                secure=True),
            'https://192.168.1.1:443')

        self.assertEqual(
            handle._UcsSession__create_uri(
                port=None,
                secure=False),
            'http://192.168.1.1:80')

        self.assertEqual(
            handle._UcsSession__create_uri(
                port=444,
                secure=False),
            'http://192.168.1.1:444')
