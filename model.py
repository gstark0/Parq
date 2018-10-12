import os
import numpy as np
import tensorflow as tf
from utils import img_to_array, unison_shuffled_copies
from config import *

def load_images(dataset_location):
	samples_0 = dataset_location + label_0
	samples_1 = dataset_location + label_1

	data_x = []
	data_y = []

	# ---- Images to arrays of numbers ----

	# Images containing empty parking spots

	images_0 = os.listdir(samples_0)
	images_1 = os.listdir(samples_1)
	data_x = np.ndarray(shape=(len(images_0 + images_1), width, height, channels), dtype=np.float32)
	data_y = np.ndarray(shape=(len(images_0 + images_1)), dtype=np.float32)

	i = 0
	errors = 0
	for img in images_0:
		img_path = samples_0 + img

		try:
			img_arr = img_to_array(img_path)
			data_x[i] = img_arr
			data_y[i] = 0.
			i += 1
		except ValueError:
			print(img, '<--- Not working')
			errors += 1

	# Images containing occupied parking spots
	for img in images_1:
		img_path = samples_1 + img

		try:
			img_arr = img_to_array(img_path)
			data_x[i] = img_arr
			data_y[i] = 1.
			i += 1
		except ValueError:
			print(img, '<--- Not working')
			errors += 1

	data_x = np.array(data_x)
	data_y = np.array(data_y)

	data_x = data_x[:-errors]
	data_y = data_y[:-errors]
	data_x, data_y = unison_shuffled_copies(data_x, data_y)

	return data_x, data_y

def main():
	data_x, data_y = load_images(train_dataset)
	print(np.shape(data_x))
	print(np.shape(data_y))
	
	model = tf.keras.models.Sequential([
		tf.keras.layers.Convolution2D(32, 3, 3, input_shape=(width, height, 3), activation=tf.nn.relu),
		tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
		tf.keras.layers.Flatten(),
		tf.keras.layers.Dense(512, activation=tf.nn.relu),
		tf.keras.layers.Dense(2, activation=tf.nn.softmax)
	])

	model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
	print('Training model...')
	model.fit(data_x, data_y, epochs=5)
	print(model.predict(data_x[:2]))
	print(data_y[:2])
	

if __name__ == '__main__':
	main()