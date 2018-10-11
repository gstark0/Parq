import numpy as np
from PIL import Image

# Convert image to numpy array of numbers
def img_to_array(img_path):
	print(img_path)
	img = Image.open(img_path)
	img_arr = np.array(img) / 255.0

	return img_arr