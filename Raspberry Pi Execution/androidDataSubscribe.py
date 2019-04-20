# importing libraries

import requests
from sense_hat import SenseHat

# instantiating the method and initialising it
sense = SenseHat()

TOKEN = key
DEVICE_LABEL = 'project'

# constructing the url to whch the data will be sent along with the urls to the particular variables
url = "http://things.ubidots.com"
url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
# variable_url = 'http://things.ubidots.com/api/v1.6/datasources/5ca8e01bc03f97387e0a8fae/variables'
android_url = 'http://things.ubidots.com/api/v1.6/variables/5cb908dfc03f9745cb92ca39/values'

# subscribing to teh topic variable android from ubidots
data = requests.get(url=android_url, headers=headers)
data = data.json()
print(data)

required_value = data['results'][0]['value']
print(required_value)

# changing display based on the android variable value
if required_value == 1.0:
    # print("Green")
    sense.show_message("Access Granted")

else:
   # print('Red')
   sense.show_message("Access Denied")






