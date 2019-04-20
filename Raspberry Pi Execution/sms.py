# importing libraries

from twilio.rest import Client
import numpy as np
import os
import time
import requests
from keras.models import load_model
import PredictModel
import gcp
import data2cloud
from time import sleep
import cloudSubscribe
from sense_hat import SenseHat

# instantiating the method and initialising it
sense = SenseHat()
sense.clear()

# client id and key to connect to the mobile
client = Client(clientId, key)

# making the loop run for 2 hours
t_end = time.time() + 60 * 200
while time.time() < t_end:
		# this will trigger the camera module when run on raspberry pi and save the image as test.jpg
		os.system('raspistill -o test.jpg')
		input_image = 'test.jpg'

		# start the sense hat and read values from that
		temperature = sense.get_temperature()
		pressure = sense.get_pressure()
		humidity = sense.get_humidity()

		# use face recognition model to predict who the person in the image is
		predicts = PredictModel.predicted(input_image, 'model-dataAug-34-0.60-0.55.hdf5')

		# if np.argmax(predicts) == 0:
		# message body that will be sent to the user
		message = "Someone rang the bell. Please check app for more details."
		# bucket credentials
		PROJECT = project name
		BUCKET = bucket name
		image = input_image

		# use this command to call the gcp.py
		gcp.upload(PROJECT, BUCKET, image)
		# calling datatocloud function from data2cloud module
		data2cloud.datatocloud(temperature, pressure, humidity)
		# calling datatoubi function from data2cloud module
		data2cloud.datatoubi(temperature, pressure, humidity)
		# the loop will stop for 5 mins
		time.sleep(300)
		# building the message body
		data = message + ' Temperature outside is : ' + str(
			temperature) + '. ' + 'Pressure outside is : ' + str(pressure) + '.' + ' Humidity outside is : ' + str(
			humidity) + '.'
		# client and host phone number to send message
		client.messages.create(to="+15086156167", from_="+17744506074", body=data)
		# subscribing the variables information from ubidots from CloudSubscribe module
		cloudSubscribe.sub()


