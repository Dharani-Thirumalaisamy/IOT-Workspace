# importing libraries

import time
import paho.mqtt.publish as publish
import requests

TOKEN = key
DEVICE_LABEL = 'project'

'''
def datatocloud(temp, press, humidity):
    publish.single("/fromrpi", payload=temp, qos=2, retain=False, hostname="m16.cloudmqtt.com",
                   port=12263, client_id="", keepalive=60, will=None,
                   auth={'username':"tfwjbnuk", 'password':"7nxSYfIISjN-"}, tls=None)
    publish.single("/fromrpi", payload=press, qos=2, retain=False, hostname="m16.cloudmqtt.com",
                   port=12263, client_id="", keepalive=60, will=None,
                   auth={'username': "tfwjbnuk", 'password': "7nxSYfIISjN-"}, tls=None)
    publish.single("/fromrpi", payload=humidity, qos=2, retain=False, hostname="m16.cloudmqtt.com",
                   port=12263, client_id="", keepalive=60, will=None,
                   auth={'username': "tfwjbnuk", 'password': "7nxSYfIISjN-"}, tls=None)
'''
# parsing data for temperature, pressure, humidity variable that is read in the sms module and making the connection


def datatoubi(temp,  press, humidity):
    payload = {'temperature': temp,
               'pressure': press,
               'humidity': humidity}

    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    # variable_url = 'http://things.ubidots.com/api/v1.6/datasources/5ca8e01bc03f97387e0a8fae/variables'
    value_url = 'http://things.ubidots.com/api/v1.6/variables/5cb171eac03f971a0c4aa748/values'
    # widget_url = 'https://app.ubidots.com/ubi/public/getdashboard/page/pDlD-AhCEjnMdZO1zefTbLZAqBY'
    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)
