# Copyright 2013 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains APIs used to launch the Java based UCSM GUI.
"""

from __future__ import print_function
from __future__ import unicode_literals

import os
import re
import subprocess
import logging

from .. import ucsgenutils
from ..ucsexception import UcsValidationException

log = logging.getLogger('ucs')


def ucs_gui_launch(handle, need_url=False):
    """
    ucs_gui_launch launches the Java based UCSM GUI.
    This method requires the necessary Jdk to be in place, for it to be
    successful.

    Args:
        handle (UcsHandle): Ucs connection handle
        need_url (bool): True/False,
                         returns the URL to launch GUI, if True

    Example:
        ucs_gui_launch(handle)\n
        ucs_gui_launch(handle, need_url=True)\n
    """

    import tempfile
    import fileinput
    import platform

    os_support = ["Windows", "Linux", "Microsoft", "Darwin"]
    if platform.system() not in os_support:
        raise UcsValidationException(
            "Unsupported operating system")

    jnlp_file = None
    try:
        ucsm_gui_url = "%s/app/ucsm/index.html" % handle.uri
        if handle:
            auth_token = handle.get_auth_token()
            log.debug("AuthToken: <%s>" % auth_token)
            if auth_token:
                ucsm_gui_url = "%s?ucsmToken=%s" % (ucsm_gui_url, auth_token)

        log.debug("UCSM URL: <%s>" % ucsm_gui_url)

        if need_url:
            return ucsm_gui_url
        else:
            javaws_path = ucsgenutils.get_java_installation_path()
            log.debug("javaws path: <%s>" % javaws_path)
            if javaws_path is not None:
                # source = urllib2.urlopen(ucsm_url).read()
                source = handle.post(uri=ucsm_gui_url)
                jnlp_dir = tempfile.gettempdir()
                log.debug("Temp Directory: <%s>" % jnlp_dir)
                jnlp_file = os.path.join(jnlp_dir, "temp.jnlp")
                if os.path.exists(jnlp_file):
                    os.remove(jnlp_file)

                jnlp_fh = open(jnlp_file, "wt+")
                jnlp_fh.write(source)
                jnlp_fh.close()

                java_str = ucsgenutils.get_java_version()
                log.debug("Java Version: <%s>" % java_str)

                # Adding both the property to enable the secure log in UCSM
                # independent of java versions.
                # if java version < 1.7_45, property to use is
                # "log.show.encrypted"
                # if java version >= 1.7_45, property to use is
                # "jnlp.ucsm.log.show.encrypted"

                debug_str_old_java = '\t<property ' \
                            'name="log.show.encrypted" ' \
                            'value="true"/>'

                debug_str_new_java = '\t<property ' \
                                'name="jnlp.ucsm.log.show.encrypted" ' \
                                'value="true"/>'

                for line in fileinput.input(jnlp_file, inplace=1):
                    if re.search(r'^\s*</resources>\s*$', line):
                        print(debug_str_old_java)
                        print(debug_str_new_java)
                    line = line.strip('\n') if line else line
                    print(line)
                subprocess.call([javaws_path, jnlp_file])
                if os.path.exists(jnlp_file):
                    os.remove(jnlp_file)
            else:
                return None
    except Exception as e:
        fileinput.close()
        if os.path.exists(jnlp_file):
            os.remove(jnlp_file)
        raise e
