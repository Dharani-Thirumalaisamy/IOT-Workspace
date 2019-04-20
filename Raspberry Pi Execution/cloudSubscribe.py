# importing libraries

import requests
import time
from sense_hat import SenseHat

# instantiating the method and initialising it
sense = SenseHat()
sense.clear()

# ubidots credentials
TOKEN = key
DEVICE_LABEL = 'project'

# constructing the url to whch the data will be sent along with the urls to the particular variables
url = "http://things.ubidots.com"
url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
# variable_url = 'http://things.ubidots.com/api/v1.6/datasources/5ca8e01bc03f97387e0a8fae/variables'
temp_url = 'http://things.ubidots.com/api/v1.6/variables/5cb171eac03f971a0c4aa748/values'
pressure_url = 'http://things.ubidots.com/api/v1.6/variables/5cb171f0c03f9719ef59e8f5/values'
humidity_url = 'http://things.ubidots.com/api/v1.6/variables/5cb171f8c03f971a0c4aa749/values'

# this function will subscribe the temperture, pressure, humidity values from the ubidots variables
def sub():

    res_temp = requests.get(url=temp_url, headers=headers)
    res_temp = res_temp.json()
    print(res_temp)

    res_pressure = requests.get(url=pressure_url, headers=headers)
    res_pressure = res_pressure.json()
    print(res_pressure)

    res_humidity = requests.get(url=humidity_url, headers=headers)
    res_humidity = res_humidity.json()
    print(res_humidity)

    # parsing the json data and scraping only the required values

    for i in range(len(res_temp['results'])-1):
        temp = res_temp['results'][i]['value']
        if temp > 20:
            modified_temp = 15
        elif temp < 15:
            modified_temp = 22
        else:
            modified_temp = temp

        print('Original Temperature:', temp)
        print('Modified Temperature', modified_temp)

    for i in range(len(res_pressure['results']) - 1):
        pressure = res_pressure['results'][i]['value']
        humidity = res_humidity['results'][i]['value']

        print('Current Pressure:', pressure)
        print('Current Humidity:', humidity)

