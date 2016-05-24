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

from ucsmsdk.utils.converttopython import convert_to_ucs_python


def test_001_convert_to_from_xml_sp():
    xml_str = '''
 <configConfMos cookie="[hidden]" response="yes"> <inConfigs> <pair
 key="org-root/ls-test_sp_123"> <lsServer agentPolicyName=""
 assignState="unassigned" assocState="unassociated" biosProfileName=""
 bootPolicyName="" configQualifier="" configState="not-applied" descr=""
 dn="org-root/ls-test_sp_123" dynamicConPolicyName="" extIPPoolName="ext-mgmt"
 extIPState="none" fltAggr="0" fsmDescr="" fsmFlags="" fsmPrev="nop"
 fsmProgr="100" fsmRmtInvErrCode="none" fsmRmtInvErrDescr="" fsmRmtInvRslt=""
 fsmStageDescr="" fsmStamp="never" fsmStatus="nop" fsmTry="0"
 hostFwPolicyName="" identPoolName="default" intId="80996" kvmMgmtPolicyName=""
 localDiskPolicyName="" maintPolicyName="" mgmtAccessPolicyName=""
 mgmtFwPolicyName="" name="test_sp_123" operBiosProfileName=""
 operBootPolicyName="" operDynamicConPolicyName="" operExtIPPoolName=""
 operHostFwPolicyName="" operIdentPoolName="" operKvmMgmtPolicyName=""
 operLocalDiskPolicyName="" operMaintPolicyName="" operMgmtAccessPolicyName=""
 operMgmtFwPolicyName="" operPowerPolicyName="" operScrubPolicyName=""
 operSolPolicyName="" operSrcTemplName="" operState="unassociated"
 operStatsPolicyName="" operVconProfileName="" operVmediaPolicyName=""
 owner="management" pnDn="" policyLevel="0" policyOwner="local"
 powerPolicyName="default" propAcl="0" resolveRemote="yes" scrubPolicyName=""
 solPolicyName="" srcTemplName="" statsPolicyName="default" status="created"
 svnicConfig="yes" type="instance" usrLbl="" uuid="derived"
 uuidSuffix="0000-000000000000" vconProfileName="" vmediaPolicyName=""/></pair>
 </inConfigs> </configConfMos>
'''
    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)


def test_002_convert_to_from_xml_sp():
    xml_str = '''
<configConfMos
inHierarchical="false">
<inConfigs>
<pair key="org-root/ls-test1234">
<lsServer
agentPolicyName=""
biosProfileName=""
bootPolicyName="default"

descr=""
dn="org-root/ls-test1234"
dynamicConPolicyName=""
extIPPoolName="ext-mgmt"
extIPState="none"
hostFwPolicyName=""
identPoolName="default"
kvmMgmtPolicyName=""
localDiskPolicyName=""
maintPolicyName=""
mgmtAccessPolicyName=""
mgmtFwPolicyName=""
name="test1234"
policyOwner="local"
powerPolicyName="default"
resolveRemote="yes"

sacl="addchild,del,mod"
scrubPolicyName=""
solPolicyName=""
srcTemplName=""
statsPolicyName="default"
status="created"
usrLbl=""
uuid="0"
vconProfileName=""
vmediaPolicyName="">
<lsVConAssign
adminHostPort="ANY"
adminVcon="any"


order="1"
rn="assign-ethernet-vnic-eth0"
sacl="addchild,del,mod"
status="created,modified"
transport="ethernet"
vnicName="eth0">
</lsVConAssign>
<lsVConAssign
adminHostPort="ANY"
adminVcon="any"


order="2"
rn="assign-fc-vnic-fc0"
sacl="addchild,del,mod"
status="created,modified"
transport="fc"
vnicName="fc0">
</lsVConAssign>
<vnicEther
adaptorProfileName=""
addr="derived"
adminCdnName=""
adminHostPort="ANY"
adminVcon="any"
cdnPropInSync="yes"
cdnSource="vnic-name"


identPoolName="default"
mtu="1500"
name="eth0"
nwCtrlPolicyName=""
nwTemplName=""
order="1"
pinToGroupName=""
qosPolicyName=""
rn="ether-eth0"
sacl="addchild,del,mod"
statsPolicyName="default"

switchId="A">
<vnicEtherIf

defaultNet="yes"

name="default"
rn="if-default"
sacl="addchild,del,mod"
>
</vnicEtherIf>
</vnicEther>
<vnicFc
adaptorProfileName=""
addr="derived"
adminCdnName=""
adminHostPort="ANY"
adminVcon="any"
cdnPropInSync="yes"
cdnSource="vnic-name"


identPoolName=""
maxDataFieldSize="2048"
name="fc0"
nwTemplName=""
order="2"
persBind="disabled"
persBindClear="no"
pinToGroupName=""
qosPolicyName=""
rn="fc-fc0"
sacl="addchild,del,mod"
statsPolicyName="default"

switchId="A">
<vnicFcIf


name="default"
rn="if-default"
sacl="addchild,del,mod"
>
</vnicFcIf>
</vnicFc>
<vnicFcNode
addr="pool-derived"


identPoolName="node-default"
rn="fc-node"
sacl="addchild,del,mod"
>
</vnicFcNode>
<lsPower


rn="power"
sacl="addchild,del,mod"
state="admin-up"
>
</lsPower>
<fabricVCon


fabric="NONE"
id="1"
instType="auto"
placement="physical"
rn="vcon-1"
sacl="addchild,del,mod"
select="all"
share="shared"

transport="ethernet,fc">
</fabricVCon>
<fabricVCon


fabric="NONE"
id="2"
instType="auto"
placement="physical"
rn="vcon-2"
sacl="addchild,del,mod"
select="all"
share="shared"

transport="ethernet,fc">
</fabricVCon>
<fabricVCon


fabric="NONE"
id="3"
instType="auto"
placement="physical"
rn="vcon-3"
sacl="addchild,del,mod"
select="all"
share="shared"
transport="ethernet,fc">
</fabricVCon>
<fabricVCon


fabric="NONE"
id="4"
instType="auto"
placement="physical"
rn="vcon-4"
sacl="addchild,del,mod"
select="all"
share="shared"

transport="ethernet,fc">
</fabricVCon>
</lsServer>
</pair>
</inConfigs>
</configConfMos>

'''
    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)


def test_003_convert_from_xml_sp_associate():
    xml_str = '''
<configConfMos
inHierarchical="false">
<inConfigs>
<pair key="org-root/org-Cisco/ls-test_sdk_12345">
<lsServer
agentPolicyName=""
biosProfileName=""
bootPolicyName="WIP_BOOT"

descr=""
dn="org-root/org-Cisco/ls-test_sdk_12345"
dynamicConPolicyName=""
extIPPoolName="ext-mgmt"
extIPState="none"
hostFwPolicyName=""
identPoolName=""
kvmMgmtPolicyName=""
localDiskPolicyName=""
maintPolicyName=""
mgmtAccessPolicyName=""
mgmtFwPolicyName=""
policyOwner="local"
powerPolicyName="default"
resolveRemote="yes"

sacl="addchild,del,mod"
scrubPolicyName=""
solPolicyName=""
srcTemplName=""
statsPolicyName="default"
status="modified"
usrLbl=""
uuid="00000000-0000-0000-0000-000000000099"
vconProfileName=""
vmediaPolicyName="">
<lsBinding


pnDn="sys/chassis-1/blade-7"
restrictMigration="no"
rn="pn"
sacl="addchild,del,mod"
>
</lsBinding>
</lsServer>
</pair>
</inConfigs>
</configConfMos>
'''
    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)


def test_004_convert_from_xml_sp_disassociate():
    xml_str = '''
    <configConfMos
        inHierarchical="false">
    <inConfigs>
    <pair key="org-root/org-Cisco/ls-test_sdk_12345/pn">
    <lsBinding

    dn="org-root/org-Cisco/ls-test_sdk_12345/pn"

    sacl="addchild,del,mod"
    status="deleted">
    </lsBinding>
    </pair>
    </inConfigs>
    </configConfMos>
    '''
    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)


def test_005_convert_from_xml():
    xml_str = '''
    <configConfMos inHierarchical="false">
    <inConfigs>
     <pair key="fabric/lan/A/phys-slot-1-port-10">
      <fabricEthLanEp adminSpeed="10gbps" adminState="enabled"
      autoNegotiate="no" dn="fabric/lan/A/phys-slot-1-port-10"
      ethLinkProfileName="default" flowCtrlPolicy="default"
      name="" portId="10" sacl="addchild,del,mod" slotId="1"
      status="created" usrLbl="">
        </fabricEthLanEp>
     </pair>
    </inConfigs>
    </configConfMos>
    '''

    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)


def test_006_convert_from_xml():
    xml_str = '''
    <configConfMos inHierarchical="false">
    <inConfigs>
     <pair key="sys/mgmt/fw-boot-def/bootunit-system">
      <firmwareBootUnit adminState="triggered"
      dn="sys/mgmt/fw-boot-def/bootunit-system" ignoreCompCheck="no"
      mode="install" resetOnActivate="yes" sacl="addchild,del,mod"
      skipValidation="yes" version="3.1(200.13)">
        </firmwareBootUnit>
     </pair>
    </inConfigs>
    </configConfMos>
    '''

    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)


def test_007_convert_from_xml():
    xml_str = '''
    <configConfRename
    dn="org-root/ls-test_clone"
    inNewName="test_clone1111"
    inHierarchical="false">
    </configConfRename>
    '''
    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)


def test_008_convert_from_xml_dumptofile():
    import os

    xml_str = '''
    <configConfRename
    dn="org-root/ls-test_clone"
    inNewName="test_clone1111"
    inHierarchical="false">
    </configConfRename>
    '''

    logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "logfile.txt")
    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True,
                          dump_to_file=True, dump_file_path=logfile)

    assert os.stat(logfile).st_size != 0

    os.remove(logfile)
