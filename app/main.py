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
from flask import Flask, render_template, request
import json
import requests
import time
import functions

app = Flask(__name__)

@app.route('/')
def main():

    # this will be the header for the html table to display the set of information
    header = ['Name','model','ip_address','serial','network_loc','product','location']
    device_list = []

    # makes call to retrieve a list of devices with several attributes from the CUCM evironment 
    # axl is for administrative details like phone name, location, model, product etc
    # risport of for realtimeservice like ip address 
    list_of_devices_axl = functions.axl_request()
    list_of_devices_risport = functions.risport_request()

    for index1, device_risport in enumerate(list_of_devices_risport):
        for index2, device_axl in enumerate(list_of_devices_axl):

            if device_risport["Name"] == device_axl["name"]:
                device = {}
                print("device created for ",device_axl["name"])

                device["name"] = device_axl["name"]
                device["ip_address"] = device_risport["IpAddress"]
                device["model"] = device_axl["model"]
                device["networkLocation"] = device_axl["networkLocation"]
                device["product"] = device_axl["product"] 
                device["locationName"] = device_axl["locationName"]
                
                if device["ip_address"] is None:
                    device["serial_number"] = "unassigned"
                else:
                    # calling function to retrieve serial number based on IP address (visiting the phone web page)
                    device["serial_number"] = functions.get_serial(device["ip_address"])

                device_list.append(device)

    return render_template('inventory.html', devices = device_list, num_devices = len(device_list), header = header)

if __name__ == "__main__":
#you may enter a routable ip address and uncomment the command
    #app.run(host='*ip address*')
    app.run(debug=True)
