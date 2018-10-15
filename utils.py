import numpy as np
from PIL import Image
from config import width, height, channels

def unison_shuffled_copies(a, b):
	assert len(a) == len(b)
	p = np.random.permutation(len(a))

	return a[p], b[p]

# Convert image to numpy array of numbers
def img_to_array(img, path=True):
	print('Works')
	if path:
		img = Image.open(img)
	img_arr = np.array(img) / 255.0
	img_arr = img_arr.reshape(width, height, channels)

	return img_arr