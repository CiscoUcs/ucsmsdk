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

import ucsmsdk.ucsxmlcodec as xc


class TestSpecialRN(unittest.TestCase):
    def test_001_StorageLocalDiskPartition(self):
        xml_str = '''
        <storageLocalDiskPartition childAction="deleteNonPresent" descr=""
        dn="org-root/local-disk-config-default/partition" intId="29002" name=""
        order="1" policyLevel="0" policyOwner="local" size="unknown" type="none"/>
        '''

        obj = xc.from_xml_str(xml_str)
        xml_element = obj.to_xml()
        xc.to_xml_str(xml_element)

    def test_002_StorageLocalDiskPartition(self):
        xml_str = '''<configResolveClass cookie="1447403324/24f7c591-2b3e-4bf4-8cee-716d3b4297b1" response="yes" classId="storageLocalDiskPartition"> <outConfigs>  <storageLocalDiskPartition childAction="deleteNonPresent" descr="" dn="org-root/local-disk-config-default/partition" intId="29002" name="" order="1" policyLevel="0" policyOwner="local" size="unknown" type="none"/>  <storageLocalDiskPartition childAction="deleteNonPresent" descr="" dn="sys/chassis-1/blade-2/board/storage-SAS-1/local-disk-config/partition" intId="none" name="" order="1" policyLevel="0" policyOwner="local" size="unknown" type="none"/> </outConfigs> </configResolveClass>
        '''

        obj = xc.from_xml_str(xml_str)
        xml_element = obj.to_xml()
        xc.to_xml_str(xml_element)

    def test_003_StorageLocalDiskPartition(self):
        xml_str = '''<storageController childAction="deleteNonPresent" controllerStatus="unknown" deviceRaidSupport="yes" faultMonitoring="supported" hwRevision="1064E(B3)" id="1" lc="allocated" locationDn="" model="SAS1064E PCI-Express Fusion-MPT SAS" oobControllerId="not-applicable" oobInterfaceSupported="no" operQualifierReason="N/A" operState="unknown" operability="unknown" pciAddr="01:00.0" pciSlot="" perf="unknown" power="unknown" presence="equipped" raidSupport="RAID0, RAID1" rebuildRate="unknown" revision="0" rn="storage-SAS-1" serial="" thermal="unknown" type="SAS" vendor="LSI Logic   Symbios Logic" voltage="unknown"> <storageLocalDiskConfigDef childAction="deleteNonPresent" descr="" flexFlashRAIDReportingState="disable" flexFlashState="disable" intId="none" mode="any-configuration" name="" policyLevel="0" policyOwner="local" protectConfig="no" rn="local-disk-config"> <storageLocalDiskPartition childAction="deleteNonPresent" descr="" intId="none" name="" order="1" policyLevel="0" policyOwner="local" rn="partition" size="unknown" type="none"/></storageLocalDiskConfigDef></storageController>
        '''

        obj = xc.from_xml_str(xml_str)
        xml_element = obj.to_xml()
        xc.to_xml_str(xml_element)
