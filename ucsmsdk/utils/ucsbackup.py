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
This module contains the api used to take backup of ucs and import the backup.
"""

import os
import platform
import time
import datetime
import logging
from ..ucsexception import UcsValidationException, UcsWarning

log = logging.getLogger('ucs')


def backup_ucs(handle, backup_type, file_dir, file_name, timeout_in_sec=600,
               preserve_pooled_values=False):
    """
        This operation creates and download the backup of ucs.

        Attributes:
            handle (UcsHandle)
            backup_type (str): specifies the type of backup
                            i.e. fullstate/config-logical/config-system/
                            config-all
            file_dir (str): directory to download ucs backup file
            file_name (str): backup file name to be imported
            timeout_in_sec (number) : time in seconds for which method waits
                                    for the backUp file to generate else exit.
            preserve_pooled_values (boolean): by default False

        Example:
            file_dir = "/home/user/backup"
            file_name = "config_backup.xml"
            backup_ucs(handle, backup_type="config-logical",
                        file_dir=test_support, file_name=file_name)
    """
    from ..mometa.mgmt.MgmtBackup import MgmtBackup, MgmtBackupConsts
    from ..mometa.top.TopSystem import TopSystem

    if not file_dir:
        raise UcsValidationException("Provide file_dir")
    if not file_name:
        raise UcsValidationException("Provide file_name.")

    if backup_type is None:
        raise UcsValidationException("Provide backup_type")

    backup_types = ["config-all", "config-logical",
                    "config-system", "full-state"]

    if backup_type not in backup_types:
        raise UcsValidationException('Valid type values are %s'
                                     % ', '.join(backup_types))

    if backup_type == "full-state" and not file_name.endswith('.tar.gz'):
        raise UcsValidationException('path_pattern should end with .tar.gz')
    elif backup_type != "full-state" and not file_name.endswith('.xml'):
        raise UcsValidationException('path_pattern should end with .xml')

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    file_path = os.path.join(file_dir, file_name)

    # create MgmtBackup
    if backup_type in [MgmtBackupConsts.TYPE_FULL_STATE,
                       MgmtBackupConsts.TYPE_CONFIG_SYSTEM]:
        preserve_pooled_values = False

    host_name = platform.node().lower() \
        + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    top_system = TopSystem()
    mgmt_backup = MgmtBackup(parent_mo_or_dn=top_system,
                             hostname=host_name,
                             admin_state=MgmtBackupConsts.ADMIN_STATE_ENABLED,
                             proto=MgmtBackupConsts.PROTO_HTTP,
                             type=backup_type,
                             remote_file=file_path)

    if preserve_pooled_values:
        mgmt_backup.preserve_pooled_values = \
            MgmtBackupConsts.PRESERVE_POOLED_VALUES_YES
    else:
        mgmt_backup.preserve_pooled_values = \
            MgmtBackupConsts.PRESERVE_POOLED_VALUES_NO

    handle.add_mo(mgmt_backup)
    handle.commit()

    # Checking for the backup to compete.
    duration = timeout_in_sec
    poll_interval = 2

    while True:
        mgmt_backup = handle.query_dn(dn=mgmt_backup.dn)
        admin_state_temp = mgmt_backup.admin_state

        # Break condition:- if state id disabled then break
        if admin_state_temp == MgmtBackupConsts.ADMIN_STATE_DISABLED:
            break

        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(mgmt_backup)
            handle.commit()
            raise UcsValidationException('backup_ucs timed out')

    print mgmt_backup  # BackUp Complete.

    # download backup
    file_source = "backupfile/" + file_name
    try:
        handle.file_download(url_suffix=file_source,
                             dest_dir=file_dir,
                             file_name=file_name)
    except Exception, err:
        UcsWarning("Download Error.....")
        UcsWarning(str(err))

    # remove backup from ucs
    handle.remove_mo(mgmt_backup)
    handle.commit()

    print mgmt_backup


def import_ucs_backup(handle, file_dir, file_name, merge=False):
    """
        This operation will upload the UCSM backup taken earlier via GUI
        or backup_ucs operation for all configuration, system configuration,
        and logical configuration files. User can perform an import while the
        system is up and running.

        Attributes:
            handle (UcsHandle)
            file_dir (str): directory contains ucs backup file
            file_name (str): backup file name to be imported
            merge (boolean): specifies whether to merge the backup
            configuration with the existing UCSM configuration

        Example:
            file_dir = "/home/user/backup"
            file_name = "config_backup.xml"
            import_ucs_backup(handle, file_dir=file_dir, file_name=file_name)
    """
    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.mgmt.MgmtImporter import MgmtImporter, MgmtImporterConsts

    if not file_dir:
        raise UcsValidationException("provide file_dir")
    if not file_name:
        raise UcsValidationException("provide file_name")

    file_path = os.path.join(file_dir, file_name)
    log.debug(file_path)
    if not os.path.exists(file_path):
        raise UcsValidationException("Backup File not found <%s>" %
                                     file_path)

    # create MgmtImporter
    host_name = os.environ['COMPUTERNAME'].lower() + \
                datetime.datetime.now().strftime('%Y%m%d%H%M')

    top_system = TopSystem()
    mgmt_importer = MgmtImporter(parent_mo_or_dn=top_system,
                                 hostname=host_name,
                                 remote_file=file_path,
                                 proto=MgmtImporterConsts.PROTO_HTTP,
                            admin_state=MgmtImporterConsts.ADMIN_STATE_ENABLED)

    if merge:
        mgmt_importer.action = MgmtImporterConsts.ACTION_MERGE
    else:
        mgmt_importer.action = MgmtImporterConsts.ACTION_REPLACE

    uri_suffix = "operations/file-%s/importconfig.txt" % file_name
    handle.file_upload(url_suffix=uri_suffix,
                       source_dir=file_dir,
                       file_name=file_name)

    handle.add_mo(mgmt_importer)
    handle.commit()

    return mgmt_importer
