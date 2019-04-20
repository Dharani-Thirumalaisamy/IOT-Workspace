# importing library
import requests

TOKEN = key
DEVICE_LABEL = 'project'

# Creates the headers for the HTTP requests
url = "http://things.ubidots.com"
url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

# reading the log text that was created from android app
android_data = open(r'/home/dharani/Android/Sdk/platform-tools/log.txt', mode='r')
data = android_data.read()
required_data = data.split(":")
# getting only the STATE value from the log file
print(required_data)
print(required_data[-1])

# using conditions to decide what value should be sent to the android variable
if required_data[-1] == str(' Access Granted\n'):
    payload = {'android': 1}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
    print("Data 1 sent")

else:
    payload = {'android': 2}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
    print("Data 2 sent")

