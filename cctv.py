from tinydb import TinyDB, Query
from utils import img_to_array
from io import BytesIO
from PIL import Image
from config import *

import tensorflow as tf
import urllib.request
import numpy as np
import requests
import cv2

db = TinyDB('db.json')

# Download and convert the camera image to PIL object
def get_img(url):
	img = BytesIO(urllib.request.urlopen(url).read())
	img = Image.open(img)
	return img

# Crop parking spot out of full-size camera image
def crop_img(img, crop_data):
	x = crop_data[0]
	y = crop_data[1]
	w = crop_data[2]
	h = crop_data[3]
	cropped_img = img.crop((x, y, x+w, y+h))
	return cropped_img

# Update data
def update():

	parkings = db.all()
	for parking in parkings:

		# Download camera image
		camera_image = get_img(parking['url'])

		# Process each parking spot
		parking_spots = parking['spots']
		updated_parking_spots = []

		for spot in parking_spots:
			# Load the model everytime in order to avoid threading error
			model = tf.keras.models.load_model('model.h5')

			spot_image = crop_img(camera_image, spot['crop'])
			spot_image = img_to_array(spot_image, path=False)
			prediction = model.predict(np.array([spot_image]))
			if prediction[0][0] > prediction[0][1]:
				spot['occupied'] = False
			else:
				spot['occupied'] = True
			updated_parking_spots.append(spot)

			# Threading error fix also
			tf.keras.backend.clear_session()
		parking_query = Query()
		db.update({'spots': updated_parking_spots}, parking_query.id == parking['id'])

# Get database
def get_data():
	return db.all()

