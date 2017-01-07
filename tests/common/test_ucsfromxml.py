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

from nose.tools import *


def test_001_mo_from_xml():
    import ucsmsdk.ucsxmlcodec as xc

    response_str = '''
        <configResolveClasses cookie="1441601790/263349a7-1897-4df0-aff3-bc27c7316862" response="yes" classId="memoryUnit">
        <outConfigs>

        <memoryUnit adminState="policy" array="1" bank="1" capacity="4096" childAction="deleteNonPresent" clock="1333"
        dn="sys/chassis-1/blade-2/board/memarray-1/mem-9" formFactor="DIMM" id="9" latency="0.800000" location="DIMM_E1" locationDn="" model="M393B5170FH0-YH9" operQualifier="" operQualifierReason="N/A" operState="operable"
        operability="operable" perf="unknown" power="not-supported" presence="equipped" revision="0" serial="0x835CE6DB"
        set="0" speed="unspecified" thermal="ok" type="Other" vendor="0x80CE" visibility="yes" voltage="not-supported"
        width="64">

        <memoryUnitEnvStats childAction="deleteNonPresent" intervals="58982460" rn="dimm-env-stats" suspect="no"
        temperature="20.000000" temperatureAvg="20.000000" temperatureMax="20.000000" temperatureMin="20.000000"
        thresholded="" timeCollected="2015-09-07T10:31:06.608" update="262146">

        <memoryUnitEnvStatsHist1 childAction="deleteNonPresent" id="1" mostRecent="no" rn="1" suspect="no"
        temperature="28.000000" temperatureAvg="25.599997" temperatureMax="28.000000" temperatureMin="24.000000"
        thresholded="" timeCollected="2015-09-07T09:43:53.262">

        <memoryUnitEnvStatsHist2 childAction="deleteNonPresent" id="1" mostRecent="no" rn="1" suspect="no"
        temperature="28.000000" temperatureAvg="25.599997" temperatureMax="28.000000" temperatureMin="24.000000"
        thresholded="" timeCollected="2015-09-07T09:43:53.262">
        </memoryUnitEnvStatsHist2>

        </memoryUnitEnvStatsHist1>

        </memoryUnitEnvStats>
        </memoryUnit>
        </outConfigs>
        </configResolveClasses>
    '''

    response = xc.from_xml_str(response_str)
    assert_equal(response.out_configs.child[0].__class__.__name__, 'MemoryUnit')
    assert_equal(response.out_configs.child[0].child[0].__class__.__name__, 'MemoryUnitEnvStats')
    assert_equal(response.out_configs.child[0].child[0].child[0].__class__.__name__, 'GenericMo')
    assert_equal(response.out_configs.child[0].child[0].child[0].child[0].__class__.__name__, 'GenericMo')


def test_002_mo_from_broken_xml():
    import ucsmsdk.ucsxmlcodec as xc

    response_str = '''
        <configResolveClasses cookie="1441601790/263349a7-1897-4df0-aff3-bc27c7316862" response="yes" classId="memoryUnit">
        <outConfigs>

        <memoryUnit adminState="policy" array="1" bank="1" capacity="4096" childAction="deleteNonPresent" clock="1333"
        dn="sys/chassis-1/blade-2/board/memarray-1/mem-9" formFactor="DIMM" id="9" latency="0.800000" location="DIMM_E1" locationDn="" model="M393B5170FH0-YH9" operQualifier="" operQualifierReason="N/A" operState="operable"
        operability="operable" perf="unknown" power="not-supported" presence="equipped" revision="0" serial="0x835CE6DB"
        set="0" speed="unspecified" thermal="ok" type="Other" vendor="0x80CE" visibility="yes" voltage="not-supported"
        width="64">

        <memoryUnitEnvStats childAction="deleteNonPresent" intervals="58982460" rn="dimm-env-stats" suspect="no"
        temperature="20.000000" temperatureAvg="20.000000" temperatureMax="20.000000" temperatureMin="20.000000"
        thresholded="" timeCollected="2015-09-07T10:31:06.608" update="262146">

        <memoryUnitEnvStatsHist childAction="deleteNonPresent" id="<BAD INDEX>" mostRecent="no" rn="1" suspect="no"
        temperature="28.000000" temperatureAvg="25.599997" temperatureMax="28.000000" temperatureMin="24.000000"
        thresholded="" timeCollected="2015-09-07T09:43:53.262">

        <memoryUnitEnvStatsHist childAction="deleteNonPresent" id="<BAD& INDEX>" mostRecent="no" rn="1" suspect="no"
        temperature="28.000000" temperatureAvg="25.599997" temperatureMax="28.000000" temperatureMin="24.000000"
        thresholded="" timeCollected="2015-09-07T09:43:53.262">
        </memoryUnitEnvStatsHist>

        </memoryUnitEnvStatsHist>

        </memoryUnitEnvStats>
        </memoryUnit>
        </outConfigs>
        </configResolveClasses>
    '''

    response = xc.from_xml_str(response_str)
    assert_equal(response.out_configs.child[0].__class__.__name__, 'MemoryUnit')
    assert_equal(response.out_configs.child[0].child[0].__class__.__name__, 'MemoryUnitEnvStats')
    assert_equal(response.out_configs.child[0].child[0].child[0].__class__.__name__, 'MemoryUnitEnvStatsHist')
    assert_equal(response.out_configs.child[0].child[0].child[0].child[0].__class__.__name__, 'MemoryUnitEnvStatsHist')

