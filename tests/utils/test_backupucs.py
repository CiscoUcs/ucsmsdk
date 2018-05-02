# Copyright 2017 Cisco Systems, Inc.
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

from nose import SkipTest
from nose.tools import with_setup
from ..connection.info import custom_setup, custom_teardown, get_skip_msg
from ucsmsdk.utils.ucsbackup import backup_ucs
from ucsmsdk.ucshandle import UcsHandle

handle = None


def setup_module():
    global handle
    handle = custom_setup()
    if not handle:
        msg = get_skip_msg()
        raise SkipTest(msg)


def teardown_module():
    custom_teardown(handle)


def _test_ucs_backup(handle, file_dir, file_name, backup_type):
    backup_ucs(handle,
               backup_type=backup_type,
               file_dir=file_dir,
               file_name=file_name)


@with_setup(setup_module, teardown_module)
def test_ucs_backup():
    _test_ucs_backup(handle, file_dir="/tmp/backup",
                     file_name="config1.xml",
                     backup_type="config-logical")


def test_ucs_backup_after_freeze_unfreeze():
    # for this test to be more meaningful there needs to be proxy server
    # configured
    h1 = custom_setup()
    frozen_handle = h1.freeze()
    h2 = UcsHandle.unfreeze(frozen_handle)


    # Try a download operation using new handle
    _test_ucs_backup(h2, file_dir="/tmp/backup",
                     file_name="config2.xml",
                     backup_type="config-logical")

    custom_teardown(h2)
