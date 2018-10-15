from flask import Flask, jsonify

import tensorflow as tf
import model as clf
import cctv as cctv

app = Flask(__name__)

# Return parking info from database
@app.route('/get_data')
def get_data():
	return jsonify(cctv.get_data())

# Refresh info about all parking spots and update database
@app.route('/update')
def update():
	cctv.update()
	return 'updated'

# Train the TensorFlow model
@app.route('/train')
def train():
	clf.train()
	return 'trained'

@app.route('/')
def index():
	return "Parq API"

if __name__ == '__main__':
	app.run()