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

from suds.client import Client
from suds.transport.https import HttpAuthenticated
from suds.xsd.doctor import ImportDoctor, Import
from urllib.request import HTTPSHandler
import urllib.error
import urllib.request
import ssl
import user_env
#import phoneQuery

def get_device_ip(phone_name):

    #Disable HTTPS certificate validation check - not recommended for production
    if hasattr(ssl, '_create_unverified_context'):ssl._create_default_https_context = ssl._create_unverified_context

    url = 'https://' + user_env.CUCM_LOCATION + ':8443/realtimeservice/services/RisPort?wsdl'
    print (url)

    tns = 'http://schemas.cisco.com/ast/soap/'
    imp = Import('http://schemas.xmlsoap.org/soap/encoding/', 'http://schemas.xmlsoap.org/soap/encoding/')
    imp.filter.add(tns)


    t = HttpAuthenticated(username=user_env.CUCM_USER, password=user_env.CUCM_PASSWORD)
    t.handler=urllib.request.HTTPBasicAuthHandler(t.pm)

    context = ssl.SSLContext()


    t1=urllib.request.HTTPSHandler(context=context)
    t.urlopener = urllib.request.build_opener(t.handler,t1)


    c = Client(url, plugins=[ImportDoctor(imp)], transport=t)

    result = c.service.SelectCmDevice('',{'SelectBy':'Name', 'Status':'Any', 'Class':'Phone'})

    total_phones = result['SelectCmDeviceResult']['TotalDevicesFound']
    list_phones = result['SelectCmDeviceResult']["CmNodes"]
    print ('number of devices found', total_phones )


    for node in result['SelectCmDeviceResult']['CmNodes']:
        for device in node['CmDevices']:
                if device["IpAddress"] is None:
                    print("IP address not assigned for" , device["Name"])
                    print("----------------")
                    continue
                else:
                    print("Name ",device["Name"], "IP Address: ",device["IpAddress"])
                    print("----------------")
                    continue

# enter name of device to retrieve the ip of the device               
get_device_ip("CSFUSER004")