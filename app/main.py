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
