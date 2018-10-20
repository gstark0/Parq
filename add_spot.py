from tinydb import TinyDB, Query, where

import numpy as np
import urllib.request
import config
import cv2
import sys
import os

db = TinyDB('db.json')
q = Query()

url = ''
coord = []

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	return image

default_img = url_to_image(url)
img = default_img

def draw_rect(event, x, y, flags, param):
	global mouseX, mouseY
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.rectangle(img, (x, y), (x+40, y+40), (255,0,0), 2)
		mouseX, mouseY = x, y

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)

spots = db.search(q.url == url)[0]['spots']
def save(x, y):
	global spots
	position_0 = int(input('Y position: '))
	position_1 = int(input('X position: '))
	spots.append({
		'coord': coord,
		'crop': [x, y, config.width, config.height],
		'position': [position_0, position_1],
		'occupied': False
	})
	db.update({'spots': spots}, q.url == url)

for spot in spots:
	cv2.rectangle(img, (spot['crop'][0], spot['crop'][1]), (spot['crop'][0] + spot['crop'][2], spot['crop'][1] + spot['crop'][3]), (255, 0, 0), 2)

while(True):
	cv2.imshow('image', img)
	k = cv2.waitKey(20) & 0xFF
	if k == 27:
		break
	elif k == ord('s'):
		save(mouseX, mouseY)
	elif k == ord('r'):
		os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
