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
