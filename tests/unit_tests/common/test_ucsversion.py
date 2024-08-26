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

from ucsmsdk.ucsmeta import VersionMeta
from ucsmsdk.ucscoremeta import UcsVersion


class TestVersion(unittest.TestCase):
    def test_nightly_version1(self):
        version1 = UcsVersion("2.0(13aS6)")
        version2 = UcsVersion("3.0(1S10)")
        self.assertLess(version1, version2)

    def test_nightly_version2(self):
        version1 = UcsVersion("2.0(13aS6)")
        version2 = UcsVersion("2.0(1S10)")
        self.assertGreater(version1, version2)

    def test_nightly_version3(self):
        # 2.0(2cS6) will be considered as 2.0(2d) internally
        version1 = UcsVersion("2.0(2cS6)")
        version2 = UcsVersion("2.0(2c)")
        self.assertNotEqual(version1, version2)

    def test_nightly_version4(self):
        version1 = UcsVersion("2.0(2cS6)")
        version2 = UcsVersion("2.0(3)")
        self.assertLess(version1, version2)

    def test_spin_version1(self):
        # version interpreted as 4.0(2b)
        version1 = UcsVersion("4.0(2aS3)")
        version2 = UcsVersion("4.0(2b)")
        self.assertEqual(version1, version2)

    def test_spin_version2(self):
        # version interpreted as 4.0(234c)
        version1 = UcsVersion("4.0(234bS3)")
        version2 = UcsVersion("4.0(234c)")
        self.assertEqual(version1, version2)

    def test_spin_version3(self):
        # version interpreted as 4.0(2z)
        version1 = UcsVersion("4.0(2S3)")
        version2 = UcsVersion("4.0(2z)")
        self.assertEqual(version1, version2)

    def test_spin_version4(self):
        # version interpreted as 4.0(234z)
        version1 = UcsVersion("4.0(234S3)")
        version2 = UcsVersion("4.0(234z)")
        self.assertEqual(version1, version2)

    def test_patch_version1(self):
        # version interpreted as 4.0(235a)
        version1 = UcsVersion("4.0(234.5)")
        version2 = UcsVersion("4.0(235a)")
        self.assertEqual(version1, version2)

    def test_build_version1(self):
        # 4.2(0.175a) is an engineering build that will later become 4.2(1a)
        version1 = UcsVersion("4.2(0.175a)")
        version2 = UcsVersion("4.2(1a)")
        self.assertLess(version1, version2)

    def test_build_version2(self):
        version1 = UcsVersion("4.2(0.175a)")
        version2 = UcsVersion("4.2(0.258a)")
        self.assertLess(version1, version2)

    def test_spin_version5(self):
        # version interpreted as 4.2(2a)
        version1 = UcsVersion("4.2(1.2021052301)")
        version2 = UcsVersion("4.2(2a)")
        self.assertEqual(version1, version2)

    def test_spin_version6(self):
        # version interpreted as 4.2(1b)
        version1 = UcsVersion("4.2(1a.2021052301)")
        version2 = UcsVersion("4.2(1b)")
        self.assertEqual(version1, version2)

    def test_gt_same_major_version(self):
        version1 = VersionMeta.Version211a
        version2 = VersionMeta.Version211e
        self.assertLess(version1, version2)

    def test_gt_different_major_version(self):
        version1 = VersionMeta.Version404a
        version2 = VersionMeta.Version412b
        self.assertLess(version1, version2)

    def test_patch_versions(self):
        # when we don't see a patch version we use z
        # so 2.0(12) will be considered as 2.0(12z)
        version1 = UcsVersion("2.0(12b)")
        version2 = UcsVersion("2.0(12)")
        self.assertLessEqual(version1, version2)

    def test_version_parsing(self):
        test_cases = [
            ("1.0(0.0a)", {"major": "1", "minor": "0", "mr": "0", "patch": "a", "spin": None, "build": "0"}),
            ("12.34(56.78z)", {"major": "12", "minor": "34", "mr": "56", "patch": "z", "spin": None, "build": "78"}),
            ("123.456(789.0b)", {"major": "123", "minor": "456", "mr": "789", "patch": "b", "spin": None, "build": "0"}),
            ("2.0(13aS1)", {"major": "2", "minor": "0", "mr": "13", "patch": "b", "spin": "S1", "build": None}),
            ("3.0(1S10)", {"major": "3", "minor": "0", "mr": "1", "patch": "z", "spin": "S10", "build": None}),
            ("66.77(67.1582251418)", {"major": "66", "minor": "77", "mr": "68", "patch": "a", "spin": None, "build": None}),
            ("4.2(0.175a)", {"major": "4", "minor": "2", "mr": "0", "patch": "a", "spin": None, "build": "175"}),
            ("4.2(1.2021052301)", {"major": "4", "minor": "2", "mr": "2", "patch": "a", "spin": None, "build": None}),
            ("4.2(1a.2021052301)", {"major": "4", "minor": "2", "mr": "1", "patch": "b", "spin": "2021052301", "build": None}),
        ]

        for version_str, expected in test_cases:
            with self.subTest(version_str=version_str):
                version = UcsVersion(version_str)
                self.assertEqual(version.major, expected["major"])
                self.assertEqual(version.minor, expected["minor"])
                self.assertEqual(version.mr, expected["mr"])
                self.assertEqual(version.patch, expected["patch"])
                self.assertEqual(version.spin, expected["spin"])
                self.assertEqual(version.build, expected["build"])
