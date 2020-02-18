""" Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

"""AXL <listProcessNode> and <listPhones> sample script, using the SUDS-Jurko library

Script Dependencies:
    suds
    logging (optional)

Depencency Installation:
    $ pip install suds-py3
"""

import pathlib
# import pydash
import ssl
from suds.client import Client
from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor

import os
import sys

# Get the absolute path for the project root
project_root = os.path.abspath(os.path.dirname(__file__))

# Extend the system path to include the project root and import the env file
sys.path.insert(0, project_root)
import user_env

#Disable HTTPS certificate validation check - not recommended for production
if hasattr(ssl, '_create_unverified_context'):ssl._create_default_https_context = ssl._create_unverified_context

tns = 'http://schemas.cisco.com/ast/soap/'
imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add(tns)

axl = Client("file://"+user_env.WSDL_PATH,
    location="https://"+user_env.CUCM_LOCATION+"/axl/",
    faults=False,plugins=[ImportDoctor(imp)],
    username=user_env.CUCM_USER,
    password=user_env.CUCM_PASSWORD)
                
def getSubs():
    res = axl.service.listProcessNode({'name': '%', 'processNodeRole': 'CUCM Voice/Video'}, returnedTags={'name': ''})
    subs = res[1]['return']['processNode']
    for sub in subs:
        if sub.name != 'EnterpriseWideData':
            print("hello",sub.name)

            

def listPhones():
    list_of_devices = []

    res = axl.service.listPhone({'name': '%'}, returnedTags={'name': '',
                                                            'description': '',
                                                            'model': '',
                                                            'networkLocation': '',
                                                            'product': '',
                                                            'class': '',
                                                            'protocol': '',
                                                            'protocolSide': '',
                                                            'callingSearchSpaceName': '' ,
                                                            'devicePoolName': '' ,
                                                            'commonDeviceConfigName': '',
                                                            'commonPhoneConfigName': '',
                                                            'networkLocation': '',
                                                            'locationName': '',
                                                            'mediaResourceListName': '',
                                                            'networkHoldMohAudioSourceId': '',
                                                            'userHoldMohAudioSourceId': '',
                                                            'automatedAlternateRoutingCssName': '',
                                                            'aarNeighborhoodName': '',
                                                            'loadInformation': '',
                                                            'traceFlag': '',
                                                            'mlppIndicationStatus': '',
                                                            'preemption': '',
                                                            'useTrustedRelayPoint': '',
                                                            'retryVideoCallAsAudio': '',
                                                            'securityProfileName': '',
                                                            'sipProfileName': '',
                                                            'cgpnTransformationCssName': '',
                                                            'useDevicePoolCgpnTransformCss': '',
                                                            'geoLocationName': '',
                                                            'geoLocationFilterName': '',
                                                            'sendGeoLocation': '',
                                                            'numberOfButtons': '',
                                                            'phoneTemplateName': '',
                                                            'primaryPhoneName': '',
                                                            'ringSettingIdleBlfAudibleAlert': '',
                                                            'ringSettingBusyBlfAudibleAlert': '',
                                                            'userLocale': '',
                                                            'networkLocale': '',
                                                            'idleTimeout': '',
                                                            'authenticationUrl': '',
                                                            'directoryUrl': '',
                                                            'idleUrl': '',
                                                            'informationUrl': '',
                                                            'messagesUrl': '',
                                                            'proxyServerUrl': '',
                                                            'servicesUrl': '',
                                                            'softkeyTemplateName': '',
                                                            'loginUserId': '',
                                                            'defaultProfileName': '',
                                                            'enableExtensionMobility': '',
                                                            'currentProfileName': '',
                                                            'loginTime': '',
                                                            'loginDuration': '',
                                                            'currentConfig': '',
                                                            'singleButtonBarge': '',
                                                            'joinAcrossLines': '',
                                                            'builtInBridgeStatus': '',
                                                            'callInfoPrivacyStatus': '',
                                                            'hlogStatus': '',
                                                            'ownerUserName': '',
                                                            'ignorePresentationIndicators': '',
                                                            'packetCaptureMode': '',
                                                            'packetCaptureDuration': '',
                                                            'subscribeCallingSearchSpaceName': '',
                                                            'rerouteCallingSearchSpaceName': '',
                                                            'allowCtiControlFlag': '',
                                                            'presenceGroupName': '',
                                                            'unattendedPort': '',
                                                            'requireDtmfReception': '',
                                                            'rfc2833Disabled': '',
                                                            'certificateOperation': '',
                                                            'authenticationMode': '',
                                                            'keySize': '',
                                                            'keyOrder': '',
                                                            'ecKeySize': '',
                                                            'authenticationString': '',
                                                            'certificateStatus': '',
                                                            'upgradeFinishTime': '',
                                                            'deviceMobilityMode': '',
                                                            'roamingDevicePoolName': '',
                                                            'remoteDevice': '',
                                                            'dndOption': '',
                                                            'dndRingSetting': '',
                                                            'dndStatus': '',
                                                            'isActive': '',
                                                            'isDualMode': '',
                                                            'mobilityUserIdName': '',
                                                            'phoneSuite': '',
                                                            'phoneServiceDisplay': '',
                                                            'isProtected': '',
                                                            'mtpRequired': '',
                                                            'mtpPreferedCodec': '',
                                                            'dialRulesName': '',
                                                            'sshUserId': '',
                                                            'digestUser': '',
                                                            'outboundCallRollover': '',
                                                            'hotlineDevice': '',
                                                            'secureInformationUrl': '',
                                                            'secureDirectoryUrl': '',
                                                            'secureMessageUrl': '',
                                                            'secureServicesUrl': '',
                                                            'secureAuthenticationUrl': '',
                                                            'secureIdleUrl': '',
                                                            'alwaysUsePrimeLine': '',
                                                            'alwaysUsePrimeLineForVoiceMessage': '',
                                                            'featureControlPolicy': '',
                                                            'deviceTrustMode': '',
                                                            'earlyOfferSupportForVoiceCall': '',
                                                            'requireThirdPartyRegistration': '',
                                                            'blockIncomingCallsWhenRoaming': '',
                                                            'homeNetworkId': '',
                                                            'AllowPresentationSharingUsingBfcp': '',
                                                            'confidentialAccess': '',
                                                            'requireOffPremiseLocation': '',
                                                            'allowiXApplicableMedia': ''})
    if res[1]['return']:
        phones = res[1]['return']['phone']
        for phone in phones:
            device = {}
            if phone.name.startswith('SEP'):
                device["name"] = phone.name
                device["model"] = phone.model
                device["networkLocation"] = phone.networkLocation
                device["product"] = phone.product 
                device["protocol_side"] = phone.protocolSide
                device["callingSearchSpaceName"] = str(phone.callingSearchSpaceName['value'])
                device["devicePoolName"] = str(phone.devicePoolName['value'])
                device["commonDeviceConfigName"] = str(phone.commonDeviceConfigName['value'])
                device["commonPhoneConfigName"] = str(phone.commonPhoneConfigName['value'])
                device["networkLocation"] = str(phone.networkLocation)
                device["locationName"] = str(phone.locationName.value)
                device["mediaResourceListName"] = str(phone.mediaResourceListName['value'])
                device["userHoldMohAudioSourceId"] = str(phone.userHoldMohAudioSourceId)
                device["traceFlag"] = str(phone.traceFlag)
                device["mlppIndicationStatus"] = str(phone.mlppIndicationStatus)
                device["preemption"] = str(phone.preemption)
                device["useTrustedRelayPoint"] = str(phone.useTrustedRelayPoint)
                device["retryVideoCallAsAudio"] = str(phone.retryVideoCallAsAudio)
                device["securityProfileName"] = str(phone.securityProfileName.value)
                device["sipProfileName"] = str(phone.securityProfileName.value)
                device["cgpnTransformationCssName"] = str(phone.securityProfileName.value)
                device["useDevicePoolCgpnTransformCss"] = str(phone.securityProfileName.value)
                device["geoLocationName"] = str(phone.securityProfileName.value)
                device["geoLocationFilterName"] = str(phone.geoLocationFilterName)
                device["sendGeoLocation"] = str(phone.sendGeoLocation)
                device["numberOfButtons"] = str(phone.numberOfButtons)
                device["phoneTemplateName"] = str(phone.securityProfileName.value)
                device["primaryPhoneName"] = str(phone.primaryPhoneName)
                device["ringSettingIdleBlfAudibleAlert"] = str(phone.ringSettingIdleBlfAudibleAlert)
                device["ringSettingBusyBlfAudibleAlert"] = str(phone.ringSettingBusyBlfAudibleAlert)
                device["userLocale"] = str(phone.userLocale)
                device["networkLocale"] = str(phone.networkLocale)
            
                list_of_devices.append(device)

    return list_of_devices



