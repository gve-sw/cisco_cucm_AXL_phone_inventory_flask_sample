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
import list_subscribers_and_phones

app = Flask(__name__)


@app.route('/')
def main():

    list_of_devices = list_subscribers_and_phones.listPhones()
    device = list_of_devices[0]
    num_device = len(list_of_devices)
    header = []

    for key in device.keys():
        header.append(key)
        print(key)

    return render_template('inventory.html', devices = list_of_devices, num_devices = num_device, header = header)

if __name__ == "__main__":
    #app.run(host='*ip address*')
    app.run(debug=True)
