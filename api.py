from flask import Flask, jsonify

import tensorflow as tf
import model as clf
import cctv as cctv

app = Flask(__name__)

# TensorFlow model
model = None

# Return parking info from database
@app.route('/get_data')
def get_data():
	return jsonify(cctv.get_data())

# Refresh info about all parking spots and update database
def update():
	cctv.update(model)
	return 'Updated'

# Train the TensorFlow model
@app.route('/train')
def train():
	global model
	model = clf.train()
	return 'Trained'

@app.route('/')
def index():
	return "Parq API"

if __name__ == '__main__':
	app.run()