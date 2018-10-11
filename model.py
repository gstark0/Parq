import os
import numpy as np
import tensorflow as tf
from utils import img_to_array

samples_0 = './dataset/free/'
samples_1 = './dataset/busy/'

def main():

	data_x = []
	data_y = []
	

	# ---- Images to arrays of numbers ----

	# Images containing empty parking spots
	images_0 = os.listdir(samples_0)
	for img in images_0:
		img_path = samples_0 + img
		img_arr = img_to_array(img_path)

		data_x.append(img_arr)
		data_y.append(np.array([1, 0]))

	# Images containing occupied parking spots
	images_1 = os.listdir(samples_1)
	for img in images_1:
		img_path = samples_1 + img
		img_arr = img_to_array(img_path)

		data_x.append(img_arr)
		data_y.append(np.array([0, 1]))

	data_x = np.array(data_x)
	data_y = np.array(data_y)

	print(data_x)

if __name__ == '__main__':
	main()