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

import threading

from tests.base import BaseTest


class TestThreading(BaseTest):
    def t1_func(self):
        from ucsmsdk.mometa.ls.LsServer import LsServer
        obj = LsServer("org-root", "temp_sp1")
        self.handle.add_mo(obj)

    def t2_func(self):
        from ucsmsdk.mometa.ls.LsServer import LsServer
        obj1 = LsServer("org-root", "temp_sp2")
        obj2 = LsServer("org-root", "temp_sp3")
        self.handle.add_mo(obj1)
        self.handle.add_mo(obj2)

    def test_test_threading_mode():
        self.handle.set_mode_threading()

        t1 = threading.Thread(name="t1", target=self.t1_func)
        t2 = threading.Thread(name="t2", target=self.t2_func)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        # commit buffers should be in different contexts
        buf1 = self.handle._get_commit_buf(tag="t1")
        buf2 = self.handle._get_commit_buf(tag="t2")

        assert_equal(len(buf1), 1)
        assert_equal(len(buf2), 2)

        self.handle.commit_buffer_discard(tag="t1")
        self.handle.commit_buffer_discard(tag="t2")

        self.handle.unset_mode_threading()
